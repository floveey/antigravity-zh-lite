# Antigravity zh-CN Lite

Google Antigravity 桌面端的轻量中文翻译层。纯 Python 标准库，不打包 exe，不依赖 Node/asar 工具。

- 一键翻译：`translate.bat`
- 一键恢复官方：`restore.bat`
- Antigravity 更新后重新解包并翻译：`python antigravity_zh.py --update`

> 与 Google 无关，使用风险自负。脚本会修改 Antigravity 安装目录下的 `preload.js` / `menu.js`。

## 特点

- 词库约 1300 条，覆盖主界面、设置、权限、模型、MCP、会话、项目等
- 右键菜单、应用菜单、托盘菜单走同一套翻译
- 翻译 `title` / `placeholder` / `aria-label` / `data-tooltip` / `alt` / 按钮 `value`
- 保护代码、终端、diff、输入框和模型输出，不翻译文件路径和思考正文
- 扩展/插件名称保留英文
- 无网络请求、无遥测、无第三方依赖

## 环境要求

- Windows 10/11 x64
- Python 3.8+
- Antigravity 安装在默认路径：`%LOCALAPPDATA%\Programs\antigravity`
- 非默认安装路径可用 `--dist` 指定

## 快速开始

1. **完全退出 Antigravity**（包括托盘里的 Quit，确保没有 `Antigravity.exe` 进程）
2. 双击 `translate.bat`
3. 重新启动 Antigravity

或者用命令行：

```bash
python antigravity_zh.py --update
```

首次运行会把 `app.asar` 解包到 `resources/app`，并把原 asar 改名为 `app.asar.disabled`，然后注入翻译。之后修改词库只需重新运行同一命令。

## Antigravity 更新后

更新程序会写入新的 `app.asar`，翻译会失效。完全退出 Antigravity 后，重新运行：

```bash
python antigravity_zh.py --update
```

脚本会重新解包新版本并再次注入。检测到 Antigravity 正在运行时会拒绝执行。

## 恢复

| 命令 | 作用 |
|---|---|
| 双击 `restore.bat` / `python restore_official.py` | **完全恢复官方**：还原 `app.asar`，删除解包目录 |
| `python antigravity_zh.py --restore` | 只移除翻译注入，保留解包目录 |

恢复前同样需要完全退出 Antigravity。

## 命令行参数

### antigravity_zh.py

| 参数 | 说明 |
|---|---|
| 无参数 | 对已解包的目录注入/更新翻译 |
| `--update` | 更新后重新解包 `app.asar`，再注入翻译（推荐始终使用） |
| `--restore` | 只移除翻译块 |
| `--dry-run` | 只显示将要执行的操作 |
| `--dist PATH` | 指定 `resources/app/dist` 路径 |

### restore_official.py

| 参数 | 说明 |
|---|---|
| 无参数 | 恢复官方 `app.asar` 并删除解包目录 |
| `--dry-run` | 只显示将要执行的操作 |
| `--dist PATH` | 指定 `resources/app/dist` 路径 |

## 工作原理

1. 读取 `resources/app.asar`，用纯 Python 解包到 `resources/app`
2. 把原 `app.asar` 改名为 `app.asar.disabled`，让 Electron 加载解包目录
3. 在 `dist/preload.js` 末尾追加 DOM 翻译器
4. 在 `dist/menu.js` 末尾追加原生菜单翻译 hook
5. 翻译器只匹配精确词条和少量固定正则，不翻译任意英文句子

## 已知限制

- 仅测试 Windows x64；macOS 未测试
- Antigravity 更新后必须重跑 `--update`
- 词库未覆盖的新文案会保持英文
- 原生菜单只能翻译 map 里已有的标签
- 扩展/插件名称按设计保留英文

## 致谢

- [MIMICTE/Antigravity-zh-CN](https://github.com/MIMICTE/Antigravity-zh-CN)：词库基础与注入思路（MIT）
- PR [#9](https://github.com/MIMICTE/Antigravity-zh-CN/pull/9)（@bitterSmilezzz）、PR [#5](https://github.com/MIMICTE/Antigravity-zh-CN/pull/5)（@NKBaa）：部分词条
- Antigravity 由 Google 开发，本项目与 Google 无关

## License

MIT，见 [LICENSE](LICENSE)。
