# Alpine


- [https://alpinelinux.org](https://alpinelinux.org)
- [http://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management#Add_a_Package](http://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management#Add_a_Package)
- [https://github.com/gliderlabs/docker-alpine](https://github.com/gliderlabs/docker-alpine)
- [https://yeasy.gitbook.io/docker_practice/os/alpine](https://yeasy.gitbook.io/docker_practice/os/alpine)

迁移至 Alpine 基础镜像
```
ubuntu/debian -> alpine
python:3 -> python:3-alpine
ruby:2.6 -> ruby:2.6-alpine
```

```
$ echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
$ apk --update add --no-cache <package>
```

```
RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g" /etc/apk/repositories \
      && apk add --no-cache <package>
```

- Alpine 官网：[https://www.alpinelinux.org](https://www.alpinelinux.org)
- Alpine 官方仓库：[https://github.com/alpinelinux](https://github.com/alpinelinux)
- Alpine 官方镜像：[https://hub.docker.com/_/alpine](https://hub.docker.com/_/alpine)
- Alpine 官方镜像仓库：[https://github.com/gliderlabs/docker-alpine](https://github.com/gliderlabs/docker-alpine)

## 调试镜像
```
docker run --rm -it python:3.10-alpine sh
```
