# FRP (Fast Reverse Proxy)

内网穿透

frp 采用 C/S 模式, 通过访问暴露在服务器上的端口, 反向代理到处于内网的服务:
- 服务端 部署在具有公网 IP 的机器上
- 客户端 部署在内网或防火墙内的机器上

项目地址: [https://github.com/fatedier/frp](https://github.com/fatedier/frp)

文档地址: [https://gofrp.org/zh-cn](https://gofrp.org/zh-cn)

常用场景: 通过自定义域名访问内网的 Web 服务 [https://gofrp.org/docs/examples/vhost-http/](https://gofrp.org/docs/examples/vhost-http/)

下载最新版 [https://github.com/fatedier/frp/releases/download/v0.52.3/frp_0.52.3_linux_arm64.tar.gz](https://github.com/fatedier/frp/releases/download/v0.52.3/frp_0.52.3_linux_arm64.tar.gz)


## 安装

- **客户端 (MacOS Intel)**
```
wget -c https://github.com/fatedier/frp/releases/download/v0.52.3/frp_0.52.3_darwin_amd64.tar.gz
tar -zxvf frp_0.52.3_darwin_amd64.tar.gz
cd frp_0.52.3_darwin_amd64
```

- **客户端 (MacOS Apple Silicon)**
```
wget -c https://github.com/fatedier/frp/releases/download/v0.52.3/frp_0.52.3_darwin_arm64.tar.gz
tar -zxvf frp_0.52.3_darwin_arm64.tar.gz
cd frp_0.52.3_darwin_arm64
```

- **客户端 (RockPi)**
```
wget -c https://github.com/fatedier/frp/releases/download/v0.52.3/frp_0.52.3_linux_arm64.tar.gz
tar -zxvf frp_0.52.3_linux_arm64.tar.gz
cd frp_0.52.3_linux_arm64
```

frpc.toml
```
serverAddr = "x.x.x.x"
serverPort = 7000

[[proxies]]
name = "ssh"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 6000

[[proxies]]
name = "web"
type = "tcp"
localIP = "127.0.0.1"
localPort = 8080
remotePort = 58080
```

- **服务端 (Linux)**
```
wget -c https://github.com/fatedier/frp/releases/download/v0.52.3/frp_0.52.3_linux_amd64.tar.gz
tar -zxvf frp_0.52.3_linux_amd64.tar.gz
cd frp_0.52.3_linux_amd64
```

frps.toml
```
bindAddr = "0.0.0.0"
bindPort = 7000

webServer.addr = "0.0.0.0"
webServer.port = 7500
# dashboard 用户名密码，可选，默认为空
webServer.user = "admin"
webServer.password = "admin"
```

公网服务器防火墙开放 7000、8000 端口

测试访问公网 [http://x.x.x.x:8000](http://x.x.x.x:8000) 转发到本地即成功

配置开机启动

服务端
```
/usr/bin/frps                       # 二进制服务端工具
/etc/frp/frps.toml                  # 服务端的配置文件
/etc/systemd/system/frps.service    # 开机启动配置文件

systemctl daemon-reload
systemctl enable frps
systemctl start frps
```

客户端
```
/usr/bin/frpc
/etc/frp/frpc.toml
/etc/systemd/system/frpc.service

systemctl daemon-reload
systemctl enable frpc
systemctl start frpc
```

```
+-------+ +-------+
|user 01| |user 02|
+---+---+ +---+---+
    |         |
+-Public  Network-+
|  +-----|-----+  |
|  |FRP  SERVER|  |
|  |Remote Port|  |
+--|----| |----|--+
|  |Local  Port|  |
|  |FRP  CLIENT|  |
|  +-----|-----+  |
+-Private Network-+
```


## 使用 systemd

[https://gofrp.org/zh-cn/docs/setup/systemd](https://gofrp.org/zh-cn/docs/setup/systemd)

```
$ sudo vim /etc/systemd/system/frps.service
```

```
[Unit]
# 服务名称，可自定义
Description = frp server
After = network-online.target syslog.target
Wants = network-online.target

[Service]
Type = simple
# 启动frps的命令，需修改为您的frps的安装路径
ExecStart = /usr/bin/frps -c /etc/frp/frps.toml
Restart = always
RestartSec = 30s

[Install]
WantedBy = multi-user.target
```

```
# 配置开机启动
sudo systemctl enable frps
# 启动frp
sudo systemctl start frps
# 停止frp
sudo systemctl stop frps
# 重启frp
sudo systemctl restart frps
# 查看frp状态
sudo systemctl status frps
```
