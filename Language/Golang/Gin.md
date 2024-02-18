# Gin

## Context

`gin.Context` 与 `context.Context`

- gin.Context
  - 赋值: Set; 例如: c.Set(key, val)
  - 取值: Get; 例如: val, ok := c.Get(key)
- context.Context
  - 赋值: context.WithValue；例如: ctx = context.WithValue(ctx, "userIP", "127.0.0.1")
  - 取值: ctx.Value; 例如: userIP := ctx.Value("userIP").(string)

context最佳实践：

- 通常不要将context放到结构体中，使用 context 的一个很好的心智模型是它应该在程序中流动，应该贯穿整个代码。不希望将其存储在结构体之中。它从一个函数传递到另一个函数，并根据需要进行扩展。
- 使用WithValue的时候注意传递的value是线程安全的，赋值无需加锁，需要注意当value是一个map对象时，不能直接修改，需要采用写时复制（英语：Copy-On-Write，简称COW）技术进行复制新的副本。
- 用Context来取消一个goroutine 的运行，这是 Context 最常用的场景之一，Context 也被称为 goroutine 生命周期范围(goroutine-scoped)的 Context，把Context 传递给 goroutine。
- 对于非用户发起的系统任务，可以传递空上下文`ctx := context.TODO()`

参考：

https://yuerblog.cc/2019/09/18/%E5%9F%BA%E4%BA%8Econtext%E6%89%A9%E5%B1%95gin%E6%A1%86%E6%9E%B6/

gin.Context提供了一个Set方法，它不是context.Context接口定义，仅能通过gin.Context.Set调用

```
// Set is used to store a new key/value pair exclusively for this context.
// It also lazy initializes  c.Keys if it was not used previously.
func (c *Context) Set(key string, value interface{}) {
    if c.Keys == nil {
        c.Keys = make(map[string]interface{})
    }
    c.Keys[key] = value
}
```

我们可以通过gin.Context.Set保存针对当前请求的trace上下文对象，然后将gin.Context作为context.Context向下透传，那么例如mysql、redis等类库内部就可以通过context.Context.Value()取到trace对象，完成埋点：

```
return func (c *gin.Context) {
    // 可以在gin.Context中设置key-value
    c.Set("trace", "假设这是一个调用链追踪sdk") 
            dbQuery(c, "select * from xxx")
```

在mysql类库内可以这样取出trace对象使用：

```
// 模拟一个MYSQL查询
func dbQuery(ctx context.Context, sql string) {
    // 模拟调用链埋点
    trace := ctx.Value("trace").(string)
```

context.WithTimeout附加超时能力

```
    return func (c *gin.Context) {
        // 可以在gin.Context中设置key-value
        c.Set("trace", "假设这是一个调用链追踪sdk")

        // 请求超时控制
        timeoutCtx, _ := context.WithTimeout(c, 5 * time.Second)
```
