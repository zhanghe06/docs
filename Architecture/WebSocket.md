# WebSocket

[https://github.com/websockets/ws](https://github.com/websockets/ws)

## 架构

## 应用场景

**扫码登录**

登录状态中的手机，对web端进行扫码授权，让web端同时获取登录态

```
{
    'room': None,
    'broadcast': False,
}
```

## 客户端

- Python客户端
  - [Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)
- Golang客户端：
  - [gorilla/websocket](https://github.com/gorilla/websocket)
  - [gobwas/ws](https://github.com/gobwas/ws)


参考：
- [如何在Go语言中使用Websockets：最佳工具与行动指南](https://tonybai.com/2019/09/28/how-to-build-websockets-in-go/)
- [Socket.IO 与 WebSocket：主要区别和使用方法](https://blog.p2hp.com/archives/10826)
- [Scaling Socket.IO - practical considerations](https://ably.com/topic/scaling-socketio)
- [Socket.IO Adapter](https://socket.io/docs/v4/adapter/)
- [用 Golang 实现百万级 Websocket 服务](https://learnku.com/articles/23560/using-golang-to-achieve-million-level-websocket-services)
- [请忘掉 Socket.io](https://maintao.com/2017/forget-socketio/)
- [可扩展的 WebSocket Server](https://maintao.com/2017/scalable-websocket-server/)
- [认真写一个 WebSocket Server](https://maintao.com/2017/write-a-websocket-server-seriously/)

其中《用 Golang 实现百万级 Websocket 服务》使用的就是`gobwas/ws`

## 框架整合

整合模板：
```
import (
    "net/http"
    "some/websocket"
)

http.HandleFunc("/ws", func(w http.ResponseWriter, r *http.Request) {
    conn, _ := websocket.Upgrade(r, w)
    //...
})
```

Gin + gobwas/ws

```
func Websocket(c *gin.Context) {
	conn, _, _, err := ws.UpgradeHTTP(c.Request, c.Writer)
	if err != nil {
		log.Println("连接失败：", err)
	}
	for {
		defer conn.Close()
		msg, op, err := wsutil.ReadClientData(conn)
		if err != nil {
			// handle error
		}
		fmt.Println("msg:", string(msg))
		err = wsutil.WriteServerMessage(conn, op, msg)
		if err != nil {
			// handle error
		}
	}
}

func main() {
	app := gin.Default()
	app.GET("/ws", Websocket)
	app.run()
}
```
