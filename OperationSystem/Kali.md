## Kali

[https://www.kali.org/](https://www.kali.org/)

[http://docs.kali.org/](http://docs.kali.org/)

[https://www.kali.org/downloads/](https://www.kali.org/downloads/)


## Vmware 安装 Kali

kali-linux-2016.2-amd64.iso

在 Vmware Workstation 中新建一个虚拟机，Linux 版本选的是 Debian 8.X 64位

虚拟机安装成功后安装

添加源

[Kali Linux Releases](https://www.kali.org/kali-linux-releases/)

[Kali sources.list Repositories](http://docs.kali.org/general-use/kali-linux-sources-list-repositories)

原文有介绍：
```
Using Official Repositories

The Kali Linux distribution has two repositories, which are mirrored world-wide:

http.kali.org (mirrorlist): the main package repository;
cdimage.kali.org (mirrorlist): the repository of pre-built Kali ISO images.
When using the default hosts listed above, you’ll automatically be redirected to a mirror site which is geographically close to you, and which is guaranteed to be up-to-date.
```
所以 kali 最新发行版 官方源，会自动重定向到国内最近的镜像


```
# leafpad /etc/apt/sources.list
```


Kali 2016 默认是不带软件源的，需要先配置软件源，这个官方源就行，它会自动定向国内源
```
deb http://http.kali.org/kali kali-rolling main non-free contrib
```

```
# apt-get update && apt-get upgrade && apt-get dist-upgrade
```

查看更新后的 python php 版本
```
root@kali:~# python -V
Python 2.7.12+
root@kali:~# php -v
PHP 7.0.12-1 (cli) ( NTS )
```
