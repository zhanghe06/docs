# OSI

OSI 7层

负载均衡分为L4 switch（四层交换），即在OSI第4层工作，就是TCP层啦。此种Load Balance不理解应用协议（如HTTP/FTP/MySQL等等）。例子：LVS，F5。

另一种叫做L7 switch（七层交换），OSI的最高层，应用层。此时，该Load Balancer能理解应用协议。例子： haproxy，MySQL Proxy。

- 7、应用层（HTTP）
- 6、表示层
- 5、会话层
- 4、传输层（TCP/UDP）
- 3、网络层（IP）
- 2、链路层
- 1、物理层
