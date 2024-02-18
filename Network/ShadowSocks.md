# ShadowSocks

[https://github.com/shadowsocks/shadowsocks](https://github.com/shadowsocks/shadowsocks)

## [Vultr](https://www.vultr.com/?ref=7428701) CentOS 7 安装 ShadowSocks 方案

注册地址: [https://www.vultr.com](https://www.vultr.com/?ref=7428701)

注册账号, 开通云主机, 登录主机

```
**[terminal]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command ssh root@my_server_ip]
```

**常用工具安装**

CentOS
```
**[terminal]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command yum install -y epel-release]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command yum install -y python2-pip net-tools vim-enhanced git]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command pip2 install -U "pip < 21.0"]
```

> [!WARNING|label:版本支持]
> pip 21.0已于2021年1月停止对Python 2.7的支持

Ubuntu
```
export LC_ALL=C  # locale.Error: unsupported locale setting
apt-get install python-pip
```

**shadowsocks安装**
```
**[terminal]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command pip install git+https://github.com/shadowsocks/shadowsocks.git@master]
```

**服务配置**
```bash
cat << EOF > /etc/shadowsocks.json
{
    "server":"my_server_ip",
    "server_port":8282,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"mypassword",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
EOF
```

TCP快速打开（TCP Fast Open, TFO）

不建议开启tcp fast open功能

对于科学上网的人，TFO更是不建议开启。根据 shadowsocks-libev 的反馈，TFO在中国移动数据网络下不能正常工作，而且长城防火墙会识别和丢弃TFO的包，开启TFO只会自找麻烦。


**服务管理**
```
**[terminal]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command ssserver -c /etc/shadowsocks.json --user nobody -d start]**[prompt     # 启动]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command ssserver -c /etc/shadowsocks.json --user nobody -d stop]**[prompt      # 关闭]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command less /var/log/shadowsocks.log]**[prompt                                # 日志]
```

**修改防火墙规则**

方式一

vultr 默认是通过系统动态防火墙firewalld控制规则的

添加规则
```
**[terminal]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command firewall-cmd --zone=public --add-port=8282/tcp --permanent]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command firewall-cmd --zone=public --add-port=8282/udp --permanent]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command firewall-cmd --reload]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command firewall-cmd --list-ports]
8282/tcp 8282/udp 3128/tcp
```

删除规则
```
**[terminal]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command firewall-cmd --zone=public --remove-port=3128/tcp --permanent]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command firewall-cmd --reload]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command firewall-cmd --list-ports]
```

方式二

也可以先关闭系统动态防火墙firewalld
```
**[terminal]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command systemctl stop firewalld]**[prompt                                  # 关系统防火墙]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command systemctl disable firewalld]**[prompt                               # 取消开机启动]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command systemctl status firewalld]**[prompt                                # 查看关闭状态]
```
然后通过web管理界面添加防火墙规则，并将规则链接到实例


## Kcptun

[https://github.com/xtaci/kcptun](https://github.com/xtaci/kcptun)

[https://qinzc.me/post-201.html](https://qinzc.me/post-201.html)

[https://muyexi.im/shadowsocks_with_kcptun](https://muyexi.im/shadowsocks_with_kcptun)

```
mkdir kcptun
cd kcptun
wget https://github.com/xtaci/kcptun/releases/download/v20230214/kcptun-linux-amd64-20230214.tar.gz
tar zxvf kcptun-linux-amd64-20230214.tar.gz
```

- **服务端配置**

/etc/shadowsocks.json
```
{
    "server":"0.0.0.0",
    "server_port":3080,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"<shadowsocks_password>",
    "timeout":300,
    "method":"aes-256-cfb"
}
```

/etc/kcptun.json
```
{
    "listen": ":8282",
    "target": "127.0.0.1:3080",
    "key": "<kcptun_password>",
    "crypt": "aes",
    "mode": "fast2",
    "mtu": 1350,
    "sndwnd": 2048,
    "rcvwnd": 2048,
    "datashard": 10,
    "parityshard": 3
}
```

开启服务
```
# 启动 kcptun 客户端
./server_linux_amd64 -c /etc/kcptun.json
# 启动 shadowsocks 客户端
ssserver -c /etc/shadowsocks.json
```

开机启动
```
cp ~/kcptun/server_linux_amd64 /usr/bin/

cat >/etc/systemd/system/kcp-server.service <<EOF
[Unit]
Description=Kcptun server
After=network.target

[Service]
ExecStart=/usr/bin/server_linux_amd64 -c /etc/kcptun.json
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl status kcp-server
systemctl enable kcp-server
systemctl restart kcp-server
```

- **客户端配置**

/etc/shadowsocks.json
```
{
    "server":"127.0.0.1",
    "server_port":2080,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"<shadowsocks_password>",
    "timeout":300,
    "method":"aes-256-cfb"
}
```

/etc/kcptun.json
```
{
    "localaddr": ":2080",
    "remoteaddr": "<kcptun_ip>:<kcptun_port>",
    "key": "<kcptun_password>",
    "crypt": "aes",
    "mode": "fast2",
    "mtu": 1350,
    "sndwnd": 2048,
    "rcvwnd": 2048,
    "datashard": 10,
    "parityshard": 3
}
```

连接服务
```
# 启动 kcptun 客户端
./client_linux_amd64 -c /etc/kcptun.json
# 启动 shadowsocks 客户端
sslocal -c /etc/shadowsocks.json --user nobody -d start     # 后台启动
sslocal -c /etc/shadowsocks.json                            # 前台启动
```

开机启动
```
cp ~/kcptun/client_linux_amd64 /usr/bin/

cat >/etc/systemd/system/kcp-client.service <<EOF
[Unit]
Description=Kcptun client
After=network.target

[Service]
ExecStart=/usr/bin/client_linux_amd64 -c /etc/kcptun.json
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl status kcp-client
systemctl enable kcp-client
systemctl restart kcp-client
```

## 使用代理

```
# 设置代理
export http_proxy=socks5://127.0.0.1:1080
export https_proxy=socks5://127.0.0.1:1080

# 设置代理
export http_proxy=http://127.0.0.1:1087
export https_proxy=http://127.0.0.1:1087

# 取消代理
unset http_proxy
unset https_proxy
```

```
curl -k https://ifconfig.me
curl -L ifconfig.me
```

## 测速

```
npm install --global fast-cli
```

## Android Shadowsocks

手机`Play Store`安装`kcptun`
```
手机管家 > 自启动管理 > 点开kcptun
设置 > 应用设置 > 授权管理 > 自启动管理 > 点开kcptun
```

## 检测IP是否被封

[https://ping.pe/](https://ping.pe/)

## socks转为http代理

```
apt-get install privoxy

vim /etc/privoxy/config
在里面添加：
forward-socks5   /               127.0.0.1:1080 .
listen-address localhost:8118

service privoxy restart

export http_proxy=http://127.0.0.1:8118
export https_proxy=http://127.0.0.1:8118
```

## Windows 客户端配置指南

- 支持aes-256-cfb协议的[Shadowsocks-4.3.3.170.zip](https://github.com/shadowsocks/shadowsocks-windows/releases/download/4.3.3.0/Shadowsocks-4.3.3.170.zip)
- [kcptun](https://github.com/xtaci/kcptun/releases) 解压后得到kcptun_gclient.exe，放到shadowsocks.exe同级目录
- Chrome 代理管理插件 [SwitchySharp](https://www.switchysharp.com/install.html) 解压switchysharp-v1.10.4.zip，得到SwitchySharp.crx，重命名为SwitchySharp.rar，再次解压为SwitchySharp目录（主要是为了解决CRX_HEADER_INVALID），Chrome加载已解压的扩展程序


shadowsocks服务器配置
```
服务器地址：45.76.103.60
服务器端口：9020
密码：RbdJ36^(^0
加密：aes-256-cfb
插件程序：C:\Users\张和\Downloads\Shadowsocks-4.3.3.170\client_windows_arm64.exe
插件选项：勾选需要命令行参数
插件参数：-l %SS_LOCAL_HOST%:%SS_LOCAL_PORT% -r %SS_REMOTE_HOST%:%SS_REMOTE_PORT% --key <kcptun_password> --crypt aes --mode fast2 --mtu 1350 --datashard 10 --parityshard 3 --sndwnd 1024
备注：日本东京
```

SwitchySharp情景模式配置
```
HTTP代理：127.0.0.1
端口：1080
勾选对所有协议均使用相同的代理服务器
```
