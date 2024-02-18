# Node

Node.js® 是一个基于 Chrome V8 引擎 的 JavaScript 运行时环境。

[https://nodejs.org/zh-cn/](https://nodejs.org/zh-cn/)

长期维护版：[node-v16.14.2](https://nodejs.org/dist/v16.14.2/node-v16.14.2.pkg)

## 安装

CentOS
```
curl -sL https://rpm.nodesource.com/setup_16.x | sudo bash -
yum install nodejs -y
```

## 多版本管理

方案一：nvm

```
nvm list
```

方案二：n

选择版本：[https://github.com/nodejs/node/tree/master/doc/changelogs](https://github.com/nodejs/node/tree/master/doc/changelogs)

```
➜  ~ node -v
v20.10.0
➜  ~ npm -v
10.2.3
```

```
sudo npm i -g n
mkdir -p $HOME/.n
echo "export N_PREFIX=\$HOME/.n\n" >> ~/.zshrc
echo "export PATH=\$N_PREFIX/bin:\$PATH\n" >> ~/.zshrc
source ~/.zshrc
n 10.24.1
```

前后对比
```
 old : /usr/local/bin/node
 new : /Users/zhanghe/.n/bin/node
```

```
➜  ~ node -v
v10.24.1
➜  ~ npm -v
6.14.12
```

```
sudo chown -R 501:20 "/Users/zhanghe/.npm"
```

```
npm install
npm start
```
