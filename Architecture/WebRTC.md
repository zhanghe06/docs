# WebRTC

音视频通信方案：

- 有中心，需要服务器转发媒体流
- 无中心，点对点，需要处理网络穿透

[WebRTC 协议介绍](https://developer.mozilla.org/zh-CN/docs/Web/API/WebRTC_API/Protocols)

[https://github.com/webrtc/adapter](https://github.com/webrtc/adapter)

[https://webrtc.github.io/adapter/adapter-latest.js](https://webrtc.github.io/adapter/adapter-latest.js)

[https://javascript.ruanyifeng.com/htmlapi/webrtc.html](https://javascript.ruanyifeng.com/htmlapi/webrtc.html)

```
mediaRecorder.ondataavailable = function(e) {
    console.log("视频流");
    ws.send(e.data);
};
```

**【直播数据流】**
```
主播（user_m）            观众（user_v_01）      观众（user_v_02）
websocket                   websocket             websocket
    -                         ^                       ^
    | emit stream             |                       |
    |                         | room a                | room a
app server                    |                       |
    |                         |                       |
    +---> broadcast stream ---+--->-------------------+
    |
    | write
    v
file system
```

**【回放数据流】**
```
观众（user_v_01）     观众（user_v_02）       观众（user_v_03）
   api                   api                     api
    ^                     ^                       ^
    |                     |                       |
    |                     |                       |
    +--->-----------------+--->-------------------+
    |
app server
    |
    | read
    -
file system
```

## 排错

当我们使用`getUserMedia`、`MediaRecorder`等API生成的webm视频时，会发现生成的webm在Chrome浏览器中是无法拖动进度条的

通过`ffprobe demo.webm`命令分析，发现`Duration`和`bitrate`的值都是`N/A`

这时需要通过`ffmpeg -i demo.webm -vcodec copy -acodec copy new-demo.webm`命令修复视频
