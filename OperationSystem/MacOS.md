# MacOS

## 安装

安装 iTerm2 oh-my-zsh

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
brew install python@3.10
```

```
brew install pyenv
pyenv install 2.7.18
export PATH="$(pyenv root)/shims:${PATH}"
echo 'PATH=$(pyenv root)/shims:$PATH' >> ~/.zshrc
pyenv global 2.7.18
python --version
```

```
brew install mysql
brew install mysql-connector-c
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


sudo rm -rf /Library/Developer/CommandLineTools

sudo xcode-select --install

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

## 排错

`zsh: no matches found:`

```
echo "setopt +o nomatch" >> ~/.zshrc
source ~/.zshrc
```
