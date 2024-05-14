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

## ubuntu20.04开机自动打开浏览器全屏访问指定页面

1、下载(全屏)组件：AutoFullScreen 添加到火狐浏览器
https://addons.mozilla.org/zh-CN/firefox/addon/autofullscreen/

2、设置浏览器打开指定地址

浏览器打开：about:preferences#home

主页和新窗口 -> 自定义网址：http://127.0.0.1:3421

3、设置浏览器开机启动

```
cd /etc/xdg/autostart
sudo vim firefox.desktop
```

```
[Desktop Entry]
Name=page-launch
Comment=Firefox Home Page
Exec=sh -c "sleep 15 && firefox"
StartupNotify=false
Terminal=false
Type=Application
```

```
# 检查文件是否存在错误，无报错表示成功
desktop-file-validate firefox.desktop
```

4、开机自动登录

设置 -> 用户 -> 自动登录(打开启用开关)

5、禁用通知

设置 -> 通知 -> 勿扰

6、屏幕常亮

设置 -> 电源 -> 节点选项 -> 屏幕变暗（开关关闭）

设置 -> 电源 -> 节点选项 -> 屏幕空白（从不）

7、Firefox自动恢复先前的浏览状态

场景：处理会议室大屏异常重启后页面白屏的情况

禁用崩溃后的会话恢复功能（默认是启用的），这样在意外退出或崩溃后，Firefox 也不会恢复上次会话：
```
在 地址栏 里输入about:config，然后按 回车。
有时会出现警告页面。点击 接受风险并继续，以打开 about:config 页面。
在顶端的 搜索首选项 框中输入 browser.sessionstore.resume_from_crash。
在结果栏中，双击 browser.sessionstore.resume_from_crash 旁边的 交替按钮并设置其值为 false。
```

8、取消浏览器弹窗

```
设置 -> 常规 -> 浏览 -> 取消在您浏览时推荐扩展
设置 -> 常规 -> 浏览 -> 取消在您浏览时推荐新功能
```

9、取消软件更新弹窗

软件和更新 -> 更新 -> 自动检查更新 -> 从不

## 镜像下载

- [ubuntu-22.04.4-desktop-amd64.iso](https://releases.ubuntu.com/22.04/ubuntu-22.04.4-desktop-amd64.iso)
- [ubuntu-22.04.4-live-server-amd64.iso](https://releases.ubuntu.com/22.04.4/ubuntu-22.04.4-live-server-amd64.iso)
- [ubuntu-22.04.4-live-server-arm64.iso](https://cdimage.ubuntu.com/releases/22.04/release/ubuntu-22.04.4-live-server-arm64.iso)

## 制作镜像

桌面版制作
```
diskutil list
diskutil unmountDisk /dev/disk7
hdiutil convert -format UDRW -o ~/Downloads/ubuntu-22.04.4-desktop-amd64 /Volumes/Transcend/系统镜像/ubuntu-22.04.4-desktop-amd64.iso
sudo dd bs=1m if=/Users/zhanghe/Downloads/ubuntu-22.04.4-desktop-amd64.dmg of=/dev/rdisk7 conv=sync
diskutil eject /dev/rdisk7
```

服务版制作
```
diskutil list
diskutil unmountDisk /dev/disk7
hdiutil convert -format UDRW -o ~/Downloads/ubuntu-22.04.4-live-server-amd64 /Volumes/Transcend/系统镜像/ubuntu-22.04.4-live-server-amd64.iso
sudo dd bs=1m if=/Users/zhanghe/Downloads/ubuntu-22.04.4-live-server-amd64.dmg of=/dev/rdisk7 conv=sync
diskutil eject /dev/rdisk7
```


## 重装系统

通过U盘安装系统
```
插入U盘
重启电脑
BIOS设置USB-HDD
    F12进入BIOS
    <Enter Setup>
    Config > USB > USB BIOS Support [Enabled]
    Startup > Boot > 将 USB HDD 设置为启动第一项
    F10 (Save and Exit)
F12 选择 USB HDD
默认选中install ubuntu，进入自动安装
安装完成，重启，拔出U盘（根据提示回车），进入系统
```

账号配置
```
Your name: xxx
Your server's name: ubuntu
Pick a username: xxx
Choose a password: xxxxxx
Confirm your password: xxxxxx
```

## 复制本地公钥到远程机器

```
# 本地公钥
ssh-copy-id mixi@192.168.2.2
# 指定公钥文件
ssh-copy-id -i ~/.ssh/id_rsa.pub mixi@192.168.2.2
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
