# BlockChain

[https://github.com/pooler/cpuminer](https://github.com/pooler/cpuminer)

- 钱包地址 Coin Space
- 矿池 [Slush Pool](https://slushpool.com)


OpenCL（全称Open Computing Language，开放运算语言）是第一个面向异构系统通用目的并行编程的开放式、免费标准，也是一个统一的编程环境，
便于软件开发人员为高性能计算服务器、桌面计算系统、手持设备编写高效轻便的代码，
而且广泛适用于多核心处理器(CPU)、图形处理器(GPU)、Cell类型架构以及数字信号处理器(DSP)等其他并行处理器，
在游戏、娱乐、科研、医疗等各种领域都有广阔的发展前景。

在线钱包 https://blockchain.info/zh-cn/wallet/ 免费申请一个在线钱包


创建在线比特币钱包
```
转到coin.space
单击“创建新钱包”
单击“生成密码”
将密码保存在某个位置，您将在哪里再次找到该密码并对该密码进行多次备份
您必须同意，您已经写下或安全地存储了密码，并且必须同意条款和条件才能继续。
单击“设置PIN”
设置PIN以快速访问
您现在已经成功创建了比特币钱包！
```

进入矿池
```
注册Slushpool
打开配置文件设置（单击右上角的用户图标》单击“设置”）
单击“比特币”选项卡
单击在“ BTC付款”上
添加您的钱包地址（在Coin Space上，可以通过单击“接收”找到该地址）
```

安装矿工

```
安装依赖项
安装并配置矿工
启动矿工

```

```
# 下载挖矿工具cgminer
wget http://ck.kolivas.org/apps/cgminer/cgminer-2.4.2.tar.bz2
tar -jxvf cgminer-2.4.2-1.tar.bz2

# 安装依赖包
apt-get installbuild-essential libncurses5-dev libcurl4-openssl-dev

# 配置
cd cgminer
./configure --enable-cpumining --disable-opencl
# –enable-cpumining: 启用CPU挖掘
# –disable-opencl: 禁用OpenCL

# 编译安装
make
make install

# 连接挖矿
./cgminer
# 根据提示输入url、username、password
cgminer -o http://api.bitcoin.cz:8332 -u username -p password
```
