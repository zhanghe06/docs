# pprof

- [runtime/pprof](https://golang.org/pkg/runtime/pprof/)
- [net/http/pprof](https://golang.org/pkg/net/http/pprof/#Index)

1. `go test benchmart`，结合`go test`使用。适用于对性能要求较高的函数进行性能优化分析。
2. `runtime/pprof`，将`pprof`监控信息以文件形式输出，在程序停止后进行分析。适用于分析一次性任务性程序，如worker类进程。
3. `net/http/pprof`，启用web监控，优点可以在程序运行整个生命周期进行监控。
