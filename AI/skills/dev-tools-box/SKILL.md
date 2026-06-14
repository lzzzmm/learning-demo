---
name: dev-tools-box
description: 开发者工具箱 — 时间戳转换、Base64 编解码、JSON 格式化、URL 编解码、Hash 计算 (MD5/SHA256)、Cron 表达式验证。当用户提到时间戳转换、base64、json格式化、url编码、md5、sha256、cron表达式或任何开发者常见的格式转换时使用此技能。即使他们没说"工具箱"这个词，只要涉及开发者常用转换工具就使用。
---

# Developer Toolbox

## 原则

**Result-only mode**: 所有工具输出纯结果，不解释原理，不废话。直接输出转换结果。

## 工具列表

所有工具统一通过脚本执行：

```bash
python scripts/devtools.py <command> <input>
```

脚本路径相对于技能目录。

---

### 1. 时间戳工具 — `time`

| 输入 | 输出 |
|------|------|
| Unix 时间戳 (如 `1700000000`) | UTC 时间、本地时间、ISO8601 |
| 日期字符串 (如 `2024-01-01 12:00:00`) | UTC 时间、Unix 时间戳、ISO8601 |

**命令**: `python scripts/devtools.py time 1700000000`

---

### 2. Base64 工具 — `base64`

自动识别 encode / decode。

**命令**: `python scripts/devtools.py base64 SGVsbG8=`

---

### 3. JSON 格式化 — `json`

输入 minified JSON，输出缩进格式化 JSON。

**命令**: `python scripts/devtools.py json '{"a":1,"b":2}'`

---

### 4. URL 编解码 — `url`

自动识别 encode / decode。

**命令**: `python scripts/devtools.py url hello world`

---

### 5. Hash 工具 — `hash`

同时输出 MD5 和 SHA256。

**命令**: `python scripts/devtools.py hash hello`

---

### 6. Cron 表达式验证 — `cron`

输入 cron 表达式，输出未来 8 次执行时间（UTC）。

**命令**: `python scripts/devtools.py cron '*/5 * * * *'`

---

## 输出格式

每个工具的输出是纯结果文本，无额外解释。错误时输出到 stderr，stdout 为空。工具输出结束即结束响应。

## 错误处理

输入无效时返回简短错误信息，不展开解释。
