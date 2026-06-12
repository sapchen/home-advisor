#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
维修搜索脚本
从 repair-index.json 中搜索维修指导
"""

import json
import argparse
import sys
import os
from pathlib import Path


def get_data_file_path(filename):
    """
    获取数据文件路径
    优先级：
    1. 环境变量 HOME_ADVISOR_DATA_DIR
    2. 配置文件 config.json
    3. 默认路径：脚本所在目录的 ../data/
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
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                data_dir = config.get('data_dir')
                if data_dir:
                    return Path(data_dir) / filename
        except:
            pass
    
    # 3. 默认路径：../data/
    default_path = script_dir.parent.parent / 'data' / filename
    if default_path.exists():
        return default_path
    
    # 4. 兼容旧路径：脚本所在目录的 4 级父目录
    legacy_path = script_dir.parent.parent.parent.parent / filename
    if legacy_path.exists():
        return legacy_path
    
    # 5. 当前工作目录
    cwd_path = Path.cwd() / filename
    if cwd_path.exists():
        return cwd_path
    
    # 默认返回预期路径
    return script_dir.parent.parent / 'data' / filename


def search_repair(query, limit=5):
    """
    搜索维修指导
    
    Args:
        query: 搜索关键词
        limit: 返回结果数量
    
    Returns:
        匹配的维修指导列表
    """
    # 获取数据文件路径
    repair_file = get_data_file_path("repair-index.json")
    
    if not repair_file.exists():
        return {"error": f"维修数据文件不存在: {repair_file}"}
    
    try:
        with open(repair_file, 'r', encoding='utf-8') as f:
            repair_data = json.load(f)
    except Exception as e:
        return {"error": f"读取维修数据失败: {str(e)}"}
    
    # 搜索匹配
    results = []
    query_lower = query.lower()
    
    for item in repair_data:
        # 在标题和内容中搜索
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
    
    return {
        "query": query,
        "total": len(results),
        "results": results
    }


def main():
    parser = argparse.ArgumentParser(description='搜索维修指导')
    parser.add_argument('--query', '-q', required=True, help='搜索关键词')
    parser.add_argument('--limit', '-l', type=int, default=5, help='返回结果数量')
    
    args = parser.parse_args()
    
    results = search_repair(args.query, args.limit)
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
