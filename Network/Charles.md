# Charles

工具: [https://www.charlesproxy.com](https://www.charlesproxy.com)

破解: [https://github.com/100apps/charles-hacking](https://github.com/100apps/charles-hacking)

[https://github.com/100apps/charles-hacking/issues/39](https://github.com/100apps/charles-hacking/issues/39)

toms' crack
```
Name: Cracked
Key: 05aeeaadc069f0ab2c
```

```
rm -f /Applications/Charles.app/Contents/Java/charles.jar
wget https://github.com/100apps/charles-hacking/blob/master/4.2/charles.jar?raw=true /Applications/Charles.app/Contents/Java/charles.jar
```

证书配置:

[https://www.charlesproxy.com/documentation/using-charles/ssl-certificates/](https://www.charlesproxy.com/documentation/using-charles/ssl-certificates/)

- Mac
1. Help -> SSL Proxying -> Install Charles Root Certificate. 
2. 然后信任证书（Charles Proxy CA）

- Iphone
1. Help -> SSL Proxying -> Install Charles Root Certificate on a Mobile Device or Remote Browser
2. safari 直接访问: https://chls.pro/ssl
3. 然后根据提示安装并信任描述文件 (设置 -> 通用 -> VPN与设备 -> 配置描述文件 -> 选择证书点击安装)
4. 设置 -> 通用 -> 关于本机 -> 证书信任设置 -> CA勾选

- Android
1. Help -> SSL Proxying -> Install Charles Root Certificate on a Mobile Device or Remote Browser
2. 使用第三方的浏览器 直接访问: https://chls.pro/ssl
3. 下载charles-proxy-ssl-proxying-certificate.pem
4. 确认手机开启锁屏密码或手势
5. 设置 -> 更多设置 -> 系统安全 -> 从存储设备安装证书 填写名称charles

红米：安全 -> 更多安全设置 -> 加密与凭据 -> 安装证书 -> 安装CA证书 -> 输入PIN码（就是屏幕解锁密码）

HTTP 中文乱码
```
vim /Applications/Charles.app/Contents/Info.plist
```

iphone 设置代理注意顺序
先忽略此网络，然后设置HTTP代理（此时并未连接WiFi）；再连接WIFI，此时刚才设置的（HTTP）代理已消失，于是再设置一次（HTTP）代理，再回来（WiFi界面），再进去（点感叹号）看就有了。注意顺序。


设置 Recording Settings

## 关于 Android 无法抓包的问题

Android 7.0 之后默认不信任用户添加到系统的 CA 证书：
```
To provide a more consistent and more secure experience across the Android ecosystem, 
beginning with Android Nougat, 
compatible devices trust only the standardized system CAs maintained in AOSP.
```

源自：[Android Developers Blog](https://android-developers.googleblog.com/2016/07/changes-to-trusted-certificate.html)

换句话说，就是对基于 SDK24 及以上的 APP 来说，即使你在手机上安装了抓包工具的证书也无法抓取 HTTPS 请求。

解决方案：
1、[官方解决方案](https://www.charlesproxy.com/documentation/using-charles/ssl-certificates/)（需修改代码）  
2、将抓包软件的证书安装成系统证书（需 ROOT）

参考: 
- [Android 7.0 之后抓包 unknown 和证书无效的解决方案](https://blog.lv5.moe/p/solutions-to-certificate-invalidation-after-android-7)
- [Charles在Android7.0以上抓包https出现<unknown>的解决办法](https://xiandan.io/posts/charles-https.html)
- [为什么你的 Charles 会抓包失败](https://supercodepower.com/use-charles)
- [小米手机开启ROOT权限从头到尾的步骤](https://zhuanlan.zhihu.com/p/499270772)


## 小米/红米 解锁 Unlock Bootloader

解锁小米手机: [https://www.miui.com/unlock/index.html](https://www.miui.com/unlock/index.html)

```
设置 -> 我的设备 -> 全部参数与信息 -> 多次(6)点击"MIUI版本" 即可打开开发者选项
设置 -> 更多设置 -> 开发者选项 -> 打开：OEM解锁、USB调试、USB调试（安全设置）
设置 -> 更多设置 -> 开发者选项 -> 设备解锁状态 -> 点击"绑定账号和设备" 等待7*24=168小时后可以刷机
打开miflash_unlock.exe 登录小米账号，一定要账号和密码登录，第三方登录解锁时会报错
手动进入Bootloader模式（关机后，同时按住开机键和音量下键）
通过USB连接手机，点击 “解锁”按钮
```

## 小米/红米 刷机 ROOT（方案不可行，无法拿到开发包）

MIUI14开发版安装方法如下:

1、将开发版的ROM包拷贝到手机SD卡根目录下，并且将其重命名为“update.zip”文件，注意全部小写。

2、打开小米手机，进入“关于手机”界面，然后点击手机上的硬按键“菜单”打开“扩展菜单”，从中选择“进入Recovery模式”项。也可以在关机状态下同时按住“音量键上”和“电源键”开机，手机会自动启动并进入Recovery模式。

3、此时手机重启，进入Recovery模式，在此模式下，利用“电源键”进行确认，利用“音量键+”和“音量键-”进行选择。首先在打开的第一界面中选择“简体中文”。

4、接着在打开的“主菜单”界面中，利用【音量键】选择“将update.zip安装到系统一”项，并按【电源键】进行确认。

5、此时将打开“更新确认”窗口中，选择“确定”并用【电源键】进行确认。

6、接着将自动完成系统的更新操作，卡刷完成，就完成了MIUI14开发版的升级安装。


## 小米/红米 开启 Play Store (Google)

应用商店 -> 搜索 Google Play 商店 -> 安装

设置 -> 账号与同步 -> 谷歌基础服务 -> 勾选
设置 -> WLAN -> 选中网络并设置代理
设置 -> 账号与同步 -> 添加账号 -> Google

## 系统证书安装

将抓包软件的证书安装成系统证书（需 ROOT）
系统证书目录：/system/etc/security/cacerts/

其中的每个证书的命名规则如下：
<Certificate_Hash>.<Number>
文件名是一个 Hash 值，而后缀是一个数字。

文件名可以用下面的命令计算出来：

openssl x509 -subject_hash_old -in <Certificate_File>

后缀名的数字是为了防止文件名冲突的，比如如果两个证书算出的 Hash 值是一样的话，那么一个证书的后缀名数字可以设置成 0，而另一个证书的后缀名数字可以设置成 1


## 开发版(公测)刷机包

[下载红米 K60 / POCO F5 Pro (mondrian) 开发版(公测)刷机包 MIUI14 V14.0.23.7.31.DEV](https://xiaomirom.com/download/redmi-k60-poco-f5-pro-mondrian-weekly-V14.0.23.7.31.DEV/)

[MIUI官方ROM仓库](https://roms.miuier.com/zh-cn/devices/mondrian/)


## 终极方案

通过`Magisk`获取手机`root`权限

- Android: 13
- MIUI: 14.0.26

一、获取最新完整卡刷包
```
设置 -> 我的设备 -> MIUI版本 -> 右上角三个点 -> 下载最新完整包
手机用数据线连上电脑（MacOS）将手机Download目录的zip包拷贝到电脑
unzip miui_MONDRIAN_V14.0.26.0.TMNCNXM_4917818288_13.0.zip
解压后找到payload.bin
```

二、获取`Android`系统启动加载文件`boot.img`
```
通过解包工具payload-dumper-go提取boot.img
git clone https://github.com/ssut/payload-dumper-go
cd payload-dumper-go
go mod tidy
go run *.go payload.bin
生成extracted_xxx目录，将其中boot.img复制到手机Download目录中
```

三、通过`Magisk`修改系统启动加载文件
```
手机通过Google的Play商店安装Magisk
主页 -> Magisk 安装 -> 选择并修补一个文件 选中boot.img -> 点击开始
成功后在Download目录中会生成一个magisk_xxxx.img
将此文件复制到电脑中，并重命名为boot.img
```

四、刷入修改后的系统启动加载文件
```
➜  ~ mkdir xiaomi
➜  ~ cd xiaomi
➜  xiaomi adb reboot fastboot
➜  xiaomi fastboot flash boot boot.img
Sending 'boot_a' (196608 KB)                       OKAY [  4.881s]
Writing 'boot_a'                                   OKAY [  0.272s]
Finished. Total time: 5.159s
➜  xiaomi fastboot reboot
Rebooting                                          OKAY [  0.000s]
Finished. Total time: 0.001s
```

五、安装信任用户证书模块
```
下载信任用户证书模块
➜  xiaomi wget https://github.com/NVISOsecurity/MagiskTrustUserCerts/releases/download/v0.4.1/AlwaysTrustUserCerts.zip
复制到手机Download目录中
Magisk安装AlwaysTrustUserCerts模块
模块 -> 从本地安装 -> 选择AlwaysTrustUserCerts.zip -> 确定
```

原因:
官方已经不提供线刷包，卡刷包需要在小米社区达到4级才有资格申请开发包的资格

参考:
- [Magisk 系列教程 (基于 v24.3)](https://www.cnblogs.com/delayer/p/16247809.html)
- [Magisk apk](https://github.com/topjohnwu/Magisk/releases)
- [Magisk 安装](https://sspai.com/post/67932)
- [golang版本 解包工具payload.bin提取boot.img](https://github.com/ssut/payload-dumper-go)
- [python版本 解包工具payload.bin提取boot.img](https://github.com/vm03/payload_dumper)
- [Android SDK Platform-Tools 平台工具](https://developer.android.com/studio/releases/platform-tools?hl=zh-cn)
- [https://github.com/NVISOsecurity/MagiskTrustUserCerts](https://github.com/NVISOsecurity/MagiskTrustUserCerts)


## SSL-PINNING认证

抖音apk做了自己内部的SSL-PINNING认证

需要用到Xposed模块

需要替换libsscronet.so

可以借助Magisk的模块

