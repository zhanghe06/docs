# Goland

## 常规配置

Terminal环境变量（解决终端显示git log中文乱码的问题）
```
File > Settings > Tools > Terminal > Project Settings > Environment variables: LESSCHARSET=utf-8
```

保存自动格式化代码
```
File > Settings > Tools > Actions on Save > 勾选：Reformat code 和 Optimize imports
```

git换行符配置
```
git config --global core.autocrlf false
```

切换格式化风格
```
File > Settings > Editor > Code Style > Go > Imports > Sorting type: goimports
```

## 远程开发（goland 2021.3 之前版本）

最佳实践：
1. 本地拉取/推送代码仓库
2. 本地推送到远端机（包含.git）
3. 远端依赖本地，本地依赖代码仓库，整体形成单线依赖，避免循环依赖

配置
```
Tools > Deployment > Configuration

# 连接配置
Connection
    Visible only for this project: 取消选中
    Type: SFTP
    SSH Configuration: root@10.4.133.58:22
    Root path: /root/code

# 设置默认（必须）
选中连接，打钩，设置默认，设置成功之后，字体变粗

# 映射配置
Mappings
    Local path: D:\code\<project_name>
    Deployment path: /<project_name>  # 注意：这里是 Root path 的相对目录
# 自动上传
Tools > Deployment > Options...
Exclude items by name: 去除.git，不然本地修改代码不会显示任何变化
Upload changed files automatically to the default server: On explicit save action(Ctrl+S) 或Always
```

拉取代码
```
Tools > Deployment > Download from...
```

上传代码
```
Tools > Deployment > Upload to...
```

远程执行
```
Tools > Start SSH Session...
或
底部Terminal 下拉选择 root@10.4.133.58:22，自动进入远程的机器
```

远程调试
```
# 远端安装工具
yum install gcc
yum install gcc-c++
go install github.com/go-delve/delve/cmd/dlv@latest
dlv version

# 方式一：直接用dlv启动go服务进程
dlv --listen=:2345 --headless=true --api-version=2 --accept-multiclient --check-go-version=false exec ./bin/<project_build_file>
# 方式二：将dlv server attach到已经运行的go服务进程上
dlv --listen=:8016 --headless=true --api-version=2 --log attach 13935  # 注意 8016端口是 dlv server的监听端口，这里的端口范围可以在8000-8100之间，注意别跟机器上的服务端口冲突即可

# 补充说明：对应的端口需要开放

# 调试设置
Run > Debug > Edit Configuration > Add New Configuration > Go Remote 
```

## 远程开发（goland 2021.3 以及之后版本）


## 必装插件

- Git 分支视图

## 快捷键

- 向前、向后：Command(ctl) + option(alt) + ←、→
- 快速搜索文件：shift 两次

## Projector 远程方案

JetBrains 说 Projector 是一种技术，而不是最终用户解决方案。

参考：https://jishuin.proginn.com/p/763bfbd543f7

```
docker pull registry.jetbrains.team/p/prj/containers/projector-goland
docker run --rm -p 8887:8887 -it registry.jetbrains.team/p/prj/containers/projector-goland
docker run -d -p 8887:8887 -v xxx:/usr/local/go registry.jetbrains.team/p/prj/containers/projector-goland
```

## 多版本安装

[https://go.dev/dl/](https://go.dev/dl/)

### Linux|MacOS 环境

版本 | 路径
--- | ---
1.16 | [/usr/local/go1.16](https://go.dev/dl/go1.16.15.darwin-amd64.tar.gz)
1.18 | [/usr/local/go1.18](https://go.dev/dl/go1.18.10.darwin-amd64.tar.gz)
1.20 | [/usr/local/go1.20](https://go.dev/dl/go1.20.12.darwin-amd64.tar.gz)

```
# 下载二进制版本
wget https://go.dev/dl/go1.16.15.darwin-amd64.tar.gz
wget https://go.dev/dl/go1.18.10.darwin-amd64.tar.gz
wget https://go.dev/dl/go1.20.12.darwin-amd64.tar.gz
# 解压至指定目录并重命名
tar -zxvf go1.16.15.darwin-amd64.tar.gz -C /usr/local --transform='s/go/go1.16/'
tar -zxvf go1.18.10.darwin-amd64.tar.gz -C /usr/local --transform='s/go/go1.18/'
tar -zxvf go1.20.12.darwin-amd64.tar.gz -C /usr/local --transform='s/go/go1.20/'
```

```
# 下载二进制版本
wget https://go.dev/dl/go1.16.15.darwin-arm64.tar.gz
wget https://go.dev/dl/go1.18.10.darwin-arm64.tar.gz
wget https://go.dev/dl/go1.20.12.darwin-arm64.tar.gz
# 解压至指定目录并重命名
tar -zxvf go1.16.15.darwin-arm64.tar.gz -C /usr/local --transform='s/go/go1.16/'
tar -zxvf go1.18.10.darwin-arm64.tar.gz -C /usr/local --transform='s/go/go1.18/'
tar -zxvf go1.20.12.darwin-arm64.tar.gz -C /usr/local --transform='s/go/go1.20/'
```

环境变量 `~/.zshrc`
```
# Go1.16
export GOROOT=/usr/local/go1.16
export GOPATH=$HOME/go1.16

# Go1.18
# export GOROOT=/usr/local/go1.18
# export GOPATH=$HOME/go1.18

# Go1.20
# export GOROOT=/usr/local/go1.20
# export GOPATH=$HOME/go1.20

export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
```

### Windows 环境

```
# 选择版本
set GOROOT=D:\go1.16.15.windows-amd64\go
set GOPATH=D:\go1.16

set GOROOT=D:\go1.18.10.windows-amd64\go
set GOPATH=D:\go1.18

set PATH=%GOROOT%\bin;%GOPATH%\bin;%PATH%
```

您可以按照以下步骤在Windows上配置多个版本的Golang：

1. 下载和安装您需要的Golang版本。
2. 将每个版本的Golang安装到不同的文件夹中。
3. 在环境变量中设置每个版本的Golang路径。
   - 右键单击“此电脑”，选择“属性”。
   - 单击“高级系统设置”。
   - 单击“环境变量”。
   - 在“系统变量”下，单击“新建”。
   - 输入变量名为“GOROOT”，变量值为Golang的安装路径。
4. 在环境变量中设置GOPATH。
   - 在“系统变量”下，找到“GOPATH”变量，如果不存在则新建。
   - 将GOPATH设置为您的工作空间路径。
5. 在PATH环境变量中添加每个版本的Golang路径。
   - 在“系统变量”下，找到“Path”变量，双击打开编辑窗口。
   - 将每个版本的Golang路径添加到“Path”变量中，用分号分隔。

完成上述步骤后，您就可以在命令行中使用不同版本的Golang了。例如，要在命令行中使用Golang 1.16，您可以输入以下命令：

```
set GOROOT=D:\go1.16.15.windows-amd64\go
set GOPATH=D:\go1.16
```

然后您就可以使用Golang 1.16了。


### 编辑器配置
```
Settings > Go > GOROOT > 选择项目对应的SDK版本
Settings > Go > GOPATH > 取消勾选"Use GOPATH that's defined in system environment"；在Project GOPATH中添加对应版本的GOPATH路径
```
