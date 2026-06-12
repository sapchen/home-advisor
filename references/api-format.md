# 数据格式说明

## dishes-index.json 格式

```json
[
  {
    "id": "dish_001",
    "name": "宫保鸡丁",
    "category": "家常菜",
    "ingredients": "鸡胸肉,花生米,辣椒,葱,姜,蒜",
    "description": "经典川菜，麻辣鲜香",
    "steps": [
      "鸡胸肉切丁，腌制15分钟",
      "花生米炸熟备用",
      "热锅下油，爆香辣椒和花椒",
      "下鸡丁翻炒至变色",
      "加入调料和花生米翻炒均匀"
    ],
    "tips": "火候要快，保持鸡肉嫩滑"
  }
]
```

## repair-index.json 格式

```json
[
  {
    "id": "repair_001",
    "title": "水龙头漏水维修",
    "category": "水路维修",
    "description": "水龙头漏水是常见的家居问题",
    "tools": ["扳手", "生料带", "新阀芯"],
    "steps": [
      "关闭水源总阀",
      "拆下水龙头把手",
      "取出旧阀芯",
      "安装新阀芯",
      "装回把手，测试是否漏水"
    ],
    "caution": "操作前务必关闭水源，避免水浸",
    "difficulty": "简单"
  }
]
```

## 搜索 API 返回格式

### 成功返回
```json
{
  "query": "鸡丁",
  "total": 1,
  "results": [...]
}
```

### 错误返回
```json
{
  "error": "错误信息"
}
```
