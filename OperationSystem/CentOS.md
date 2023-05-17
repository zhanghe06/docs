# CentOS

官网: [https://www.centos.org](https://www.centos.org)

光盘镜像: [https://www.centos.org/download](https://www.centos.org/download)

软件镜像: [https://www.debian.org/mirror/list](https://www.debian.org/mirror/list)

官方基本容器: [https://hub.docker.com/_/centos](https://hub.docker.com/_/centos)

应用程序容器: [https://hub.docker.com/u/centos](https://hub.docker.com/u/centos)

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
