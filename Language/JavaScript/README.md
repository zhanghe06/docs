# JavaScript

- ECMAScript
- BOM（Browser Object Model）是指浏览器对象模型，它使 JavaScript 有能力与浏览器进行“对话”。
- DOM（Document Object Model）是指文档对象模型，通过它，可以访问HTML文档的所有元素。

## BOM

1、window对象
一些常用的Window方法：

window.innerHeight - 浏览器窗口的内部高度
window.innerWidth - 浏览器窗口的内部宽度
window.open() - 打开新窗口
window.close() - 关闭当前窗口


html tab页面切换事件
```
$(document).bind("visibilitychange",function(e){
　　// 只对tab页面切换有效
　　// document.visibilityState === 'visible' OR 'hidden'
})

$(window).bind("focus",function(e){
    // tab页面，浏览器和程序切换都有效果
});
```

2、window的子对象

navigator对象
```
navigator.appName　　// Web浏览器全称
navigator.appVersion　　// Web浏览器厂商和版本的详细字符串
navigator.userAgent　　// 客户端绝大部分信息
navigator.platform　　　// 浏览器运行所在的操作系统
```

screen对象
```
screen.availWidth - 可用的屏幕宽度
screen.availHeight - 可用的屏幕高度　
```

history对象
```
history.forward()  // 前进一页
history.back()  // 后退一页
```

location对象
```
location.href  获取URL
location.href="URL" // 跳转到指定页面
location.reload() 重新加载页面
```

window.location

属性 | 描述
---         | ---
hash        | 设置或获取 href 属性中在井号“#”后面的分段。
host        | 设置或获取 location 或 URL 的 hostname 和 port 号码。
hostname    | 设置或获取 location 或 URL 的主机名称部分。
href        | 设置或获取整个 URL 为字符串。
pathname    | 设置或获取对象指定的文件名或路径。
port        | 设置或获取与 URL 关联的端口号码。
protocol    | 设置或获取 URL 的协议部分。
search      | 设置或获取 href 属性中跟在问号后面的部分。

弹出框
```
alert("你看到了吗？");  // 警告框
confirm("你确定吗？")  // 确认框
prompt("请在下方输入","你的答案")  // 提示框
```

延时
```
// 在指定时间之后执行一次相应函数
var timer = setTimeout(function(){alert(123);}, 3000)
// 取消setTimeout设置
clearTimeout(timer);
```

周期
```
// 每隔一段时间就执行一次相应函数
var timer = setInterval(function(){console.log(123);}, 3000)
// 取消setInterval设置
clearInterval(timer);　
```

## DOM

一些常用的 HTML DOM 方法：

getElementById(id) - 获取带有指定 id 的节点（元素）
appendChild(node) - 插入新的子节点（元素）
removeChild(node) - 删除子节点（元素）
一些常用的 HTML DOM 属性：

innerHTML - 节点（元素）的文本值
parentNode - 节点（元素）的父节点
childNodes - 节点（元素）的子节点
attributes - 节点（元素）的属性节点

事件
```
onclick        当用户点击某个对象时调用的事件句柄。
ondblclick     当用户双击某个对象时调用的事件句柄。
 
onfocus        元素获得焦点。               // 练习：输入框
onblur         元素失去焦点。               应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证.
onchange       域的内容被改变。             应用场景：通常用于表单元素,当元素内容被改变时触发.（select联动）
 
onkeydown      某个键盘按键被按下。          应用场景: 当用户在最后一个输入框按下回车按键时,表单提交.
onkeypress     某个键盘按键被按下并松开。
onkeyup        某个键盘按键被松开。
onload         一张页面或一幅图像完成加载。
onmousedown    鼠标按钮被按下。
onmousemove    鼠标被移动。
onmouseout     鼠标从某元素移开。
onmouseover    鼠标移到某元素之上。
 
onselect      在文本框中的文本被选中时发生。
onsubmit      确认按钮被点击，使用的对象是form。
```

