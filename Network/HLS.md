# HLS

- [http://nginx.org/en/docs/http/ngx_http_hls_module.html](http://nginx.org/en/docs/http/ngx_http_hls_module.html)
- [https://github.com/TareqAlqutami/rtmp-hls-server](https://github.com/TareqAlqutami/rtmp-hls-server)
- [https://github.com/arut/nginx-rtmp-module](https://github.com/arut/nginx-rtmp-module)
- [https://www.ffmpeg.org](https://www.ffmpeg.org)
- [视频流媒体播放](https://juejin.cn/post/7195100669911498811)
- [https://www.npmjs.com/package/hls.js](https://www.npmjs.com/package/hls.js)
- [https://juejin.cn/post/6960606591997444109](https://juejin.cn/post/6960606591997444109)
- [视频播放客户端 video.js](https://videojs.com)
- [视频播放客户端 hls.js](https://github.com/video-dev/hls.js)

HLS 协议（HTTP Live Streaming）
- ts 视频片段文件
- m3u8 格式列表文件


## FFmpeg

[https://ffmpeg.org](https://ffmpeg.org)

```
brew install ffmpeg

ffmpeg -h
ffprobe -h
```

```
网络协议： HTTP

封装格式： TS

编码格式： 视频编码格式 -> H.264 音频编码格式 -> MP3、AAC、AC-3

索引文件： M3U8
```

方案描述：

它的基本原理也是服务端把文件或媒体流按照不同的码率切分成一个个小片段进行传输。
客户端在播放码流时，可以根据自身的带宽及性能限制，在同一视频内容的不同码率的备用源中，选择合适码率的码流进行下载播放。
在传输会话开始时，客户端首先需要下载描述不同码流元数据的M3U8索引文件。

```
# 查看视频文件的元信息
ffmpeg -i VID_20231020_171028.mp4 -hide_banner

# 分片
ffmpeg -v verbose -i VID_20231020_171028.mp4  -vf scale=1920:1080 -c:a aac -c:v libx264  -hls_time 10 -hls_playlist_type vod -b:v 2000k -maxrate 2500k -bufsize 2000k -b:a 96k -hls_segment_filename 1920p_%03d.ts -f hls 1920p.m3u8

# 执行两次命令，比一次命令效率高
# 转换为ts文件
ffmpeg -i 4.mp4 -c copy -bsf:v h264_mp4toannexb 4.ts

# 将ts切片
ffmpeg -i 4.ts -c copy -map 0 -f segment -segment_time 10 -segment_list 4.m3u8 4_%05d.ts

```

```
--录制屏幕 推送 flv
ffmpeg -f gdigrab -i desktop -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -f flv rtmp://127.0.0.1:1985/myapp/ck
--录制屏幕 推送 hls
ffmpeg -f gdigrab -i desktop -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -f hls -hls_time 5.0 -hls_list_size 1 -hls_wrap 30  F:/ps/nginx-rtmp/html/hls/test.m3u8

```


server.py
```
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)
if __name__ == '__main__':
    BaseHTTPServer.test(CORSRequestHandler, BaseHTTPServer.HTTPServer)
```

```
python server.py 9000
```

直接使用会导致跨域：
```
python -m SimpleHTTPServer 9000
```

## FFprobe

提取音频元数据
```
ffprobe -v quiet -show_format -show_streams -print_format json "程响-可能.mp3"

ffprobe -show_streams 大欢-化风行万里.mp3
```

添加歌词
```
ffmpeg -i 大欢-化风行万里.mp3 -metadata lyrics-eng="[00:00.00]化风行万里-大欢" output.mp3
```

添加封面
```

```

添加
```
title 曲名
artist 歌手
album 专辑
```

播放音频
```
ffplay output.mp3
ffplay -i -vf subtitles=就是南方凯-离别开出花.lrc -i output.mp3 -x 800 -y 600
```

## 环境构建




## 后端服务



## 前端集成

创建基于h5的hls播放器hls.js

默认情况下，浏览器并不支持播放hls格式的视频，但是集成开源的hls库hls.js后，可以使用h5自带的video标签播放hls(即m3u8)视频。

```
<!DOCTYPE html>
<html>
<head></head>
<body>
  <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
  <video id="video"></video>
</body>

<script>
  var video = document.getElementById('video');
  var videoSrc = 'http://127.0.0.1:9000/1920p.m3u8';
  if (Hls.isSupported()) {
    var hls = new Hls();
    hls.loadSource(videoSrc);
    hls.attachMedia(video);
  }
  // hls.js is not supported on platforms that do not have Media Source
  // Extensions (MSE) enabled.
  //
  // When the browser has built-in HLS support (check using `canPlayType`),
  // we can provide an HLS manifest (i.e. .m3u8 URL) directly to the video
  // element through the `src` property. This is using the built-in support
  // of the plain video element, without using hls.js.
  //
  // Note: it would be more normal to wait on the 'canplay' event below however
  // on Safari (where you are most likely to find built-in HLS support) the
  // video.src URL must be on the user-driven white-list before a 'canplay'
  // event will be emitted; the last video event that can be reliably
  // listened-for when the URL is not on the white-list is 'loadedmetadata'.
  else if (video.canPlayType('application/vnd.apple.mpegurl')) {
    video.src = videoSrc;
  }
</script>

</html>
```

## 网络视频下载

以[https://cn.pornhub.com/view_video.php?viewkey=ph5f364cc4ed76b](https://cn.pornhub.com/view_video.php?viewkey=ph5f364cc4ed76b)为例


### m3u8
https://ev-h.phncdn.com/hls/videos/202008/14/342254971/,1080P_4000K,720P_4000K,480P_2000K,240P_400K,_342254971.mp4.urlset/master.m3u8?validfrom=1690217272&validto=1690224472&ipa=45.76.103.60&hdl=-1&hash=G94OliyGL4SrqvxKUWYG4HQwVxI%3D

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3081028,RESOLUTION=1920x1080,FRAME-RATE=30.000,CODECS="avc1.640028,mp4a.40.2"
index-f1-v1-a1.m3u8?validfrom=1690217272&validto=1690224472&ipa=45.76.103.60&hdl=-1&hash=G94OliyGL4SrqvxKUWYG4HQwVxI%3D
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1741531,RESOLUTION=1280x720,FRAME-RATE=30.000,CODECS="avc1.64001f,mp4a.40.2"
index-f2-v1-a1.m3u8?validfrom=1690217272&validto=1690224472&ipa=45.76.103.60&hdl=-1&hash=G94OliyGL4SrqvxKUWYG4HQwVxI%3D
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=953063,RESOLUTION=854x480,FRAME-RATE=30.000,CODECS="avc1.64001f,mp4a.40.2"
index-f3-v1-a1.m3u8?validfrom=1690217272&validto=1690224472&ipa=45.76.103.60&hdl=-1&hash=G94OliyGL4SrqvxKUWYG4HQwVxI%3D
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=463695,RESOLUTION=426x240,FRAME-RATE=30.000,CODECS="avc1.640015,mp4a.40.2"
index-f4-v1-a1.m3u8?validfrom=1690217272&validto=1690224472&ipa=45.76.103.60&hdl=-1&hash=G94OliyGL4SrqvxKUWYG4HQwVxI%3D
```

### ts

第一种：
https://ev-h.phncdn.com/hls/videos/202008/14/342254971/,1080P_4000K,720P_4000K,480P_2000K,240P_400K,_342254971.mp4.urlset/seg-1-f1-v1-a1.ts?validfrom=1690217272&validto=1690224472&ipa=45.76.103.60&hdl=-1&hash=G94OliyGL4SrqvxKUWYG4HQwVxI%3D

第二种：
https://cv-h.phncdn.com/hls/videos/202301/21/423809591/,1080P_4000K,720P_4000K,480P_2000K,240P_1000K,_423809591.mp4.urlset/seg-30-f1-v1-a1.ts?E5t_C98mEllxT8bFAIEUwNFYFcQR-ATxpcL2ga7ZK17HurXLN7PSc_R7VROEuTOWa7_w1YLZCt52gJlSKmJwn35l1z1S8W3W4LFA9-7hrg4f2-RLLP3iUvELspAz_l6ia4WAau_0hvDeqRXL0GXppXP2j-ZPb5VdYo6-EhmjEA8Q76y3mkUYHejD6ZW2qoA2jDrHtq14

### 编码规则

第一种：
https://ev-h.phncdn.com/hls/videos/202008/14/342254971/,1080P_4000K,720P_4000K,480P_2000K,240P_400K,_342254971.mp4.urlset/seg-1-f1-v1-a1.ts?validfrom=1690217272&validto=1690224472&ipa=45.76.103.60&hdl=-1&hash=G94OliyGL4SrqvxKUWYG4HQwVxI%3D

```
seg-xxx-f1-v1-a1.ts

1
10 - 19
2
20 - 29
3
31 - 39
...

10
101 - 119
...
24
241 - 249
```
编号有分组

第二种：
https://cv-h.phncdn.com/hls/videos/202301/21/423809591/,1080P_4000K,720P_4000K,480P_2000K,240P_1000K,_423809591.mp4.urlset/seg-30-f1-v1-a1.ts?E5t_C98mEllxT8bFAIEUwNFYFcQR-ATxpcL2ga7ZK17HurXLN7PSc_R7VROEuTOWa7_w1YLZCt52gJlSKmJwn35l1z1S8W3W4LFA9-7hrg4f2-RLLP3iUvELspAz_l6ia4WAau_0hvDeqRXL0GXppXP2j-ZPb5VdYo6-EhmjEA8Q76y3mkUYHejD6ZW2qoA2jDrHtq14

```
seg-xxx-f1-v1-a1.ts

1
2
3
...
10
11
12
...
```
编号整体有序

拖到视频最后，查看最后一个ts的编号

https://ev-h.phncdn.com/hls/videos/202008/14/342254971/,1080P_4000K,720P_4000K,480P_2000K,240P_400K,_342254971.mp4.urlset/seg-249-f1-v1-a1.ts?validfrom=1690217272&validto=1690224472&ipa=45.76.103.60&hdl=-1&hash=G94OliyGL4SrqvxKUWYG4HQwVxI%3D
https://cv-h.phncdn.com/hls/videos/202008/14/342254971/,1080P_4000K,720P_4000K,480P_2000K,240P_400K,_342254971.mp4.urlset/seg-8-f1-v1-a1.ts?pxuttgaSdXz8gLZTWncLBZ8mXRfDCuW91feyZSyw3CSrZzgTPkrszrm0rPaD9zSsaU6XndGFoxo7ovtNJcODxBgJojEe0I6AfwDef0IXV1elmmVBbOE8mLfCDKyAFYmmdGskb_cKheDpzVMT7wgJHRx0km6Wull9-_KDaNXvkl7WOg-iPYnkkepjrcYDK2qiC6qfyIaH

编号为249
