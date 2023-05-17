# HTTP

[HTTP权威指南](https://www.amazon.cn/dp/B00M2DKYRC)

[Mozilla开发者网站](https://developer.mozilla.org/zh-CN/docs/Web/HTTP)

HTTP请求和响应都由HTTP Header和HTTP Body构成，其中HTTP Header每行都以`\r\n`结束。
如果遇到两个连续的`\r\n`，那么后面就是HTTP Body。
浏览器读取HTTP Body，并根据Header信息中指示的Content-Type、Content-Encoding等解压后显示网页、图像或其他内容。

通常浏览器获取的第一个资源是HTML网页，在网页中，如果嵌入了JavaScript、CSS、图片、视频等其他资源，浏览器会根据资源的URL再次向服务器请求对应的资源。


名称 | 描述 | 缓存 | 可见 | 长度限制 | 安全
--- | --- | --- | --- | --- | ---
GET | 获取资源 | 可以缓存 | 浏览器地址可见 | 有限制（浏览器、服务器的限制; 与HTTP协议无关） | 容易CSRF
POST | 提交数据 | 无法缓存 | 浏览器地址不可见 | 无限制 | 可设置CSRF
