# 领域驱动 (DDD)

[https://github.com/8treenet/freedom/tree/master/example/fshop](https://github.com/8treenet/freedom/tree/master/example/fshop)

- TDD
- DDD
- 数据驱动
- 贫血模型
- 演进式设计

DDD 分层

1. interfaces 表示层
2. application 应用层
3. domain 领域层
4. infrastructure 基础设施层


Service
Entity
Repo

## DDD和OO的重要区别

- DDD 更注重上下文边界，这种边界代表区分差异
- OO 更注重抽象，从差异中寻找共同点，然后将其抽象出来

DDD某种程度上是对OO的一种颠覆
OO是找共同点，然后抽象
DDD是找边界，然后处理关系

## 分布式与解耦
分布式不等同于解耦
虽然 “分布式”（Distributed）和 “解耦”（Decoupled）都以 D 开头，但它们本身不是一回事。


## 用事件替代你的DTO数据结构

## DDD的演进

### DDD：

技术专家专注于实现
领域专家专注于模型

两者的结合，能够激发创造性的合作

### 架构

DDD方法中并没有指定使用特定的架构（四层架构、五层架构和六边形架构）

四层架构：
- User Interface 用户界面层（或表示层）
- Application 应用层
- Domain 领域层（或模型层）
- Infrastructure 基础实施层

五层架构：
- User Interface 用户界面层（或表示层）
- Application 应用层
- Context 环境层
- Domain 领域层（或模型层）
- Infrastructure 基础实施层

六边形架构：
核心是依赖倒置，把分层架构推平；不再是上下或左右，而是变成了内部和外部。

- 内部 代表了application和domain层，现在微服务体系下Application已经没有存在的必要了，一个微服务就是一个Application。
- 外部 代表应用的驱动逻辑（主要是输入和输出的适配器）、基础设施或其他应用。

## 六边形架构

六边形架构的优点
- 业务领域的边界更加清晰
- 更好的可扩展性
- 对测试的友好支持
- 更容易实施DDD

在很多情况下，从开发者的角度进行的假设都会在事后被证明是错误的。
人们在预测软件未来演进方向时往往会做很多错误的决定。
比如对关系型数据库的选用，对前端框架的选用，对中间件的选用等等，六边形架构可以很好的帮助我们避免这一点。
