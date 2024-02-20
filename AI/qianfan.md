# 百度千帆

- [千帆大模型计费说明](https://developer.baidu.com/article/detail.html?id=520000)


开通百度智能云千帆大模型平台服务自动获取1000000+免费tokens

价格费用举例:

tokens约等于「服务输入+服务输出」的「中文字+其他语种单词数 x 1.3」，向下取整，标点符号不计数

输入：“请给我念一首诗”
输出：“春眠不觉晓，处处闻啼鸟。 夜来风雨声，花落知多少。”

共中文字数为27，总计tokens为27

调用价格为0.008 x 27 x 0.001=0.000216元

配置：
```
AI_BD_QIANFAN = {
    # https://console.bce.baidu.com/iam/#/iam/accesslist
    'access_key': '',
    'secret_key': '',  # 查看需要短信验证码
    # https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    'app_id': '',
    'app_api_key': '',
    'app_secret_key': '',
}
```
