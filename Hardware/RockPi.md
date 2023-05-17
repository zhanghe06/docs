# RockPi

[Install from USB OTG port](https://wiki.radxa.com/Rockpi4/dev/usb-install)

[官方 ROCK Pi 系统镜像](https://wiki.radxa.com/Rockpi4/downloads)

[Rock Pi 4 Ubuntu Server](https://wiki.radxa.com/Rockpi4/Ubuntu)

[RockPi-3-Penta-Sata-Hat](https://hardware.developpez.com/dossiers/NAS/RockPi-3-Penta-Sata-Hat/)

硬件准备（带星号为必备）

- * 安联新创 NAS 套件 [Penta Sata Kit](https://shop.allnetchina.cn/collections/sata-hat/products/penta-sata-kit-for-rock-pi-4-model-c-with-pre-order-reward)
    - [PENTA SATA HAT board](https://wiki.radxa.com/Penta_SATA_HAT)
    - SATA HAT Top board, management board including OLED status display and active cooling
    - HAT connector cable
    - ecoPI Penta Sata case (aluminum)
    - High performance ribbon data cable and connector
    - heat sink for Rock Pi 4
    - Rock Pi 4 Model C
- * USB3.0数据线公对公 [绿联 1米 黑色 数据线](https://item.jd.com/100002277407.html) OTG端口为板子最上面的蓝色3.0端口
- 显示器，显示免驱，触屏需要驱动 [树莓派显示器 raspberry pi 4b电阻显示屏可触屏幕 3.5英寸电阻触摸TFT屏 HDMI+SPI接口](https://item.jd.com/70651873046.html)
- Micro HDMI转HDMI转接线 [绿联 1米 转接线](https://item.jd.com/2301937.html)
- USB键鼠套装 [爱国者 白色 USB键鼠套装](https://item.jd.com/100023935358.html)

## 系统安装

刷机工具
```
brew install automake autoconf libusb lsusb

git clone https://github.com/rockchip-linux/rkdeveloptool
cd rkdeveloptool
autoreconf -i
./configure
make
sudo cp rkdeveloptool /usr/local/bin/
```

镜像选择

RockPi 4b 的镜像安装在 RockPi 4c 的设备上，无法正常启动

系统安装

1. 如果您的电路板有可拆卸的 eMMC 模块，请将其卸下
2. 将USB Male A to Mail A线插入ROCK Pi 4 OTG端口（主板上面的USB3端口，针脚朝上），另一端连接PC
3. 给板子上电，绿灯亮
4. lsusb，查看端口（貌似可以省略这一步）
5. 现在插上eMMC模块，继续下一步刷机

```
# 运行 rkdeveloptool
rkdeveloptool ld

# 下载loader（flash helper）来初始化ram，准备刷机环境等
wget -c https://dl.radxa.com/rockpi/images/loader/rk3399_loader_v1.20.119.bin
rkdeveloptool db rk3399_loader_v1.20.119.bin

# 将GPT镜像写入eMMC，从offset 0开始写入
wget -c https://github.com/radxa/rock-pi-images-released/releases/download/v20210126/rockpi4c_ubuntu_focal_server_arm64_20210126_0004-gpt.img.gz
gunzip rockpi4c_ubuntu_focal_server_arm64_20210126_0004-gpt.img.gz
ls rockpi4c_ubuntu_focal_server_arm64_20210126_0004-gpt.img
rkdeveloptool wl 0 rockpi4c_ubuntu_focal_server_arm64_20210126_0004-gpt.img

# Debian桌面版如下
rkdeveloptool wl 0 rockpi4c_debian_buster_xfce4_arm64_20210824_0245-gpt.img

# 重启设备
rkdeveloptool rd

一切顺利的话，蓝灯亮/闪（系统启动），如果蓝灯熄灭，说明系统安装/启动失败
```

擦除镜像（如果需要）
```
wget -c https://dl.radxa.com/rockpi4/images/others/zero.img.gz
gunzip zero.img.gz
ls zero.img
rkdeveloptool db rk3399_loader_v1.20.119.bin
rkdeveloptool wl 0 zero.img
```

操作记录
```
➜  rkdeveloptool ld
DevNo=1	Vid=0x2207,Pid=0x330c,LocationID=1402	Maskrom
➜  rkdeveloptool db rk3399_loader_v1.20.119.bin
Downloading bootloader succeeded.
➜  rkdeveloptool wl 0 rockpi4c_ubuntu_focal_server_arm64_20210126_0004-gpt.img
Write LBA from file (100%)
➜  rkdeveloptool rd
Reset Device OK.
```

远程登录(新版镜像已启用ssh)
```
# 默认用户名和密码
default username: rock
default password: rock
# 切换root
sudo su  # rock is sudo user and switch to root
```

在路由器网关中找到对应名称为rockpi4c设备的IP地址，ssh登录即可
```
➜  ssh rock@192.168.3.144
rock@rockpi4c:~$
```

系统关闭，蓝灯熄灭

电源断开，绿灯等待10秒左右才熄灭

查看内核版本
```
rock@rockpi4c:~$ sudo lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04 LTS
Release:	20.04
Codename:	focal
rock@rockpi4c:~$ uname -a
Linux rockpi4c 4.4.154-112-rockchip-gfdb18c8bab17 #1 SMP Thu Jan 21 04:50:13 UTC 2021 aarch64 aarch64 aarch64 GNU/Linux
```

更新源 /etc/apt/sources.list

debian
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


```
apt update && apt upgrade
```

Configuring tzdata >> Geographic area >> Asia
                      timezone area >> Shanghai


添加源 [Radxa APT](https://wiki.radxa.com/Rockpi4/radxa-apt#Introduction) 并更新内核 (此处忽略，无需操作)
```
# 重要，此处一定要使用testing源
# 编辑 /etc/apt/sources.list.d/apt-radxa-com.list 注释掉focal-stable，取消注释focal-testing

cat /etc/apt/sources.list.d/apt-radxa-com.list
export DISTRO=buster-stable
# export DISTRO=focal-stable
sudo apt-get install wget
wget -O - apt.radxa.com/$DISTRO/public.key | sudo apt-key add -
sudo apt-get update && sudo apt-get upgrade

sudo apt-get install rockchip-overlay
sudo apt-get install -y rockpi4b-rk-u-boot-latest
sudo apt-get install linux-base
sudo apt-get install linux-4.4-latest
echo 'default kernel-4.4.154-115-rockchip-g00fccd37c63c' >> /boot/extlinux/extlinux.conf
```

PENTA SATA HAT board 需要驱动支持，否则风扇不转、屏显不亮

支持的镜像为:
```
*** Tested distributions:
***   Armbian 20.05.4 focal
***   Armbian 20.05.3 buster
***   Debian 9 Desktop (radxa official image)
***   Ubuntu Server 18.04 (radxa official image)
```

```
sudo apt update
sudo apt install curl

# 安装依赖
sudo apt-get install rockpi4b-rk-u-boot-latest libmraa gcc python3-dev python3-setuptools python3-pip python3-pil
curl -sL https://rock.sh/get-rockpi-penta | sudo -E bash -

# 安装过程，在安装 Adafruit-PureIO 的过程中卡住了
# 需要手动通过pip3安装离线whl版本 https://www.piwheels.org/simple/adafruit-pureio/Adafruit_PureIO-1.1.9-py3-none-any.whl#sha256=17473ffd6f00af6d4be37579baabc396cfceb682b305272e457f078241b6fd0e

# 重启系统
reboot

sudo systemctl status rockpi-penta.service
sudo systemctl restart rockpi-penta.service
```

排错

针对 [Adafruit-PureIO](https://www.piwheels.org/project/Adafruit-PureIO/#install) 需要手工下载whl包，pip3安装 

```
# 测试 OLED
python3 /usr/bin/rockpi-penta/oled.py
```

测试
```
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools
sudo i2cdetect -y 1
```

WIFI
```
sudo su
# 开启无线
nmcli r wifi on
nmcli dev wifi
# 连接网络
nmcli dev wifi connect "wifi_name" password "wifi_password"
# 激活配置
nmcli connection up "wifi_name"
nmcli connection show --active
# 查看地址
hostname -I
# 显示状态
nmcli -p dev status
```


备注：MacOS无法识别 eMMC to uSD，不清楚是不是适配器的问题，以下直接烧入eMMC的方法没有成功
```
wget -c https://github.com/radxa/rock-pi-images-released/releases/download/v20210126/rockpi4c_ubuntu_focal_server_arm64_20210126_0004-gpt.img.gz
gunzip -c rockpi4c_ubuntu_focal_server_arm64_20210126_0004-gpt.img.gz | dd of=/dev/mmcblk0
```

## 显示设备

[HDMI显示](https://wiki.radxa.com/Rockpi4/hardware/display)

Waveshare 3.5 inch LCD

/boot/hw_intfc.conf
```
intfc:uart4=off
intfc:spi1=on

intfc:dtoverlay=spi1-waveshare35c
```

```
$ sudo apt-get update
$ sudo apt-get install xserver-xorg-video-fbdev
```

/etc/X11/xorg.conf.d/20-modesetting.conf
```
Section "Device"
    Identifier  "Rockchip Graphics"
    Driver      "fbdev"
    Option      "fbdev"          "/dev/fb1"
    Option      "DRI"            "2"
EndSection
```

Reboot

## Raid 配置

配置工具: mdadm
配置方案: RAID 10
硬件设备: 4块 1T HDD

```
sudo apt install mdadm
```
mdadm：为软RAID提供管理界面，RAID设备可命名为/dev/md0、/dev/md1、/dev/md2、/dev/md3等

```
/dev/sda
/dev/sdb
/dev/sdc
/dev/sdd
```

```
mdadm -Cv /dev/md0 -a yes -n 4 -l 10 /dev/sda /dev/sdb /dev/sdc /dev/sdd    # 创建磁盘阵列
# 等待resync完成（通过 cat /proc/mdstat 查看进度）初始化阵列
mkfs.ext4 /dev/md0              # 格式化磁盘
mkdir /data                     # 创建挂载目录
mount /dev/md0 /data            # 挂载磁盘
df -h                           # 检查挂载情况
blkid                           # 查看设备ID
echo "UUID=f53e0cd8-6bb3-4b0f-8025-83a7ba625597	/data	ext4	defaults	0	2" >> /etc/fstab   # 开机自动生效
mount -a                        # 重新加载/etc/fstab配置，运行通过说明写入成功
```

/etc/fstab 格式说明
```
# <file system>        <dir>         <type>    <options>             <dump> <pass>
/dev/sda1              /             ext4      defaults              1      1
/dev/hdxx              /usr          ext4      defaults              1      1
/dev/sda5              swap          swap      defaults              0      0
UUID=xxxx              /media/sdb2   ext4      defaults              0      2

末尾两个数字
第一个数字0表示不使用bump程序对它进行备份。
第二个数字2表示开机不优先检查此磁盘，1表示开机优先检查磁盘，用于根分区/, 2用于普通分区，0禁止磁盘检查。
```

```
mdadm -D /dev/md0               # 查看阵列磁盘信息
mdadm /dev/md0 -f /dev/sdc      # 移除损坏磁盘，阵列依然正常使用
mdadm /dev/md0 -a /dev/sdc      # 加入恢复磁盘
```

```
cat /proc/mdstat                # 查看
umount /dev/md0                 # 卸载
mdadm --stop /dev/md0           # 停止
lsblk
```

软Raid配置之后，初始化阶段，CPU通常在50%以上

### Raid 配置配置 - 实操记录:
```
rock@rockpi4c:~$ lsblk | grep sd
sda            8:0    0 931.5G  0 disk
sdb            8:16   0 931.5G  0 disk
sdc            8:32   0 931.5G  0 disk
sdd            8:48   0 931.5G  0 disk
```

```
root@rockpi4c:/home/rock# mdadm -Cv /dev/md0 -a yes -n 4 -l 10 /dev/sda /dev/sdb /dev/sdc /dev/sdd
mdadm: layout defaults to n2
mdadm: layout defaults to n2
mdadm: chunk size defaults to 512K
mdadm: size set to 976630272K
mdadm: automatically enabling write-intent bitmap on large array
mdadm: Fail create md0 when using /sys/module/md_mod/parameters/new_array
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.
```

```
root@rockpi4c:/home/rock# cat /proc/mdstat
Personalities : [raid10]
md0 : active raid10 sdd[3] sdc[2] sdb[1] sda[0]
      1953260544 blocks super 1.2 512K chunks 2 near-copies [4/4] [UUUU]
      [>....................]  resync =  0.3% (7399744/1953260544) finish=401.6min speed=80736K/sec
      bitmap: 15/15 pages [60KB], 65536KB chunk

unused devices: <none>
```

```
root@rockpi4c:/home/rock# mdadm -D /dev/md0
/dev/md0:
           Version : 1.2
     Creation Time : Sun Oct 24 17:29:55 2021
        Raid Level : raid10
        Array Size : 1953260544 (1862.77 GiB 2000.14 GB)
     Used Dev Size : 976630272 (931.39 GiB 1000.07 GB)
      Raid Devices : 4
     Total Devices : 4
       Persistence : Superblock is persistent

     Intent Bitmap : Internal

       Update Time : Sun Oct 24 17:32:43 2021
             State : clean, resyncing
    Active Devices : 4
   Working Devices : 4
    Failed Devices : 0
     Spare Devices : 0

            Layout : near=2
        Chunk Size : 512K

Consistency Policy : unknown

     Resync Status : 0% complete

              Name : rockpi4c:0  (local to host rockpi4c)
              UUID : 8e666316:d85a425f:be25ba96:a1c1ea83
            Events : 31

    Number   Major   Minor   RaidDevice State
       0       8        0        0      active sync set-A   /dev/sda
       1       8       16        1      active sync set-B   /dev/sdb
       2       8       32        2      active sync set-A   /dev/sdc
       3       8       48        3      active sync set-B   /dev/sdd
```

```
root@rockpi4c:/home/rock# mkfs.ext4 /dev/md0
mke2fs 1.44.5 (15-Dec-2018)
Creating filesystem with 488315136 4k blocks and 122085376 inodes
Filesystem UUID: f825ec10-d075-4f79-ab50-8f03622f93f2
Superblock backups stored on blocks:
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
	4096000, 7962624, 11239424, 20480000, 23887872, 71663616, 78675968,
	102400000, 214990848

Allocating group tables: done
Writing inode tables: done
Creating journal (262144 blocks): done
Writing superblocks and filesystem accounting information: done
```

```
root@rockpi4c:/home/rock# mkdir /data
root@rockpi4c:/home/rock# mount /dev/md0 /data
root@rockpi4c:/home/rock# df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            1.9G     0  1.9G   0% /dev
tmpfs           382M  548K  381M   1% /run
/dev/mmcblk1p5   57G  2.4G   52G   5% /
tmpfs           1.9G   28K  1.9G   1% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           1.9G     0  1.9G   0% /sys/fs/cgroup
tmpfs           382M     0  382M   0% /run/user/109
tmpfs           382M     0  382M   0% /run/user/1000
/dev/mmcblk1p4  511M   75M  437M  15% /boot
/dev/md0        1.8T   77M  1.7T   1% /data
```

```
root@rockpi4c:/home/rock# mdadm -D /dev/md0
/dev/md0:
           Version : 1.2
     Creation Time : Sun Oct 24 17:29:55 2021
        Raid Level : raid10
        Array Size : 1953260544 (1862.77 GiB 2000.14 GB)
     Used Dev Size : 976630272 (931.39 GiB 1000.07 GB)
      Raid Devices : 4
     Total Devices : 4
       Persistence : Superblock is persistent

     Intent Bitmap : Internal

       Update Time : Sun Oct 24 17:43:05 2021
             State : active, resyncing
    Active Devices : 4
   Working Devices : 4
    Failed Devices : 0
     Spare Devices : 0

            Layout : near=2
        Chunk Size : 512K

Consistency Policy : unknown

     Resync Status : 3% complete

              Name : rockpi4c:0  (local to host rockpi4c)
              UUID : 8e666316:d85a425f:be25ba96:a1c1ea83
            Events : 153

    Number   Major   Minor   RaidDevice State
       0       8        0        0      active sync set-A   /dev/sda
       1       8       16        1      active sync set-B   /dev/sdb
       2       8       32        2      active sync set-A   /dev/sdc
       3       8       48        3      active sync set-B   /dev/sdd
```

```
root@rockpi4c:/home/rock# lsblk
NAME         MAJ:MIN RM   SIZE RO TYPE   MOUNTPOINT
sda            8:0    0 931.5G  0 disk
`-md0          9:0    0   1.8T  0 raid10 /data
sdb            8:16   0 931.5G  0 disk
`-md0          9:0    0   1.8T  0 raid10 /data
sdc            8:32   0 931.5G  0 disk
`-md0          9:0    0   1.8T  0 raid10 /data
sdd            8:48   0 931.5G  0 disk
`-md0          9:0    0   1.8T  0 raid10 /data
mmcblk1      179:0    0  57.6G  0 disk
|-mmcblk1p1  179:1    0   3.9M  0 part
|-mmcblk1p2  179:2    0     4M  0 part
|-mmcblk1p3  179:3    0     4M  0 part
|-mmcblk1p4  179:4    0   512M  0 part   /boot
`-mmcblk1p5  179:5    0  57.1G  0 part   /
mmcblk1boot0 179:32   0     4M  1 disk
mmcblk1boot1 179:64   0     4M  1 disk
mmcblk1rpmb  179:96   0     4M  0 disk
```

注意: 系统损坏，可能导致磁盘阵列不可用

常见的错误，参考 https://www.stellarinfo.co.in/blog/raid-server-recovery/

## 参数配置

/etc/rockpi-penta.conf
```
[fan]
# When the temperature is above lv0 (35'C), the fan at 25% power,
# and lv1 at 50% power, lv2 at 75% power, lv3 at 100% power.
# When the temperature is below lv0, the fan is turned off.
# You can change these values if necessary.
lv0 = 35
lv1 = 40
lv2 = 45
lv3 = 50
```

风扇太吵了，调整配置为
```
[fan]
lv0 = 45
lv1 = 50
lv2 = 55
lv3 = 60
```

`sudo systemctl restart rockpi-penta.service`

## 重装系统后的数据恢复(未测试)

参考: [https://www.cnblogs.com/felix-zp/p/9742514.html](https://www.cnblogs.com/felix-zp/p/9742514.html)

一、导入
```
mdadm --assemble --scan
或
mdadm -A /dev/md0 /dev/sda /dev/sdb /dev/sdc /dev/sdd
```


二、保存
```
mdadm --detail --scan >> /etc/mdadm/mdadm.conf
或
mdadm -Ds > /etc/mdadm/mdadm.conf
```


三、解决md127的问题
为了解决重启后变成/dev/md127的问题，还需要修改mdadm.conf：
把第二列：/dev/md/raid1
修改成：/dev/md0

再执行(貌似没有生效)：
update-initramfs -u


## mdadm 手册

参考: [https://blog.csdn.net/a7320760/article/details/10442715](https://blog.csdn.net/a7320760/article/details/10442715)

mdadm是一个用于创建、管理、监控RAID设备的工具，它使用linux中的md驱动，是一个独立的程序，能完成所有软件RAID的管理功能。

主要有7种使用模式:

模式名字 | 主要功能 |（对于存储管理系统）
--- | --- | ---
Create | 使用空闲的设备创建一个新的阵列，每个设备具有元数据块 | 创建RAID时使用的命令
Assemble | 将原来属于一个阵列的每个块设备组装为阵列 | 在存储管理系统一般不使用该模式
Build | 创建或组装不需要元数据的阵列，每个设备没有元数据块 | 在存储管理系统一般不使用该模式
Manage | 管理已经存储阵列中的设备，比如增加热备磁盘或者设置某个磁盘失效，然后从阵列中删除这个磁盘 | 用于增加热备盘，移除失效盘
Misc | 报告或者修改阵列中相关设备的信息，比如查询阵列或者设备的状态信息 | 用于查询RAID信息
Grow | 改变阵列中每个设备被使用的容量或阵列中的设备的数目，改变阵列属性（不能改变阵列的级别） | 在存储管理系统一般不使用该模式
Monitor | 监控一个或多个阵列，上报指定的事件，可以实现全局热备 | 监控RAID，写入日志

概念描述

概念 | 描述
--- | ---
`/proc/mdstat` | 当前md(软RAID)的状态信息
`/etc/mdadm.conf` | mdadm的配置文件
`Active devices` | RAID中的活动组件设备
`Faulty device` | RAID中失效的设备
`Spare device` | RAID中热备盘
`Device Names` | RAID设备名、标准格式是`/dev/mdNN`或者`/dev/md/NN`
`md` | Multiple Devices虚拟块设备（利用底层多个块设备虚拟出一个新的虚拟块设备）。
`md driver` | MD的驱动
`Array` | 阵列，跟RAID意思相同
`Raid` | 不解释
`md device` | 就是使用MD创建的软件RAID
`md array` | 同上


命令概要: `mdadm [模式选项] [RAID设备名] [子选项…] [组件设备名…]`

## SeaweedFS

部署参考: [http://www.diyhi.com/seaweedfs.html](http://www.diyhi.com/seaweedfs.html)

```
wget -c https://github.com/chrislusf/seaweedfs/releases/download/2.76/linux_arm64.tar.gz
tar -zxvf linux_arm64.tar.gz
```

使用Redis管理文件映射关系，可选，默认使用leveldb2
```
./weed scaffold -config filer -output="/data/weed_data/"
```

filer.toml
```
[leveldb2]
enabled = false

[redis]
enabled = true
address  = "127.0.0.1:6379"
password = "123456"
```

```
chown -R seaweedfs:seaweedfs /data/weed_data
```

启动[master](http://127.0.0.1:9333)服务
```
./weed master -mdir="/data/weed_data/master"
```

启动[volume](http://127.0.0.1:8080)服务
```
./weed volume -max=32 -mserver=":9333" -dir="/data/weed_data/volume"
```

启动[filer](http://127.0.0.1:8888)服务
```
./weed filer -master=":9333" -dir="/data/weed_data/filer"
```

grpc端口为http端口 `+10000`
默认的grpc端口：
```
主服务器(master) -- 默认http为 9333，grpc为 19333
卷服务器(volume) -- 默认http为 8080，grpc为 18080
管理服务器(filer) -- 默认http为 8888，grpc为 18888
```


```
getent group seaweedfs || groupadd -r seaweedfs
getent passwd seaweedfs || useradd -r -d /home/seaweedfs -s /usr/sbin/nologin -g seaweedfs seaweedfs
chown -R seaweedfs:seaweedfs /data/weed_data
cat /etc/group | grep seaweedfs
```

```
cp weed /usr/bin/
```

配置开机启动

一、master服务 `/etc/systemd/system/weed-master.service`
```
cat >/etc/systemd/system/weed-master.service <<EOF
[Unit]
Description=SeaweedFS Master
After=network.target

[Service]
User=seaweedfs
Group=seaweedfs

ExecStart=/usr/bin/weed master -mdir="/data/weed_data/master"
Restart=always

[Install]
WantedBy=multi-user.target
EOF
```

```
systemctl daemon-reload
systemctl status weed-master
systemctl enable weed-master
systemctl restart weed-master
```

二、volume服务 `/etc/systemd/system/weed-volume.service` 同上

三、filer服务 `/etc/systemd/system/weed-filer.service` 同上


## 测速

```
curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -
```
需要科学上网

```
rock@rockpi4c:~/tools$ python speedtest.py
Retrieving speedtest.net configuration...
Testing from China Telecom (101.85.123.191)...
Retrieving speedtest.net server list...
Selecting best server based on ping...

Hosted by China Telecom Wuhan Branch (Wuhan) [685.16 km]: 31.988 ms
Testing download speed................................................................................
Download: 90.16 Mbit/s
Testing upload speed................................................................................................
Upload: 35.90 Mbit/s
```

查询网卡速率
```
rock@rockpi4c:~/tools$ ethtool eth0
Settings for eth0:
	Supported ports: [ TP AUI BNC MII FIBRE ]
	Supported link modes:   10baseT/Half 10baseT/Full
	                        100baseT/Half 100baseT/Full
	                        1000baseT/Half 1000baseT/Full
	Supported pause frame use: No
	Supports auto-negotiation: Yes
	Supported FEC modes: Not reported
	Advertised link modes:  10baseT/Half 10baseT/Full
	                        100baseT/Half 100baseT/Full
	                        1000baseT/Half 1000baseT/Full
	Advertised pause frame use: No
	Advertised auto-negotiation: Yes
	Advertised FEC modes: Not reported
	Link partner advertised link modes:  10baseT/Half 10baseT/Full
	                                     100baseT/Half 100baseT/Full
	Link partner advertised pause frame use: No
	Link partner advertised auto-negotiation: Yes
	Link partner advertised FEC modes: Not reported
	Speed: 100Mb/s
	Duplex: Full
	Port: MII
	PHYAD: 0
	Transceiver: external
	Auto-negotiation: on
Cannot get wake-on-lan settings: Operation not permitted
	Current message level: 0x0000003f (63)
			       drv probe link timer ifdown ifup
	Link detected: yes
```

从结果看出，网卡支持千兆，实际速率`Speed: 100Mb/s`只有百兆

原来是路由设备的问题，使用千兆网线直接插入电信光猫，显示`Speed: 1000Mb/s`，然后再测试一下网速

```
rock@rockpi4c:~/tools$ python speedtest.py
Retrieving speedtest.net configuration...
Testing from China Telecom (101.85.123.191)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by 江苏电信5G (Yangzhou) [252.85 km]: 20.892 ms
Testing download speed................................................................................
Download: 236.89 Mbit/s
Testing upload speed................................................................................................
Upload: 35.52 Mbit/s
```
可以看出下载速率有一定提升

## 安装 docker

检查系统版本
```
root@rockpi4c:~# lsb_release -cs
focal
root@rockpi4c:~# dpkg --print-architecture
arm64
```

[官方安装指南](https://docs.docker.com/engine/install/ubuntu/)

[配置修改指南](https://docs.docker.com/config/daemon/)

修改Docker目录
```
root@rockpi4c:~# docker info | grep "Docker Root Dir"
 Docker Root Dir: /var/lib/docker
```

```
vim /etc/docker/daemon.json
{
    "data-root": "/data/docker"
}
mkdir -p /data/docker
systemctl stop docker.socket
systemctl stop docker.service
systemctl daemon-reload
systemctl start docker.service
```

```
root@rockpi4c:~# docker info | grep "Docker Root Dir"
 Docker Root Dir: /data/docker
```

## 软路由

pppoe拨号
```
sudo apt install pppoeconf
```
