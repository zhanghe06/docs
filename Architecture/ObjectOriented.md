# 面向对象 (Object Oriented)

依赖倒置(DIP)、控制反转(IOC)和依赖注入(DI)

## 依赖倒置 - DIP, Dependence Inversion Principle

原始定义：
```
上层模块不应该依赖底层模块，它们都应该依赖于抽象。
抽象不应该依赖于细节，细节应该依赖于抽象。
```
依赖倒置是软件设计六大设计原则之一

抽象：即抽象类或接口，两者是不能够实例化的。
细节：即具体的实现类，实现接口或者继承抽象类所产生的类，两者可以通过关键字new直接被实例化。

依赖倒置实质上是面向接口编程的体现

经典例子：
```
public class Person {

//  private Bike mBike;
//  private Car mCar;
//  private Train mTrain;
    private Driveable mDriveable;

    public Person() {
        //mBike = new Bike();
        //mCar = new Car();
        //mTrain = new Train();
        mDriveable = new Train();
    }

    public void chumen() {
        System.out.println("出门了");
        //mBike.drive();
        //mCar.drive();
        //mTrain.drive();
        mDriveable.drive();
    }
}
```
可以看出，依赖倒置之后，交通方式的变化对Person类产生的影响较小。
较小的代码变动，意味着项目的稳定。

## 控制反转 - IOC, Inversion of Control

上面代码，Person 自己掌控着内部 mDriveable 的实例化。 
现在，我们可以更改一种方式。将 mDriveable 的实例化移到 Person 外面。

经典例子：
```
public class Person {

    private Driveable mDriveable;

    public Person(Driveable driveable) {
        this.mDriveable = driveable;
    }

    public void chumen() {
        System.out.println("出门了");

        mDriveable.drive();
    }
}
```
可以看出，控制反转之后，无论出行方式怎么变化，Person这个类都不需要更改代码了。

## 依赖注入 - DI, Dependency Injection

依赖注入是一种实现控制反转的方式

依赖注入有三种方法：
1、构造函数注入
2、setter方式注入
3、接口方式注入

接口注入的方式和setter注入的方式很相似，不同点在于接口注入使用了统一的方法来完成注入，而setter注入的方法名称比较随意，通过接口注入能够体现类型依赖注入的能力

DI 帮助我解决了之前在 Go 应用程序中遇到的很多问题 - 过度使用 init 函数，滥用全局变量和复杂的应用程序设置等。

场景解说：（参考：https://zhuanlan.zhihu.com/p/189391362）

假设你构造 Server 需要 Config 结构体。一种方法是在初始化期间 Server 构建 Config 。
现在我们将 Server 与Config 分离。我们可以根据自己的逻辑创造 Config 然后将结果传递给 New 函数。
此外，如果 Config 是一个接口，这为我们提供了一个简单的模拟途径 。只要 New 实现了我们的接口，就可以传递任何我们想要的东西。这使得测试实现了 Config 接口的 Server 很简单。


## 全局变量

使用全局连接对象时，后台服务无法在并发条件下测试出相同的数据。

使用全局变量：
```
var MongoService mongo.Service
 
func InitMongoService(url string) {
  MongoService = ...
}
 
func GetApp(id uint64) *App {
  a := new(App)
  MongoService.Session().Find(..).One(a)
  return a
}
```

清除全局变量：
```
type AppLoader struct {
  MongoService mongo.Service
}
 
func (l *AppLoader) Get(id uint64) *App {
  a := new(App)
  l.MongoService.Session().Find(..).One(a)
  return a
}
```
许多引用全局变量的函数现在变成了结构体中存储了它们的依赖。

于是main函数会变成这个样子：
```
func main() {
  mongoURL := flag.String(...)
  mongoService := mongo.NewService(mongoURL)
  cacheService := cache.NewService(...)
  appLoader := &AppLoader{
    MongoService: mongoService,
  }
  handlerOne := &HandlerOne{
    AppLoader: appLoader,
  }
  handlerTwo := &HandlerTwo{
    AppLoader:    appLoader,
    CacheService: cacheService,
  }
  rootHandler := &RootHandler{
    HandlerOne: handlerOne,
    HandlerTwo: handlerTwo,
  }
  ...
}
```
如果一直这样写下去，main()函数的方法体将会被被大量的代码占据。
而这些代码仅仅只是做了两件很普通的事情：分配内存空间、装配对象和组件关系。

## 组合与聚合

原则：整体对部分依赖，而不是部分对整体依赖。
例如：汽车依赖车轮，而不是车轮依赖汽车。

