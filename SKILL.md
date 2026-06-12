---
name: home-advisor
description: This skill provides home advisory services including dish recommendations and home repair guidance. It should be used when users ask about cooking recipes, dish recommendations, home repair instructions, or related household advice.
version: 1.0.0
author: 宸良手纪
triggers:
  - 菜品推荐
  - 做什么菜
  - 维修指导
  - 家居维修
  - 菜谱查询
---

# 家居顾问 Skill (Home Advisor)

## 功能说明

本 Skill 提供两大核心功能：
1. **菜品推荐** - 根据用户需求推荐菜品，提供详细做法
2. **维修指导** - 提供家居维修的步骤和指导

## 使用场景

### 菜品推荐
- 用户问："今天做什么菜？"
- 用户问："推荐一些家常菜"
- 用户问："怎么做宫保鸡丁？"

### 维修指导
- 用户问："水龙头怎么修？"
- 用户问："墙面裂缝怎么办？"
- 用户问："电路故障如何排查？"

## 工具使用

### search_dishes

搜索菜品数据库，返回匹配的菜品信息和做法。

**使用方法：**

```bash
python scripts/search_dishes.py --query "鸡丁"
python scripts/search_dishes.py --query "西红柿" --limit 3
```

**参数：**
- `query`: 搜索关键词（菜名、食材、口味等）
- `limit`: 返回结果数量（默认 5）

### search_repair

搜索维修知识库，返回维修步骤和注意事项。

**使用方法：**

```bash
python scripts/search_repair.py --query "水龙头"
python scripts/search_repair.py --query "漏水" --limit 2
```

**参数：**
- `query`: 搜索关键词（维修项目、故障现象等）
- `limit`: 返回结果数量（默认 5）

## 数据源

- 菜品数据：`data/dishes-index.json`
- 维修数据：`data/repair-index.json`

## 配置

详细配置说明请参考 [CONFIG.md](CONFIG.md)。

快速配置：

1. **使用环境变量**：
   ```bash
   export HOME_ADVISOR_DATA_DIR="/path/to/data"
   ```

2. **使用配置文件**：
   创建 `config.json`：
   ```json
   {
     "data_dir": "./data"
   }
   ```

3. **使用默认路径**：
   将数据文件放在 `./data/` 目录即可。

## 安装到 AI 助手

### CodeBuddy
将整个项目复制到 `.codebuddy/skills/home-advisor/` 目录。

### Trae
参考 Trae 的 Skill 安装文档，将 Skill 文件放到指定目录。

### Qoder
参考 Qoder 的 Skill 安装文档，将 Skill 文件放到指定目录。

### 通用方法
将以下文件放到 AI 助手的 skills 目录：
- `skill.json`
- `SKILL.md`
- `scripts/` 目录
- `references/` 目录（如有）

## 注意事项

1. 搜索结果基于本地索引文件，确保数据文件存在
2. 返回结果包含详细步骤，可直接用于指导
3. 维修操作请注意安全，必要时请联系专业人员
4. 本 Skill 遵循标准 Skill 规范，支持多种 AI 助手平台
