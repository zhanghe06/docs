# 图片格式 (Picture Format)

- GIF (Graphics Interchange Format: 图形交换格式)
1、支持透明，可以任意形状，不再呈现矩形边框，原生支持动态图像  
2、不支持24bit彩色模式，最多存储256色  
3、版权归Compu Serve公司所有，Compu Serve通过免费发行格式说明书推广GIF，但要求使用GIF文件格式的软件要包含其版权信息的说明

- PNG
1、可以保存24位的真彩色图像，并且支持透明背景和消除锯齿边缘的功能，可以在不失真的情况下压缩保存图像  
2、在保存PNG格式的图像时，会弹出对话框，如果在对话框中选中（交错的）按钮，那么在使用浏览器欣赏该图片时就会以**由模糊逐渐转为清晰**的效果方式渐渐显示出来

- JPEG

1、JPEG不支持透明度

- TIFF

PNG规范中不包含嵌入式EXIF（可交换图像文件格式）图像数据的标准，比如数码像机拍得的图像。而TIFF，JPEG 2000, DNG都支持EXIF。

## Exif (Exchangeable image file format: 可交换图像文件格式)

是专门为数码相机的照片设定的，可以记录数码照片的属性信息和拍摄数据。

Python版本: [https://gitlab.com/TNThieding/exif](https://gitlab.com/TNThieding/exif)

[https://exif.readthedocs.io/en/latest/usage.html](https://exif.readthedocs.io/en/latest/usage.html)

JS版本: [https://github.com/exif-js/exif-js](https://github.com/exif-js/exif-js)

```
pip install exif
```
