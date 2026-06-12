#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
家居顾问 MCP Server
提供菜品搜索和维修指导功能

遵循 Model Context Protocol (MCP) 标准
"""

import json
import sys
import os
import asyncio
from pathlib import Path
from typing import Any, Sequence


def get_data_file_path(filename):
    """
    获取数据文件路径
    优先级：
    1. 环境变量 HOME_ADVISOR_DATA_DIR
    2. 配置文件 config.json
    3. 默认路径：脚本所在目录的 data/
    """
    # 1. 检查环境变量
    data_dir = os.environ.get('HOME_ADVISOR_DATA_DIR')
    if data_dir:
        return Path(data_dir) / filename
    
    # 2. 检查配置文件
    script_dir = Path(__file__).parent
    config_file = script_dir / 'config.json'
    if config_file.exists():
        try:
            with config_file.open('r', encoding='utf-8') as f:
                config = json.load(f)
                data_dir = config.get('data_dir')
                if data_dir:
                    return Path(data_dir) / filename
        except:
            pass
    
    # 3. 默认路径：./data/
    default_path = script_dir / 'data' / filename
    if default_path.exists():
        return default_path
    
    # 4. 当前工作目录
    cwd_path = Path.cwd() / 'data' / filename
    if cwd_path.exists():
        return cwd_path
    
    # 默认返回预期路径
    return script_dir / 'data' / filename

# MCP Server 基础类
class MCPServer:
    """MCP Server 基础实现"""
    
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version
        self.tools = []
    
    def add_tool(self, tool):
        """添加工具"""
        self.tools.append(tool)
    
    def get_tools(self):
        """获取工具列表"""
        return [tool.to_dict() for tool in self.tools]
    
    async def handle_request(self, request: dict) -> dict:
        """处理 MCP 请求"""
        method = request.get("method")
        
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {
                        "name": self.name,
                        "version": self.version
                    },
                    "capabilities": {
                        "tools": {}
                    }
                }
            }
        
        elif method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "tools": self.get_tools()
                }
            }
        
        elif method == "tools/call":
            tool_name = request.get("params", {}).get("name")
            arguments = request.get("params", {}).get("arguments", {})
            
            for tool in self.tools:
                if tool.name == tool_name:
                    result = await tool.execute(arguments)
                    return {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "result": result
                    }
            
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "error": {
                    "code": -32601,
                    "message": f"Tool not found: {tool_name}"
                }
            }
        
        else:
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                }
            }
    
    async def run(self):
        """运行 MCP Server（stdio 模式）"""
        for line in sys.stdin:
            try:
                request = json.loads(line)
                response = await self.handle_request(request)
                print(json.dumps(response, ensure_ascii=False))
                sys.stdout.flush()
            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32700,
                        "message": f"Parse error: {str(e)}"
                    }
                }
                print(json.dumps(error_response))
                sys.stdout.flush()


class MCPTool:
    """MCP 工具定义"""
    
    def __init__(self, name: str, description: str, input_schema: dict):
        self.name = name
        self.description = description
        self.input_schema = input_schema
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            "name": self.name,
            "description": self.description,
            "inputSchema": self.input_schema
        }
    
    async def execute(self, arguments: dict) -> dict:
        """执行工具（子类需要实现）"""
        raise NotImplementedError


class SearchDishesTool(MCPTool):
    """搜索菜品工具"""
    
    def __init__(self):
        super().__init__(
            name="search_dishes",
            description="搜索菜品信息，支持按菜名、食材、口味等关键词搜索",
            input_schema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索关键词，如菜名、食材等"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "返回结果数量，默认 5",
                        "default": 5
                    }
                },
                "required": ["query"]
            }
        )
    
    async def execute(self, arguments: dict) -> dict:
        """执行搜索菜品"""
        query = arguments.get("query")
        limit = arguments.get("limit", 5)
        
        # 读取菜品数据
        dishes_file = get_data_file_path("dishes-index.json")
        
        if not dishes_file.exists():
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"错误：菜品数据文件不存在 ({dishes_file})"
                    }
                ]
            }
        
        try:
            with open(dishes_file, 'r', encoding='utf-8') as f:
                dishes_data = json.load(f)
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"错误：读取菜品数据失败 - {str(e)}"
                    }
                ]
            }
        
        # 搜索匹配
        results = []
        query_lower = query.lower()
        
        for dish in dishes_data:
            search_fields = [
                dish.get('title', ''),
                dish.get('content', ''),
                dish.get('file', '')
            ]
            
            for field in search_fields:
                if query_lower in str(field).lower():
                    results.append(dish)
                    break
            
            if len(results) >= limit:
                break
        
        # 格式化结果
        if not results:
            text = f"未找到与 '{query}' 相关的菜品"
        else:
            text = f"找到 {len(results)} 个与 '{query}' 相关的菜品：\n\n"
            for i, dish in enumerate(results, 1):
                text += f"{i}. {dish.get('title', '未知菜品')}\n"
                text += f"   文件：{dish.get('file', '未知')}\n"
                text += f"   链接：{dish.get('url', '无')}\n"
                # 显示内容摘要（前200字符）
                content = dish.get('content', '')
                if content:
                    summary = content[:200].replace('\n', ' ')
                    if len(content) > 200:
                        summary += '...'
                    text += f"   简介：{summary}\n"
                text += "\n"
        
        return {
            "content": [
                {
                    "type": "text",
                    "text": text
                }
            ]
        }


class SearchRepairTool(MCPTool):
    """搜索维修工具"""
    
    def __init__(self):
        super().__init__(
            name="search_repair",
            description="搜索家居维修指导，支持按维修项目、故障现象等关键词搜索",
            input_schema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索关键词，如维修项目、故障现象等"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "返回结果数量，默认 5",
                        "default": 5
                    }
                },
                "required": ["query"]
            }
        )
    
    async def execute(self, arguments: dict) -> dict:
        """执行搜索维修指导"""
        query = arguments.get("query")
        limit = arguments.get("limit", 5)
        
        # 读取维修数据
        repair_file = get_data_file_path("repair-index.json")
        
        if not repair_file.exists():
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"错误：维修数据文件不存在 ({repair_file})"
                    }
                ]
            }
        
        try:
            with open(repair_file, 'r', encoding='utf-8') as f:
                repair_data = json.load(f)
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"错误：读取维修数据失败 - {str(e)}"
                    }
                ]
            }
        
        # 搜索匹配
        results = []
        query_lower = query.lower()
        
        for item in repair_data:
            search_fields = [
                item.get('title', ''),
                item.get('content', ''),
                item.get('file', '')
            ]
            
            for field in search_fields:
                if query_lower in str(field).lower():
                    results.append(item)
                    break
            
            if len(results) >= limit:
                break
        
        # 格式化结果
        if not results:
            text = f"未找到与 '{query}' 相关的维修指导"
        else:
            text = f"找到 {len(results)} 个与 '{query}' 相关的维修指导：\n\n"
            for i, item in enumerate(results, 1):
                text += f"{i}. {item.get('title', '未知项目')}\n"
                text += f"   文件：{item.get('file', '未知')}\n"
                text += f"   链接：{item.get('url', '无')}\n"
                # 显示内容摘要（前200字符）
                content = item.get('content', '')
                if content:
                    summary = content[:200].replace('\n', ' ')
                    if len(content) > 200:
                        summary += '...'
                    text += f"   简介：{summary}\n"
                text += "\n"
        
        return {
            "content": [
                {
                    "type": "text",
                    "text": text
                }
            ]
        }


async def main():
    """主函数"""
    # 创建 MCP Server
    server = MCPServer(
        name="home-advisor",
        version="1.0.0"
    )
    
    # 添加工具
    server.add_tool(SearchDishesTool())
    server.add_tool(SearchRepairTool())
    
    # 运行服务器
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())
