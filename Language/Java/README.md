# Java

## openjdk

[windows openjdk-8](https://download.java.net/openjdk/jdk8u42/ri/openjdk-8u42-b03-windows-i586-14_jul_2022.zip)

Win10下DPI过高导致java程序字体特别小问题解决方法 https://www.cnblogs.com/AirCrk/p/12909262.html

环境变量 (MAC)
```
export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-18.jdk/Contents/Home
export CLASS_PATH=${JAVA_HOME}/lib
export PATH=$PATH:${JAVA_HOME}/bin
```

## Apache Tomcat®

[https://tomcat.apache.org](https://tomcat.apache.org)

环境变量
```
CATALINA_HOME=C:\Program Files\apache-tomcat-8.5.38
```

安装完成，双击startup.bat

[http://127.0.0.1:8080](http://127.0.0.1:8080)

## 基础教程

### 数据类型

- 基本数据类型
    - 整数类型：byte，short，int，long
    - 浮点数类型：float，double
    - 字符类型：char
    - 布尔类型：boolean
- 引用类型
    - 所有class和interface类型，包括：字符串（String）、数组（类型[]）、对象（Object）、Runnable、Exception、null...

定义变量的时候，如果加上`final`修饰符，这个变量就变成了常量

### 空间占用

计算机内存的最小存储单元是字节（byte），一个字节就是一个8位二进制数，即8个bit。它的二进制表示范围从00000000~11111111，换算成十进制是0~255，换算成十六进制是00~ff。

类型 | 空间（字节）
--- | ---
byte | 1
short | 2
int | 4
long | 8
float | 4
double | 8
char | 2

### 面向对象
- 类（class）
- 实例（instance）
- 修饰（public、protected、private；static；final；abstract）
- 重载（Overload）多个方法的方法名相同，但各自的参数不同，称为方法重载，返回值类型通常都是相同的
- 继承（extends）
- 多态（Polymorphic）在继承关系中，子类如果定义了一个与父类方法签名完全相同的方法，被称为覆写（Override）
- 接口（interface）
- 包（package）
- 模块（Module）

核心类:
- JavaBean 是一种符合命名规范的class，它通过getter和setter来定义属性，可以利用IDE快速生成getter和setter
- 枚举类 通过enum定义的枚举类；enum的构造方法要声明为private，字段强烈建议声明为final
- 记录类 使用record关键字，可以一行写出一个不变类

修饰符:
- 访问控制修饰符 (保护对类、变量、方法和构造方法的访问)
    + default (默认的，什么也不写) 使用对象: 类、接口、变量、方法
    + private (私有的) 使用对象: 变量、方法
    + public (公共的) 对所有类可见 使用对象: 类、接口、变量、方法
    + protected (受限的) 使用对象：变量、方法
- 非访问修饰符
    + static (静态的) 用来修饰类方法和类变量。静态方法不能使用类的非静态变量; 静态变量也被称为类变量
    + final (最终的) 用来修饰类、方法和变量。修饰的类不能够被继承; 修饰的方法不能被继承类重新定义; 修饰的变量为常量，是不可修改的。
    + abstract (抽象的) 用来创建抽象类和抽象方法。抽象类不能用来实例化对象, 一个类不能同时被 abstract 和 final 修饰; 抽象方法是一种没有任何实现的方法，该方法的的具体实现由子类提供, 抽象方法不能被声明成 final 和 static
    + synchronized (同步的) 主要用于线程的编程。synchronized 关键字声明的方法同一时间只能被一个线程访问, 可以应用于四个访问修饰符
    + transient (短暂的) 序列化的对象包含被 transient 修饰的实例变量时, java 虚拟机(JVM)跳过该特定的变量, 不会被序列化
    + volatile (易失的) 主要用于线程的编程。volatile 修饰的成员变量在每次被线程访问时，都强制从共享内存中重新读取该成员变量的值。而且，当成员变量发生变化时，会强制线程将变化值回写到共享内存。这样在任何时刻，两个不同的线程总是看到某个成员变量的同一个值。

### 异常
- Error（无需捕获的严重错误）
- Exception（应该捕获的可处理的错误）
    - RuntimeException 以及它的子类
    - 非RuntimeException（包括IOException、ReflectiveOperationException等等）

### 反射（Reflection）
反射是为了解决在运行期，对某个实例一无所知的情况下，如何调用其方法。
通过Class实例获取class信息的方法称为反射（Reflection）

### 注解（Annotation）
- @Target 定义Annotation能够被应用于源码的哪些位置
- @Retention 定义了Annotation的生命周期
- @Repeatable 定义Annotation是否可重复
- @Inherited 定义子类是否可继承父类定义的Annotation

### 泛型
泛型就是定义一种模板，例如ArrayList<T>，然后在代码中为用到的类创建对应的ArrayList<类型>
例如: `ArrayList<String> strList = new ArrayList<String>();`

### 单元测试
JUnit
- @Test
- 断言（Assertion）: assertTrue()、assertFalse()、assertNotNull()、assertArrayEquals()...
- Fixture: @BeforeEach、@AfterEach；@BeforeAll、@AfterAll

### 集合（Collection）
- List 有序列表的集合
- Set 保证没有重复元素的集合
- Map 通过键值（key-value）查找的映射表集合

## 项目实践



框架

- SSH: Struts2+Spring+Hibernate
- SSM
    - Spring+Struts2+Mybatis (历史项目)
    - Spring+SpringMVC+Mybatis (现在主流)
- Spring Boot


Mybatis 是半自动的，Mybatis自动化的地方在于它把数据给我们封装后返回给我们，手动的部分在于我们自己来写sql，这样的方式很灵活，我们可以根据需求写最优的sql语句。

Hibernate 是全自动的，sql都帮我们写好了，但是这也是Hibernate一个很大的缺点，有时候它给的sql语句并不是最优的，就极大的影响了我们的效率。

### 常用概念

- Entity 最常用实体类，基本和数据表一一对应，一个实体一张表
- BO (business object) 业务对象
- VO (value object) 值对象
- PO (persistant object) 持久层对象
- DTO (data transfer object) 数据传输对象
- POJO (plian ordinary java object) 简单无规则java对象 POJO是DO/DTO/BO/VO的统称
- DAO (data access object) 数据访问对象
- Controller 控制层
- View 视图层


Controller（控制层）
Service（业务层 - 接口）
ServiceImpl（业务层 - 实现）
Dao（持久层）一般一个DAO类和一张表对应
Mapper（数据层）
Model （模型层）

Bean类的实际意义是作为一个储存结构临时储存数据库中取得的一些多列数据
ArrayList是为了让多行数据变得简单存储
Dao类的意义就是将页面和后台增删改查四大操作分离，有了这些后台类，你要做的只是在JSP页面中调用这些数据，将会变得更加简洁！


### JDBC

常用数据库种类:

付费商用
- Oracle，甲骨文公司的一款关系数据库管理系统；
- SQL Server，微软自家产品，Windows定制专款；
- DB2，IBM的产品，听起来挺高端；
- Sybase，曾经跟微软是好基友，后来关系破裂，现在家境惨淡。

开源免费
- MySQL，大家都在用，一般错不了；
- PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；
- sqlite，嵌入式数据库，适合桌面和移动应用。
- Hbase NoSQL的一种，一个分布式的、面向列的开源数据库。属于hadoop生态圈、存储基于hdfs等
- Hive 基于Hadoop的一个数据仓库工具，用来进行数据提取、转化、加载，属于hadoop生态圈、存储基于hdfs等

常用的JDBC连接池有:
- HikariCP (SpringBoot默认采用的连接池)
- C3P0
- BoneCP
- Druid (阿里巴巴出品)

目前使用最广泛的是HikariCP

### ~~Servlet~~

常用的支持Servlet API的Web服务器:

- Tomcat: Apache开发的开源免费服务器；
- Jetty: Eclipse开发的开源免费服务器；
- GlassFish: 一个开源的全功能JavaEE服务器。
- WebLogic: Oracle 商用服务器
- WebSphere: IBM 商用服务器

### ~~JSP~~

1. JSP是一种在HTML中嵌入动态输出的文件，它和Servlet正好相反，Servlet是在Java代码中嵌入输出HTML；
2. JSP可以引入并使用JSP Tag，但由于其语法复杂，不推荐使用；
3. JSP本身目前已经很少使用，我们只需要了解其基本用法即可。

### ~~MVC~~

- Servlet 适合编写Java代码，实现各种复杂的业务逻辑，但不适合输出复杂的HTML；
- JSP 适合编写HTML，并在其中插入动态内容，但不适合编写复杂的Java代码。

MVC模式是一种分离业务逻辑和显示逻辑的设计模式，广泛应用在Web和桌面应用程序。

可以通过Servlet和JSP实现了一个简单的MVC模型，但它还不够简洁和灵活，后续我们会介绍更简单的Spring MVC开发

通过结合Servlet和JSP的MVC模式，我们可以发挥二者各自的优点：
1. Servlet实现业务逻辑；
2. JSP实现展示逻辑。

但是，直接把MVC搭在Servlet和JSP之上还是不太好，原因如下：
1. Servlet提供的接口仍然偏底层，需要实现Servlet调用相关接口；
2. JSP对页面开发不友好，更好的替代品是模板引擎；
3. 业务逻辑最好由纯粹的Java类实现，而不是强迫继承自Servlet。

Java有很多开源的模板引擎，常用的有：
- Thymeleaf
- FreeMarker
- Velocity
- Pebble (Jinja语法)

### Maven

Apache Maven是一个Java项目的管理和构建工具

1. Maven使用pom.xml定义项目内容，并使用预设的目录结构；
2. 在Maven中声明一个依赖项可以自动下载并导入classpath；
3. Maven使用groupId，artifactId和version唯一定位一个依赖。

[https://maven.apache.org](https://maven.apache.org)

```
cd $HOME/tools/
wget -c https://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.8.1/binaries/apache-maven-3.8.1-bin.tar.gz
tar xzvf apache-maven-3.8.1-bin.tar.gz
```

```
# java
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_101.jdk/Contents/Home
export CLASS_PATH=${JAVA_HOME}/lib
export PATH=$PATH:${JAVA_HOME}/bin
export PATH=$HOME/tools/apache-maven-3.8.1/bin:$PATH
```

```
mvn --version
```

中央仓库: [https://repo1.maven.org](https://repo1.maven.org)

镜像仓库: [https://maven.aliyun.com/mvn/guide](https://maven.aliyun.com/mvn/guide)

私有仓库: 需要在本地的`~/.m2/settings.xml`中配置好，使用方式和中央仓位没有任何区别

本地仓库: 不推荐使用

Maven支持模块化管理，可以把一个大项目拆成几个模块：
1. 可以通过继承在parent的pom.xml统一定义重复配置；
2. 可以通过<modules>编译多个模块。

### Spring

[https://start.spring.io](https://start.spring.io)

Spring是JavaEE的一个轻量级开发框架，主营IoC和AOP，集成JDBC、ORM、MVC等功能便于开发。

- IoC (Inversion of Control) 控制反转

IoC又称为依赖注入（DI：Dependency Injection），它解决了一个最主要的问题：将组件的创建+配置与组件的使用相分离，并且，由IoC容器负责管理组件的生命周期。

- AOP (Aspect Oriented Programming) 面向切面编程

### Spring Boot

Spring Boot是基于Spring，提供开箱即用的积木式组件，目的是提升开发效率。

- DAO层 包括XxxMapper.java(数据库访问接口类)，XxxMapper.xml(数据库链接实现)；（这个命名，有人喜欢用Dao命名，有人喜欢用Mapper，看个人习惯了吧）
- Bean层：也叫model层，模型层，entity层，实体层，就是数据库表的映射实体类，存放POJO对象；
- Service层：也叫服务层，业务层，包括XxxService.java(业务接口类)，XxxServiceImpl.java（业务实现类）；（可以在service文件夹下新建impl文件放业务实现类，也可以把业务实现类单独放一个文件夹下，更清晰）
- Web层：就是Controller层，实现与web前端的交互。

### Spring Cloud

Spring Cloud顾名思义是跟云相关的，云程序实际上就是指分布式应用程序，所以Spring Cloud就是为了让分布式应用程序编写更方便，更容易而提供的一组基础设施，它的核心是Spring框架，利用Spring Boot的自动配置，力图实现最简化的分布式应用程序开发。

- SpringCloud 为微服务架构开发涉及的 配置管理、服务治理、熔断机制、智能路由、微代理、控制总线、一次性token、全局一致性锁、leader选举、分布式session、集群状态管理 等操作提供了一种简单的开发方式
    - SpringCloud Config 配置管理工具，支持使用git存储配置内容，支持应用配置的外部化存储，支持客户端配置信息刷新，加解密配置内容等
    - SpringCloud Bus 事件、消息总线、用于在集群（例如，配置变化事件）中传播状态变化，可以与springcloud config联合实现热部署
    - SpringCloud Netflix 针对多种netflix组件提供的开发工具包，其中包括eureka、hystrix、zuul、archaius等
        - Netflix-Eureka 一个基于rest服务的服务治理组件，包括服务注册中心，服务注册与服务发现机制的实现，实现了云端负载均衡和中间层服务器的故障转移
        - Netflix-Hystrix 容错管理工具，实现断路器模式，通过控制服务的节点，从而对延迟和故障提供更强大的容错能力
        - Netflix-Ribbon 客户端负载均衡的服务调用组件
        - Netflix-Feign 基于ribbon和hystrix的声明式服务调用组件
        - Netflix-Zuul 微服务网关，提供动态路由，访问过滤等服务
        - Netflix-Archaius 配置管理API，包含一系列配置管理API，提供动态类型化属性、线程安全配置操作、轮询框架、回调机制等功能

### ORM

- Hibernate
- JPA
- MyBatis 

SpringBoot 整合数据库操作，目前主流使用的是 HikariCP 连接池和 Mybatis 持久层，同样的，starter 提供了简洁的整合方案

JDBC | Hibernate | JPA
--- | --- | ---
DataSource | SessionFactory | EntityManagerFactory
Connection | Session | EntityManager
