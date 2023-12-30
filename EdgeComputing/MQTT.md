# MQTT

[EMQX](https://github.com/emqx/emqx/blob/master/README-CN.md)


```
docker run -d --name emqx -p 1883:1883 -p 8083:8083 -p 8084:8084 -p 8883:8883 -p 18083:18083 emqx:4
```

EMQX Dashboard: [http://localhost:18083](http://localhost:18083)

默认用户名及密码: admin/public

设置用户名及密码: admin/mqtt123456

端口:

端口 | 说明
--- | ---
1883 | TCP 端口
8883 | TCP SSL 端口
8083 | WebSocket 端口
8084 | WebSocket SSL 端口
8080 | 执行引擎HTTP API 端口
18083 | EMQX Dashboard 管理控制台端口

参考:

- [安装 EMQX](https://www.emqx.io/docs/zh/v5.0/getting-started/getting-started.html#%E5%90%AF%E5%8A%A8-emqx)


## 客户端

- [MQTT Go Client library](https://www.emqx.io/docs/en/v4/development/go.html)
- [MQTT Python client library](https://www.emqx.io/docs/en/v4/development/python.html)
- [MQTT JavaScript client library](https://www.emqx.io/docs/en/v4/development/javascript.html)
