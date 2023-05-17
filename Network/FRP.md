# FRP (Fast Reverse Proxy)

内网穿透

项目地址: [https://github.com/fatedier/frp](https://github.com/fatedier/frp)

文档地址: [https://gofrp.org/docs](https://gofrp.org/docs)

常用场景: 通过自定义域名访问内网的 Web 服务 [https://gofrp.org/docs/examples/vhost-http/](https://gofrp.org/docs/examples/vhost-http/)

下载最新版 [https://github.com/fatedier/frp/releases/download/v0.37.1/frp_0.37.1_linux_arm64.tar.gz](https://github.com/fatedier/frp/releases/download/v0.37.1/frp_0.37.1_linux_arm64.tar.gz)


## 安装

- **客户端 (MacOS)**
```
wget -c https://github.com/fatedier/frp/releases/download/v0.37.1/frp_0.37.1_darwin_amd64.tar.gz
tar -zxvf frp_0.37.1_darwin_amd64.tar.gz
cd frp_0.37.1_darwin_amd64
```

- **客户端 (RockPi)**
```
wget -c https://github.com/fatedier/frp/releases/download/v0.37.1/frp_0.37.1_linux_arm64.tar.gz
tar -zxvf frp_0.37.1_linux_arm64.tar.gz
cd frp_0.37.1_linux_arm64
```

frpc.ini
```
[common]
server_addr = x.x.x.x
server_port = 7000
token = 123456

[web]
type = tcp
local_ip = 127.0.0.1
local_port = 8000
remote_port = 8000
```

- **服务端 (Linux)**
```
wget -c https://github.com/fatedier/frp/releases/download/v0.37.1/frp_0.37.1_linux_amd64.tar.gz
tar -zxvf frp_0.37.1_linux_amd64.tar.gz
cd frp_0.37.1_linux_amd64
```

frps.ini
```
[common]
bind_port = 7000
token = 123456
```

公网服务器防火墙开放 7000、8000 端口

测试访问公网 [http://x.x.x.x:8000](http://x.x.x.x:8000) 转发到本地即成功

配置开机启动

服务端
```
/usr/bin/frps                       # 二进制服务端工具
/etc/frp/frps.ini                   # 服务端的配置文件
/etc/systemd/system/frps.service    # 开机启动配置文件

systemctl daemon-reload
systemctl enable frps
systemctl start frps
```

客户端
```
/usr/bin/frpc
/etc/frp/frpc.ini
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
