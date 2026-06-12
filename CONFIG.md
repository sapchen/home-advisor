# 配置说明

本文档说明如何配置家居顾问工具。

## 配置文件

### 1. 环境变量（最高优先级）

设置环境变量 `HOME_ADVISOR_DATA_DIR` 指向数据目录：

**Windows (PowerShell):**
```powershell
$env:HOME_ADVISOR_DATA_DIR = "C:\path\to\data"
```

**Linux/macOS:**
```bash
export HOME_ADVISOR_DATA_DIR="/path/to/data"
```

### 2. 配置文件 config.json（中等优先级）

在项目根目录创建 `config.json`：

```json
{
  "data_dir": "./data",
  "dishes_file": "dishes-index.json",
  "repair_file": "repair-index.json",
  "default_limit": 5
}
```

**字段说明：**
- `data_dir`: 数据文件所在目录（相对或绝对路径）
- `dishes_file`: 菜品数据文件名
- `repair_file`: 维修数据文件名
- `default_limit`: 默认返回结果数量

### 3. 默认路径（最低优先级）

如果未设置环境变量和配置文件，程序将按以下顺序查找数据文件：

1. `scripts/../data/` - 脚本所在目录的上级目录的 data 文件夹
2. `./data/` - 当前工作目录的 data 文件夹
3. 当前工作目录 - 直接在当前目录查找

## 数据文件格式

### dishes-index.json

菜品数据文件，格式如下：

```json
[
  {
    "id": "unique-id",
    "source": "数据源名称",
    "title": "菜品名称",
    "file": "文件路径",
    "content": "菜品详细内容",
    "url": "在线链接（可选）"
  }
]
```

### repair-index.json

维修数据文件，格式如下：

```json
[
  {
    "id": "unique-id",
    "source": "数据源名称",
    "title": "维修项目标题",
    "file": "文件路径",
    "content": "维修详细步骤",
    "url": "在线链接（可选）"
  }
]
```

## 示例配置

### 示例 1：使用默认配置

将数据文件放在 `./data/` 目录，无需任何配置。

### 示例 2：使用自定义数据目录

```bash
# 设置环境变量
export HOME_ADVISOR_DATA_DIR="/path/to/my/data"

# 运行
python scripts/search_dishes.py --query "鸡"
```

### 示例 3：使用配置文件

创建 `config.json`:

```json
{
  "data_dir": "/path/to/my/data",
  "default_limit": 10
}
```

## 故障排除

### 问题：找不到数据文件

**解决方案：**
1. 检查数据文件是否存在
2. 检查文件路径是否正确
3. 尝试使用绝对路径
4. 运行测试脚本：`python test_search.py`

### 问题：编码错误

**解决方案：**
确保数据文件使用 UTF-8 编码。

### 问题：权限错误

**解决方案：**
确保有读取数据文件的权限。
