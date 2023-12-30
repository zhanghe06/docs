# 六边形架构 Hexagonal Architecture

## 端口和适配器架构

参考：

[Ports & Adapters Architecture](https://herbertograca.com/2017/09/14/ports-adapters-architecture/)

[Hexagonal Architecture, there are always two sides to every story](https://medium.com/ssense-tech/hexagonal-architecture-there-are-always-two-sides-to-every-story-bc0780ed7d9c)

[Using Domain-Driven Design(DDD)in Golang](https://dev.to/stevensunflash/using-domain-driven-design-ddd-in-golang-3ee5)

[DDD, Hexagonal, Onion, Clean, CQRS, … How I put it all together](https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/)


端口和适配器架构只有一个目标：将业务逻辑与系统使用的交付机制和工具隔离开来，防止逻辑泄露。
它通过使用一种通用的编程语言结构来做到这一点：接口。
- 在 UI 端（驱动适配器），我们创建使用我们的应用程序接口的适配器，即：控制器。
- 在基础设施方面（驱动的适配器），我们创建了实现我们的应用程序接口的适配器，即：存储库。


实现细节：

- 端口（Ports）将（大多数情况下，取决于您选择的语言）在代码中表示为接口（Interface）。
- 主动驱动适配器（Driver Adapters）将使用端口（Port），应用服务（Application Service）将实现端口定义的接口，在这种情况下，端口的接口和实现都在六边形（Hexagon）内部。
- 从动驱动适配器（Driven Adapters）将实现端口（Port），应用服务（Application Service）将使用它，在这种情况下，端口在六边形（Hexagon）内部，但实现在适配器中，因此在六边形（Hexagon）之外。


六边形架构上下文中的依赖倒置：

