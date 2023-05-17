# K3S

[https://k3s.io/](https://k3s.io/)

两者命令对比表：

containerd 命令   | docker 命令                             |   备注
---|---------------------------------------|---
ctr image ls    | docker images                         |   获取image信息
ctr image pull nginx    | docker pull nginx                     |   pull 一个nginx的image
ctr image tag nginx nginx-test  | docker tag nginx nginx-test           |   tag 一个nginx的image
ctr image push nginx-test   | docker push nginx-test                |   push nginx-test的image
ctr image pull nginx    | docker pull nginx                     |   pull 一个nginx的image
ctr image import nginx.tar  | docker load < nginx.tar.gz            |   导入本地镜像ctr不支持压缩
ctr run -d --env 111 nginx-test nginx   | docker run -d --name=nginx nginx-test |   运行的一个容器
ctr task ls | docker ps                             |   查看运行的容器
