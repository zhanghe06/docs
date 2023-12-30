# MySQL


Uber宣布从Postgres切换到MySQL?


## 基础

操作 | 命令
--- | ---
查看表结构的详细信息 | DESC 表名;
修改表名 | ALTER TABLE 表名 RENAME TO 新的表名;
添加新列 | ALTER TABLE 表名 ADD COLUMN 列名 结构描述 \[AFTER 指定插入位置列名\];
删除旧列 | ALTER TABLE 表名 DROP COLUMN 列名;
修改列名 | ALTER TABLE 表名 CHANGE 旧列名 新列名 结构描述;
改列属性 | ALTER TABLE 表名 MODIFY 列名 新的结构描述;


## 常用操作
```
# 登陆 MySQL:
mysql -u root -p
# 查看系统已存在的数据库
show databases;
# 删除名为 test 的空数据库
drop database test;
drop database if exists test;
# 建立名为 test 的数据库
create database test;
# 创建数据库并且指定指定字符集
create database test default character set utf8;
# 建立对 test 数据库有完全操作权限的名为 admin 的用户
grant all privileges on test.* to admin@localhost identified by 'password';
# 取消 admin 用户对数据库的操作权限
revoke all privileges on *.* from admin@localhost;
# 删除 admin 用户
delete from mysql.user where user='admin' and host='localhost';
# 增加一个用户 www 密码为 abc，让他可以在任何主机上登录，并对所有数据库有查询、插入、修改、删除的权限。
grant select,insert,update,delete on *.* to www@"%" Identified by "abc";
# 刷新,使所做的改动生效
flush privileges;
```

mysql赋权操作：
```
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;

flush privileges;
GRANT：赋权命令
ALL PRIVILEGES：当前用户的所有权限
ON：介词
*.*：当前用户对所有数据库和表的相应操作权限
TO：介词
'root'@'%'：权限赋给root用户，所有ip都能连接
IDENTIFIED BY '123456'：连接时输入密码，密码为123456
WITH GRANT OPTION：允许级联赋权
```

备份 mysqldump
```
-t 不输出建表信息，即只输出表数据
-d 不输出数据信息，即只输出表结构
# 备份表结构和数据到本地
mysqldump -h[host] -P[port] -u[user] -p[passwd] [db] [table] [--where=" 1=1"] --skip-lock-tables > /tmp/table.sql
```

导入
```
mysql -h[host] -P[port] -u[user] -p[pass] [db] < /tmp/table.sql
```


## 数据表建立

```
DROP DATABASE IF EXISTS `test`;
CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET utf8 */;
use test;
```

```
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT '' COMMENT '姓名',
  `age` tinyint(2) DEFAULT '0' COMMENT '年龄',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';
```

```
CREATE TABLE `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT '' COMMENT '名称',
  `site` varchar(45) DEFAULT '' COMMENT '网站',
  `address` varchar(100) DEFAULT '' COMMENT '地址',
  `industry` varchar(45) DEFAULT '' COMMENT '行业',
  `email` varchar(45) DEFAULT '' COMMENT '邮箱',
  `phone` varchar(45) DEFAULT '' COMMENT '电话',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司表';
```

```
CREATE TABLE `position` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT '' COMMENT '名称',
  `city` varchar(45) DEFAULT '' COMMENT '地区',
  `address` varchar(100) DEFAULT '' COMMENT '地址',
  `industry` varchar(45) DEFAULT '' COMMENT '行业',
  `email` varchar(45) DEFAULT '' COMMENT '邮箱',
  `phone` varchar(45) DEFAULT '' COMMENT '电话',
  `description` varchar(500) DEFAULT '' COMMENT '描述',
  `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='职位表';
```

## 数据表删除（DROP）
```
DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `company`;
DROP TABLE IF EXISTS `position`;
```

## 数据表清除（TRUNCATE）
```
SET FOREIGN_KEY_CHECKS=0; # 禁用外键

TRUNCATE TABLE admininfo; # 清除数据

SET FOREIGN_KEY_CHECKS=1; # 启用外键
```
若存在foreign key关联，无法使用TRUNCATE，执行前需要禁用外键

## 忘记 MySQL 的 root 密码
```
# 如果 MySQL 正在运行，首先杀之
killall -TERM mysqld
# 启动 MySQL
PATH_TO_MYSQL/bin/mysqld --skip-grant-tables &
就可以不需要密码就进入 MySQL 了。
然后就是
mysql>use mysql
mysql>update user set password=password("new_pass") where user="root";
mysql>flush privileges;
重新杀 MySQL ，用正常方法启动 MySQL
一定注意：很多新手没有用password=password("...")，而是直接password="..."所以改掉密码不好使
```


## 高级功能

