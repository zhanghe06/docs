# VMWare

[https://www.vmware.com/products/fusion/fusion-evaluation.html](https://www.vmware.com/products/fusion/fusion-evaluation.html)

TRY PRO FOR FREE

M芯片Mac只能安装 ARM 版的系统

激活方面
VMware Fusion 13.0 Player 面向个人用户是免费的，但需要用户向 VMware 申请个人版免费许可证。而面向商业用户则需要购买许可证。而且Player版本功能上比Pro版本少太多了，建议用户直接升级Pro版。

注：Pro 版则不存在免费版许可证的说法。

批量许可证激活密钥
经过测试， VMware Fusion 13.0 Pro 是可以使用批量许可证进行激活的，如下：

HF200-0W05K-089X8-4R1EK-032J0

## 安装 Windows 11 专业版

指定引导固件：UEFI

Partial Encryption -> Auto Generate Password

您的密码为: s2+c+mjjtRZe3fbN

当屏幕出现 Press any key to boot from CD or DVD...... 鼠标点击屏幕并快速敲击任意键

跳过网络连接 fn+shift(option)+F10 输入 OOBE\BYPASSNRO 回车

约3-4分钟的等待

这里虽然看起来快成功了，但是你会发现电脑是没有网络的，还有分辨率是没办法调整的

搜索power，以管理员身份运行，打开控制台

输入：
Set-ExecutionPolicy RemoteSigned
A
回车

菜单栏 虚拟机 -> 安装VMware Tools

DVD驱动器文件夹，从我的电脑进去，接下来以管理员身份运行 setup

安装完成，重启系统
