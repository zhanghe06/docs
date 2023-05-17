# SeaweedFS

[SeaweedFS 项目地址](https://github.com/chrislusf/seaweedfs)


## 安装

### Go (Golang)

下载页面： https://golang.org/dl/

```
$ wget https://dl.google.com/go/go1.11.1.linux-amd64.tar.gz
$ sudo tar -C /usr/local -xzf go1.11.1.linux-amd64.tar.gz
$ sudo vim /etc/profile
    export GOROOT=/usr/local/go
    export GOPATH=$HOME/work
    export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
$ source /etc/profile
```

或者仅为当前用户设置环境变量
```
$ vim ~/.bashrc
$ source ~/.bashrc
```

注意：使用 zsh 的用户, 需要为 zsh 设置环境变量
```
$ vim ~/.zshrc
$ source ~/.zshrc
```

### Weed

依赖 git (版本控制工具)

```
go get github.com/chrislusf/seaweedfs/weed
```


## 启动

Start Master Server
```
$ weed master
```

Start Volume Servers
```
$ mkdir /tmp/data1 /tmp/data2
$ chmod 777 /tmp/data1 /tmp/data2
$ weed volume -dir="/tmp/data1" -max=5  -mserver="localhost:9333" -port=8080 &
$ weed volume -dir="/tmp/data2" -max=10 -mserver="localhost:9333" -port=8081 &
```

```
$ weed volume -dir=/tmp/data1/ -mserver="localhost:9333" -ip="192.168.2.32" -port=8080
```


## 启动（方式二）
```
$ weed server -dir=/tmp/data1/ -filer -filer.port=8000 -master.port=9333 -volume.port=8001
```
集群管理: http://127.0.0.1:9333/

归档管理: http://localhost:8000/

卷管理: http://localhost:8001/ui/index.html

图片地址: http://localhost:8001/


上传文件请求
```
$ curl http://localhost:9333/dir/assign
{"fid":"2,055a54a8ec","url":"127.0.0.1:8080","publicUrl":"127.0.0.1:8080","count":1}
```

上传文件
```
$ curl -X PUT -F file=@/home/zhanghe/metro.jpg http://127.0.0.1:8080/2,055a54a8ec
{"name":"metro.jpg","size":1830848}
```

删除文件
```
$ curl -X DELETE http://127.0.0.1:8080/2,055a54a8ec
{"size":1830869}
```

文件读取
```
$ curl "http://localhost:9333/dir/lookup?volumeId=2"
{"volumeId":"2","locations":[{"url":"127.0.0.1:8080","publicUrl":"127.0.0.1:8080"}]}
```

访问文件
- [http://127.0.0.1:8080/2,055a54a8ec.jpg](http://127.0.0.1:8080/2,055a54a8ec.jpg)
- [http://127.0.0.1:8080/2/055a54a8ec.jpg](http://127.0.0.1:8080/2/055a54a8ec.jpg)
- [http://127.0.0.1:8080/2/055a54a8ec](http://127.0.0.1:8080/2/055a54a8ec)
- [http://127.0.0.1:8080/2/055a54a8ec?height=200&width=200](http://127.0.0.1:8080/2/055a54a8ec?height=200&width=200)


导出文件打包
```
$ weed export -dir=/tmp/data1 -volumeId=1 -o=/tmp/data1.tar -fileNameFormat={{.Name}} -newer='2006-01-02T15:04:05'
```

解包具体文件
```
$ tar -xvf data1.tar
```

## 快速安装
```bash
# Mac系统
$ wget -c https://github.com/chrislusf/seaweedfs/releases/download/1.74/darwin_amd64.tar.gz -O weed_darwin_arm64.tar.gz
$ tar -zxvf weed_darwin_arm64.tar.gz

# Linux系统
$ wget -c https://github.com/chrislusf/seaweedfs/releases/download/1.74/linux_arm64.tar.gz -O weed_linux_arm64.tar.gz
$ tar -zxvf weed_linux_arm64.tar.gz

# 启动
$ ./weed server -dir=weed_data/ -filer -filer.port=8000 -master.port=9333 -volume.port=8001 -volume.max=32 -dataCenter=dc1 -rack=rack1
```

`-dataCenter=dc1 -rack=rack1`数据中心和机架可以省略

每个数据卷的大小为32GB，每个单独的文件大小都受限于卷大小。

最大可以有4GiB个卷，所以理论最大容量为：128EiB（8 x 4GiB x 4GiB）

支持卷级别复制策略
```
curl http://localhost:9333/dir/assign?replication=001

000: 没有复制
001: 在同一个机架上复制一次
010: 在不同的机架上复制一次，但是在相同的数据中心
100: 在不同的数据中心复制一次
200: 在两个不同的数据中心复制两次
110: 复制一次在不同的机架上，另一次在不同的数据中心上
```
Value | Meaning
--- | ---
000	| no replication, just one copy
001	| replicate once on the same rack
010	| replicate once on a different rack in the same data center
100	| replicate once on a different data center
200	| replicate twice on two other different data center
110	| replicate once on a different rack, and once on a different data center


Column | Meaning
--- | ---
x	| number of replica in other data centers
y	| number of replica in other racks in the same data center
z	| number of replica in other servers in the same rack


[集群模式](https://github.com/chrislusf/seaweedfs/wiki/Failover-Master-Server)

```
weed server -master.ip=localhost -master.port=9333 -dir=./1 -volume.port=8080 \ 
  -master.peers=localhost:9333,localhost:9334,localhost:9335
weed server -master.ip=localhost -master.port=9334 -dir=./2 -volume.port=8081 \ 
  -master.peers=localhost:9333,localhost:9334,localhost:9335
weed server -master.ip=localhost -master.port=9335 -dir=./3 -volume.port=8082 \ 
  -master.peers=localhost:9333,localhost:9334,localhost:9335
```

或
```
weed master -ip=localhost -port=9333 -mdir=./1 -peers=localhost:9333,localhost:9334,localhost:9335
weed master -ip=localhost -port=9334 -mdir=./2 -peers=localhost:9333,localhost:9334,localhost:9335
weed master -ip=localhost -port=9335 -mdir=./3 -peers=localhost:9333,localhost:9334,localhost:9335
# now start the volume servers, specifying any one of the master server
weed volume -dir=./1 -port=8080 -mserver=localhost:9333,localhost:9334,localhost:9335
weed volume -dir=./2 -port=8081 -mserver=localhost:9333,localhost:9334,localhost:9335
weed volume -dir=./3 -port=8082 -mserver=localhost:9333,localhost:9334,localhost:9335
```
