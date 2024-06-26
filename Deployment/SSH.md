# SSH

SSH分客户端openssh-client和服务端openssh-server

如果只是登陆别的机器，SSH只需要安装openssh-client（ubuntu有默认安装）
```
sudo apt-get install openssh-client
```

如果要使本机开放SSH服务就需要安装openssh-server
```
$ sudo apt-get install openssh-server
```

确认sshserver是否启动
```
$ ps -e | grep ssh
 1767 ?        00:00:00 sshd
 3383 ?        00:00:00 ssh-agent
```

如果看到sshd那说明ssh-server已经启动了。
如果没有则可以这样启动：
```
sudo /etc/init.d/ssh start
```

ssh-server配置文件位于/etc/ssh/sshd_config，可以定义SSH的服务端口，默认端口是22，可以自己定义成其他端口号。

查看ssh端口号
```
$ cat /etc/ssh/sshd_config | grep Port
```

查看22端口情况
```
$ netstat -antpl | grep -E '22|State'
```

然后重启SSH服务：
```
$ sudo /etc/init.d/ssh stop
$ sudo /etc/init.d/ssh start
```

然后使用以下方式登陆SSH：
```
$ ssh username@192.168.1.112
```
username为192.168.1.112 机器上的用户，需要输入密码。

断开连接：exit

## 排错

`Unable to negotiate with x.x.x.x port 22: no matching host key type found. Their offer: ssh-rsa,ssh-dss`

自 2021 年 8 月 20 日发布的 OpenSSH 8.8 起，ssh-rsa 签名方案已被弃用。

可以通过添加`-o HostKeyAlgorithms=+ssh-rsa`参数解决

```
alias dev_mysql="sshpass -p '123456' ssh root@x.x.x.x -o StrictHostKeyChecking=no -o HostKeyAlgorithms=+ssh-rsa"
```

或者更新ssh配置
```
cat ~/.ssh/config

Host *
  HostKeyAlgorithms ssh-rsa
```

## ubuntu ssh 同时支持公钥和密码登录

22.04.4 安装完成之后默认都支持（默认yes并注释）

/etc/ssh/sshd_config

确保下面两行没有被注释掉（前面不包含#符号）
```
PubkeyAuthentication yes
PasswordAuthentication yes
```

重新加载SSH服务器配置
```
sudo service ssh reload
```
