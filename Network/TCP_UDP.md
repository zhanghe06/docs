# TCP UDP

TCP（transport control protocol，传输控制协议）是面向连接的，面向流的，提供高可靠性服务。

UDP（user datagram protocol，用户数据报协议）是无连接的，面向消息的，提供高效率服务。

TCP的协议数据不会丢，没有收完包，下次接收，会继续上次继续接收，己端总是在收到ack时才会清除缓冲区内容。数据是可靠的，但是会粘包。

TCP 是基于字节流的传输服务，无法区分边界，存在粘包问题

UDP 是基于消息的报文，是有边界的

TCP 与语言无关，只能处理字节流，不同语言需要实现自己的数据编码


TCP 粘包/分包的原因：
- 应用程序写入的字节大小大于套接字发送缓冲区的大小，会发生拆包现象。
- 而应用程序写入数据小于套接字缓冲区大小，网卡将应用多次写入的数据发送到网络上，这将会发生粘包现象；

解决方式：
- 消息定长
- 包尾增加特殊字符分割
- 将消息分为消息头和消息体

零拷贝：