## JavaScript Array 对象

Array 对象方法

方法 | 描述
--- | ---
concat()	|   连接两个或更多的数组，并返回结果。
join()	    |   把数组的所有元素放入一个字符串。元素通过指定的分隔符进行分隔。
pop()	    |   删除并返回数组的最后一个元素
push()	    |   向数组的末尾添加一个或更多元素，并返回新的长度。
reverse()	|   颠倒数组中元素的顺序。
shift()	    |   删除并返回数组的第一个元素
slice()	    |   从某个已有的数组返回选定的元素
sort()	    |   对数组的元素进行排序
splice()	|   删除元素，并向数组添加新元素。
toSource()	|   返回该对象的源代码。
toString()	|   把数组转换为字符串，并返回结果。
toLocaleString()	|   把数组转换为本地数组，并返回结果。
unshift()	|   向数组的开头添加一个或更多元素，并返回新的长度。
valueOf()	|   返回数组对象的原始值

包含
```
['1', '2'].includes('1')
```

删除

方式一： 在Array原型对象上添加删除方法
```
// 查找指定的元素在数组中的位置
Array.prototype.indexOf = function(val) {
    for (var i = 0; i < this.length; i++) {
        if (this[i] == val) {
            return i;
        }
    }
    return -1;
 };
// 通过索引删除数组元素
Array.prototype.remove = function(val) {
    var index = this.indexOf(val);
    if (index > -1) {
        this.splice(index, 1);
    }
};
// demo使用
var arr = [1, 2, 3, 5, 6, 'abc', 'ert'];
arr.remove('abc');
/************** 打印输出 arr ***************/
    [1, 2, 3, 5, 6, "ert"]
/************** 打印输出  ***************/
```

方式二： ES6的简介写法
```
var arr = [
    {
        id: 1,
        name: 'Janche'
    },
    {
        id: 2,
        name: '老王'
    }
]
arr.splice(arr.findIndex(e => e.id === 1), 1) // 将删除id等于1的选项
/************** 打印输出 arr ***************/
{
    id: 2,
    name: '老王'
}
/************** 打印输出  ***************/
```

### array转map
```
arrayToMap (array, k, v) {
  const map = new Map()
  for (let item of array) {
    map.set(item[k], item[v])
  }
  return map
}
```

### Array 中的高阶函数 map, filter, reduce

```
var array1 = [1,4,9,16];
const map1 = array1.map(x => x *2);
console.log(array1);  // [1,4,9,16]
console.log(map1);  // [2,8,18,32]

const objArray = array1.map(x => Object.assign(
    {
        id: x.id,
        label: x.name
    }
))
```

```
var arr = [20,30,50,96,50]
var newArr = arr.filter(item => item>40) 
console.log(arr)  // [20,30,50, 96,50]
console.log(newArr)  // [50, 96, 50]
```

```
// 高频用途：去掉数组中的 空字符串、0、undefined、null；
var arr = ['1', '2', null, '3.jpg', null, 0]
var newArr = arr.filter(item => item)
// 也可以写成
// var newArr = arr.filter(Boolean);
console.log(newArr) // ["1", "2", "3.jpg"]
```

```
// 统计字符串中每个字符出现的次数
const str = '9kFZTQLbUWOjurz9IKRdeg28rYxULHWDUrIHxCY6tnHleoJ'
const obj = {}
Array.from(str).reduce((accumulator, current) => {
  current in accumulator ? accumulator[current]++ : accumulator[current] = 1
  return accumulator;
}, obj)
```

```
// 列表分组
const data = [
    { source: 'test1', target: 'test7', value: 20 },
    { source: 'test5', target: 'test3', value: 50 },
    { source: 'test1', target: 'test4', value: 90 },
    { source: 'test6', target: 'test3', value: 10 }
]
const obj = {}
data.reduce((grouping, current) => {
  current['source'] in grouping ? grouping[current['source']].push(current) : grouping[current['source']] = [current]
  return grouping;
}, obj)
```

