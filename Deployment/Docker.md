# Docker

Get Docker CE for CentOS
```
# yum install -y yum-utils device-mapper-persistent-data lvm2
# yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
# yum install -y docker-ce
# systemctl start docker
# docker -v
# docker ps
```
参考: [https://docs.docker.com/engine/install/centos/](https://docs.docker.com/engine/install/centos/)

Get Docker CE for Ubuntu
```
# apt-get update
# apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
# apt-key fingerprint 0EBFCD88
# add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
# apt-get update
# apt-get install docker-ce docker-ce-cli containerd.io
# docker -v
# docker ps
```
参考: [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)


Docker 中国官方镜像加速 registry mirror [https://registry.docker-cn.com](https://registry.docker-cn.com)

```
{
    "registry-mirrors": ["https://registry.docker-cn.com"]
}
```

## 错误调试

拉取镜像报错
```
docker: Error response from daemon: Get https://registry-1.docker.io/v2/: EOF.
```

通过dig找到可用ip
```
➜  ~ dig @114.114.114.114 registry-1.docker.io

; <<>> DiG 9.10.6 <<>> @114.114.114.114 registry-1.docker.io
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26129
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;registry-1.docker.io.		IN	A

;; ANSWER SECTION:
registry-1.docker.io.	35	IN	A	52.22.201.61
registry-1.docker.io.	35	IN	A	34.232.31.24
registry-1.docker.io.	35	IN	A	34.233.151.211
registry-1.docker.io.	35	IN	A	52.22.67.152
registry-1.docker.io.	35	IN	A	34.205.207.96
registry-1.docker.io.	35	IN	A	52.206.40.44
registry-1.docker.io.	35	IN	A	34.206.236.31
registry-1.docker.io.	35	IN	A	34.228.211.243

;; Query time: 10 msec
;; SERVER: 114.114.114.114#53(114.114.114.114)
;; WHEN: Wed Mar 13 13:40:36 CST 2019
;; MSG SIZE  rcvd: 177
```

向hosts添加可用域名解析（有时候这一步不需要）
```
echo '52.22.201.61 registry-1.docker.io' >> /etc/hosts
```

## 离线处理镜像

[https://docs.docker.com/engine/reference/commandline/save](https://docs.docker.com/engine/reference/commandline/save)

```
# 下载
docker save -o myimage.tar myimage:latest
docker save myimage:latest | gzip > myimage_latest.tar.gz
# 加载
docker load -i myimage.tar
```

## 搜索镜像

```
docker search httpd
```

```
NAME                                    DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
httpd                                   The Apache HTTP Server Project                  3569      [OK]
centos/httpd-24-centos7                 Platform for running Apache httpd 2.4 or bui…   40
centos/httpd                                                                            34                   [OK]
polinux/httpd-php                       Apache with PHP in Docker (Supervisor, CentO…   5                    [OK]
...
```

清空全部镜像
```
docker rmi -f $(docker images -qa)
```


## 时区

ubuntu基础镜像可以直接添加环境变量
```
docker run \
    ...
    -e TZ=Asia/Shanghai \
    ...
    nginx:logrotate
```

alpine基础镜像需要在Dockerfile中安装服务
```
# 替换镜像
RUN echo "https://mirrors.aliyun.com/alpine/v3.16/main" > /etc/apk/repositories && echo "https://mirrors.aliyun.com/alpine/v3.16/community" >> /etc/apk/repositories

RUN apk add -U tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```


## 原理

- Cgroups = limits how much you can use;
- Namespaces = limits what you can see(and therefore use)

Cgroups involve resource metering and limiting

Namespaces provide processes with their own view of the system.(障眼法)

中文结论: namespace 是用来做资源隔离, cgroup 是用来做资源限制

## 重启策略

Docker提供的重启策略不只是always，有如下：

策略  | 描述
--- | ---
no  | 默认值，不会自动重启。
on-failure  | 因为错误退出就会重启，错误退出指非0退出码。
always  | 停止就会重启。如果是手工停止，则在Docker daemon或容器本身重启时启动。
unless-stopped  | 类似于 always，除了当容器被停止，它是不会重启的。

对于已经在运行的容器，需要修改重启策略，则可以通过update命令来增加：
```
docker update --restart=no xxx
docker update --restart=always xxx
```

## 网络

```
docker network ls
```

1、--network=bridge
默认就是 bridge，即桥接网络，以桥接模式连接到宿主机，创建一个独立网络
可以通过自定义bridge将多个容器互通
bridge还可以使用指定容器网络和自定义网络名称
```
--network=netName
--network=container:Name/ID
```

2、--network=host
与宿主机共享网络，也就是在网络这块不会与宿主机隔离，而是共享宿主机的网络配置，并且 容器不会分配自己的ip地址
由于不需要端口映射，host网络的性能较高.
host模式主机网络驱动程序仅适用于Linux主机，并且不支持Docker for Mac，Docker for Windows或Docker EE for Windows Server。

判断host模式是否生效
```
ping host.docker.internal
# 如果是127.0.0.1就对了
```

3、--network=none
无网络，容器将无法联网。

## 修改存储目录

```
sudo systemctl stop docker
mkdir -p /data/docker-root
```

/etc/docker/daemon.json
```
{
    "data-root": "/data/docker-root"
}
```

```
mv /var/lib/docker/* /data/docker-root/
sudo systemctl start docker
sudo docker info | grep "Docker Root Dir"
```

## 清理镜像

清理为None的镜像
```
sudo docker images | grep none | awk '{print $3}' | xargs sudo docker rmi
```

## 查看信息

```
docker inspect -f '{{.NetworkSettings.Networks.net_name.IPAddress}}' ba_mariadb
```

## 僵尸进程回收

`docker run`启动容器时可以添加`--init`参数，此时`Docker`会使用`docker-init`作为1号进程，帮你管理容器内子进程，例如回收僵尸进程等。

## 将当前普通用户加入到docker组

```
sudo gpasswd -a $USER docker        # 将当前普通用户加入到docker组
newgrp docker                       # 更新docker组
```

普通用户执行docker命令无需sudo

## 动态更新容器资源限制

```
# 查看容器资源占用
docker stats

# 更新容器内存限制
docker container update <container_name> --memory="512m" --memory-swap="512m"

# 更新容器核数限制
docker container update <container_name> --cpus="0.5"
```