根据分隔符反转字符串
```
MariaDB [s2c]> select reverse(substring_index('aa,bb,cc,dd', ',', 4));
+-------------------------------------------------+
| reverse(substring_index('aa,bb,cc,dd', ',', 4)) |
+-------------------------------------------------+
| dd,cc,bb,aa                                     |
+-------------------------------------------------+
```

分离IP地址段
```
SET @ip = '222.71.21.51';

select ip,
CONVERT(SUBSTRING_INDEX(ip , '.', 1),UNSIGNED INTEGER),
CONVERT(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2),'.',-1),UNSIGNED INTEGER), 
CONVERT(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', -2),'.',1),UNSIGNED INTEGER),
CONVERT(SUBSTRING_INDEX(ip, '.', -1),UNSIGNED INTEGER);
+--------------+-------+--------+-------+--------+
| @ip          | first | second | third | fourth |
+--------------+-------+--------+-------+--------+
| 222.71.21.51 |   222 |     71 |    21 |     51 |
+--------------+-------+--------+-------+--------+
1 row in set (0.00 sec)
```

延时查询
```
select sleep(1);
```

按日，按周，按月分组统计数据
```
select DATE_FORMAT(create_time,'%Y%m%d') days,count(caseid) count from tc_case group by days;
select DATE_FORMAT(create_time,'%Y%u') weeks,count(caseid) count from tc_case group by weeks;
select DATE_FORMAT(create_time,'%Y%m') months,count(caseid) count from tc_case group by months;
```

查看数据库大小
```
-- 查看数据库占用空间（MB）
SELECT round((sum(DATA_LENGTH)+sum(INDEX_LENGTH))/1024/1024, 2) AS data FROM information_schema.TABLES where TABLE_SCHEMA='scrapy_news';

select concat(round(sum(DATA_LENGTH/1024/1024),2), 'MB') as data from information_schema.TABLES;
```

## 分支

- Percona Server
- MariaDB

## 与 PostgreSQL 对比

参考: https://database.51cto.com/art/202007/620924.htm

**开源协议**
1. PostgreSQL 基于自由的 BSD/MIT 许可，组织可以使用、复制、修改和重新分发代码，只需要提供一个版权声明即可。
2. MySQL 的开源协议是基于 GPL 协议，任何公司都可以免费使用，不允许修改后和衍生的代码做为闭源的商业软件发布和销售，MySQL 的版权在甲骨文手中，甲骨文可以推了其商业闭源版本。

**ACID 支持方面**
1. PostgreSQL 支持事务的强一致性，事务保证性好，完全支持 ACID 特性。
2. MySQL 只有 innodb 引擎支持事务，事务一致性保证上可根据实际需求调整，为了最大限度的保护数据，MySQL 可配置双一模式，对 ACID 的支持上比 PG 稍弱弱。

**SQL 标准的支持方面**
1. PostgreSQL 几乎支持所有的 SQL 标准，支持类型相当丰富。
2. MySQL 只支持部分 SQL 标准，相比于 PG 支持类型稍弱。

**复制**
1. PostgreSQL 可以做到同步，异步，半同步复制，以及基于日志逻辑复制，可以实现表级别的订阅和发布。
2. MySQL 的复制是基于 binlog 的逻辑异步复制，无法实现同步复制。

**并发控制**
1. PostgreSQL 通过其 MVCC 实现有效地解决了并发问题，从而实现了非常高的并发性。
2. MySQL 仅在 InnoDB 中支持 MVCC。InnoDB 的基于回滚段实现的 MVCC 机制，但是 MySQL 的间隙锁影响较大，锁定数据较多。

**性能**
PostgreSQL

**高可用技术的实现**
1. PostgreSQL
2. MySQL


## LOAD CSV (大数据量导入方案)

[LOAD DATA Statement](https://dev.mysql.com/doc/refman/8.0/en/load-data.html)

```
load data
    local -- 从客户端加载文件
    infile 'xxx/suppliers.csv'
    ignore -- 与唯一键重复的行将被忽略，默认指定 ignore，（可选项：replace 和 ignore）
    into table supplier
    character set utf8 -- 可选，避免中文乱码问题
    fields terminated by ',' -- 字段分隔符，每个字段(列)以什么字符分隔，默认是 \t
        optionally enclosed by '"' -- 文本限定符，每个字段被什么字符包围，默认是空字符
        escaped by '"' -- 转义符，默认是 \
lines terminated by '\n' -- 记录分隔符，如字段本身也含\n，那么应先去除，否则load data 会误将其视作另一行记录进行导入
ignore 1 lines -- 忽略首行表头
(supplier_name, category_level_1, category_level_2); -- 每一行文本按顺序对应的表字段，建议不要省略
```

## 两阶段提交

#### bin log 二进制日志、归档日志

场景：
- 主从复制
- 数据恢复

#### redo log 事务日志、重做日志

为了保证持久性，记录事务对数据页做了哪些修改

#### undo log 事务日志、撤销日志

为了保证原子性，主要记录了数据的逻辑变化

