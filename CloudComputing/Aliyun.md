# Aliyun

**官网**

[https://www.aliyun.com](https://www.aliyun.com)

> [!TIP|label:购机指南]
> 最新活动 -> 特惠专区 -> HI拼团

**云盾**

关闭云盾
```
**[terminal]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command systemctl stop aegis]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command systemctl disable aegis]
```

检查状态
```
**[terminal]
**[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command systemctl status aegis]
```

**存储**

方案 | [NAS(文件存储)](https://nasnext.console.aliyun.com/introduction) | [OSS(对象存储)](https://help.aliyun.com/document_detail/31817.html) | 云盘(块存储、裸磁盘)
--- | --- | --- | ---
共享访问 | 支持上千台ECS同时挂载 | 支持百万并发请求 | 单台ECS访问
协议接口 | POSIX / NFS(Linux) / SMB(Windows) / MPI | RESTful API / SDK / 客户端 | 格式化后支持POSIX协议
最大容量 | 10PiB | 无限 | 32TiB
适用场景 | 共享文件 | 图片、视频 | 数据库
按量付费 | - | - | 18.8 K/T/年
包年包月 | 3.75 K/T/年 | 0.9 K/T/年(不含下行流量) | 6.25 K/T/年


自建存储

NAS 套件（RockPi4C主板*1、外壳*1、扩展卡*1、eMMC*1） + WD2.5寸1T垂直HDD蓝盘*4

费用 225USD + 840RMB

条件:
- 自有域名
- 内网穿透


**带宽**

阿里云带宽上行和下行当超过10M带宽时是对等的，以10M为分割点，规则如下：
1. 当出网带宽小于10 Mbit/s时，入网带宽最大为10 Mbit/s。
2. 当出网带宽大于10 Mbit/s时，入网带宽与您购买的出网带宽一致。

## OSS

- [使用STS临时访问凭证访问OSS](https://help.aliyun.com/zh/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss)
- [对象存储 OSS](https://help.aliyun.com/zh/oss/)
- [图片处理](https://help.aliyun.com/zh/oss/user-guide/latest-version-of-img-guide/)
- [x-oss-process使用指南](https://help.aliyun.com/zh/imm/user-guide-for-x-oss-process)

参数处理
```
# 图片定宽
?x-oss-process=image/resize,w_540,m_lfit
?x-oss-process=image/resize,m_pad,w_540,h_960,color_000000
# 视频截帧
?x-oss-process=video/snapshot,t_4000,f_jpg,w_540,m_fast
```

?x-oss-process=image/info