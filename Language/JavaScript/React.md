# React

[https://react.docschina.org](https://react.docschina.org)

[https://zh-hans.reactjs.org/docs/](https://zh-hans.reactjs.org/docs/)

- 声明式
- 组件化

## JavaScript 概览

[JavaScript（JS 教程）](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/A_re-introduction_to_JavaScript)

## node版本

升级Node LTS版本 [https://nodejs.org/en/](https://nodejs.org/en/)

否则通过create-react-app创建项目会报错
```
error @typescript-eslint/eslint-plugin@2.24.0: The engine "node" is incompatible with this module. Expected version "^8.10.0 || ^10.13.0 || >=11.10.1".
```

## yarn版本

如果遇到因yarn版本报错
```
error fork-ts-checker-webpack-plugin@3.1.1: The engine "yarn" is incompatible with this module. Expected version ">=1.0.0".
```
安装或升级yarn
```
npm install -g npm
npm install -g yarn
```

## 创建项目

```
npm install -g create-react-app
create-react-app react_project
cd react_project
npm start
```

访问：[http://localhost:3000](http://localhost:3000)

## Redux

三大原则:
- 单一数据源
- State 是只读的
- 使用纯函数来执行修改

```
npm install --save redux
npm install --save react-redux                  //react绑定库
npm install --save-dev redux-devtools-extension //调试相关
```

## Axios

[Axios最完整封装适用于Vue、React](https://www.jianshu.com/p/e59aa71e1840)
[vue，react，axios接口再封装](https://www.jianshu.com/p/8d23f5990494)

```
npm i axios -S
```

## UI框架

- PC端
  - Vue：Element-UI
  - React：antd
- 移动端
  - Vue：Vant
  - React：Ant Design Mobile


## this

```
var x = 1;
var obj = {
  x: 2,
  getValue: function() {
    return this.x
  }
}

// 函数的this指向是在进入执行上下文的时候才确定的，它并不是静态绑定的。
// this是在哪调用就指向哪的
var fn = obj.getValue
fn() // 1
obj.getValue() // 2

// 使用bind,可以返回一个新的函数，当这个函数调用的时候this指向的是传入值
var fn = obj.getValue.bind(obj)
fn() // 2
```
