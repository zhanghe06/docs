# CAP

一个分布式系统无法同时满足三个条件：一致性、可用性、分区容忍性

- C:consistency 数据在多个副本中能保持一致的状态
- A:Availability 整个系统在任何时刻都能提供可用的服务
- P:Partition tolerance 分区容错性，在出现分区的情况下依然能提供服务

分布式一致性算法: Paxos、Raft、ZAB、Gossip

[https://zhuanlan.zhihu.com/p/130332285](https://zhuanlan.zhihu.com/p/130332285)


[raft动画](https://raft.github.io/)
