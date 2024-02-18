# Shell

echo
```
# 不换行输出
echo -n
# 转义输出
echo -e
```

整站抓取
```
wget -c -m -k https://ip.cn
```

-H 允许外链递归，针对某些静态cdn资源是外链的情况
-D 指定 域名列表
-U 指定 AGENT

去除?及后缀的2种方法
```
echo 'www.baidu.com?a=b' | sed 's/\?[^?]*$//'
echo 'www.baidu.com?a=b' | awk -F "\?" '{print $1}'
```

去除当前目录下所有文件名的?及后缀
```
find . -name "*\?*" | xargs -I ls | awk -F "\?" '{print "mv "$0" "$1}' | sh
```

将换行符`CRLF`转为`CR`
```
zip -r -ll zipfile.zip some_dir/
unzip zipfile.zip
```

遇到nofollow的站点时
```
<meta name='robots' content='noindex,nofollow' />
```
设置忽略robots协议
```
-e robots=off
```

设置User-Agent
```
--header="User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
```

## tar

压缩，并排除目录
```
tar -zcvf demo_project.tar.gz --exclude=.venv --exclude=.git --exclude=__pycache__ demo_project
```

解压到当前目录
```
tar -zxvf demo_project.tar.gz
```

## zip

压缩
```
zip -r demo_project.zip demo_project
```

解压
```
unzip demo_project.zip
```
