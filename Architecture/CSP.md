# CSP

CSP并发模型

Golang 就是借用CSP模型的一些概念(process和channel)，process是在go语言上的表现就是 goroutine 是实际并发执行的实体，每个实体之间是通过channel通讯来实现数据共享。
