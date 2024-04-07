# Harbor

[https://goharbor.io/docs/2.2.0/](https://goharbor.io/docs/2.2.0/)

```
docker login reg.yourdomain.com
docker push reg.yourdomain.com/myproject/myrepo:mytag
```

/etc/docker/daemon.json
```
{
    "insecure-registries" : ["myregistrydomain.com:5000", "0.0.0.0"]
}
```

## 本地安装

https://github.com/goharbor/harbor/releases/download/v2.10.1/harbor-offline-installer-v2.10.1.tgz

```

```
