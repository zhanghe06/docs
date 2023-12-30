# PIP

## 安装

CentOS

```
yum install -y python-pip
```

MacOS

```

```

## 离线处理依赖

```
# 导出
pip download -d my_env_pkgs/ -r requirements.txt
# 加载（一定要使用绝对路径，所以有三个/）
pip install -r requirements.txt --no-index -f file:///home/user_name/my_env_pkgs
pip install -r requirements.txt --no-index -f ./env_pkgs
```

创建本地源

```
# 安装pip2pi模块
pip install pip2pi
# 建立索引（my_env_pkgs目录下会多出一个simple文件夹）
dir2pi ~/my_env_pkgs/
# 进入目标文件夹（就是对外发布的文件夹，因为开启HTTP Server是将当前文件夹发布）
cd ~/my_env_pkgs/simple/
# 开启HTTP Server - Python3
python -m http.server
# 开启HTTP Server - Python2
python -m SimpleHTTPServer
```

[http://127.0.0.1:8000](http://127.0.0.1:8000)

```
pip install -i http://127.0.0.1:8000 -r requirements.txt
```

## 排错`ImportError: No module named main`

pip2重装

```
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
sudo python get-pip.py --force-reinstall
```

pip3重装

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py --force-reinstall
```

## 清理所有软件包

```
pip freeze | xargs pip uninstall -y
```

## virtualenv

[installing-using-pip-and-virtual-environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

virtualenv --no-site-packages .venv -p python2
