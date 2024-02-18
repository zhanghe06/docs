# 一键登录 OneClick

参考: [App一键登录（获取本机手机号码）](https://saas.onlinedown.net/detail/15100.html)

目前市面上APP的常见登录方式有：
- 手机号码+密码登录
- 手机号码+短信验证码
- 一键登录

## 登录对比

1.1 手机号码+密码登录：
实现方式：用户输入手机号和密码，先注册再登录，都在服务器进行处理验证

优点：较早的登陆方法，没什么优势

缺点：需要用户注册后再进行登录，操作步骤繁琐；

耗时：一整套操作约25秒左右

费用：不会产生费用

1.2 手机号码+短信验证码：
实现方式：用户输入手机号，等待短信，输入短信进行验证登录

优点：比1.1的方式要便捷

缺点：高峰期时会出现无法接收短信等情况，间接导致用户流失

耗时：一整套操作约15秒左右

费用：会产生短信费用

1.3 一键登录：
实现方式：使用运行商网关验证登录【运行商含：中国移动 中国联通 中国电信】

优点：点击按钮即可，操作简单；比1.1和1.2更便捷

缺点：暂未发现

耗时：2s左右

费用：会产生费用，但是低于短信费用

## 登录平台

方案1：阿里云
》接入SDK：[点击查看SDK](https://help.aliyun.com/document_detail/615126.html)

》支持客户端：Android；iOS；UniApp；

》支持运营商：中国移动；中国联通；中国电信

》费用：[点击查看费用](https://help.aliyun.com/document_detail/85132.html)

》推荐程度：强烈推荐


方案2：极光
》接入SDK：[点击查看SDK](https://www.jiguang.cn/identify)

》支持客户端：Android；iOS；

》支持运营商：中国移动；中国联通；中国电信

》费用：[点击查看费用](https://www.jiguang.cn/identify)

》推荐程度：强烈推荐


方案3：Mob
》接入SDK：[点击查看SDK](https://www.mob.com/mobService/secverify)

》支持客户端：Android；iOS；

》支持运营商：中国移动；中国联通；中国电信

》费用：[点击查看费用](https://www.mob.com/mobService/secverify)

》推荐程度：强烈推荐


方案4：中国移动
》接入SDK：[点击查看SDK](http://dev.10086.cn/idenRealNameLoginOneKey)

》支持客户端：Android；iOS；

》支持运营商：中国移动；

》费用：[点击查看费用](http://dev.10086.cn/idenRealNameLoginOneKey)

》推荐程度：不推荐【不能同时支持三大运营商，费用较高】
