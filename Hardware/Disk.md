# Disk

查看文件系统及挂载点
```
zhanghe@ubuntu:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            974M     0  974M   0% /dev
tmpfs           199M   14M  185M   7% /run
/dev/sda1        18G  1.5G   16G   9% /
tmpfs           992M     0  992M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           992M     0  992M   0% /sys/fs/cgroup
tmpfs           199M     0  199M   0% /run/user/1000
```

查看块设备
```
zhanghe@ubuntu:~$ lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
fd0      2:0    1    4K  0 disk
sda      8:0    0   20G  0 disk
|-sda1   8:1    0   18G  0 part /
|-sda2   8:2    0    1K  0 part
`-sda5   8:5    0    2G  0 part [SWAP]
sr0     11:0    1 1024M  0 rom
sr1     11:1    1 1024M  0 rom
```

查看磁盘
```
# 查看磁盘
sudo fdisk -l | grep Disk
# 挂载磁盘
mount <磁盘> <挂载点>
# 卸载磁盘
umount <挂载点>
```

dd 命令模拟高密集 I/O 任务
```
dd if=/dev/sda of=/dev/null bs=1MB
```

iostat
```
# 需要安装
sudo apt install -y sysstat     # Ubuntu
yum install -y sysstat          # CentOS
```

## IO测试

```
apt install fio
```

随机读写（随机读写频繁的应用，如小文件存储(图片)、OLTP数据库、邮件服务器，关注随机读写性能，IOPS是关键衡量指标。）
```
fio -filename=/dev/md127 -allow_mounted_write=1 -direct=1 -iodepth 1 -thread -rw=randrw -ioengine=psync -bs=16k -size=200G -numjobs=10 -runtime=100 -group_reporting -name=raidtest
```

测试报告 - 随机读写
```
raidtest: (g=0): rw=randrw, bs=(R) 16.0KiB-16.0KiB, (W) 16.0KiB-16.0KiB, (T) 16.0KiB-16.0KiB, ioengine=psync, iodepth=1
...
fio-3.12
Starting 10 threads
Jobs: 10 (f=10): [m(10)][100.0%][r=656KiB/s,w=672KiB/s][r=41,w=42 IOPS][eta 00m:00s]
raidtest: (groupid=0, jobs=10): err= 0: pid=3404: Thu Oct 28 02:35:42 2021
  read: IOPS=45, BW=733KiB/s (750kB/s)(71.6MiB/100109msec)
    clat (msec): min=6, max=298, avg=76.48, stdev=43.23
     lat (msec): min=6, max=298, avg=76.49, stdev=43.23
    clat percentiles (msec):
     |  1.00th=[   10],  5.00th=[   14], 10.00th=[   18], 20.00th=[   34],
     | 30.00th=[   50], 40.00th=[   63], 50.00th=[   75], 60.00th=[   87],
     | 70.00th=[   99], 80.00th=[  115], 90.00th=[  136], 95.00th=[  153],
     | 99.00th=[  182], 99.50th=[  194], 99.90th=[  215], 99.95th=[  259],
     | 99.99th=[  300]
   bw (  KiB/s): min=   31, max=  192, per=10.47%, avg=76.67, stdev=33.81, samples=1908
   iops        : min=    1, max=   12, avg= 4.66, stdev= 2.15, samples=1908
  write: IOPS=47, BW=764KiB/s (783kB/s)(74.7MiB/100109msec); 0 zone resets
    clat (msec): min=2, max=323, avg=135.28, stdev=45.07
     lat (msec): min=2, max=323, avg=135.29, stdev=45.07
    clat percentiles (msec):
     |  1.00th=[   55],  5.00th=[   67], 10.00th=[   79], 20.00th=[   94],
     | 30.00th=[  110], 40.00th=[  122], 50.00th=[  133], 60.00th=[  144],
     | 70.00th=[  159], 80.00th=[  174], 90.00th=[  197], 95.00th=[  213],
     | 99.00th=[  251], 99.50th=[  262], 99.90th=[  300], 99.95th=[  317],
     | 99.99th=[  326]
   bw (  KiB/s): min=   31, max=  192, per=10.42%, avg=79.58, stdev=32.95, samples=1917
   iops        : min=    1, max=   12, avg= 4.84, stdev= 2.09, samples=1917
  lat (msec)   : 4=0.02%, 10=0.89%, 20=4.69%, 50=9.61%, 100=31.97%
  lat (msec)   : 250=52.28%, 500=0.54%
  cpu          : usr=0.07%, sys=0.63%, ctx=69522, majf=0, minf=0
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=4584,4782,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=733KiB/s (750kB/s), 733KiB/s-733KiB/s (750kB/s-750kB/s), io=71.6MiB (75.1MB), run=100109-100109msec
  WRITE: bw=764KiB/s (783kB/s), 764KiB/s-764KiB/s (783kB/s-783kB/s), io=74.7MiB (78.3MB), run=100109-100109msec

