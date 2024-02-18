# HTTPS

## 本地证书浏览器配置

### Chrome 浏览器

访问页面，会出现提示：该网站的安全证书不受信任！

仍然继续访问, https 标识为 X

三道杠（新版是三点） >> 设置 >> HTTPS/SSL >> 管理证书 >> 证书管理器 >> 授权中心 >> 导入 >> 选择证书 >> 勾选信任该证书，以标识网站的身份。

再次访问，图标变为绿色，心情瞬间变好了。

### IE 浏览器

```
Internet 选项 >> 内容 >> 证书 >> 受信任的根证书颁发机构 >> 导入 >> 下一步 >> 浏览 >> 选择 >> 弹出提示，选是 
```

附加：  
Windows 修改 hosts `C:\Windows\System32\drivers\etc\hosts`


## HSTS

[https://hstspreload.appspot.com/](https://hstspreload.appspot.com/)

状态码：307

## 免费工具

- **[Let's Encrypt](https://letsencrypt.org/)**

结合 [Certbot](https://certbot.eff.org/) 工具，自动生成

参考: [Certbot-免费的HTTPS证书](https://zhuanlan.zhihu.com/p/80909555)

- **[ZeroSSL](https://zerossl.com/)**

[Installing-SSL-Certificate-on-NGINX](https://help.zerossl.com/hc/en-us/articles/360058295894-Installing-SSL-Certificate-on-NGINX)

第二步`Merge .crt Files`，文档错误之处，更正为：
```
cat ca_bundle.crt >> certificate.crt
```

## 为什么有了https, 还需要做签名验证？

当用户在浏览器当中加载受HTTPS保护的网站时，浏览器实际上只会验证两件事：
1. 网站是否提供了证书；
2. 证书是不是浏览器（操作系统）信任的根证书CA机构颁发的。

一切都是建立在我们对根证书CA机构的信任基础之上。
有时候根CA机构会被骗，如果我们安装个代理工具（fiddler）的证书，就可以用代理工具抓到https请求的内容，还可以篡改数据。
这时签名可以防止篡改数据，因为签名的密钥没有在网络中进行传输（服务器端线下颁发给客户端或者客户端自己输入的登陆密码作为密钥，甚至登陆使用的短信验证码也可以作为密钥）

