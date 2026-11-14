# <p align="center"> MCArchive API for Python <img src="https://gitee.com/AngryMouse7891/mcarchive-api-python/badge/star.svg?theme=dark" alt="star" /> <img src="https://gitee.com/AngryMouse7891/mcarchive-api-python/badge/fork.svg?theme=dark" alt="star" /> <img src="https://img.shields.io/github/stars/AngryMouse7891/mcarchive-api-python" alt="GitHub Stars" /> <img src="https://img.shields.io/github/forks/AngryMouse7891/mcarchive-api-python" alt="GitHub Forks" /> <img src="https://img.shields.io/pypi/v/mcarchive-api" alt="latest"/> </p>

!!! warning
    This library has no affication with MCArchive.

## Introduction

This is a Python library that allows developers to interact with the MCArchive API, using [`httpx`](https://pypi.org/project/httpx/) for API requests and [`urllib`](https://pypi.org/project/urllib/) to convert variables into URL parameters.

## Installation

Install via the `pip` package manager:

```bash
pip install mcarchive-api
poetry install mcarchive-api # or use Poetry
uv pip install mcarchive-api # or use uv
```

You can also download the wheel and install it:

```bash
pip install ./mcarchive_api-x.x.x-py3-none-any.whl
```

Or clone the Git repository and build the wheel:

```bash
git clone https://github.com/AngryMouse7891/mcarchive-api-python.git
cd mcarchive-api-python
uv build
```

## How to Use

Here are the descriptions of all the modules in this library:

- `mcarchive_api.default`: Get Minecraft game versions and authors

- `mcarchive_api.mods`: Get all mods or fetch them using a specific slug

- `mcarchive_api.files`: Get files by filename/SHA256 hash

For example, to get all Minecraft game versions:

```python
from mcarchive_api.default import get_game_versions

print(f'Game Versions: {get_game_versions()}')
```

## Dependencies

| Package | Latest Version | Description |
| ------------------------------------------- | ------------------------------------------ | ------------------------- |
| [`httpx`](https://pypi.org/project/httpx) | ![latest](https://img.shields.io/pypi/v/httpx) | HTTP client |
| [`urllib3`](https://pypi.org/project/httpx) | ![latest](https://img.shields.io/pypi/v/urllib3) | HTTP library with thread-safe connection pooling, file uploads, and more |
| [`colorama`](https://pypi.org/project/colorama) | ![latest](https://img.shields.io/pypi/v/colorama) | Colored text output |

## Open Source License

Uses the [MIT License](https://choosealicense.com/licenses/mit/).