Disk stats (read/write):
    md127: ios=4608/4965, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=1679/4080, aggrmerge=214/31, aggrticks=36426/64877, aggrin_queue=99350, aggrutil=77.25%
  sda: ios=2563/4056, merge=215/34, ticks=60916/75372, in_queue=134876, util=74.66%
  sdb: ios=781/4047, merge=201/43, ticks=11932/54192, in_queue=64008, util=51.88%
  sdc: ios=2612/4112, merge=224/21, ticks=61956/77636, in_queue=137132, util=77.25%
  sdd: ios=761/4105, merge=217/28, ticks=10900/52308, in_queue=61384, util=51.27%
```

顺序读写（顺序读写频繁的应用，传输大量连续数据，如电视台的视频编辑，视频点播VOD(Video On Demand)，关注连续读写性能。数据吞吐量是关键衡量指标。）
```
fio -filename=/dev/md127 -allow_mounted_write=1 -direct=1 -iodepth 1 -thread -rw=rw -ioengine=psync -bs=16k -size=200G -numjobs=10 -runtime=100 -group_reporting -name=raidtest
```

测试报告 - 顺序读写
```
raidtest: (g=0): rw=rw, bs=(R) 16.0KiB-16.0KiB, (W) 16.0KiB-16.0KiB, (T) 16.0KiB-16.0KiB, ioengine=psync, iodepth=1
...
fio-3.12
Starting 10 threads
Jobs: 10 (f=10): [M(10)][100.0%][r=9177KiB/s,w=9657KiB/s][r=573,w=603 IOPS][eta 00m:00s]
raidtest: (groupid=0, jobs=10): err= 0: pid=4712: Thu Oct 28 02:49:02 2021
  read: IOPS=485, BW=7764KiB/s (7950kB/s)(759MiB/100054msec)
    clat (usec): min=161, max=247705, avg=9681.81, stdev=12474.25
     lat (usec): min=162, max=247707, avg=9685.02, stdev=12474.40
    clat percentiles (usec):
     |  1.00th=[   314],  5.00th=[   424], 10.00th=[   570], 20.00th=[  2376],
     | 30.00th=[  3261], 40.00th=[  3949], 50.00th=[  4752], 60.00th=[  6259],
     | 70.00th=[ 10683], 80.00th=[ 15533], 90.00th=[ 23725], 95.00th=[ 34341],
     | 99.00th=[ 56361], 99.50th=[ 64750], 99.90th=[115868], 99.95th=[126354],
     | 99.99th=[242222]
   bw (  KiB/s): min=   32, max= 1728, per=10.02%, avg=778.09, stdev=229.32, samples=1996
   iops        : min=    2, max=  108, avg=48.53, stdev=14.34, samples=1996
  write: IOPS=490, BW=7842KiB/s (8030kB/s)(766MiB/100054msec); 0 zone resets
    clat (usec): min=372, max=358485, avg=10675.23, stdev=14590.60
     lat (usec): min=376, max=358489, avg=10682.03, stdev=14590.49
    clat percentiles (usec):
     |  1.00th=[   652],  5.00th=[   979], 10.00th=[  1418], 20.00th=[  3064],
     | 30.00th=[  4015], 40.00th=[  4752], 50.00th=[  5669], 60.00th=[  7242],
     | 70.00th=[ 11076], 80.00th=[ 15795], 90.00th=[ 23987], 95.00th=[ 34866],
     | 99.00th=[ 64750], 99.50th=[ 83362], 99.90th=[145753], 99.95th=[223347],
     | 99.99th=[333448]
   bw (  KiB/s): min=   64, max= 1568, per=10.00%, avg=784.21, stdev=222.76, samples=2000
   iops        : min=    4, max=   98, avg=48.91, stdev=13.92, samples=2000
  lat (usec)   : 250=0.03%, 500=3.89%, 750=4.01%, 1000=2.80%
  lat (msec)   : 2=5.97%, 4=18.46%, 10=32.92%, 20=18.19%, 50=12.03%
  lat (msec)   : 100=1.49%, 250=0.21%, 500=0.01%
  cpu          : usr=0.35%, sys=3.96%, ctx=480326, majf=0, minf=0
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=48550,49038,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=7764KiB/s (7950kB/s), 7764KiB/s-7764KiB/s (7950kB/s-7950kB/s), io=759MiB (795MB), run=100054-100054msec
  WRITE: bw=7842KiB/s (8030kB/s), 7842KiB/s-7842KiB/s (8030kB/s-8030kB/s), io=766MiB (803MB), run=100054-100054msec

