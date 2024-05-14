# Curl

## 服务器多网卡场景下的常用排错命令

服务器多网卡场景下的常用排错命令，适用于通过管理网络排查业务网络问题

```
# 测试网络连通性
ping -c 4 -I <业务网络接口 NETROEK_INTERFACE> <业务HOST/IP>

# 测试服务可用性
curl --interface <业务网络接口 NETROEK_INTERFACE> <业务服务地址>
```

原理：通过指定网卡（网络出口）来测试网络