```
// 组合子集
const data = [
    { id: 1, tags: ['A', 'B'] },
    { id: 2, tags: ['C', 'D'] },
    { id: 3, tags: ['E', 'F'] },
    { id: 4, tags: ['G', 'H'] }
]
const obj = []
data.reduce((items, current) => {
  //for (var i = 0; i < current['tags'].length; i++) {
  //  items.push(current['tags'][i]);
  //}
  items.push.apply(items, current['tags'])
  return items;
}, obj)
```

## JavaScript String 对象

方法 | 描述
--- | ---
anchor() | 创建 HTML 锚。
big() | 用大号字体显示字符串。
blink() | 显示闪动字符串。
bold() | 使用粗体显示字符串。
charAt() | 返回在指定位置的字符。
charCodeAt() | 返回在指定的位置的字符的 Unicode 编码。
concat() | 连接字符串。
fixed() | 以打字机文本显示字符串。
fontcolor() | 使用指定的颜色来显示字符串。
fontsize() | 使用指定的尺寸来显示字符串。
fromCharCode() | 从字符编码创建一个字符串。
indexOf() | 检索字符串。
italics() | 使用斜体显示字符串。
lastIndexOf() | 从后向前搜索字符串。
link() | 将字符串显示为链接。
localeCompare() | 用本地特定的顺序来比较两个字符串。
match() | 找到一个或多个正则表达式的匹配。
replace() | 替换与正则表达式匹配的子串。
search() | 检索与正则表达式相匹配的值。
slice() | 提取字符串的片断，并在新的字符串中返回被提取的部分。
small() | 使用小字号来显示字符串。
split() | 把字符串分割为字符串数组。
strike() | 使用删除线来显示字符串。
sub() | 把字符串显示为下标。
substr() | 从起始索引号提取字符串中指定数目的字符。
substring() | 提取字符串中两个指定的索引号之间的字符。
sup() | 把字符串显示为上标。
toLocaleLowerCase() | 把字符串转换为小写。
toLocaleUpperCase() | 把字符串转换为大写。
toLowerCase() | 把字符串转换为小写。
toUpperCase() | 把字符串转换为大写。
toSource() | 代表对象的源代码。
toString() | 返回字符串。
valueOf() | 返回某个字符串对象的原始值。


## 对象操作

动态创建对象：
Object.assign({a: 1, b: 2})
注意 Object.assign 与 Object.create 区别

给对象添加属性：
obj.属性=属性值;
obj={属性:属性值};
但是对于变量：
obj\[key\]=value;

检查属性是否存在：
const obj = {'a': 1}
'a' in obj // true
'toString' in obj // true
obj.hasOwnProperty('a') // true
obj.hasOwnProperty('b') // false
obj.hasOwnProperty('toString') // false


## JSON

​JSON.parse 将json字符串反序列化为json对象
```
// 定义一个字符串
var data='{"name":"tom"}'
// 解析对象​
​JSON.parse(data)
// 结果
{name: "tom"}

typeof(JSON.parse(data))
"object"
JSON.parse(data)["name"]
"tom"
JSON.parse(data).name
"tom"
```

JSON.stringify 将json对象序列化为json字符串
```
var data={name: 'tom'}
JSON.stringify(data)
'{"name":"tom"}'
```

## Ajax

