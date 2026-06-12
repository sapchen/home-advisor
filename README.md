# 家居顾问 Skill (Home Advisor)

一个通用的 AI 助手 Skill，为 AI 提供家居知识搜索能力，包括菜品推荐和家居维修指导。

本 Skill 遵循标准 Skill 规范，可无缝集成到支持 Skill 的 AI 编程助手，包括：
- **CodeBuddy**
- **Trae**
- **Qoder**
- 其他支持标准 Skill 的 AI 助手

## ✨ 功能特性

- **🍳 菜品推荐**：搜索家常菜谱数据库，返回详细的做法和技巧
- **🔧 维修指导**：搜索家居维修知识库，返回详细的维修步骤和注意事项
- **🔌 多平台支持**：支持 CodeBuddy、Trae、Qoder 等主流 AI 助手
- **📦 易于扩展**：JSON 格式数据，方便添加和维护知识库
- **🔀 多种使用方式**：可作为 Skill 使用，也可作为独立脚本或 MCP Server

## 🚀 安装方式

### 方式一：安装到 AI 助手（推荐）

每种 AI 助手的安装方式可能略有不同，但基本原理相同：

#### CodeBuddy
将 Skill 目录放到 CodeBuddy 的 skills 目录：
```bash
# 方法1：直接复制到 CodeBuddy skills 目录
cp -r .codebuddy/skills/home-advisor ~/.codebuddy/skills/

# 方法2：在 CodeBuddy 中通过命令安装（如果支持）
# 具体命令请参考 CodeBuddy 文档
```

#### Trae
参考 Trae 的 Skill 安装文档，通常也是将 Skill 目录放到指定位置。

#### Qoder
参考 Qoder 的 Skill 安装文档，按照其规范放置 Skill 文件。

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
├── .gitignore                # Git 忽略文件
│
├── skill.json                # Skill 元数据分析（通用格式）
├── SKILL.md                  # Skill 使用说明（通用格式）
├── scripts/                  # 搜索脚本
│   ├── search_dishes.py      # 搜索菜品
│   └── search_repair.py      # 搜索维修指导
├── references/               # 参考文档
│   └── api-format.md         # API 格式说明
│
├── mcp_server.py             # MCP Server 实现（可选）
├── test_search.py            # 测试脚本
└── data/                     # 数据文件
    ├── dishes-index.json     # 菜品数据
    └── repair-index.json     # 维修数据
```

**注意**：
- `skill.json` 和 `SKILL.md` 是 Skill 的核心配置文件，放在根目录以符合通用规范
- 脚本位于 `scripts/` 目录
- 数据文件统一放在 `data/` 目录
- 可以通过环境变量 `HOME_ADVISOR_DATA_DIR` 或配置文件 `config.json` 自定义数据目录

## 💬 使用场景

在任意支持 Skill 的 AI 助手中，通过对话触发：

### 菜品推荐
- "推荐一些家常菜"
- "怎么做宫保鸡丁？"
- "我想吃鸡，有什么做法？"
- "搜索西红柿的做法"

### 维修指导
- "水龙头漏水怎么办？"
- "墙面裂缝如何修复？"
- "马桶堵塞怎么处理？"
- "搜索水龙头维修方法"

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

**字段说明：**
- `id`：唯一标识符
- `source`：数据来源（如"宸良家常菜"）
- `title`：菜品名称
- `file`：原始文件路径
- `content`：菜品详细内容（搜索基于此字段）
- `url`：在线查看链接（可选）

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

**字段说明：**
- `id`：唯一标识符
- `source`：数据来源（如"家居维修指南"）
- `title`：维修项目标题
- `file`：原始文件路径
- `content`：维修详细步骤（搜索基于此字段）
- `url`：在线查看链接（可选）

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

## 🔧 扩展知识库

### 添加新菜品

1. 准备菜品数据（Markdown 格式）
2. 将数据添加到 `dishes-index.json`
3. 确保 `content` 字段包含完整的做法和技巧

### 添加新维修项目

1. 准备维修指导（Markdown 格式）
2. 将数据添加到 `repair-index.json`
3. 确保 `content` 字段包含详细的步骤和注意事项

### 批量导入

可以编写脚本将现有数据（如 Markdown 文件、数据库等）批量转换为 JSON 格式。

## 🌟 使用示例

### 示例 1：在 AI 助手中使用

**用户：** "推荐一些家常菜"

**AI：** "我为您找到了以下菜品：
1. 柠檬辣子烤虾 - 利用柠檬皮精油去腥...
2. 西红柿洋葱煎牛排 - 平底锅煎制...
..."

**用户：** "水龙头漏水怎么办？"

**AI：** "我为您找到了以下维修指导：
1. 水龙头密封圈更换 - 关闭水源，拆卸水龙头...
..."

### 示例 2：作为独立脚本使用

```bash
python scripts/search_dishes.py --query "鸡"
```

**输出：**
```
找到 3 个与 '鸡' 相关的菜品：

1. 柠檬辣子烤虾
   文件：1-煎烤/1-柠檬辣子烤虾.md
   链接：https://example.com/...
   简介：柠檬先削皮，然后切片...

2. 洋葱煎牛排
   文件：1-煎烤/3-洋葱煎牛排.md
   ...
```

### 示例 3：作为 MCP Server 使用

配置好 MCP Server 后，AI 助手会自动调用相关工具。

## 🤝 贡献

欢迎贡献！您可以：

- 🐛 报告 Bug
- 💡 提出新功能建议
- 📖 完善文档
- 🍳 添加更多菜品数据
- 🔧 添加更多维修指导
- 💻 改进代码
- 🌐 支持更多 AI 助手平台

### 贡献步骤

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 许可证

本项目采用 **MIT License** 开源。

数据文件中的内容可能有各自的许可证，请参考具体数据源的许可证。

## 🙏 致谢

- 数据来源：[宸良的家常菜](https://sapchen.cn/Chenliang-Home-Dishes/)
- Skill 规范：感谢各 AI 助手平台提供的 Skill 标准
- MCP 协议：[Model Context Protocol](https://modelcontextprotocol.io/)

## 📧 联系方式

如有问题或建议，欢迎：

- 提交 Issue
- 发送邮件至：[271203081@qq.com]
- 在相关社区讨论

---
