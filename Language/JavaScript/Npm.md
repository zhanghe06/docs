# Npm

安装Node，自动安装Npm (Node.js 的包管理工具)

下载 [node-v14.15.4](https://nodejs.org/dist/v14.15.4/node-v14.15.4.pkg) 并安装
```
This package will install:
	•	Node.js v14.15.4 to /usr/local/bin/node
	•	npm v6.14.10 to /usr/local/bin/npm
Make sure that /usr/local/bin is in your $PATH.
```

Mac环境查找根目录
```
npm root -g
```

WIndows在`C:\Users(your username)\AppData\Roaming`


排错

TypeError: cb.apply is not a function
```
# /usr/local/lib/node_modules/gitbook-cli/node_modules/npm/node_modules/graceful-fs/polyfills.js
# 注释以下3行
 62 //  fs.stat = statFix(fs.stat)
 63 //  fs.fstat = statFix(fs.fstat)
 64 //  fs.lstat = statFix(fs.lstat)
```

npm WARN checkPermissions Missing write access to /usr/local/lib/node_modules
```
sudo chown -R $USER /usr/local/lib/node_modules
```

## 使用

```
npm i module_name -S       # npm install module_name --save        写入到 package.json 文件 dependencies 对象 要发布到生产环境的
npm i module_name -D       # npm install module_name --save-dev    写入到 package.json 文件 devDependencies 对象 只用于开发环境
npm i module_name -g       # npm install module_name --global      全局安装
```

## npx

npx是一种npm包的执行器

一、npm原始方式:

`package.json`文件中配置`scripts`
```
{
	"name": "my-project",
	"version": "1.0.0",
	"scripts": {
		"some-package": "some-package"
	}
}
```

再执行`npm run some-package`

二、npx方式:

`npx some-package`

## 加速

配置代理（不推荐）
```
npm config set proxy=http://127.0.0.1:8087
```

配置镜像（推荐）
```
npm config get registry
npm config set registry https://registry.npmmirror.com
```

如果需要解除镜像并恢复到官方源，请执行以下命令：
```
npm config set registry https://registry.npmjs.org
```

注意：原淘宝 npm 域名即将停止解析，正如在《淘宝 NPM 镜像站喊你切换新域名啦》 中预告的那样：http://npm.taobao.org 和 http://registry.npm.taobao.org 将在 2022.06.30 号正式下线和停止 DNS 解析。
域名切换规则：
- http://npm.taobao.org => http://npmmirror.com
- http://registry.npm.taobao.org => http://registry.npmmirror.com
