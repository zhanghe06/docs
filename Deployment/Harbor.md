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

## 安装指南

https://goharbor.io/docs/latest/install-config/


```
wget https://github.com/goharbor/harbor/releases/download/v2.10.2-rc1/harbor-offline-installer-v2.10.2-rc1.tgz
tar xzvf harbor-offline-installer-v2.10.2-rc1.tgz
cd harbor
cp harbor.yml{.tmpl,}
./prepare
./install.sh
docker compose -f docker-compose.yml ps
```

## 使用指南

http://<my_registry_domain>
```
账号：admin
密码：Harbor12345
```

```
docker login <my_registry_domain>
```

新建私有项目：test

```
docker tag nginx:1.24-alpine <my_registry_domain>/test/nginx:1.24-alpine
docker push <my_registry_domain>/test/nginx:1.24-alpine
```

```
docker logout  # 注销Docker Hub
docker logout <my_registry_domain> # 注销私有仓库
```

```
docker login <my_registry_domain> -u admin -p Harbor12345 && docker pull <my_registry_domain>/test/nginx:1.24-alpine && docker logout <my_registry_domain>
```
