# Golang

官网: [https://golang.org](https://golang.org)

文档: [https://golang.org/doc](https://golang.org/doc)

并发模型：通过 Goroutine + Channel 实现 CSP 模型

内存分配：TCMalloc 是 Google 开发的内存分配器

垃圾回收：Golang的垃圾回收采用的是 标记-清理（Mark-and-Sweep）算法 

一般结构

```
// 当前程序的包名
package main
// 导入其他的包
import "fmt"
// 一次导入多个包
import (
    "io"
    "os"
)
// 常量的定义
const PI = 3.14
// 全局变量的声明与赋值，该变量在整个package中使用
var name = "go"
// 一般类型声明
type newType int
// 结构的声明
type go struct{}
// 接口的声明
type golang interface{}
// 由main函数作为程序入口启动
func main() {
    fmt.Println("Hello World!")
}
```

- 基本数据类型
  
  + 变量、常量
  + 整数类型、浮点数类型、复数类型、字符串类型、byte与rune（byte与rune都属于别名类型。byte是uint8的别名类型，而rune是int32的别名类型）

- 高级数据类型
  
  + 数组类型
  + 切片类型，注意区分：切片表达式
  + 字典类型
  + 通道类型

- 容器数据类型
  
  + 数组
    
    + 定义 `name [size]type`
    
    + 示例 `q := [3]int{1, 2, 3}`
    
    + 示例 `q := [...]int{1, 2, 3}`
    
    + 遍历 `for k, v := range team {
      
                fmt.Println(k, v)
            }`
  
  + 切片 name []type
  
  + 映射 name map[key_type] value_type
  
  + sync.Map
    
    + Load
    + Store
    + Delete
  
  + 双向链表 container/list

指针：
    - 取值 value := *ptr
    - 取址 ptr := &house

channel:
    - 重复关闭，引发异常
    - 向关闭的通道读取数据，读到零值
    - 向关闭的通道发送数据，引发异常
    - 向堆满的通道发送数据，阻塞发送

| 操作        | nil的channel | 正常的channel | 已关闭的channel |
| --------- | ----------- | ---------- | ----------- |
| <- ch     | 阻塞          | 成功或阻塞      | 读到零值        |
| ch <-     | 阻塞          | 成功或阻塞      | panic       |
| close(ch) | panic       | 成功         | panic       |

`~/.zshrc` 或者 `/etc/profile`

```
# Golang environment variable
export GOROOT=/usr/local/go
export GOPATH=$HOME/work
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
```

测试演示:

```
➜  ~ go version
go version go1.17.2 darwin/amd64
➜  ~ cd
➜  ~ mkdir hello
➜  ~ cd hello
➜  hello go mod init example/hello
go: creating new go.mod: module example/hello
➜  hello vim hello.go
➜  hello go run .
Hello, World!
```

## Install

[https://go.dev/doc/install](https://go.dev/doc/install)

```
# 下载安装
wget https://golang.google.cn/dl/go1.16.linux-amd64.tar.gz
rm -rf /usr/local/go
tar -C /usr/local -xzf go1.16.linux-amd64.tar.gz

# 环境变量
echo "export PATH=$PATH:/usr/local/go/bin:/root/go/bin" >> ~/.bashrc
source ~/.bashrc

go version

# 配置环境
go env -w GOPRIVATE=github.com/org_name     # 私有仓库，跳过安全校验
go env -w GOPROXY=https://goproxy.cn,direct # 加速
go env -w GO111MODULE=on                    # 强制开始 GOMODULE
```

`GOROOT` and `GOPATH`

If you see empty for `GOROOT`:
1. Run `which go` (On my computer : `/usr/local/go/bin/go`)
2. then export like this `export GOROOT=/usr/local/go`

If you see empty for `GOPATH`:
1. Create any directory anywhere on your computer for go projects in my case: `~/GO_PROJECTS`
2. Then `export GOPATH=~/GO_PROJECTS`

```
export GOROOT=/usr/local/go
export GOPATH=~/GO_PROJECTS
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
```

## EOF

```go
func init() {
    io.EOF = nil
}
```

errors.Is(err, EOF)

err == EOF

## 内存泄露

## 资源泄露
