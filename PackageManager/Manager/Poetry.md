# Poetry

[https://github.com/python-poetry/poetry](https://github.com/python-poetry/poetry)

```
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="/Users/zhanghe/.local/bin:$PATH"' >> ~/.zshrc
poetry --version
```

```
export POETRY_PYPI_MIRROR_URL=https://mirrors.aliyun.com/pypi/simple/
```

常用命令
```
poetry new <project_name>                   # 创建指定名称新项目
poetry init                                 # 初始化已存在的项目
poetry config virtualenvs.in-project true   # 项目根目录生成.venv虚拟目录
poetry env list                             # 显示所有虚拟环境列表
poetry env info                             # 显示当前虚拟环境信息
poetry check                                # 检查 pyproject.toml 配置是否正确
poetry shell                                # 进入虚拟环境
poetry add <dependency_name>                # 安装依赖
poetry remove <dependency_name>             # 删除依赖
poetry show
poetry show --tree

poetry lock --no-update                     # 重新生成poetry.lock
poetry install --no-root                    # 安装全部模块，同步到虚拟环境
poetry update                               # 更新全部模块

poetry export --with=dev --without-hashes -o requirements.txt
```
