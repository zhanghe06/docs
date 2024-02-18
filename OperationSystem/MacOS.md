# MacOS

## 安装

安装 iTerm2 oh-my-zsh

```
sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"
```

zsh-autosuggestions：历史补全
```
# 安装插件
git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions.git ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-autosuggestions

# 配置插件
vim ~/.zshrc

plugins=(
    git
    # other plugins...
    zsh-autosuggestions
)
```

安装 Homebrew
```
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```

安装 wget
```
brew install wget
```

废弃
```
brew install python@3.10
```

废弃
```
brew install pyenv
pyenv install 2.7.18
export PATH="$(pyenv root)/shims:${PATH}"
echo 'PATH=$(pyenv root)/shims:$PATH' >> ~/.zshrc
pyenv global 2.7.18
python --version
```

废弃
```
brew install mysql
brew install mysql-connector-c
```

python多版本

官方下载入口：https://www.python.org/downloads/macos/

```
# python 2.7
wget https://www.python.org/ftp/python/2.7.18/python-2.7.18-macosx10.9.pkg

# python 3.10
wget https://www.python.org/ftp/python/3.10.11/python-3.10.11-macos11.pkg
```


升级`Big Sur`之后，需要安装`Xcode 13 beta 2`，大约需要11G空间

[https://developer.apple.com/download/](https://developer.apple.com/download/)

[Command_Line_Tools_for_Xcode_12.3.dmg](https://download.developer.apple.com/Developer_Tools/Command_Line_Tools_for_Xcode_12.3/Command_Line_Tools_for_Xcode_12.3.dmg)

sshpass
```
wget https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
brew install sshpass.rb

sshpass -p "PASSWORD" ssh USER@IP
```


[https://nodejs.org/](https://nodejs.org/)

```
➜  ~ node -v
v20.10.0
➜  ~ npm -v
10.2.3
```

```
sudo npm install -g redoc-cli
```


sudo rm -rf /Library/Developer/CommandLineTools

sudo xcode-select --install

## 输入法

[在 Mac 上更改“输入法”设置](https://support.apple.com/zh-cn/guide/mac-help/mchl84525d76/14.0/mac/14.0)

系统设置 键盘 文字输入 简体拼音 勾选纠正模糊拼音（搜狗是默认打开的，不打开体验很差）

点按 中/英 切换 中英文

长按 中/英 切换 大小写

## 制作ubuntu22.04的U盘启动

1. [下载ubuntu](https://cn.ubuntu.com/download/desktop)

2. 查看U盘设备
```
diskutil list
```

3. 卸载U盘
```
# diskutil unmountDisk /dev/<U盘设备号>
diskutil unmountDisk /dev/disk2
```

4. 转换镜像格式(mac的dd不支持iso格式的镜像)
```
# hdiutil convert -format UDRW -o ~/Downloads/<dmg镜像文件,这里不用加后缀,后缀会自动加上> ~/Downloads/<iso镜像文件>
hdiutil convert -format UDRW -o ~/Downloads/ubuntu-22.04-desktop-amd64 ~/Downloads/ubuntu-22.04-desktop-amd64.iso
```

5. 复制镜像到U盘
```
cd ~/Downloads/
sudo dd bs=1m if=<dmg镜像文件> of=/dev/<原始U盘设备号,U盘设备号加r前缀> conv=sync
sudo dd bs=1m if=ubuntu-22.04-desktop-amd64.dmg of=/dev/rdisk2 conv=sync
```

6. 弹出U盘
```
diskutil eject /dev/<原始U盘设备号,U盘设备号加r前缀>
diskutil eject /dev/rdisk2
```

7. 测试U盘启动
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

8. 恢复U盘

制作启动盘后，U盘显示容量从几十G变成几M

插入U盘 磁盘管理工具 显示 显示所有设备 外置 选中第一级 抹掉 ExFAT(支持大文件) 方案：GUID 分区图/映射

关于分区方案参考：[Mac 上的“磁盘工具”中可用的分区方案](https://support.apple.com/zh-cn/guide/disk-utility/dsku1c614201/mac)

## 快捷键

- 直接删除（不进废纸篓）：option + command + delete

## 系统命令

```
# 查看当前目录磁盘空间占用并降序排列
# Linux系统命令为：du -h --max-depth=1 | sort -hr
du -h -d 1 | sort -hr
```

## Xcode

Xcode 是 Apple 的主要工作环境，供开发人员为 Apple 生态系统开发应用程序和其他项目。
如果它是iOS或iPadOS应用程序，或者可以在macOS中运行的软件，那么制作它的人可能在其创建的某个时候使用了 Xcode。

## VMware

[https://www.vmware.com/products/fusion/fusion-evaluation.html](https://www.vmware.com/products/fusion/fusion-evaluation.html)

TRY PRO FOR FREE

M芯片Mac只能安装 ARM 版的系统

激活方面
VMware Fusion 13.0 Player 面向个人用户是免费的，但需要用户向 VMware 申请个人版免费许可证。而面向商业用户则需要购买许可证。而且Player版本功能上比Pro版本少太多了，建议用户直接升级Pro版。

注：Pro 版则不存在免费版许可证的说法。

批量许可证激活密钥
经过测试， VMware Fusion 13.0 Pro 是可以使用批量许可证进行激活的，如下：

HF200-0W05K-089X8-4R1EK-032J0

## Windows 远程连接工具

Microsoft Remote Desktop Beta

AppStore 不支持中国区，需要找其他下载资源

## 网线直连（支持共享网络，通过Mac的Wi-Fi上外网）

雷雳接口通过网口转换器插入网线连接另一台设备（电脑）

查看连接类型：
```
系统设置 网络 已连接的网络会显示：AX88x72A 或 USB 10/100/1000 LAN
```

设置网络共享：
```
系统设置 通用 共享 互联网共享 设置（感叹号）

    共享以下来源的连接：Wi-Fi
    使用以下端口共享给设备：AX88x72A、USB 10/100/1000 LAN

系统设置 通用 共享 互联网共享 打开（开关）
```

注意：如果本地开启VPN，另一台设备无法通过共享网络上外网

## 开启SSH服务

系统设置 通用 共享 远程登录 打开（开关）

## 网络代理

MacOS 终端默认不走系统代理，即使我们已经打开了网络代理客户端的全局代理

代理配置：
```
cat ~/.zshrc

# proxy
alias proxy='export all_proxy=socks5://127.0.0.1:1086 && curl -L cip.cc'
alias unproxy='unset all_proxy && curl -L cip.cc'
```

## WinRAR

[https://www.win-rar.com/postdownload.html?&L=7](https://www.win-rar.com/postdownload.html?&L=7)

## 扩容

```
➜  ~ df -h /Volumes/*
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   926Gi    13Gi   730Gi     2%    391k  4.3G    0%   /
/dev/disk5s1     932Gi    43Mi   932Gi     1%       1     0  100%   /Volumes/Transcend
```

## 排错

`zsh: no matches found:`

```
echo "setopt +o nomatch" >> ~/.zshrc
source ~/.zshrc
```
