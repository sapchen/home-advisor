# 家居顾问 Skill (Home Advisor)

一个通用的 AI 助手 Skill，为 AI 提供家居知识搜索能力，包括菜品推荐和家居维修指导。

本 Skill 遵循标准 Skill 规范，可无缝集成到支持 Skill 的 AI 编程助手。

## ✨ 功能特性

- **🍳 菜品推荐**：搜索家常菜谱数据库，返回详细的做法和技巧
- **🔧 维修指导**：搜索家居维修知识库，返回详细的维修步骤和注意事项
- **🔌 多平台支持**：支持 CodeBuddy、Trae、Qoder 等主流 AI 助手
- **📦 易于扩展**：JSON 格式数据，方便添加和维护知识库
- **🔀 多种使用方式**：可作为 Skill 使用，也可作为独立脚本或 MCP Server

## 🚀 安装方式

### 方式一：安装到 AI 助手（推荐）

将 Skill 目录放到 AI 助手的 skills 目录：

#### CodeBuddy
```bash
# 将整个项目复制到 CodeBuddy skills 目录
cp -r home-advisor ~/.codebuddy/skills/
```

#### Trae / Qoder
参考对应平台的 Skill 安装文档，将 Skill 文件放到指定目录。

**通用步骤：**
1. 将本项目的 `skill.json` 和 `SKILL.md` 放到 AI 助手的 skills 目录
2. 确保 `scripts/` 目录中的脚本可以被 AI 助手访问
3. 根据需要配置 `config.json`（可选）

### 方式二：作为 MCP Server 使用

运行 MCP Server，使其可以被支持 MCP 的 AI 助手调用：

```bash
# 安装依赖（如果需要）
pip install mcp

# 运行 MCP Server
python mcp_server.py
```

然后在 AI 助手中配置此 MCP Server（参考各 AI 助手的 MCP 配置文档）。

### 方式三：独立使用

直接使用 Python 脚本搜索菜品或维修指导：

```bash
# 搜索菜品
python scripts/search_dishes.py --query "鸡"
python scripts/search_dishes.py --query "西红柿" --limit 3

# 搜索维修指导
python scripts/search_repair.py --query "水龙头"
python scripts/search_repair.py --query "漏水" --limit 2
```

## 📦 项目结构

```
home-advisor/
├── README.md                  # 本文件
├── LICENSE                    # MIT 许可证
├── CONFIG.md                  # 配置说明
├── config.json.example        # 配置示例
├── skill.json                 # Skill 元数据
├── SKILL.md                   # Skill 使用说明
├── scripts/                   # 搜索脚本
│   ├── search_dishes.py       # 搜索菜品
│   └── search_repair.py       # 搜索维修指导
├── references/                # 参考文档
│   └── api-format.md          # API 格式说明
├── mcp_server.py              # MCP Server 实现
├── test_search.py             # 测试脚本
└── data/                      # 数据文件
    ├── dishes-index.json      # 菜品数据
    └── repair-index.json      # 维修数据
```

## 💬 使用场景

在任意支持 Skill 的 AI 助手中，通过对话触发：

### 菜品推荐
- "推荐一些家常菜"
- "怎么做宫保鸡丁？"
- "我想吃鸡，有什么做法？"

### 维修指导
- "水龙头漏水怎么办？"
- "墙面裂缝如何修复？"
- "马桶堵塞怎么处理？"

AI 助手会自动调用相应的搜索脚本，并返回结构化的结果。

## 📊 数据格式

### 菜品数据格式 (dishes-index.json)

```json
[
  {
    "id": "unique-id",
    "source": "数据源名称",
    "title": "菜品名称",
    "file": "文件路径",
    "content": "菜品详细内容（做法、技巧等）",
    "url": "在线链接（可选）"
  }
]
```

### 维修数据格式 (repair-index.json)

```json
[
  {
    "id": "unique-id",
    "source": "数据源名称",
    "title": "维修项目标题",
    "file": "文件路径",
    "content": "维修详细步骤和注意事项",
    "url": "在线链接（可选）"
  }
]
```

## ⚙️ 配置

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

## 📄 许可证

本项目采用 **MIT License** 开源。

数据文件中的内容可能有各自的许可证，请参考具体数据源的许可证。

## 🙏 致谢

- 数据来源：
  - [宸良的家常菜](https://sapchen.cn/Chenliang-Home-Dishes/) - 菜品数据
  - [家庭维修手册](https://sapchen.cn/home-repair-manual/) - 维修指导数据
- Skill 规范：感谢各 AI 助手平台提供的 Skill 标准
- MCP 协议：[Model Context Protocol](https://modelcontextprotocol.io/)

## 📧 联系方式

如有问题或建议，欢迎：

- 提交 Issue
- 发送邮件至：271203081@qq.com
- 在相关社区讨论
