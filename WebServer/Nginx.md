# Nginx

## 配置

查看cpu核数
```
root@node:~# cat /proc/cpuinfo | grep processor | wc -l
2
```

查看系统参数
```
root@node:~# ulimit -n
65535
root@node:~# ulimit -u
15075

root@node:~# ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 15075
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 65535
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 15075
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```

nginx.conf
```
worker_processes  2; # cpu核数，建议不大于8
events {
    worker_connections  10240;
}
```

正常情况最大并发数: 
```
max_clients = worker_processes * worker_connections
```

作为反向代理，因为浏览器默认会开启2个连接到server，而且Nginx还会使用fds（file descriptor）从同一个连接池建立连接到upstream后端
```
nginx作为http服务器的时候：
    max_clients = worker_processes * worker_connections/2
nginx作为反向代理服务器的时候：
    max_clients = worker_processes * worker_connections/4
```


## 限流模块
http://nginx.org/en/docs/http/ngx_http_limit_req_module.html

```nginx
http {
    limit_req_zone $binary_remote_addr zone=one:10m rate=1r/s;
    server {
        #限制每ip每秒不超过20个请求，漏桶数burst为5
        #brust的意思就是，如果第1秒、2,3,4秒请求为19个，
        #第5秒的请求为25个是被允许的。
        #但是如果你第1秒就25个请求，第2秒超过20的请求返回503错误。
        #nodelay，如果不设置该选项，严格使用平均速率限制请求数，
        #第1秒25个请求时，5个请求放到第2秒执行，
        #设置nodelay，25个请求将在第1秒执行。
        limit_req   zone=one  burst=1 nodelay;
    }
}
```

$binary_remote_addr 表示：客户端IP地址
zone 表示漏桶的名字
rate 表示nginx处理请求的速度有多快
burst 表示峰值
nodelay 表示是否延迟处理请求，还是直接503返回给客户端，如果超出rate设置的情况下。

测试：

```
docker pull nginx:1.24-alpine

docker run \
    -h nginx_test \
    --name nginx_test \
    --restart always \
    -p 80:80 \
    -d \
    nginx:1.24-alpine
```

```
docker exec -it nginx_test sh

apk add vim

vim /etc/nginx/nginx.conf

vim /etc/nginx/conf.d/default.conf

nginx -s reload
```

查看模块
```
/ # nginx -V
nginx version: nginx/1.24.0
built by gcc 12.2.1 20220924 (Alpine 12.2.1_git20220924-r4)
built with OpenSSL 3.0.7 1 Nov 2022 (running with OpenSSL 3.0.12 24 Oct 2023)
TLS SNI support enabled
configure arguments: --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --with-perl_modules_path=/usr/lib/perl5/vendor_perl --user=nginx --group=nginx --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-cc-opt='-Os -fomit-frame-pointer -g' --with-ld-opt=-Wl,--as-needed,-O1,--sort-common
```

mac 自带 apache
```
apachectl -v
ab -V

ab -n 100 -c 10 http://localhost/
```

## 视频分片

https://nginx.org/en/docs/http/ngx_http_hls_module.html

```
docker run \
    -h nginx_test \
    --name nginx_test \
    --restart always \
    -v ${PWD}/videos:/var/videos \
    -p 80:80 \
    -d \
    nginx:1.24-alpine
```

```
docker exec -it nginx_test sh

apk add vim

vim /etc/nginx/nginx.conf

vim /etc/nginx/conf.d/default.conf

nginx -s reload
```


## 反向代理域名
https://www.nginx.com/resources/wiki/modules/domain_resolve/

```nginx
http {
    resolver 8.8.8.8;
    resolver_timeout 10s;

    upstream backend {
        jdomain  www.baidu.com;
        # keepalive 10;
    }
    server {
        listen 8080;

        location / {
            proxy_pass http://backend;
        }
    }
}
```

注意windows环境下，proxy_pass指向localhost访问时非常慢，需要替换为127.0.0.1

```
# Localhost (DO NOT REMOVE)
127.0.0.1       localhost
```

## 多租户

网关服务在处理租户头信息时，路由部分的逻辑为判断Header中`X-Scope-OrgID`带租户信息的请求，并将其转发到对应的服务。

```
#upstream内地址由sidecar从CRD中获取Loki实例后渲染生成

upstream tenantA {
    server x.x.x.x:3100;
}
upstream tenantB {
    server y.y.y.y:3100;
}
server {
    location / {
        set tenant $http_x_scope_orgid;
        proxy_pass http://$tenant;
        include proxy_params;
    }
}
```

## 日志切割

参考日志部分


## IPV6

```
# nginx -V
nginx version: nginx/1.13.0
built by gcc 6.3.0 20170205 (Debian 6.3.0-6)
built with OpenSSL 1.1.0e  16 Feb 2017
TLS SNI support enabled
configure arguments: --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-cc-opt='-g -O2 -fdebug-prefix-map=/data/builder/debuild/nginx-1.13.0/debian/debuild-base/nginx-1.13.0=. -specs=/usr/share/dpkg/no-pie-compile.specs -fstack-protector-strong -Wformat -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fPIC' --with-ld-opt='-specs=/usr/share/dpkg/no-pie-link.specs -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -pie'

# whereis nginx
nginx: /usr/sbin/nginx /usr/lib/nginx /etc/nginx /usr/share/nginx

# cd /usr/sbin
# ./configure --prefix=/etc/nginx ... --with-ipv6

# make && make install
```

nginx配置
```
server {
    listen      80 default_server;
    listen      [::]:80 default_server;
    server_name _;
    root        /usr/share/nginx/html/html;
    index       index.html;
```

## 顺序

nginx location 顺序：

```
精准匹配 =
前缀匹配 ^~
正则匹配 ~、~*
不带修饰符的前缀匹配
```

## 排错

### ERR_INCOMPLETE_CHUNKED_ENCODING

事故现象：

Chrome
```
(failed)net::ERR_INCOMPLETE_CHUNKED_ENCODING
```

Nginx
```
upstream timed out (110: Connection timed out) while reading response header from upstream

upstream prematurely closed connection while reading upstream
```

Gunicorn
```
OSError: [Errno 11] Resource temporarily unavailable
```

事故原因：架构上Nginx + Gunicorn，Nginx没有做动静分离，所有请求转发到Gunicorn，而Gunicorn并不擅长处理静态文件，特别是大文件。

处理方案：Nginx配置将static目录直接指向文件目录，不往后端转发即可。

### ERR_CONTENT_LENGTH_MISMATCH

事故现象：

部分js报错，但不是所有的js或css报错，报错的文件较没报错的文件偏大。
并且报错的文件也可以单独在浏览器中打开，所以排除了最简单的地址错误。
前端项目是由nginx代理的，所以查看nginx error.log 但是未看到错误记录。

事故原因：

nginx开启了gzip，但是没有配置`gzip_buffers`

## 分片


