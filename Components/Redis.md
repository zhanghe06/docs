# Redis

Redis 4.0 发生的最大变化
1. 加入了模块系统, 可以参考[Redis Labs 开发的模块](http://redismodules.com)
2. 新增了Memeory命令
3. ...

## 数据结构

- [String 字符串](https://www.runoob.com/redis/redis-strings.html)
  + 数据结构: 简单动态字符串（simple dynamic string,SDS）
  + 常用操作: get、set、del、incr、decr 等
  + 应用场景: 缓存、计数器、session
- [Hash 哈希](https://www.runoob.com/redis/redis-hashes.html)
  + 数据结构: 压缩列表（ziplist）；哈希表（hashtable）
  + 常用操作: hget、hset、hdel 等
  + 应用场景: 购物车、配置信息
- [List 列表](https://www.runoob.com/redis/redis-lists.html)
  + 数据结构: 压缩列表（ziplist）；双向链表（LinkedList）
  + 常用操作:
    + lpush+lpop=Stack（栈）
    + lpush+rpop=Queue（队列）
    + lpush+ltrim=Capped Collection（有限集合）
    + lpush+brpop=Message Queue（消息队列）
  + 应用场景: 时间轴
- [Set 集合](https://www.runoob.com/redis/redis-sets.html)
  + 数据结构: 整数集合（inset）；哈希表（hashtable）
  + 常用操作: sset、srem、scard、smembers、sismember
  + 应用场景: 标签、点赞、收藏
- [Sorted Set 有序集合](https://www.runoob.com/redis/redis-sorted-sets.html)
  + 数据结构: 压缩列表（ziplist）；跳跃表（skiplist）
  + 常用操作: zadd、zrange、zscore
  + 应用场景: 排行榜

[发布订阅](https://www.runoob.com/redis/redis-pub-sub.html) 消息通信模式


## 为什么快

- 完全基于内存

Redis是纯内存数据库，相对于读写磁盘，读写内存的速度就不是几倍几十倍了，一般，hash查找可以达到每秒百万次的数量级。

- 多路复用IO

"多路"指的是多个网络连接，"复用"指的是复用同一个线程。
采用多路 I/O 复用技术可以让单个线程高效的处理多个连接请求（尽量减少网络IO的时间消耗）。
可以直接理解为：单线程的原子操作，避免上下文切换的时间和性能消耗；加上对内存中数据的处理速度，很自然的提高redis的吞吐量。

## 极端业务场景

- 新闻应用中的热点新闻内容；
- 活动系统中某个用户疯狂参与的活动的活动配置；
- 商城秒杀系统中，最吸引用户眼球，性价比最高的商品信息；
- 论坛中的大型持久盖楼活动；
- 聊天室系统中热门聊天室的消息列表；


## 优化方向

- Hot Key 集群请求倾斜
    - 本地缓存（占用业务资源）
    - 分片打散（推荐，需要业务支持）
- Big Key 集群内存倾斜
    - 对 big key 存储的数据 （big value）进行拆分
        - big value 是个大 json: 使用 mget、mset 将内容打散（取 mget key1, key2 ... keyN；存 mset key1, key2 ... keyN）
        - big value 是个大 list: 变成value1，value2… valueN
- Die Key 死键
    - 已过期未清理
    - 没有业务使用
- 缓存雪崩
    - 坡度过期
- 缓存穿透
    - 缓存空数据
- keys 模糊匹配
    - 禁用keys，用set替代

非字符串的 BigKey, 不要使用del删除（会block实例）, 使用hscan、sscan、zscan等迭代方式渐进删除，同时注意防止BigKey过期时间自动删除问题


## 客户端

- **连接池**

默认情况下，每个redis实例都会维护自己的连接池

可以直接建立一个连接池，实例化对象的时候使用连接池作为参数，这样可以实现多个redis实例共享连接池


- **数据类型**

默认读取的是字节，如需字符串，需要设置`decode_responses=True`

```
import redis

redis_client = redis.Redis(host='localhost', port=6379,
                 db=0, password=None,
                 decode_responses=True)
```
