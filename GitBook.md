# GitBook

## 操作指南

### 安装环境
```bash
npm install -g gitbook-cli
cd docs
gitbook install
gitbook init
```

### 开启服务
```bash
gitbook serve
```

访问 [http://localhost:4000](http://localhost:4000)

### 生成文件

下载依赖(Mac环境)

https://calibre-ebook.com/download_osx

```bash
ln -s /Applications/calibre.app/Contents/MacOS/ebook-convert /usr/local/bin
```

生成pdf
```bash
gitbook pdf . school_project.pdf
```

## 集成GitHub

### 简单方式

缺点: 主分支会带上_book目录

1. 将_book从.gitignore中移除

2. 提交_book
```
gitbook build
git add _book && git commit -m '文档更新'
```

3. 推送_book
```
git subtree push --prefix=_book origin gh-pages  # 注意，分支名必须为gh-pages
```

4. 访问页面

https://<你的用户名称>.github.io/<你的项目名称>/

[https://zhanghe06.github.io/dev-doc/](https://zhanghe06.github.io/dev-doc/)

### 完整方式

初次部署
```
# 一、更新文档分支
git checkout master
# 更新代码
git add .
git commit -m '创建项目'
git push origin master

# 二、更新页面分支
git checkout -b github
gitbook build
# 将_book从.gitignore中移除
# 更新路径配置[可选]
git add . && git commit -m '页面更新'
git subtree push --prefix=_book origin gh-pages  # 注意，分支名必须为gh-pages

# 三、访问页面 https://<你的用户名称>.github.io/<你的项目名称>/
```

后续更新
```
# 一、更新文档分支
git checkout master
# 更新代码
git add .
git commit -m '文档更新'
git push origin master

# 二、更新页面分支
git checkout github
git rebase master
gitbook build
git add . && git commit -m '页面更新'
git subtree push --prefix=_book origin gh-pages
git checkout master
```
