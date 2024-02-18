# CentOS

官网: [https://www.centos.org](https://www.centos.org)

光盘镜像: [https://www.centos.org/download](https://www.centos.org/download)

软件镜像: [https://www.debian.org/mirror/list](https://www.debian.org/mirror/list)

官方基本容器: [https://hub.docker.com/_/centos](https://hub.docker.com/_/centos)

应用程序容器: [https://hub.docker.com/u/centos](https://hub.docker.com/u/centos)

查看系统版本
```
# cat /etc/redhat-release
CentOS release 6.6 (Final)
```

查看CPU架构
```
# uname -m
x86_64
```

```
# 解决中文乱码
export LANG=C.UTF-8
export LC_ALL=C.UTF-8

# 如果不行，采用以下方式
export LANG="zh_CN.UTF-8"
export LC_ALL="zh_CN.UTF-8"

echo $LANG
locale -a|grep zh
vim /etc/sysconfig/i18n
LANG="zh_CN"
LC_ALL="zh_CN"
source /etc/sysconfig/i18n

vim /etc/locale.conf
LANG="zh_CN.utf8"
source /etc/locale.conf

vim /etc/profile
export LC_ALL="zh_CN.utf8"
reboot
```

## CentOS 6 源404

```
lsb_release -a


# 更新基础源
cp /etc/yum.repos.d/CentOS-Base.repo{,.bak}
wget --no-check-certificate -O /etc/yum.repos.d/CentOS-Base.repo https://static.lty.fun/%E5%85%B6%E4%BB%96%E8%B5%84%E6%BA%90/SourcesList/Centos-6-Vault-Aliyun.repo
yum clean all && yum makecache
```

安装docker
```
yum install https://get.docker.com/rpm/1.7.1/centos-6/RPMS/x86_64/docker-engine-1.7.1-1.el6.x86_64.rpm
yum -y install docker-io
```

```
service docker status
service docker start
docker -d

docker version
```


## 查看内网IP

查看内网IP
```
hostname -I | awk '{print $1}'
```
