# Webpack

中文文档: [https://webpack.docschina.org/concepts/](https://webpack.docschina.org/concepts/)

核心概念：

- 入口(entry)
- 输出(output)
- loader
- 插件(plugin)
- 模式(mode)
- 浏览器兼容性(browser compatibility)
- 环境(environment)

webpack.config.js 示例
```
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};
```