部分对象的创建、存在和消亡都是和整体对象一起的就成为组合。
例如：嘴、胃伴随着人的存在而存在。

可以在初始化之后能够更换的或者不需要强制完整的整体与部分的关系称之为聚合。
例如：人截肢后换成机械腿，也可以走路，只是行走有困难。

## 领域驱动设计(DDD) 

领域驱动设计(DDD) 做为一种软件工程的方法论，它可以帮助我们设计高质量的软件，或者说任何工程的设计都需要方法论，不论是城市设计、建筑设计、室内设计。

架构分层:

1. interface 表示层 (与其他系统交互的所有内容)
    - facade 外观（类似三层架构的controller，他负责将外部请求委派给一个或多个service进行处理，本身不处理任何业务逻辑）
    - routes
    - middlewares
    - utils
3. application 应用层 (领域层和表示层之间的通道)
    - service 应用服务（接口，并实现；区别于domain层的domain service）
    - assembler 组装器（负责完成domain model对象到dto的转换）
4. domain 领域层 (定义应用程序的域和业务逻辑的地方)
    - service 领域服务（接口，并实现）
    - aggregate 聚合
    - entity 领域实体
    - model 
    - repository 存储库 (类似三层架构的DAO接口，不包括实现；只管CRUD，不管业务逻辑)
5. infrastructure 基础设施层 (为其他层提供通用的技术能力：业务平台，编程框架，持久化机制，消息机制，第三方库的封装，通用算法，等等)
    - config 配置
    - db 数据库
    - persistence 持久化 (对domain层的repository接口的实现)
    - log 日志
    - clients 第三方库的封装

```
interface层调用application层
application层会调用domain、infrastructure层
domain层不依赖其余层，它定义repository接口，infrastructure层会实现
interfaces层通常调用application层或者infrastructure层
```

从DDD分层架构来看，将基础设施层放入底层是存在缺点的，领域层依赖于基础设施层，这对领域层的内聚性产生影响。
一个解决方案就是依赖倒置。

采用了依赖注入方式后，其实可以发现事实上已经没有分层概念了。
无论高层还是底层，实际只依赖于抽象，整个分层好像被推平了，这就引入下一个架构六边形架构。

参考: [https://www.jianshu.com/p/5fceb6fb42a1](https://www.jianshu.com/p/5fceb6fb42a1)


## 六边形架构

实际上它也是一种分层架构，只不过不是上下或左右，而是变成了内部和外部。

内部代表了application和domain层。
外部代表应用的驱动逻辑、基础设施或其他应用。
内部通过端口和外部系统通信，端口代表了一定协议，以API呈现。

一个典型的六边形架构应用有两个端口：
一个端口对应用户接口层，用于应用控制，
一个端口对应数据访问层，用于数据获取和持久化。
每个端口都可以对应几个适配器，该应用可以被自动化测试，系统层面的回归测试，用户交互操作，远程HTTP调用，REST调用或者其他。

domain - 领域模型
    aggregate - 聚合
    entity - 实体
    dto - 传输对象
    po - 持久化对象
    *.go - 领域服务
adapter - 端口适配器
    controller - 输入适配器
    repository - 输出适配器
server - 服务端程序入口
    conf - 配置文件
    main.go - 主函数
infra - 基础设施
    *go - 基础设施组件



概念：
- VO（View Object）：视图对象，用于展示层，它的作用是把某个指定页面（或组件）的所有数据封装起来。
- DTO（Data Transfer Object）：数据传输对象，这个概念来源于J2EE的设计模式，原来的目的是为了EJB的分布式应用提供粗粒度的数据实体，以减少分布式调用的次数，从而提高分布式调用的性能和降低网络负载，但在这里，我泛指用于展示层与服务层之间的数据传输对象。
- DO（Domain Object）：领域对象，就是从现实世界中抽象出来的有形或无形的业务实体。
- PO（Persistent Object）：持久化对象，它跟持久层（通常是关系型数据库）的数据结构形成一一对应的映射关系，如果持久层是关系型数据库，那么，数据表中的每个字段（或若干个）就对应PO的一个（或若干个）属性。


```
用户发出请求（可能是填写表单），表单的数据在展示层被匹配为VO。

展示层把VO转换为服务层对应方法所要求的DTO，传送给服务层。

服务层首先根据DTO的数据构造（或重建）一个DO，调用DO的业务方法完成具体业务。

服务层把DO转换为持久层对应的PO（可以使用ORM工具，也可以不用），调用持久层的持久化方法，把PO传递给它，完成持久化操作。

对于一个逆向操作，如读取数据，也是用类似的方式转换和传递，略。
```