Disk stats (read/write):
    md127: ios=48500/50742, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=16018/26285, aggrmerge=121/1274, aggrticks=25930/35806, aggrin_queue=61566, aggrutil=39.41%
  sda: ios=23074/24427, merge=125/1145, ticks=31036/27048, in_queue=58056, util=31.99%
  sdb: ios=9052/28313, merge=126/1483, ticks=21000/43060, in_queue=63756, util=39.41%
  sdc: ios=23164/24253, merge=117/1070, ticks=31216/36056, in_queue=67232, util=35.08%
  sdd: ios=8782/28150, merge=116/1399, ticks=20468/37060, in_queue=57220, util=36.29%
```

## LVM (Logical Volume Manager) Linux磁盘逻辑卷管理器

LVM是在硬盘的硬盘分区上又创建一个逻辑层，以方便系统管理硬盘分区系统。

适合单机服务器，优势就是具有弹性，比如某个分区不够了或者太大了，可以无损的改变分区大小

LVM只是一种管理工具，称不上文件系统，并且不具备冗余性，基本上就有点像一个大容器，把所有的空间给合并起来。

- 物理存储介质（PhysicalStorageMedia）
指系统的物理存储设备：磁盘，如：/dev/hda、/dev/sda等，是存储系统最底层的存储单元。
- 物理卷（Physical Volume，PV）
指磁盘分区或从逻辑上与磁盘分区具有同样功能的设备（如RAID），是LVM的基本存储逻辑块，但和基本的物理存储介质（如分区、磁盘等）比较，却包含有与LVM相关的管理参数。
- 卷组（Volume Group，VG）
类似于非LVM系统中的物理磁盘，其由一个或多个物理卷PV组成。可以在卷组上创建一个或多个LV（逻辑卷）。
- 逻辑卷（Logical Volume，LV）
类似于非LVM系统中的磁盘分区，逻辑卷建立在卷组VG之上。在逻辑卷LV之上可以建立文件系统（比如/home或者/usr等）。
- 物理块（Physical Extent，PE）
PE是物理卷PV的基本划分单元，具有唯一编号的PE是可以被LVM寻址的最小单元。PE的大小是可配置的，默认为4MB。所以物理卷（PV）由大小等同的基本单元PE组成。
- 逻辑块（Logical Extent，LE）
逻辑卷LV也被划分为可被寻址的基本单位，称为LE。在同一个卷组中，LE的大小和PE是相同的，并且一一对应。

## RAID

区别：

LVM:灵活的管理磁盘的容量，有一定的冗余和性能功能，但很弱。

RAID:更侧重性能和数据安全。

硬RAID与软RAID

软RAID安全性不好，当有一块硬盘损坏时，它不能实现重建的功能，而且它的局限性也很在。
而硬RAID有硬盘丢失时，它可以实现重建，以及如果RAID卡损坏时，它可以通过更换RAID卡，实现不丢失数据的功能。

差异:
1、绑定操作系统：软件RAID通常特定于所使用的操作系统，因此通常不能用于操作系统之间共享的分区
2、磁盘故障恢复：硬件RAID很简单，只需将其插入并换上新磁盘即可；软件RAID须先告诉系统停止使用磁盘然后更换磁盘

RAID10

https://www.jianshu.com/p/f087257665d3?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation

RAID方案对比

方案 | 盘数 | 组织方式 | 容量 | 安全 | 速度 | 备注
--- | --- | --- | --- | --- | --- | ---
RAID0 | 4 | 条带式，不允许坏盘 | 4 | 最差 | 最快 | 适用: 最求极致性能，不重要的数据
RAID1 | 4 | 镜像式，允许坏2个盘 | 4 * 0.5 = 2 | 最高 | 一般 | 适用: 重要数据
RAID5 | 4 | 允许坏1个盘 | 4 -1 = 3 | 比较高 | 比较快 | 适用: 一般场景
RAID5 | 4 | 3+1模式，1个热备，允许坏1个盘 | 3 -1 = 2 | 比较高 | 写入性能不高 | 4块盘时，此方案没有RAID10的优势；热备盘实现故障恢复
RAID10 | 4 | 允许坏2个盘 | 4 * 0.5 = 2 | 最高 | 最快 | 适用: 银行、数据库


LVM + RAID 结合，待验证

方案一: 先对多个盘做 raid5，再用 raid 盘做 VG ，最后创建LV
方案二: 先对多个盘做 VG ，先创建 raid5 类型的 LV


四盘举例:

RAID1
```
                                +--+--+--+--+--+--+--+--+
                            +-->|A1|A2|A3|A4|A5|A6|A7|A8|
