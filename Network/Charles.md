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
3. 然后根据提示安装并信任描述文件 (设置 -> 通用 -> 描述文件 -> 选择证书点击安装)
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
