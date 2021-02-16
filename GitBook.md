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

[https://zhanghe06.github.io/docs/](https://zhanghe06.github.io/docs/)

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
git merge master
gitbook build
git add . && git commit -m '页面更新'
git subtree push --prefix=_book origin gh-pages
git checkout master
```

## 插件

gitbook插件名称 | npm插件名称 | 说明
--- | --- | ---
back-to-top-button | - | -
sharing-plus | gitbook-plugin-sharing-plus | 增强分享插件
todo | [gitbook-plugin-todo](https://github.com/ly-tools/gitbook-plugin-todo) | 添加 Todo 功能
mermaid-full@>=0.5.1 | - | -
mathjax-full@>=0.6.2 | [gitbook-plugin-mathjax](https://github.com/GitbookIO/plugin-mathjax) | 数学公式
donate | [gitbook-plugin-donate](https://github.com/willin/gitbook-plugin-donate) | 打赏插件
insert-logo | - | -
flexible-alerts | [gitbook-plugin-flexible-alerts](https://github.com/zanfab/gitbook-plugin-flexible-alerts) | 增强提示框
terminal | gitbook-plugin-terminal | 模拟终端
graph | [gitbook-plugin-graph](https://github.com/cjam/gitbook-plugin-graph) | 使用 [function-plot](https://mauriciopoppe.github.io/function-plot/) 绘制数学函数图
chart | [gitbook-plugin-chart](https://github.com/csbun/gitbook-plugin-chart) | 使用 [C3.js](https://github.com/c3js/c3) 或者 [HighCharts](https://github.com/highcharts/highcharts) 绘制图形
mcqx | [gitbook-plugin-mcqx](https://github.com/ymcatar/gitbook-plugin-mcqx) | 选择题插件
fbqx | [gitbook-plugin-fbqx](https://github.com/Erwin-Chan/gitbook-plugin-fbqx) | 填空题插件
spoiler | [gitbook-plugin-spoiler](https://github.com/manchiyiu/gitbook-plugin-spoiler) | 隐藏答案


`chart`插件使用`HighCharts`生成的图表右下角会默认显示页脚`Highcharts.com`

> [!COMMENT|label:去除图表页脚]
> - 找到文件`node_modules/gitbook-plugin-chart/assets/highcharts/highcharts.js`<br>
> - 搜索到`credits`将其属性`enabled:!0`修改为`enabled:0`

不太厚道, 请勿模仿
