# Ubuntu

官网: [https://ubuntu.com](https://ubuntu.com)

光盘镜像: [https://releases.ubuntu.com](https://releases.ubuntu.com)

软件镜像: [https://wiki.ubuntu.org.cn/模板:18.04source](https://wiki.ubuntu.org.cn/模板:18.04source)

```
deb http://cn.archive.ubuntu.com/ubuntu/ boinc main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ boinc-security main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ boinc-updates main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ boinc-backports main restricted universe multiverse
##测试版源
deb http://cn.archive.ubuntu.com/ubuntu/ boinc-proposed main restricted universe multiverse
# 源码
deb-src http://cn.archive.ubuntu.com/ubuntu/ boinc main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ boinc-security main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ boinc-updates main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ boinc-backports main restricted universe multiverse
##测试版源
deb-src http://cn.archive.ubuntu.com/ubuntu/ boinc-proposed main restricted universe multiverse
# Canonical 合作伙伴和附加
deb http://archive.canonical.com/ubuntu/ boinc partner
deb http://extras.ubuntu.com/ubuntu/ boinc main
```

长期支持版本对照

Released (Current & Stable) | Version | Release Schedule | Support Date
--- | --- | --- | ---
[Xenial Xerus](https://releases.ubuntu.com/xenial/) | 16.04 LTS | April 21, 2016 | Supported until April 2021
[Bionic Beaver](https://releases.ubuntu.com/bionic/) | 18.04 LTS | April 26, 2018 | Supported until April 2023
[Focal Fossa](https://releases.ubuntu.com/focal/) | 20.04 LTS | April 23, 2020 | Supported until April 2025
[Jammy Jellyfish](https://releases.ubuntu.com/jammy/) | 22.04 LTS | April 21, 2022 | Supported until April 2027


## Rsync

默认已安装，但是未开启

将文件`/etc/default/rsync`中`RSYNC_ENABLE=false`修改为`RSYNC_ENABLE=true`
```
vim /etc/default/rsync
cp /usr/share/doc/rsync/examples/rsyncd.conf /etc
```

## 单位

```
在计算存储容量时，K代表1024，即：
    1MByte=1024KByte=1024*1024Byte
    其含义为： K为Kibi的缩写，1 KiB (kibibyte)=210 bytes=1024 bytes

在计算网卡速率时，k代表1000，即：
   1Gbps=1000*1Mbps=1000*1000*kbps=1000*1000*1000bps
   其含义为： k为kilo的缩写，1 kB (kilobyte)=103 bytes=1000 bytes
```

内存单位是kB，采用1000换算
```
root@ubuntu:~# grep MemTotal /proc/meminfo
MemTotal:        7947492 kB
```
