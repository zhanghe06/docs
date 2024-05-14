# Stress

压力测试工具

- [https://hub.docker.com/r/polinux/stress](https://hub.docker.com/r/polinux/stress)

```
# 拉取压力测试镜像
docker pull --platform linux/amd64 polinux/stress:1.0.4

# 随机（最大间隔1小时）触发压力测试，每次持续36秒
docker run \
  -h stress \
  --name stress \
  -d \
  --restart=always \
  polinux/stress:1.0.4 \
    sh -c "sleep $[($RANDOM%3600)+1] && stress \
    -c 2 \
    -i 2 -d 4 --hdd-bytes 512M \
    -m 2 --vm-bytes 128M \
    -t 36s \
    -v"
```

## 使用手册

CPU压力测试
```
# 生成4个工作进程，进行开方运算
stress -c 4
```

```
 进程号 USER      PR  NI    VIRT    RES    SHR    %CPU  %MEM     TIME+ COMMAND
2464788 root      20   0     780    256    256 R  99.7   0.0   0:52.92 stress
2464789 root      20   0     780    256    256 R  99.0   0.0   0:52.96 stress
2464790 root      20   0     780    256    256 R  99.0   0.0   0:53.01 stress
2464791 root      20   0     780    256    256 R  99.0   0.0   0:52.99 stress
```

内存压力测试
```
# 生成3个进程，每个进程占用300M内存（默认256M）
stress -m 3 --vm-bytes 300M
```
虽然只是对内存进行压力测试，但实际上CPU也是很繁忙的，占有率也接近100%

磁盘压力测试
```
# 两个指标
# stress -i N 会产生N个进程，每个进程反复调用sync()将内存上的内容写到硬盘上
# stress -d N 会产生N个进程，每个进程往当前目录中写入固定大小的临时文件，然后执行unlink操作删除该临时文件
# 生成2个进程，每个进程反复调用sync()将内存上的内容写到硬盘上
# 生成4个进程，每个进程往当前目录中写入固定大小的临时文件，然后执行unlink操作删除该临时文件，临时文件的大小512M（默认为1G）
stress -i 2 -d 4 --hdd-bytes 512M
```

设置超时时间
```
# 压力测试可以组合使用
# 10秒后自动退出
stress -c 4 -m 2 -d 1 -t 10s
```
