# RaspberryPi


## 系统安装

硬件设备
- MAC OS
- SanDisk U盘（128G）

系统镜像
- raspbian_lite（精简版 - 非桌面）

参考 [INSTALLING OPERATING SYSTEM IMAGES ON MAC OS](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md)

安装步骤

1. 下载系统镜像
```bash
wget http://vx2-downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-12-01/2017-11-29-raspbian-stretch-lite.zip
unzip 2017-11-29-raspbian-stretch-lite.zip
```

2. 插入U盘, 并检查状态

如果非空U盘, 磁盘工具 >> 抹掉 >> MS-DOS(FAT) >> 确认抹掉

```
➜  ~ diskutil list
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *500.3 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:                 Apple_APFS Container disk1         500.1 GB   disk0s2

/dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +500.1 GB   disk1
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            419.7 GB   disk1s1
   2:                APFS Volume Preboot                 23.4 MB    disk1s2
   3:                APFS Volume Recovery                518.1 MB   disk1s3
   4:                APFS Volume VM                      7.5 GB     disk1s4

/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *7.7 GB     disk2
   1:                 DOS_FAT_32 UNTITLED                7.7 GB     disk2s1
```

```
disk2           # Media BSD 名称
/dev/disk2s1    # 宗卷 BSD 名称
```

3. 卸载U盘
```bash
diskutil unmountDisk /dev/disk2
```

卸载前后对比
```
➜  ~ df -h
Filesystem      Size   Used  Avail Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   466Gi  381Gi   83Gi    83% 2618235 9223372036852157572    0%   /
devfs          193Ki  193Ki    0Bi   100%     666                   0  100%   /dev
/dev/disk1s4   466Gi  1.0Gi   83Gi     2%       1 9223372036854775806    0%   /private/var/vm
map -hosts       0Bi    0Bi    0Bi   100%       0                   0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%       0                   0  100%   /home
/dev/disk2s1   115Gi   36Mi  114Gi     1%       0                   0  100%   /Volumes/NO NAME
➜  ~ df -h
Filesystem      Size   Used  Avail Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   466Gi  381Gi   83Gi    83% 2618323 9223372036852157484    0%   /
devfs          193Ki  193Ki    0Bi   100%     668                   0  100%   /dev
/dev/disk1s4   466Gi  1.0Gi   83Gi     2%       1 9223372036854775806    0%   /private/var/vm
map -hosts       0Bi    0Bi    0Bi   100%       0                   0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%       0                   0  100%   /home
```

4. 系统写入U盘
```bash
sudo dd bs=1m if=2018-04-18-raspbian-stretch-lite.img of=/dev/rdisk2 conv=sync
```

```
➜  ~ df -h
Filesystem      Size   Used  Avail Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   466Gi  383Gi   80Gi    83% 2618347 9223372036852157460    0%   /
devfs          194Ki  194Ki    0Bi   100%     672                   0  100%   /dev
/dev/disk1s4   466Gi  2.0Gi   80Gi     3%       2 9223372036854775805    0%   /private/var/vm
map -hosts       0Bi    0Bi    0Bi   100%       0                   0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%       0                   0  100%   /home
/dev/disk2s1    41Mi   21Mi   20Mi    51%       0                   0  100%   /Volumes/boot
➜  ~ diskutil list
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *500.3 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:                 Apple_APFS Container disk1         500.1 GB   disk0s2

/dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +500.1 GB   disk1
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            411.3 GB   disk1s1
   2:                APFS Volume Preboot                 22.4 MB    disk1s2
   3:                APFS Volume Recovery                509.8 MB   disk1s3
   4:                APFS Volume VM                      2.1 GB     disk1s4

/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *123.0 GB   disk2
   1:             Windows_FAT_32 boot                    43.5 MB    disk2s1
   2:                      Linux                         1.8 GB     disk2s2
```

5. 弹出U盘
```bash
sudo diskutil eject /dev/rdisk2
```

## 重置密码

默认的登录帐号为 pi 密码是 raspberry

更改密码
```bash
passwd
```
内容如下:
```
为 pi 更改 STRESS 密码。
（当前）UNIX 密码：raspberry
输入新的 UNIX 密码：raspberry000
重新输入新的 UNIX 密码：raspberry000
passwd：已成功更新密码
```

设置root用户
```
// 设置 root 账号的密码，会让你输入两次新密码
sudo passwd root // 启用 root 账号登录
sudo passwd --unlock root
reboot
```

## 设置U盘启动

准备工作:

SD card, USB mass storage device 都装好相同最新系统

参考:

https://github.com/raspberrypi/documentation/blob/master/hardware/raspberrypi/bootmodes/msd.md#prepare-the-usb-storage-device

