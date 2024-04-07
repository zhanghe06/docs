# Poetry

[https://github.com/python-poetry/poetry](https://github.com/python-poetry/poetry)

[https://python-poetry.org/docs/#installing-with-the-official-installer](https://python-poetry.org/docs/#installing-with-the-official-installer)

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

## MacOS环境 安装poetry过程中报错 `SSL: CERTIFICATE_VERIFY_FAILED`

```
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
```

查看默认证书位置
```
➜  ~ python3
Python 3.10.11 (v3.10.11:7d4cc5aa85, Apr  4 2023, 19:05:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ssl
>>> print(ssl.get_default_verify_paths())
DefaultVerifyPaths(cafile=None, capath=None, openssl_cafile_env='SSL_CERT_FILE', openssl_cafile='/Library/Frameworks/Python.framework/Versions/3.10/etc/openssl/cert.pem', openssl_capath_env='SSL_CERT_DIR', openssl_capath='/Library/Frameworks/Python.framework/Versions/3.10/etc/openssl/certs')
>>>
```

发现文件不存在

下载CA
```
➜  ~ ls /Library/Frameworks/Python.framework/Versions/3.10/etc/openssl
➜  ~ 
➜  ~ cd /Library/Frameworks/Python.framework/Versions/3.10/etc/openssl
➜  openssl ls
➜  openssl mkdir -p certs
➜  openssl wget http://curl.haxx.se/ca/cacert.pem -O cert.pem
➜  openssl ls
cert.pem certs
```