[https://xhr.spec.whatwg.org/](https://xhr.spec.whatwg.org/)

原生js实现Ajax方法
```javascript
var Ajax = {
    get: function(url,callback){
        // XMLHttpRequest对象用于在后台与服务器交换数据
        var xhr=new XMLHttpRequest();
        xhr.open('GET',url,false);
        xhr.onreadystatechange=function(){
            // readyState == 4说明请求已完成
            if(xhr.readyState==4){
                if(xhr.status==200 || xhr.status==304){
                    console.log(xhr.responseText);
                    callback(xhr.responseText);
                }
            }
        }
        xhr.send();
    },

    // data应为'a=a1&b=b1'这种字符串格式，在jq里如果data为对象会自动将对象转成这种字符串格式
    post: function(url,data,callback){
        var xhr=new XMLHttpRequest();
        xhr.open('POST',url,false);
        // 添加http头，发送信息至服务器时内容编码类型
        xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
        xhr.onreadystatechange=function(){
            if (xhr.readyState==4){
                if (xhr.status==200 || xhr.status==304){
                    // console.log(xhr.responseText);
                    callback(xhr.responseText);
                }
            }
        }
        xhr.send(data);
    }
}
```

拓展ES6的 Promise 的AJAX GET方法请求数据
```typescript
const getJSON = function(url) {
    const promise = new Promise(function(resolve, reject){
        const handler = function() {
            if (this.readyState !== 4) {
                return;
            }
            if (this.status === 200) {
                resolve(this.response);
            } else {
                reject(new Error(this.statusText));
            }
        };
        const client = new XMLHttpRequest();
        client.open("GET", url);
        client.onreadystatechange = handler;
        client.responseType = "json";
        client.setRequestHeader("Accept", "application/json");
        client.send();

    });
    return promise;
};
getJSON("get_promise.json").then(function(json) {
    console.log('Data: ', json);
}, function(error) {
    console.error('err', error);
});

const postJSON = function(url,data) {
    const promise = new Promise(function(resolve, reject){
        const handler = function() {
            if (this.readyState !== 4) {
                return;
            }
            if (this.status === 200) {
                resolve(this.response);
            } else {
                reject(new Error(this.statusText));
            }
        };
        const client = new XMLHttpRequest();
        client.open("POST", url);
        client.onreadystatechange = handler;
        client.responseType = "json";
        client.setRequestHeader("Content-Type", "application/json");
        client.setRequestHeader("Accept", "application/json");
        client.send(data);

    });
    return promise;
};
postJSON("post_promise.json", {"a": 1, "b": 2}).then(function(json) {
    console.log('Data: ', json);
}, function(error) {
    console.error('err', error);
});
```

同步、异步
```
// 同步
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

// 异步 需要回调函数处理响应
function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}
```

## Promise

什么是异步？

　　同步：一定要等任务执行完了，得到结果，才执行下一个任务。

　　异步：不等任务执行完，直接执行下一个任务。

为什么要用promise？

　　Promise的出现主要是解决地狱回调的问题，比如你需要结果需要请求很多个接口，这些接口的参数需要另外那个的接口返回的数据作为依赖，这样就需要我们一层嵌套一层，但是有了Promise 我们就无需嵌套

　　Promise的本质就是分离了异步数据获取和业务逻辑

async / await

async 函数返回的是一个 Promise 对象

Promise 的特点——无等待，所以在没有 await 的情况下执行 async 函数，它会立即执行，返回一个 Promise 对象，
并且，绝不会阻塞后面的语句。
这和普通返回 Promise 对象的函数并无二致。

await 可以用于等待一个 async 函数的返回值，await 后面实际是可以接普通函数调用或者直接量的。

## 事件冒泡

假设有3层div: bottom、middle、top
```
<script type="text/javascript">
    window.onload = function() {
        document.getElementById("body").addEventListener("click",eventPerformed);
    }
    function eventPerformed(event) {
        var target = event.target;
        switch (target.id) {
        case "bottom_div": 
            alert("bottom_div");
            break;
        case "middle_div":
            alert("middle_div");
            break;
        case "top_div":
             alert("top_div");
            break;
        }
    }
</script>
```

## 编码解码

方法说明 | JS方法 | Python方法 | 备注
--- | --- | --- | ---
取余 | % | % | -
URI编码 | encodeURI | 不编码`, / ? : @ & = + $ #`
URI解码 | decodeURI | 不解码`, / ? : @ & = + $ #`
URI组件编码 | encodeURIComponent | 把字符串作为 URI 组件进行编码 | 编码`, / ? : @ & = + $ #`
URI组件解码 | decodeURIComponent | 解码`, / ? : @ & = + $ #`
字符串编码 | escape | 对字符串进行编码 | 不编码`* @ - _ + . / `
字符串解码 | unescape | 对字符串进行解码 | 不解码`* @ - _ + . / `

示例
```
encodeURI('http://www.baidu.com?cn=中文&en=english')
"http://www.baidu.com?cn=%E4%B8%AD%E6%96%87&en=english"

decodeURI('http://www.baidu.com?cn=%E4%B8%AD%E6%96%87&en=english')
"http://www.baidu.com?cn=中文&en=english"

encodeURIComponent('http://www.baidu.com?cn=中文&en=english')
"http%3A%2F%2Fwww.baidu.com%3Fcn%3D%E4%B8%AD%E6%96%87%26en%3Denglish"

decodeURIComponent('http%3A%2F%2Fwww.baidu.com%3Fcn%3D%E4%B8%AD%E6%96%87%26en%3Denglish')
"http://www.baidu.com?cn=中文&en=english"

escape('@全世界_江河湖海！')
"@%u5168%u4E16%u754C_%u6C5F%u6CB3%u6E56%u6D77%uFF01"

unescape('@%u5168%u4E16%u754C_%u6C5F%u6CB3%u6E56%u6D77%uFF01')
"@全世界_江河湖海！"
```

Python2
```
# ASCII
>>> ord('a')
97

>>> chr(97)
'a'

# BASE 64
>>> import base64
>>> base64.b64encode('sd')
'c2Q='
>>> base64.b64decode('c2Q=')
'sd'

# URI (本质上是将字节转十六进制)
>>> urllib.quote_plus('http://www.baidu.com?cn=中文&en=english')
'http%3A%2F%2Fwww.baidu.com%3Fcn%3D%E4%B8%AD%E6%96%87%26en%3Denglish'

>>> urllib.unquote_plus('http%3A%2F%2Fwww.baidu.com%3Fcn%3D%E4%B8%AD%E6%96%87%26en%3Denglish')
'http://www.baidu.com?cn=\xe4\xb8\xad\xe6\x96\x87&en=english'
```

JS
```
// ASCII
> 'a'.charCodeAt(0)
< 97

> String.fromCharCode(97)
< "a"

// BASE 64
> window.btoa('sd')
< "c2Q="

> window.atob('c2Q=')
< "sd"

// URI (本质上是将字节转十六进制)
> encodeURIComponent('http://www.baidu.com?cn=中文&en=english')
< "http%3A%2F%2Fwww.baidu.com%3Fcn%3D%E4%B8%AD%E6%96%87%26en%3Denglish"

> decodeURIComponent('http%3A%2F%2Fwww.baidu.com%3Fcn%3D%E4%B8%AD%E6%96%87%26en%3Denglish')
< "http://www.baidu.com?cn=中文&en=english"
```

方法| Python表达式 | Python结果 | JS表达式 | JS结果
--- | --- | --- | --- | ---
ASCII 字符转整数 | `ord('a')` | `97` | `'a'.charCodeAt(0)` | `97`
ASCII 整数转字符 | `chr(97)` | `'a'` | `String.fromCharCode(97)` | `"a"`
BASE 64 字符转编码 | `base64.b64encode('a')` | `'YQ=='` | `window.btoa('a')` | `"YQ=="`
BASE 64 编码转字符 | `base64.b64decode('YQ==')` | `'a'` | `window.atob('YQ==')` | `"a"`
URI 字符转编码 | `urllib.quote_plus('http://www.baidu.com?cn=中文&en=english')` | `'http%3A%2F%2Fwww.baidu.com%3Fcn%3D%E4%B8%AD%E6%96%87%26en%3Denglish'` | `encodeURIComponent('http://www.baidu.com?cn=中文&en=english')` | `"http%3A%2F%2Fwww.baidu.com%3Fcn%3D%E4%B8%AD%E6%96%87%26en%3Denglish"`
URI 编码转字符 | `urllib.unquote_plus('http%3A%2F%2Fwww.baidu.com%3Fcn%3D%E4%B8%AD%E6%96%87%26en%3Denglish')` | `'http://www.baidu.com?cn=\xe4\xb8\xad\xe6\x96\x87&en=english'` | `decodeURIComponent('http%3A%2F%2Fwww.baidu.com%3Fcn%3D%E4%B8%AD%E6%96%87%26en%3Denglish')` | `"http://www.baidu.com?cn=中文&en=english"`
十进制整数 转 二进制 | `bin(18)` | `'0b10010'` | `const num = 18; num.toString(2);` | `"10010"`
十进制整数 转 八进制 | `oct(18)` | `'0o22'` | `const num = 18; num.toString(8);` | `"22"`
十进制整数 转 十六进制 | `hex(18)` | `'0x12'` | `const num = 18; num.toString(16);` | `"12"`
二进制整数 转 十进制 | `int('0b10010', 2)` | `18` | `parseInt('10010', 2)` | `18`
八进制整数 转 十进制 | `int('0o22', 8)` | `18` | `parseInt('22', 8)` | `18`
十六进制整数 转 十进制 | `int('0x12', 16)` | `18` | `parseInt('12', 16)` | `18`
Json序列化 | `json.dumps({'a': 1, 'b': 2}, separators=(',',':'))` | `'{"a":1,"b":2}'` | `JSON.stringify({'a': 1, 'b': 2})` | `"{\"a\":1,\"b\":2}"`
Json反序列化 | `json.loads('{"a":1,"b":2}')` | `{'a': 1, 'b': 2}` | `JSON.parse('{"a":1,"b":2}')` | `{a: 1, b: 2}`

Python3
```
>>> print(u'中文'.encode('utf-8'))
b'\xe4\xb8\xad\xe6\x96\x87'

>>> print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
中文
```

Python2
```
>>> '中文'
'\xe4\xb8\xad\xe6\x96\x87'

>>> print('\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
中文
```

JS
```
> encodeURIComponent('中文').substring(1).split('%').map(x => parseInt(x, 16))
< (6) [228, 184, 173, 230, 150, 135]

> decodeURIComponent([228, 184, 173, 230, 150, 135].map(x => '%'+x.toString(16)).join(''))
< "中文"
```

## 闭包

所谓闭包，指的就是一个函数。当两个函数彼此嵌套时，内部的函数就是闭包。

## H5 js 真机调试

js引入
```
<script src="https://cdn.bootcss.com/vConsole/3.3.4/vconsole.min.js"></script>
```

页面使用
```
// 实例化
var vConsole = new VConsole();

$(document).ready(function () {
	loadTimer();
	console.log(123)
});
```

## 遍历

for in 对象|数组
```
for(let index in array) {  
    console.log(index, array[index]);
};
```

for of 数组
```
for(let value of array) {  
    console.log(value);
};
```

## 跨域测试

[https://yq.aliyun.com/articles/688172](https://yq.aliyun.com/articles/688172)
```
var token= "Bearer eyJhbGciOiJIUzUxMiIsImV4cCI6MTU4Nzk5NTcyOCwiaWF0IjoxNTg3OTk0NTI4fQ.eyJ0b2tlbl9pZCI6MX0.3Tb1lsGKdEAHepuIxeSCJ9ZOyO3pMIbL6sfRbxHv8Vt0C2_syBEF9BsCA7MzqUfRIqubFKX3IIYaxO8MuxNuxg";
var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://127.0.0.1:8000/task?page=1&size=20');
xhr.setRequestHeader("Authorization",token);
xhr.send(null);
xhr.onload = function(e) {
    var xhr = e.target;
    console.log(xhr.responseText);
}
```

使用浏览的开发者工具console测试跨域功能
