# 设计模式 (Design Patterns)

- 装饰器
- 观察者
- 单例模式
  - 概念: 单例模式（Singleton Pattern）提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象
  - 应用: 生成唯一序列号；计数器；创建耗资源的对象（如:I/O与数据库的连接）
- 享元模式
  - 概念: 享元模式（Flyweight）运用共享技术有效地支持大量细粒度的对象
  - 应用: 系统中存在大量相似对象；需要缓冲池的场景
- 适配器模式
  - 概念: 适配器模式（Adapter Pattern）是作为两个不兼容的接口之间的桥梁。

## 多重继承

部分语言（C++）支持多重继承，因多重继承破坏了"is-a"关系，Java提供了接口interface功能，Python没有接口功能，采用Mixin模式

## 全局变量

使用简单，避免变量通过参数传递；不便测试

## 单例模式 VS 依赖注入

- 单例模式，设计简单，本质上充当全局变量角色，阻碍了测试性
- 依赖注入，可以测试