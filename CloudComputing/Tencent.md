# Tencent

**官网**

[https://cloud.tencent.com](https://cloud.tencent.com)

**云盾**

> [!NOTE|label:关闭理由]
> 数据说话，占用额外资源

```
**[terminal]
  PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND
13946 root      20   0 1009216  69912   4152 S  0.7  3.7 113:10.82 YDService
```

关闭云盾

1、控制台方式
> [!TIP|labelVisibility:hidden|iconVisibility:hidden]
> 在 [主机安全（云镜）-资产管理-主机列表](https://console.cloud.tencent.com/cwp/asset/machine) 里找到自己的机器，点击卸载即可。<br>
> 约1分钟同步状态，实测没有卸载成功，这就有点扯了。

2、终端方式
> [!TIP|labelVisibility:hidden|iconVisibility:hidden]
> ```
> **[terminal]
> **[prompt root@node]**[delimiter :]**[path ~]**[delimiter # ]**[command /usr/local/qcloud/YunJing/uninst.sh]
> ```
