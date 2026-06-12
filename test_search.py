#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本：验证搜索功能是否正常
"""

import subprocess
import sys
import json

def test_search_dishes():
    """测试菜品搜索"""
    print("=" * 50)
    print("测试菜品搜索")
    print("=" * 50)
    
    # 测试搜索"鸡"
    result = subprocess.run(
        ['python', '.codebuddy/skills/home-advisor/scripts/search_dishes.py', '--query', '鸡', '--limit', '2'],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        data = json.loads(result.stdout)
        print(f"[OK] 搜索成功")
        print(f"  查询词: {data.get('query')}")
        print(f"  结果数: {data.get('total')}")
        if 'results' in data:
            for i, item in enumerate(data['results'][:2], 1):
                print(f"  {i}. {item.get('title')}")
    else:
        print(f"[FAIL] 搜索失败: {result.stderr}")
    
    print()

def test_search_repair():
    """测试维修搜索"""
    print("=" * 50)
    print("测试维修搜索")
    print("=" * 50)
    
    # 测试搜索"水龙头"
    result = subprocess.run(
        ['python', '.codebuddy/skills/home-advisor/scripts/search_repair.py', '--query', '水龙头', '--limit', '2'],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        data = json.loads(result.stdout)
        print(f"[OK] 搜索成功")
        print(f"  查询词: {data.get('query')}")
        print(f"  结果数: {data.get('total')}")
        if 'results' in data:
            for i, item in enumerate(data['results'][:2], 1):
                print(f"  {i}. {item.get('title')}")
    else:
        print(f"[FAIL] 搜索失败: {result.stderr}")
    
    print()

def test_data_files():
    """测试数据文件是否存在"""
    print("=" * 50)
    print("测试数据文件")
    print("=" * 50)
    
    import os
    from pathlib import Path
    
    # 检查 data 目录
    data_dir = Path('./data')
    if data_dir.exists():
        print(f"[OK] data 目录存在: {data_dir.absolute()}")
        
        # 检查菜品数据
        dishes_file = data_dir / 'dishes-index.json'
        if dishes_file.exists():
            print(f"[OK] 菜品数据文件存在: {dishes_file}")
        else:
            print(f"[FAIL] 菜品数据文件不存在: {dishes_file}")
        
        # 检查维修数据
        repair_file = data_dir / 'repair-index.json'
        if repair_file.exists():
            print(f"[OK] 维修数据文件存在: {repair_file}")
        else:
            print(f"[FAIL] 维修数据文件不存在: {repair_file}")
    else:
        print(f"[FAIL] data 目录不存在: {data_dir.absolute()}")
        print("  请运行: python setup_data.py")
    
    print()

def main():
    """主函数"""
    print("\n家居顾问 - 功能测试\n")
    
    # 测试数据文件
    test_data_files()
    
    # 测试搜索功能
    test_search_dishes()
    test_search_repair()
    
    print("=" * 50)
    print("测试完成")
    print("=" * 50)
    print()

if __name__ == '__main__':
    main()
