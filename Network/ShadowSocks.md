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
```
**[terminal]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command yum install -y python-pip net-tools vim-enhanced git]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command pip install -U pip]
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
    "fast_open": true
}
EOF
```

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
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command firewall-cmd --reload]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command firewall-cmd --list-ports]
8282/tcp 3128/tcp
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
