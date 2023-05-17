# Vue

官方风格指南: [https://cn.vuejs.org/v2/style-guide/](https://cn.vuejs.org/v2/style-guide/)

vue是框架名称，vue也是vue-cli在终端里面的命令。

vue-cli 是vue框架开发的快速工程化命令工具。

vue-cli2.0 vue-cli3.0/4.0 差异
```
2.0名称 vue-cli
2.0安装 npm install vue-cli -g
2.0创建 vue init webpack 项目名称
2.0启动 npm run dev
2.0静态目录 static
2.0配置文件 config/(dev.env.js,prod.env.js);config/index.js

3.0名称 @vue/cli
3.0安装 npm install @vue/cli -g
3.0创建 vue create 项目名称
3.0启动 npm run serve
3.0静态目录 public
3.0配置文件 .env.production,.env.development;vue.config.js
```

3.0/4.0 需要手动配置 [vue.config.js](https://cli.vuejs.org/zh/config/#vue-config-js)

@vue/cli-service 对 webpack 配置进行了抽象

安装基础依赖
```
npm i -D less@3.8.1             # 高版本会报错
npm i -D less-loader@5.0.0      # 高版本会报错
npm i -D @vue/cli-service
```

```
npm i -S vuex
npm i -S vue-router
npm i -S element-ui
npm i -S axios
npm i -S moment
```

- vue create
是vue-cli3.x的初始化方式，目前模板是固定的，模板选项可自由配置
使用方式：vue create 项目名称
目录结构：
```
node_modules:通过npm install安装的依赖代码库
public:部署到生产环境的目录
src:源码
.gitignore：git忽略里面设定的这些文件的提交
babel.config.js:babel转码配置
package.json：项目的配置文件，用于描述一个项目，包括我们init时的设置、开发环境、生成环境的依赖插件及版本等。
package-lock.json：普通package.json文件“^2.0”这样写的，意味着版本可以大于等于2.0，如此就会出现各种错误。
```

- vue init
是vue-cli2.x的初始化方式，可以使用github上面的一些模板来初始化项目，webpack是官方推荐的标准模板名
使用方式：vue init webpack 项目名称
目录结构：
```
build及config：webpack配置相关
node_modules:通过npm install安装的依赖代码库
src：项目源码
static：存放静态资源
.babelrc：babel相关配置（因为我们的代码大多都是    ES6，而大多浏览器是不支持ES6的，所以我们需要babel帮我们转换成ES5语法）
.editorconfig：编辑器的配置，可以在这里修改编码、缩进等
.eslintignore：设置忽略语法检查的目录文件
.eslintrc.js：eslint的配置文件
.gitignore：git忽略里面设定的这些文件的提交
index.html：入口html文件
package.json：项目的配置文件，用于描述一个项目，包括我们init时的设置、开发环境、生成环境的依赖插件及版本等。
package-lock.json：普通package.json文件“^2.0”这样写的，意味着版本可以大于等于2.0，如此就会出现各种错误。
```


```
npm install cnpm -g
cnpm install vue
cnpm install webpack -g
```

## [Element](https://element.eleme.cn/#/zh-CN)

第一步：安装项目模板
```
npm install -g webpack
npm install -g vue-cli
vue init webpack element_project

cd element_project      //进入项目目录
npm install             //安装项目依赖（新建项目省略此步）
npm run dev             //运行项目
```

访问：[http://localhost:8080](http://localhost:8080)

第二步：安装主题框架
```
cd element_project
npm i element-ui -S
npm i vuex -S
```
第三步：打包
```
npm run build
```

布局：

名称 | 尺寸
--- | ---
xs | <768px
sm | ≥768px
md | ≥992px
lg | ≥1200px
xl | ≥1920px

效果：宽屏页面时内容仅仅占页面宽50%居中显示。窄屏幕时占70%，手机时占100%。
```
<el-row :gutter="10">
  <el-col :xs="{span:24,offset:0}" :sm="{span:16,offset:4}" :md="{span:12,offset:6}">
  </el-col>
</el-row>
```

颜色：
- primary
- success
- warning
- danger
- info

## 插值表达式

插值表达式`{{  }}`默认已文本形式显示

## 指令

指令 | 解释 | 缩写
--- | --- | ---
v-once | 渲染一次 | -
v-html | HTML | -
v-bind | HTML属性 | :<属性名称>
v-model | 表单双向绑定 | -
v-on | 事件 | @<事件名称>
v-if | 条件 | -
v-for | 循环 | -

## 事件处理器

事件修饰符

按键修饰符

## 组件（Vue的核心）

包含关系，不是继承关系

- 父组件，包含子组件
- 子组件，被父组件引用

方式 | 数据流 | 说明
--- | --- | ---
props | 父组件 -> 子组件 | 组件实例的作用域是孤立的; 不应该在一个子组件内部改变 prop，即子组件不能改变父组件的数据
$emit | 子组件 -> 父组件 | v-on:input="$emit('input', $event.target.value)"; 或者定义在子组件的方法内


$emit，仅kebab-case命名
$event

$refs dom节点、组件节点
$store 子组件可通过this.$store访问

## 插槽

插槽显不显示、怎样显示是由父组件来控制的，而插槽在哪里显示就由子组件来进行控制


## Vuex 和 单纯的全局对象

[Vuex](https://vuex.vuejs.org/zh/guide/)

全局对象，方式一
```
// demo.vue
import global_ from 'components/tool/Global'

export default {
  data () {
    return {
      getColor: global_.getRandColor,
```

全局对象，方式二
```
// main.js
import global_ from './components/tool/Global'
Vue.prototype.GLOBAL = global_

// demo.vue
export default {
  data () {
    return {
      getColor: this.GLOBAL.getRandColor,
```

全局对象，方式三
```
Vuex
```


## 学习路径

1. VUE基础
2. 组件化
3. 工程化
4. Element（页面布局，导航，表格，表单...）


## 语法

日期格式化
`yyyy-MM-dd HH:mm:SS`

### 模板循环

循环 - 列表
```
<p v-for="(item, i) in list_data" :key="item.id">索引: {{i}}, 值: {{item.name}}</p>
```

循环 - 对象
```
<p v-for="(val, key, i) in obj_data">索引: {{i}}, 键: {{key}}, 值: {{val}}</p>
```

循环 - 数字
```
<p v-for="count in 5">第{{count}}次</p>
```
以上数字从1开始

### 脚本循环
```
for(let item of response.data.result) {
    // 用item操作每一条数据。
}
```
注意：这里是 of 不是 in，of和in是有区别的

```
response.data.result.forEach((item, index) => {
    // 用item操作每一条数据。
})
```


总结：

`for in` 总是得到对像的key、数组或字符串的下标

`for of` 和`forEach`一样, 是直接得到值, 但是`for of`不能用于对象


列表操作
```
this.list.push({})
this.list.unshift({})
```

## Router


## Axios

```
npm i axios -S
```

main.js
```ecmascript 6
import Vue from 'vue'

import axios from 'axios'

Vue.prototype.$http = axios
```

发送示例
```ecmascript 6
const formData = {
  age: this.ruleForm.age,
  pass: this.ruleForm.pass
}
// 发送数据
this.loading = true
this.$http.post('/api.json', formData)
  .then(res => {
    // 数据发送成功回调
    console.log("数据发送成功")
    console.log(res.data)
  })
  .catch((error) => {
    // 数据发送失败回调
    console.log(error)
  })
  .finally(() => {
    this.loading = false
  })
```

请求示例 - 不含参数
```ecmascript 6
this.loading = true
this.$http.get('/api.json')
  .then(res => {
    // 数据请求成功回调
    console.log(res.data)
  })
  .catch((error) => {
    // 数据请求失败回调
    console.log(error)
  })
  .finally(() => {
    this.loading = false
  })
```

请求示例 - 含有参数
```ecmascript 6
let params = {
  name: 12345
}
this.$http.get('/api.json', {params})
  .then(res => {
    // 数据请求成功回调
    console.log(res.data)
  })
  .catch((error) => {
    // 数据请求失败回调
    console.log(error)
  })
  .finally(() => {
    this.loading = false
  })
```
注意 params 外层需要花括号再包一层

## 生命周期

```
mounted() {
  // 定时刷新
  if (this.timer) {
    clearInterval(this.timer)
  } else {
    this.timer = setInterval(() => {
      this.getMigrateDetail()
    }, 1000)
  }
}
```

```
destroyed() {
  // 清除定时
  clearInterval(this.timer)
}
```

循环执行（setInterval）
```
export default {
  data() {
    return {
      timer: '',
      value: 0
    }
  },
  methods: {
    get() {
      this.value ++
      console.log(this.value)
    }
  },
  mounted() {
    this.timer = setInterval(this.get, 1000)
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }
}
```
以上循环多次执行

定时执行（setTimeout）
```
export default {
  data() {
    return {
      timer: '',
      value: 0
    }
  },
  methods: {
    get() {
      this.value ++;
      console.log(this.value)
    }
  },
  mounted() {
    this.timer = setTimeout(this.get, 1000)
  },
  beforeDestroy() {
    clearTimeout(this.timer)
  }
}
```
以上仅仅执行一次

延时执行
```
var that = this;
setTimeout(function () {
  that.$notify({
    title: "成功",
    message: "这是一条成功的提示消息",
    type: "success",
  });
}, 3000);
```

循环延时执行任务
```
for(var i = 0; i < 3; i++) {
  (function(i) {
    setTimeout(function() {
      console.log(i);
    }, (i + 1) * 1000);
  })(i)
}
```

循环延时调用外部方法
```
testTimeSleepLog (i) {
  console.log(i)
},
testTimeSleep () {
  const that = this
  for (let i = 0; i < 3; i++) {
    (function (i) {
      setTimeout(function () {
        that.testTimeSleepLog(i)
      }, (i + 1) * 1000)
    })(i)
  }
}
```

每个任务间隔3秒请求一次，对应任务2秒之后取结果
```
// 请求
req (i) {
  console.log('req: ' + i)
},
// 响应
res (i) {
  console.log('res: ' + i)
},
// 执行
run () {
  const that = this
  const tasks = ['a', 'b', 'c', 'd']
  // 请求任务
  for (let i = 0; i < tasks.length; i++) {
    (function (i) {
      setTimeout(function () {
        that.req(tasks[i])
      }, i * 3 * 1000)
    })(i)
  }
  // 响应任务
  for (let i = 0; i < tasks.length; i++) {
    (function (i) {
      setTimeout(function () {
        that.res(tasks[i])
      }, ((i + 1) * 3 - 1) * 1000)
    })(i)
  }
}
```

```
req时间:  [0]  1   2  [3]  4   5  [6]  7   8
res时间:   0   1  [2]  3   4  [5]  6   7  [8]
```


## 使用element-ui的分页组件刷新后保留在当前页

```
<div class="pagination">
  <el-pagination
    @size-change="handleSizeChange"
    @current-change="handleCurrentChange"
    :page-sizes="[10, 20, 50, 100]"
    :page-size="pageSize"
    :current-page.sync="currentPage"
    layout="total, sizes, prev, pager, next" background
    :total="count">
  </el-pagination>
</div>
```

```
//每页大小变化
handleSizeChange(val) {
  this.$router.replace({
    path: this.$route.path,
    query: {
      page: this.$route.query.page ? this.$route.query.page : 1,
      pageSize: val,
    }
  });
  this.getData();
},
//分页页码变化
handleCurrentChange(val) {
  this.$router.replace({
    path: this.$route.path,
    query: {
      page: val,
      pageSize: this.$route.query.pageSize ? this.$route.query.pageSize : 10,
    }
  });
  this.getData();
},
//获取数据
getData(){
  axios.post({
    page: this.$route.query.page ? this.$route.query.page : 1,
    pageSize: this.$route.query.pageSize ? this.$route.query.pageSize : 10,
  }).then((res) => {
    console.log(res)
  }).catch((err) => {
    console.error('获取列表出错');
    console.error(err);
  });
},
```


## props
```
demo: {
  type: Array,
  default: function () {
    return []
  }
}

demo: {
  type: Object,
  default: function () {
    return {}
  }
}

demoArray: {
  type: Array,
  default: () => []
}

demoObject: {
  type: Object,
  default: () => ({})
}
```

## 路由

页面跳转的2种方式：

Declarative	| Programmatic
--- | ---
<router-link :to="...">	| router.push(...)
<router-link :to="..." replace>	| router.replace(...)
- | router.go(n)

```
// literal string path
router.push('home') // -> /home

// object
router.push({ path: 'home' }) // -> /home

// named route, /user/123
router.push({ name: 'user', params: { userId: '123' } })

// with query, resulting in /register?plan=private
router.push({ path: 'register', query: { plan: 'private' } })

// -> /user/123
const userId = '123'
router.push({ name: 'user', params: { userId } })
router.push({ path: `/user/${userId}` })

// This will NOT work, /user
router.push({ path: '/user', params: { userId } })
```

动态路由：
```
const User = {
  template: '<div>User {{ $route.params.id }}</div>'
}

const router = new VueRouter({
  routes: [
    // dynamic segments start with a colon
    { path: '/user/:id', component: User }
  ]
})
```

嵌套路由：
```
<div id="app">
  <!-- 顶级路由 -->
  <router-view></router-view>
</div>
```
```
const User = {
  template: `
    <div class="user">
      <h2>User {{ $route.params.id }}</h2>
      <!-- 嵌套路由 -->
      <router-view></router-view>
    </div>
  `
}

const router = new VueRouter({
  routes: [
    { path: '/user/:id', component: User,
      children: [
        {
          // UserProfile will be rendered inside User's <router-view>
          // when /user/:id/profile is matched
          path: 'profile',
          component: UserProfile
        },
        {
          // UserPosts will be rendered inside User's <router-view>
          // when /user/:id/posts is matched
          path: 'posts',
          component: UserPosts
        },
        {
          // UserHome will be rendered inside User's <router-view>
          // when /user/:id is matched
          path: '',
          component: UserHome
        },
        // ...other sub routes
      ]
    }
  ]
})
```


## iconfont

## 经典问题：对象内部元素变了，但是页面没有重新渲染

原因：由于 JavaScript 的限制，Vue 不能检测数组和对象的变化。

参考：[https://cn.vuejs.org/v2/guide/reactivity.html](https://cn.vuejs.org/v2/guide/reactivity.html)

修改的正确方式：

- 对象

`this.$set(this.someObject,'b',2)`

`this.someObject = Object.assign({}, this.someObject, { a: 1, b: 2 })`

- 数组

`vm.items.splice(indexOfItem, 1, newValue)`

数组操作 | 表达式 | 响应值 | 原值变化 | 参数说明
--- | --- | --- | --- | ---
插入 | del_arr = array.splice(index, 0, value) | 被删除的数组(空数组[]) | 插入后的数组 | (插入位置, 删除数量0, 插入的项)
替换 | del_arr = array.splice(index, 1, value) | 被替换的数组 | 替换后的数组 | (替换位置, 删除数量1, 替换的项)
删除 | del_arr = array.splice(index, n) | 被删除的数组 | 删除后的数组 | (删除位置, 删除数量n)


对于嵌套对象，可以做一层拷贝，赋值给你想要赋值的对象或者变量（貌似没用）
`JSON.parse(JSON.stringify(obj))`

## 参考

[https://github.com/lin-xin/vue-manage-system](https://github.com/lin-xin/vue-manage-system)

## 文件上传

CHROME 异常`net::ERR_UPLOAD_FILE_CHANGED`

复现步骤：
```
1、点击上传（上传失败、表单未重置）
2、修改文件，再次上传
```

## 插件

- 图片裁剪 [vue-cropper](https://github.com/xyxiao001/vue-cropper)

## 有赞

[Vant](https://vant-contrib.gitee.io/vant/#/zh-CN)

业务代码国际化 [vue-i18n](https://github.com/kazupon/vue-i18n)
