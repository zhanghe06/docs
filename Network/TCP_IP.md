# TCP IP

TCP 建立连接：三次握手

1. client: syn
2. server: syn+ack
3. client: ack

TCP 断开连接：四次挥手

1. client: fin
2. server: ack
3. server: fin
4. client: ack

断开为什么要四次？

被动关闭的一端可能还在发送数据，没有想要关闭数据口的意思，所以FIN与ACK不是同时发送的，而是等到数据发送完了，才会发送FIN给另一端。
