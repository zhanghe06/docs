# Debian

官网: [https://www.debian.org](https://www.debian.org)

光盘镜像: [https://www.debian.org/CD/http-ftp/#mirrors](https://www.debian.org/CD/http-ftp/#mirrors)

软件镜像: [https://www.debian.org/mirror/list](https://www.debian.org/mirror/list)


[阿里镜像](https://developer.aliyun.com/mirror/debian)

/etc/apt/sources.list
```
deb http://mirrors.aliyun.com/debian/ buster main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib
deb http://mirrors.aliyun.com/debian-security buster/updates main
deb-src http://mirrors.aliyun.com/debian-security buster/updates main
deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
```