SD card 启动
```bash
sudo apt-get update && sudo apt-get upgrade
echo program_usb_boot_mode=1 | sudo tee -a /boot/config.txt
sudo reboot
vcgencmd otp_dump | grep 17:    # 17:3020000a
```
然后 USB mass storage device 启动

查看系统信息
```bash
gpio readall
cat /etc/rpi-issue
vcgencmd version
```

## 无线网络配置

https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
文件末尾新增
```
network={
    ssid="testing"
    psk="testingPassword"
}
```

priority 是指连接优先级，数字越大优先级越高（不可以是负数）


```bash
# 重启网卡使设置生效
sudo ifdown wlan0
sudo ifup wlan0
# 或重启系统
sudo reboot
```

设置固定IP
```bash
sudo nano /etc/dhcpcd.conf
```
新增
```
interface wlan0
static ip_address = 192.168.1.100
static routers = 192.168.1.1
```

## 正确关机方式:
1. 终端执行关机（以下任意一种）
```bash
sudo shutdown -h now
sudo halt
sudo poweroff
sudo init 0
```
2. 然后拔掉电源, 电源指示灯灭

重启方式
```bash
sudo reboot
shutdown -r now
shutdown -r 04:00:00  # 定时重启在凌晨四点关闭重启
```


## 初始配置

```bash
sudo apt-get update
```

- 开启 SSH
```bash
sudo raspi-config
```

```
Interfacing Options >> SSH >> Yes >> Ok
```

默认用户名、密码（pi、raspberry）
```bash
ssh pi@10.21.2.215
```

- 配置环境变量
```bash
sudo raspi-config
```

- 安装中文字体
```bash
sudo apt-get install ttf-wqy-zenhei ttf-wqy-microhei
```

- 配置语言时区
```
Localisation Options >> Change Locale >> zh_CN.UTF-8 UTF-8 >> 空格 + * >> Ok >> zh_CN.UTF-8

Localisation Options >> Change Timezone >> Asia >> Shanghai >> ok
```


## 寻找局域网内的树莓派地址

无`ping`扫描, 防火墙禁止`ping`, 这可以穿透防火墙, 也可以避免被防火墙发现
```bash
nmap -P0 192.168.0.0/24
```

```
Nmap scan report for 192.168.1.119
Host is up (0.0083s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
```

## 蓝牙配置

https://github.com/ev3dev/ev3dev/issues/198

```
$ sudo apt-get install -y pulseaudio
$ sudo apt-get install -y pulseaudio-module-bluetooth
$ sudo bluetoothctl
# agent on
# 
```

```
systemctl status bluetooth


```

## 树莓派无界面配置WiFi

SD卡根目录 新增/修改 `wpa_supplicant.conf`
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="testing"
    psk="testingPassword"
}
```

例如
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="PING"
    psk="13818732593"
    priority=100
}

network={
    ssid="TD-LTE-4G"
    psk="0987654321"
    priority=90
}

network={
    ssid="chinac.com"
    psk="1qazxsw2"
    priority=80
}
```

## 树莓派无界面配置SSH

SD卡根目录 新增 `ssh`空文件

## 安装 docker

http://dockone.io/article/1732

```
curl -sSL get.docker.com |sh
```

## 常用工具库

官方：[https://github.com/gpiozero/gpiozero](https://github.com/gpiozero/gpiozero)

[https://github.com/WiringPi/WiringPi-Python](https://github.com/WiringPi/WiringPi-Python)

[https://pypi.python.org/pypi/RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)


```bash
pip install rpi.gpio
```


## 计算模块

树莓派 计算模块3/3 Lite扩展板 兼容Compute Module IO Board V3
微雪 Compute Module 3 Lite 树莓派 Raspberry Pi 3 计算模块


## 传感器种类:


## 配件

- 继电器

    远程控制电路开关

- 红外摄像头

    普通红外摄像头因为`CCD`没有红外滤光片，所以在白天看起来会有些偏红，但正因如此，夜晚才能正常使用。
    如果需要白天和夜晚都能正常显示，推荐使用`RPi IR-CUT Camera`

- 舵机

- 转台

- 滑轨

## 显示屏

http://www.lcdwiki.com/zh/3.5inch_HDMI_Display-B

https://github.com/goodtft/LCD-show

```
sudo rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./MPI3508-show
```

## 安装说明

使用官方推荐的[Raspberry Pi Imager](https://www.raspberrypi.com/software/)工具界面烧录系统到SD卡

ssh zhanghe@192.168.3.159
```
zhanghe
123456
```

```
git clone https://github.com/goodtft/LCD-show.git
scp -r LCD-show zhanghe@192.168.3.159:~
```
