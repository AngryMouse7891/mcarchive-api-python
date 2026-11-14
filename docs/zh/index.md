# <p align="center"> MCArchive API for Python <img src="https://gitee.com/AngryMouse7891/mcarchive-api-python/badge/star.svg?theme=dark" alt="star" /> <img src="https://gitee.com/AngryMouse7891/mcarchive-api-python/badge/fork.svg?theme=dark" alt="star" /> <img src="https://img.shields.io/github/stars/AngryMouse7891/mcarchive-api-python" alt="GitHub Stars" /> <img src="https://img.shields.io/github/forks/AngryMouse7891/mcarchive-api-python" alt="GitHub Forks" /> <img src="https://img.shields.io/pypi/v/mcarchive-api" alt="latest"/> </p>

!!! warning
    这个库与 MCArchive 没有任何关联。

## 简介

这是一个允许开发者与MCArchive API交互的Python库，使用[`httpx`](https://pypi.org/project/httpx/)进行API交互，[`urllib`](https://pypi.org/project/urllib/)库作为变量转URL参数。

## 安装

通过`pip`包管理器安装：

```bash
pip install mcarchive-api
poetry install mcarchive-api #或者使用Poetry
uv pip install mcarchive-api #或者使用uv
```

你也可以下载轮子并安装：

```bash
pip install ./mcarchive_api-x.x.x-py3-none-any.whl
```

或者克隆Git仓库并构建轮子：

```bash
git clone https://github.com/AngryMouse7891/mcarchive-api-python.git
cd mcarchive-api-python
uv build
```

## 使用方法

以下是该库所有模块的描述：

- `mcarchive_api.default`：获取Minecraft游戏版本和作者

- `mcarchive_api.mods`：获取所有模组以及通过特定slug获取

- `mcarchive_api.files`：通过文件名/SHA256哈希值获取文件

比如获取所有Minecraft游戏版本：

```python
from mcarchive_api.default import get_game_versions

print(f'Game Versions: {get_game_versions()}')
```

## 使用的依赖

| 包名                                          | 最新版本                                       | 描述                        |
| ------------------------------------------- | ------------------------------------------ | ------------------------- |
| [`httpx`](https://pypi.org/project/httpx)   | ![latest](https://img.shields.io/pypi/v/httpx)   | HTTP客户端                   |
| [`urllib3`](https://pypi.org/project/httpx) | ![latest](https://img.shields.io/pypi/v/urllib3) | 带有线程安全连接池、文件上传等功能的 HTTP 库 |

## 开源许可

使用[MIT许可证](https://choosealicense.com/zh/licenses/mit/)。
