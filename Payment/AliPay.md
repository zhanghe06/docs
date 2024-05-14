# AliPay

- [开放平台](https://open.alipay.com/develop/manage)
- [沙箱应用](https://open.alipay.com/develop/sandbox/app)
- [创建应用](https://opendocs.alipay.com/open/200/105310)
- [沙盒版支付宝]()
- [https://github.com/smartwalle/alipay](https://github.com/smartwalle/alipay)
- [App支付]()
- [支付宝公钥](https://opendocs.alipay.com/support/01rauu)
- [教程](https://blog.csdn.net/qq_56282336/article/details/130845610)
- [当面付接口如何计算优惠](https://developer.aliyun.com/article/710915)


2、下载沙盒版支付宝并使用沙盒账号中的买家信息进行登陆，之后使用此账号登陆的支付宝来进行扫码

使用自定义密钥，默认密钥测试失败



https://opendocs.alipay.com/open/203/107084?pathHash=a33de091


支付宝网关：
不用动

应用网关：
必填。用于接收支付宝异步通知消息，需要传入 http(s) 公网可访问网页地址，可查看 应用网关。
填写域名

授权回调地址：
选填。网页/移动应用 指定的回调页面 URL，用户信息授权 成功后，将在该 URL 后携带授权码等信息并跳转至该页面。
说明：授权链接中配置的 redirect_uri 的值必须与此回调地址保持一致 (如：https://www.alipay.com) 。

回调配置
```
应用网关地址
https://xxx.com/api/payment/alipay/notify
授权回调地址
https://xxx.com/api/payment/alipay/return
```

return_url

支付成功后点击完成会自动跳转回商家页面地址， 同时在 URL 地址上附带支付结果参数，回跳参数可查看本文 附录 > 前台回跳参数说明。在 iOS 系统中，唤起支付宝客户端支付完成后，不会自动回到浏览器或商家 App。用户可手工切回到浏览器或商家 App。
前台页面地址
GET方式
可以是本地地址


notify_url

异步通知地址，用于接收支付宝推送给商户的支付/退款成功的消息。
后台接口地址
POST方式
需是服务器地址


回调日志
```
[GIN] 2023/10/10 - 21:28:13 | 401 |      97.038µs |  39.144.105.161 | GET      "/api/payment/alipay/return?charset=utf-8&out_trade_no=5&method=alipay.trade.wap.pay.return&total_amount=4354.50&sign=Rrch2x3VzLj15kxso2G8RDWpVLTA%2B74uVBj7cgAC%2BNHAMYr5nijF%2FkRGyAdWfKEEXSde81mMVUSWaKPtXVDkUkyygu%2B2KymN%2BKJl2iVHVPSMVmiTbXkg5MZpU4c2R3WGTSiXhVPd4K8HW6upcnDF1HGcMh2%2F80DcdMnCfHxZ18Ch1tY4rkrY3Myp%2BCPunAsMLbKQiNmdowgOPPYtaPVrsUBU32n8aOm2v2YlRabI0Tbu9Ttq9ktn9g6fB3R5pfk0p6CZrrJySL8FjJPlJDGOCJxWoQr%2B9FCtxvyjJpnJ9gi6Fgi3kCo9uIeQMe03j9n8xhRbN0estknRNlt%2Fci0IYw%3D%3D&trade_no=2023101022001497300500953093&auth_app_id=9021000128688617&version=1.0&app_id=9021000128688617&sign_type=RSA2&seller_id=2088721014934993&timestamp=2023-10-10+21%3A28%3A13"
```


接口响应

响应值	| 描述	| 是否重试
--- | --- | ---
fail	| 消息获取失败	| 重试
success	| 消息获取成功	| 不重试


## 开发

三步实现支付宝支付【go语言 支付宝沙箱】
https://blog.csdn.net/xiao_xiao_w/article/details/136586052

合并支付
https://opendocs.alipay.com/open/direct-payment/qadp9d?pathHash=854361c6


## 注册

- [常见问题](https://opendocs.alipay.com/open/204/105849/)
- [开放平台](https://open.alipay.com/develop/manage)
- [商家平台](https://b.alipay.com/page/store-management/infomanage)

确认主体信息
```
账号中心 -> 绑定 -> APPID绑定 -> 绑定详情 -> APPID信息
```