+--+--+--+--+--+--+--+--+   |   +--+--+--+--+--+--+--+--+
|A1|A2|A3|A4|A5|A6|A7|A8|-->|             Disk0
+--+--+--+--+--+--+--+--+   |   +--+--+--+--+--+--+--+--+
          RAID 1            +-->|A1|A2|A3|A4|A5|A6|A7|A8|
                                +--+--+--+--+--+--+--+--+
                                          Disk1
```

RAID0
```
                                +--+--+
                            +-->|A1|A5|
                            |   +--+--+
                            |    Disk0
                            |   +--+--+
                            +-->|A2|A6|
+--+--+--+--+--+--+--+--+   |   +--+--+
|A1|A2|A3|A4|A5|A6|A7|A8|-->|    Disk1
+--+--+--+--+--+--+--+--+   |   +--+--+
          RAID 0            +-->|A3|A7|
                            |   +--+--+
                            |    Disk2
                            |   +--+--+
                            +-->|A4|A8|
                                +--+--+
                                 Disk3
```

RAID10
```
                                +--+--+--+--+
                            +-->|A1|A3|A5|A7|
                            |   +--+--+--+--+
                            |       Disk0
                            |   +--+--+--+--+
                            +-->|A1|A3|A5|A7|
+--+--+--+--+--+--+--+--+   |   +--+--+--+--+
|A1|A2|A3|A4|A5|A6|A7|A8|-->|       Disk1|      
+--+--+--+--+--+--+--+--+   |   +--+--+--+--+
          RAID 10           +-->|A2|A4|A6|A8|
                            |   +--+--+--+--+
                            |       Disk2
                            |   +--+--+--+--+
                            +-->|A2|A4|A6|A8|
                                +--+--+--+--+
                                    Disk3
```

RAID5
```
                                +--+--+------+
                            +-->|A1|A4|B7->A7|
                            |   +--+--+------+
                            |       Disk0
                            |   +--+--+------+
                            +-->|A2|A5|Q3->P3|
+--+--+--+--+--+--+--+--+   |   +--+--+------+
|A1|A2|A3|A4|A5|A6|A7|A8|-- |       Disk1(P3=B7 XOR A7 XOR B8 XOR A8 XOR Q3)
+--+--+--+--+--+--+--+--+   |   +--+--+------+
          RAID 5            +-->|A3|P2|B8->A8|
                            |   +--+--+------+
                            |       Disk2(P2=A4 XOR A5 XOR A6)
                            |   +--+--+
                            +-->|P1|A6|
                                +--+--+
                                    Disk3(P1=A1 XOR A2 XOR A3)
```


## Btrfs vs Ext4

功能优劣对比: [Btrfs vs Ext4 - Functionalities, Strengths, and Weaknesses](https://linoxide.com/btrfs-vs-ext4/)

[mdadm+EXT4/XFS/BTRFS RAID 与 原生BTRFS+RAID 的对比](https://chiaforum.com/t/filesystem-performance-of-ext4-xfs-btrfs-raid-0/8866)
