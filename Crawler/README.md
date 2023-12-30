# 爬虫 (Crawler)

## 辅助工具

### Chrome 浏览器调试：[https://zh.javascript.info/debugging-chrome](https://zh.javascript.info/debugging-chrome)

### CURL转代码工具：curlconverter

将curl命令转换为Python、JavaScript等: [https://curlconverter.com](https://curlconverter.com)

### JS解析工具：execjs

```
# python3安装
pip install PyExecJS
# python2安装
pip install pyexecjs
```

```
import execjs

jsFunc = '''
    function add(x,y){
    return x+y;
    }
'''
jscontext = execjs.compile(jsFunc)
a = jscontext.call('add',3,5)
print(a)
```

## JS逆向

AST（Abstract Syntax Tree），中文抽象语法树，简称语法树（Syntax Tree）

AST 在线解析: [https://astexplorer.net](https://astexplorer.net)
