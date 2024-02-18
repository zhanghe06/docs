# Firewall

Linux中有两种防火墙软件: 
CentOS 7.0以上使用的是firewall
CentOS 7.0以下使用的是iptables

## Firewall

常用操作
```
systemctl start firewalld                                       # 开启服务
systemctl stop firewalld                                        # 关闭服务
systemctl status firewalld                                      # 查看服务状态
systemctl enable firewalld                                      # 设置开机启动
systemctl disable firewalld                                     # 取消开机启动
firewall-cmd --reload                                           # 重启服务
firewall-cmd --zone=public --add-port=8080/tcp --permanent      # 开放端口
firewall-cmd --zone=public --remove-port=8080/tcp --permanent   # 关闭端口
firewall-cmd --list-ports                                       # 查看端口
```

## Iptables

```
yum install iptables
yum install iptables-services
systemctl start iptables.service                    # 开启服务
systemctl stop iptables.service                     # 关闭服务
systemctl status iptables.service                   # 查看服务状态
systemctl enable iptables.service                   # 设置开机启动
systemctl disable iptables.service                  # 取消开机启动
iptables -L -n                                      # 查看filter表的几条链规则（INPUT链可以看出开放了哪些端口）
iptables -t nat -L -n                               # 查看NAT表的链规则
iptables -F                                         # 清除防火墙所有规则
iptables -X                                         # 清除防火墙所有规则
iptables -Z                                         # 清除防火墙所有规则
iptables -I INPUT -p tcp --dport 8080 -j ACCEPT     # 给INPUT链添加规则（开放8080端口）
iptables -L INPUT --line-numbers -n                 # 查找规则所在行号
iptables -D INPUT 1                                 # 根据行号删除过滤规则（关闭8080端口）
```

## docker 与 firewalld 冲突解决方案

背景：
centos7/8 自带防火墙是firewalld。
firewall的底层是使用iptables进行数据过滤，建立在iptables之上，这可能会与 Docker 产生冲突。
当 firewalld 启动或者重启的时候，将会从 iptables 中移除 DOCKER 的规则，从而影响了 Docker 的正常工作。
当你使用的是 Systemd 的时候，firewalld 会在 Docker 之前启动，但是如果你在 Docker 启动之后再启动 或者重启 firewalld ，你就需要重启 Docker 进程了。

方案：
```
# 禁用防火墙
systemctl disable firewalld
systemctl stop firewalld
systemctl status firewalld
```
