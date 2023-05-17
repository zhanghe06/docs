# MariaDB

## 与 MySQL 的兼容性

[https://mariadb.com/kb/en/mariadb-vs-mysql-compatibility](https://mariadb.com/kb/en/mariadb-vs-mysql-compatibility)

| MariaDB版本                              | MySQL版本   | 说明   |
| -------------------------------------- | --------- | ---- |
| MariaDB 10.2，MariaDB 10.3和MariaDB 10.4 | MySQL 5.7 | 有限替代 |
| MariaDB 10.0和MariaDB 10.1              | MySQL 5.6 | 有限替代 |
| MariaDB 5.5                            | MySQL 5.5 | 可以替代 |
| MariaDB 5.1，MariaDB 5.2和MariaDB 5.3    | MySQL 5.1 | 直接替代 |

MariaDB 10.2、MySQL 5.7 版本开始，支持JSON字段类型，但是实现方式不同；如果将MySQL迁移到MariaDB，JSON则被转换为TEXT

## 存储引擎

分类:

- InnoDB：frm是表定义文件，ibd是数据文件
- MyISAM：frm是表定义文件，myd是数据文件，myi是索引文件

介绍:

1. InnoDB支持事务，MyISAM不支持，对于InnoDB每一条SQL语言都默认封装成事务，自动提交，这样会影响速度，所以最好把多条SQL语言放在begin和commit之间，组成一个事务；
2. InnoDB支持外键，而MyISAM不支持。对一个包含外键的InnoDB表转为MYISAM会失败；
3. InnoDB是聚集索引，使用B+Tree作为索引结构，数据文件是和（主键）索引绑在一起的（表数据文件本身就是按B+Tree组织的一个索引结构），必须要有主键，通过主键索引效率很高。但是辅助索引需要两次查询，先查询到主键，然后再通过主键查询到数据。因此，主键不应该过大，因为主键太大，其他索引也都会很大。
4. InnoDB不保存表的具体行数，执行select count(*) from table时需要全表扫描。而MyISAM用一个变量保存了整个表的行数，执行上述语句时只需要读出该变量即可，速度很快（注意不能加有任何WHERE条件）；
5. Innodb不支持全文索引，而MyISAM支持全文索引，在涉及全文索引领域的查询效率上MyISAM速度更快高；PS：5.7以后的InnoDB支持全文索引了
6. MyISAM表格可以被压缩后进行查询操作
7. InnoDB支持表、行(默认)级锁，而MyISAM支持表级锁
8. InnoDB表必须有唯一索引（如主键）（用户没有指定的话会自己找/生产一个隐藏列Row_id来充当默认主键），而Myisam可以没有
9. Innodb存储文件有frm、ibd，而Myisam是frm、MYD、MYI

如何选择:

1. 是否要支持事务，如果要请选择innodb，如果不需要可以考虑MyISAM；
2. 如果表中绝大多数都只是读查询，可以考虑MyISAM，如果既有读也有写，请使用InnoDB。
3. 系统崩溃后，MyISAM恢复起来更困难，能否接受；
4. MySQL5.5版本开始Innodb已经成为Mysql的默认引擎(之前是MyISAM)，说明其优势是有目共睹的，如果你不知道用什么，那就用InnoDB，至少不会差。

Q: InnoDB为什么推荐使用自增ID作为主键？  
A: 自增ID可以保证每次插入时B+索引是从右边扩展的，可以避免B+树和频繁合并和分裂（对比使用UUID）。如果使用字符串主键和随机主键，会使得数据随机插入，效率比较差。

Q: In到底走不走索引？
A: in通常是走索引的，当in后面的数据过大时，会走全表扫描，即不走索引，因此in走不走索引和后面的数据有关系。其它范围查询同理，进行范围查询时，比如：>、< 、>=、<=等, 如果数据量过大的话，即使where条件字段已经建立了索引，查询语句执行时还是有可能进行全表扫描的

innodb引擎的4大特性:

- 插入缓冲（insert buffer)
- 二次写(double write)
- 自适应哈希索引(ahi)
- 预读(read ahead)

应该创建索引的列:

- 在经常需要搜索的列上，可以加快搜索的速度
- 在作为主键的列上，强制该列的唯一性和组织表中数据的排列结构
- 在经常用在连接（JOIN）的列上，这些列主要是一外键，可以加快连接的速度
- 在经常需要根据范围（<，<=，=，>，>=，BETWEEN，IN）进行搜索的列上创建索引，因为索引已经排序，其指定的范围是连续的
- 在经常需要排序（order by）的列上创建索引，因为索引已经排序，这样查询可以利用索引的排序，加快排序查询时间；
- 在经常使用在WHERE子句中的列上面创建索引，加快条件的判断速度。

## 索引

树
查找树
平衡查找树
多叉平衡查找树

Mysql 索引底层数据结构选型
哈希表（Hash）

## 事务

一般来说，事务是必须满足4个条件（ACID）:
1. 原子性（Atomicity，或称不可分割性）
2. 一致性（Consistency）
3. 隔离性（Isolation，又称独立性）
4. 持久性（Durability）

描述:
- **原子性**：一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。
- **一致性**：在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。
- **隔离性**：数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。
- **持久性**：事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。

## 隔离级别

| 级别                     | 并发性 | 一致性 | 副作用              |
| ---------------------- | --- | --- | ---------------- |
| 读未提交（Read uncommitted） | 最高  | 最低  | 脏读（可能读取到不一致的数据）  |
| 读已提交（Read committed）   | 低   | 高   | 不可重复读            |
| 可重复读（Repeatable read）  | 高   | 高   | 幻读（Phantom Read） |
| 串行化（Serializable ）     | 最低  | 最高  | 效率低              |

MySQL 默认的为Repeatable read (可重复读)   
Oracle 默认的为 Read committed（读已提交）

- 脏读
  指一个事务在处理数据的过程中，读取到另一个为提交事务的数据。

- 不可重复读
  指对于数据库中的某个数据，一个事务范围内的多次查询却返回了不同的结果，这是由于在查询过程中，数据被另外一个事务修改并提交了

- 幻读
  一个事务(同一个read view)在前后两次查询同一范围的时候，后一次查询看到了前一次查询没有看到的行。幻读专指读到新插入的行  
  幻读和不可重复读都是读取了另一条已经提交的事务（这点就脏读不同），所不同的是不可重复读查询的都是同一个数据项，而幻读针对的是一批数据整体（比如数据的个数）。

总的来说，解决不可重复读的方法是**锁行**，解决幻读的方式是**锁表**。

## 测试 “幻读”（phantom read）

因高并发场景下, 会出现同一时刻交叉多个事务的情况, 接下来通过2个例子的模拟, 观察一下对数据库及业务产生的影响

准备测试数据表

```
MariaDB [flask_restful]> DROP TABLE IF EXISTS `t_products`;
CREATE TABLE `t_products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) NOT NULL DEFAULT '' COMMENT 'product name',
  `num` INT NOT NULL DEFAULT '0' COMMENT 'stock num',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='stock table';
MariaDB [flask_restful]> select @@global.tx_isolation, @@tx_isolation;
+-----------------------+-----------------+
| @@global.tx_isolation | @@tx_isolation  |
+-----------------------+-----------------+
| REPEATABLE-READ       | REPEATABLE-READ |
+-----------------------+-----------------+
```

InnoDB事务的隔离级别有四级，默认是“可重复读”（REPEATABLE READ）

1. 插入库存（不存在则插入）

模拟多个用户同时创建产品

```
T Session A                                     Session B
|
| START TRANSACTION;                            START TRANSACTION;
|
| SELECT * FROM t_products WHERE name='a';
| empty set
|                                               INSERT INTO t_products (`name`, `num`) VALUES ('a', 5);
|
| SELECT * FROM t_products;                     SELECT * FROM t_products WHERE name='a';
| empty set                                     +----+------+-----+
|                                               | id | name | num |
|                                               +----+------+-----+
|                                               |  1 | a    |   5 |
|                                               +----+------+-----+
|
|                                               COMMIT;
|
| SELECT * FROM t_products WHERE name='a';
| empty set
|
| INSERT INTO t_products (`name`, `num`) VALUES ('a', 5);
| ERROR 1062 (23000): Duplicate entry 'a' for key 'uk_name'
-
```

虽然因幻读导致数据库级别插入异常, 但是异常回滚不会影响业务


2. 抢购秒杀（库存存在则扣除库存数量）

假定库存为1

```
MariaDB [flask_restful]> UPDATE t_products SET num=1;
```

模拟2个用户同时抢购

```
T Session A                                         Session B
|
| START TRANSACTION;                                START TRANSACTION;
|
| SELECT num FROM t_products WHERE id=1;            SELECT num FROM t_products WHERE id=1;
| +-----+                                           +-----+
| | num |                                           | num |
| +-----+                                           +-----+
| |   1 |                                           |   1 |
| +-----+                                           +-----+
|
| UPDATE t_products SET num=num-1 WHERE id=1 and num>0;
|
| SELECT num FROM t_products WHERE id=1;            SELECT num FROM t_products WHERE id=1;
| +-----+                                           +-----+
| | num |                                           | num |
| +-----+                                           +-----+
| |   0 |                                           |   1 |
| +-----+                                           +-----+
|
| COMMIT;
|
|                                                   SELECT num FROM t_products WHERE id=1;
|                                                   +-----+
|                                                   | num |
|                                                   +-----+
|                                                   |   1 |
|                                                   +-----+
|
|                                                   UPDATE t_products SET num=num-1 WHERE id=1 and num>0;
|
|                                                   SELECT num FROM t_products WHERE id=1;
|                                                   +-----+
|                                                   | num |
|                                                   +-----+
|                                                   |  -1 |
|                                                   +-----+
|
|                                                   COMMIT;
|
-
```

因幻读, 并没有导致数据库更新异常, 但是出现了库存超卖的现象, 即业务层面的异常

如何避免, 通过悲观锁（FOR UPDATE）方式处理:

```
MariaDB [flask_restful]> UPDATE t_products SET num=1;

T Session A                                         Session B
|
| START TRANSACTION;                                START TRANSACTION;
|
| SELECT num FROM t_products WHERE id=1 FOR UPDATE;
| +-----+
| | num |
| +-----+
| |   1 |
| +-----+
|
|                                                   SELECT num FROM t_products WHERE id=1 FOR UPDATE;
|                                                   等待...直到超时, 当其他事物提交返回更新后的结果
|
| UPDATE t_products SET num=num-1 WHERE id=1 and num>0;
|
| SELECT num FROM t_products WHERE id=1;
| +-----+
| | num |
| +-----+
| |   0 |
| +-----+
|
| COMMIT;
|
|                                                   +-----+
|                                                   | num |
|                                                   +-----+
|                                                   |   0 |
|                                                   +-----+
|
|                                                   UPDATE t_products SET num=num-1 WHERE id=1 and num>0;
|
|                                                   SELECT num FROM t_products WHERE id=1;
|                                                   +-----+
|                                                   | num |
|                                                   +-----+
|                                                   |   0 |
|                                                   +-----+
|
|                                                   COMMIT;
|
-
```

通过悲观锁的方式, 可以防止高并发场景下的超卖现象

如果指定主键, 为行级别锁, 否则为表级别锁

## Flask + Sqlalchemy 测试

1. 默认不加锁

代码示例:

```
inventory_obj = db.session.query(Inventory).filter(Inventory.id == inventory_id)
import time
time.sleep(2)
if inventory_obj.one().stock_qty >= num:
time.sleep(2)
data = {
'stock_qty': Inventory.stock_qty - num
}
inventory_obj.update(data)
db.session.commit()
return True
```

出现超卖现象

2. 加悲观锁/排它锁（with_for_update）

代码示例:

```
inventory_obj = db.session.query(Inventory).filter(Inventory.id == inventory_id)
import time
time.sleep(2)
if inventory_obj.with_for_update().one().stock_qty >= num:
time.sleep(2)
data = {
'stock_qty': Inventory.stock_qty - num
}
inventory_obj.update(data)
db.session.commit()
return True
```

一切正常, 没有超卖, 会阻塞其它事务, 性能较差

需要注意的是`for update`要放到`mysql`的事务中，即`begin`和`commit`之间，否者不起作用。

3. 乐观锁

通过版本机制实现乐观锁

```mysql
update table set x=x+1, version=version+1 where id=#{id} and version=#{version};
```

4. 分布式锁

很多时候，我们需要对某一个共享变量进行多线程/多进程同步访问

为了确保分布式锁可用，我们至少要确保锁的实现同时满足以下四个条件：

```
互斥性。在任意时刻，只有一个客户端能持有锁。
不会发生死锁。即使有一个客户端在持有锁的期间崩溃而没有主动解锁，也能保证后续其他客户端能加锁。
具有容错性。只要大部分的Redis节点正常运行，客户端就可以加锁和解锁。
解铃还须系铃人。加锁和解锁必须是同一个客户端，客户端自己不能把别人加的锁给解了。
```

- Redis 方案

```
127.0.0.1:6379> SETNX lock_key request_id
(integer) 1
127.0.0.1:6379> SETNX lock_key 2018
(integer) 0
127.0.0.1:6379> TTL lock_key
(integer) -1
127.0.0.1:6379> EXPIRE lock_key 10
(integer) 1
127.0.0.1:6379> TTL lock_key
(integer) 9
127.0.0.1:6379> DEL lock_key
(integer) 1
127.0.0.1:6379> DEL lock_key
(integer) 0
127.0.0.1:6379> TTL lock_key
(integer) -2
```

| 锁操作名称 | redis操作 |
| ----- | ------- |
| 获取锁   | SETNX   |
| 释放锁   | DEL     |
| 防死锁   | EXPIRE  |

以上方案看起来不错，有两个问题:

1. `SETNX`与`EXPIRE`是2个命令，不是原子的，如果中间崩溃，将会死锁
2. 先拿到锁的事务，如果事务处理时间超过锁过期时间，会出现锁被抢占

改进：

| 锁操作名称 | redis操作                   |
| ----- | ------------------------- |
| 获取锁   | SET(NX, EX) 将2个操作变成一个原子操作 |
| 释放锁   | DEL                       |

- Etcd 方案

TODO

## 死锁

说到锁, 必然要考虑死锁的情况

应避免非主键条件的更新操作

## OLTP 和 OLAP

- OLTP On-Line Transaction Processing 联机事务处理
- OLAP On-Line Analytical Processing 联机分析处理

已有的两个主流开源数据库，MySQL和PostgreSQL都是针对OLTP环境的，在OLAP在线分析需求下它们的性能明显不足。

## ETL

ETL，Extraction-Transformation-Loading的缩写，即数据抽取（Extract）、转换（Transform）、装载（Load）的过程，它是构建数据仓库的重要环节。

## Innodb事务锁相关的三个表：`INNODB_TRX`、`INNODB_LOCKS`、`INNODB_LOCK_WAITS`

`INNODB_TRX`表主要是包含了正在InnoDB引擎中执行的所有事务的信息，包括`waiting for a lock`和`running`的事务

```mysql
SELECT * FROM information_schema.INNODB_TRX\G
```

`INNODB_LOCKS`表主要包含了InnoDB事务锁的具体情况，包括事务正在申请加的锁和事务加上的锁。

```mysql
SELECT * FROM information_schema.INNODB_LOCKS\G
```

`INNODB_LOCK_WAITS`表包含了`blocked`的事务的锁等待的状态

```mysql
SELECT * FROM information_schema.INNODB_LOCK_WAITS\G
```

## 缓存

```
MariaDB [None]> show variables like '%query_cache%';
+------------------------------+----------+
| Variable_name                | Value    |
+------------------------------+----------+
| have_query_cache             | YES      |
| query_cache_limit            | 131072   |
| query_cache_min_res_unit     | 4096     |
| query_cache_size             | 67108864 |
| query_cache_strip_comments   | OFF      |
| query_cache_type             | ON       |
| query_cache_wlock_invalidate | OFF      |
+------------------------------+----------+
7 rows in set (0.00 sec)
```

- mysql 有查询缓存, 调试时需要关闭查询缓存

```mysql
EXPLAIN SELECT * FROM `table_name` WHERE field_name="test";
  SELECT SQL_NO_CACHE * FROM `table_name` WHERE field_name="test";
```

- postgres 没有查询缓存, 使用的是系统缓存`/proc/sys/vm/drop_caches`

```bash
sync; sudo service postgresql stop; echo 1 > /proc/sys/vm/drop_caches; sudo service postgresql start
```

```postgresql
EXPLAIN (buffers, analyze, verbose) SELECT * FROM table_name WHERE field_name="test";
```

postgres 打开计时

```
table_name=# \timing
```

## 索引

1、联合索引，最左原则：建了一个(a,b,c)的复合索引，那么实际等于建了(a),(a,b),(a,b,c)三个索引
2、索引类型，查询条件值类型必须与定义一致，特别注意数值类型和字符类型

## 排错

### sqlalchemy.exc.OperationalError

OperationalError: (_mysql_exceptions.OperationalError) (2006, 'MySQL server has gone away')

MySQL 提前回收了空闲连接，与连接池配置没有协调好，一般长时间闲置之后的第一次连接会出现这种错误。

检查配置

```
MariaDB [flask_project]> show global variables like "%timeout%";
+-----------------------------+----------+
| Variable_name               | Value    |
+-----------------------------+----------+
| connect_timeout             | 5        |
| deadlock_timeout_long       | 50000000 |
| deadlock_timeout_short      | 10000    |
| delayed_insert_timeout      | 300      |
| innodb_flush_log_at_timeout | 1        |
| innodb_lock_wait_timeout    | 50       |
| innodb_rollback_on_timeout  | OFF      |
| interactive_timeout         | 28800    |
| lock_wait_timeout           | 31536000 |
| net_read_timeout            | 30       |
| net_write_timeout           | 60       |
| slave_net_timeout           | 3600     |
| thread_pool_idle_timeout    | 60       |
| wait_timeout                | 600      |
+-----------------------------+----------+
14 rows in set (0.00 sec)
```

查看连接情况

```
MariaDB [flask_project]> show full processlist;
+-----+------+------------------+---------------+---------+------+-------+------------------+----------+
| Id  | User | Host             | db            | Command | Time | State | Info             | Progress |
+-----+------+------------------+---------------+---------+------+-------+------------------+----------+
| 176 | root | 172.17.0.5:46672 | flask_project | Query   |    0 | init  | show processlist |    0.000 |
| 180 | root | 172.17.0.1:39592 | flask_project | Sleep   |  284 |       | NULL             |    0.000 |
+-----+------+------------------+---------------+---------+------+-------+------------------+----------+
2 rows in set (0.00 sec)
```

查看当前打开的连接的数量

```
MariaDB [flask_project]> show status like '%Threads_connected%';
+-------------------+-------+
| Variable_name     | Value |
+-------------------+-------+
| Threads_connected | 2     |
+-------------------+-------+
1 row in set (0.01 sec)
```

修改连接超时时间（测试）

```
MariaDB [flask_project]> set global wait_timeout=6;
```

```
MariaDB [flask_project]> show global variables like 'wait_timeout';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| wait_timeout  | 600   |
+---------------+-------+
1 row in set (0.00 sec)
MariaDB [flask_project]> show variables like 'wait_timeout';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| wait_timeout  | 28800 |
+---------------+-------+
1 row in set (0.00 sec)
MariaDB [flask_project]> show global status like 'uptime';
+---------------+--------+
| Variable_name | Value  |
+---------------+--------+
| Uptime        | 204519 |
+---------------+--------+
1 row in set (0.00 sec)

MariaDB [flask_project]> show global variables like 'max_allowed_packet';
+--------------------+----------+
| Variable_name      | Value    |
+--------------------+----------+
| max_allowed_packet | 16777216 |
+--------------------+----------+
1 row in set (0.00 sec)
```

错误重现:

当有事务没有提交或者没有回滚时，sqlalchemy 的连接回收时间（SQLALCHEMY_POOL_RECYCLE）大于数据库关闭等待连接时间（global wait_timeout）；

一旦数据库连接超时自动断开，此时 sqlalchemy 尝试连接数据库，会出现 OperationalError: (_mysql_exceptions.OperationalError) (2006, 'MySQL server has gone away')

处理方案:

1. sqlalchemy 的超时时间 小于 数据库的超时时间
2. 代码操作数据库，立即提交事务，错误回滚

官方说明:

http://flask-sqlalchemy.pocoo.org/2.2/config/#timeouts

### MySQLdb._exceptions.OperationalError

(MySQLdb._exceptions.OperationalError) (2013, 'Lost connection to MySQL server during query')

```
MariaDB [bearing_project]> SHOW GLOBAL VARIABLES LIKE 'wait_timeout';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| wait_timeout  | 600   |
+---------------+-------+
1 row in set (0.00 sec)

MariaDB [bearing_project]> SET GLOBAL wait_timeout=5;
Query OK, 0 rows affected (0.00 sec)
```

错误重现:

当事务处理时间过长，超过`wait_timeout`时间，会出现(MySQLdb._exceptions.OperationalError) (2013, 'Lost connection to MySQL server during query')

### sqlalchemy.exc.InvalidRequestError

StatementError: (sqlalchemy.exc.InvalidRequestError) Can't reconnect until invalid transaction is rolled back

一旦出现前面2种情况，再次请求,`sqlalchemy`会报错

### InnoDB: Cannot allocate memory for the buffer pool

内存不足导致错误

```
# free -m
              total        used        free      shared  buff/cache   available
Mem:           1838        1549          70           0         217         118
Swap:             0           0           0
```

```
MariaDB [bearing_project]> show global variables like 'innodb_buffer_pool_size';
+-------------------------+-----------+
| Variable_name           | Value     |
+-------------------------+-----------+
| innodb_buffer_pool_size | 268435456 |
+-------------------------+-----------+
1 row in set (0.00 sec)
```

### Specified key was too long; max key length is 767 bytes

MySQL在大字段上创建索引时，偶尔会遇到如下错误。

```
Specified key was too long; max key length is 767 bytes
```

例如安装 django-celery 后配置数据库时报错

```
django.db.utils.OperationalError: (1071, 'Specified key was too long; max key length is 767 bytes')
```

问题原因

由于MySQL的InnoDB引擎表索引字段长度的限制为767字节，因此对于多字节字符集的大字段或者多字段组合，创建索引时会出现该问题。

```
说明：以utf8mb4字符集字符串类型字段为例。
utf8mb4是4字节字符集，默认支持的索引字段最大长度是191字符（767字节/4字节每字符≈191字符），因此在varchar(255)或char(255)类型字段上创建索引会失败。
详情请参见[MySQL官网文档](https://dev.mysql.com/doc/refman/5.6/en/charset-unicode-utf8mb4.html?spm=a2c4g.11186623.2.14.4c247177s7YQCS)。
```

解决方案

`SET GLOBAL innodb_large_prefix = ON;`

```
MariaDB [school_project]> SHOW GLOBAL VARIABLES LIKE 'innodb_large_prefix';
+---------------------+-------+
| Variable_name       | Value |
+---------------------+-------+
| innodb_large_prefix | OFF   |
+---------------------+-------+
1 row in set (0.004 sec)

MariaDB [school_project]> SET GLOBAL innodb_large_prefix = ON;
Query OK, 0 rows affected (0.004 sec)
```

### Index column size too large. The maximum column size is 767 bytes.

报错主要出在mysql5.6版本和MariaDB10，改参数什么就不好使了，最直接的就是修改CHARACTER和COLLATE，将utf8mb4改为utf8

`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci`

### \[Warning\] 'proxies_priv' entry '@% root@mariadb' ignored in --skip-name-resolve mode.

数据库未正常退出的情况下，意外关机、强行重启服务器，导致数据库服务重启后不正常

修改`/etc/mysql/my.cnf`，注释掉`skip-name-resolve`，重启数据库服务，再开启`skip-name-resolve`，再重启服务就好了

```
root@mariadb:/# mysql -h 127.0.0.1 -u root -p
Enter password:
MariaDB [(none)]> use mysql;
MariaDB [mysql]> delete from mysql.proxies_priv where Host='mariadb';
```

### Lost connection to MySQL server at 'reading initial communication packet'

### ERROR 2003 (HY000): Can't connect to MySQL server on '172.17.0.2' (111 "Connection refused")

### Error 1615: Prepared statement needs to be re-prepared

项目中使用了视图表，使用过程中，报了`Error 1615`

```
MariaDB [(none)]> show global status like 'open%tables%';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| Open_tables   | 12    |
| Opened_tables | 10671 |
+---------------+-------+
2 rows in set (0.005 sec)
```

Opened_tables数值非常大，说明cache太小，导致要频繁地open table，可以查看下当前的table_open_cache设置：

```
MariaDB [(none)]> show variables like '%table_open_cache%';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| table_open_cache | 400   |
+------------------+-------+
1 row in set (0.017 sec)
```

参考：[官方文档](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html)

```
MariaDB [(none)]> set global table_open_cache=524288;
Query OK, 0 rows affected (0.011 sec)

MariaDB [(none)]> set global table_definition_cache=524288;
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]>
MariaDB [(none)]> show variables like '%table_open_cache%';
+------------------+--------+
| Variable_name    | Value  |
+------------------+--------+
| table_open_cache | 524288 |
+------------------+--------+
1 row in set (0.002 sec)
```

### Too many open files


## 调优

- 超时时间只对非活动状态的connection进行计算。
- 超时时间只以session级别的wait_timeout 为超时依据，global级别只决定session初始化时的超时默认值。
- 交互式连接的wait_timeout 继承于global的interactive_timeout。非交互式连接的wait_timeout继承于global的wait_timeout
- 继承关系和超时对 TCP/IP 和 Socket 连接均有效果

查看当前连接数

```
MariaDB [bearing_project]> show status like 'Threads%';
+-------------------+-------+
| Variable_name     | Value |
+-------------------+-------+
| Threads_cached    | 8     |
| Threads_connected | 1     |
| Threads_created   | 9     |
| Threads_running   | 1     |
+-------------------+-------+
4 rows in set (0.00 sec)
```

最大连接数

```
MariaDB [bearing_project]> show variables like '%max_connections%';
+-----------------------+-------+
| Variable_name         | Value |
+-----------------------+-------+
| extra_max_connections | 1     |
| max_connections       | 100   |
+-----------------------+-------+
2 rows in set (0.00 sec)
```

修改

```
set global max_connections = 1000;
```

## sqlalchemy 最佳实践

根据业务场景：

- 网页应用
  处理时间短，并发量高，逻辑（事务）处理快，每次数据操作，可通过连接池复用，短期之内连接不会回收

- 任务脚本
  处理时间长，并发量低，逻辑（事务）处理慢，每次数据操作，最好开启独立连接，防止历史连接会被回收
  避免事务耗时过长，控制单个连接处理时间

## 查询页大小

InnoDB存储引擎中有页（Page）的概念，页是其磁盘管理的最小单位。InnoDB存储引擎中默认每个页的大小为16KB

```
MariaDB [bearing_project]> show variables like 'innodb_page_size';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| innodb_page_size | 16384 |
+------------------+-------+
1 row in set (0.01 sec)
```

## sql_mode

```
MariaDB [(none)]> select @@GLOBAL.sql_mode;
+--------------------------------------------+
| @@GLOBAL.sql_mode                          |
+--------------------------------------------+
| NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+--------------------------------------------+
1 row in set (0.002 sec)
MariaDB [(none)]> select @@SESSION.sql_mode;
+--------------------------------------------+
| @@SESSION.sql_mode                         |
+--------------------------------------------+
| NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+--------------------------------------------+
1 row in set (0.004 sec)
```

## SQL优化

1. 使用limit对查询结果的记录进行限定
2. 避免select *，将需要查找的字段列出来
3. 使用连接(join)来代替子查询
4. 拆分大的delete或insert语句
5. 可通过开启慢查询日志来找出较慢的SQL
6. 不做列运算：SELECT id WHERE age + 1 = 10，任何对列的操作都将导致表扫描，它包括数据库教程函数、计算表达式等等，查询时要尽可能将操作移至等号右边
7. sql语句尽可能简单：一条sql只能在一个cpu运算;大语句拆小语句，减少锁时间；一条大sql可以堵死整个库
8. OR改写成IN：OR的效率是n级别，IN的效率是log(n)级别，in的个数建议控制在200以内
9. 不用函数和触发器，在应用程序实现
10. 避免%xxx式查询
11. 少用JOIN
12. 使用同类型进行比较，比如用'123'和'123'比，123和123比，否则全表扫描
13. 尽量避免在WHERE子句中使用!=或<>操作符，否则将引擎放弃使用索引而进行全表扫描
14. 对于连续数值，使用BETWEEN不用IN：SELECT id FROM t WHERE num BETWEEN 1 AND 5
15. 列表数据不要拿全表，要使用LIMIT来分页，每页数量也不要太大
16. 多条件排序，order by a,b,c 最左前缀匹配，注意联合索引顺序

## 概念

1. 数据查询语言（DQL: Data Query Language）
   语法：
   
   ```
   SELECT <字段名> FROM <表或视图名> WHERE <查询条件>;
   ```

2. 数据操纵语言（DML: Data Manipulation Language）
   语法：
   
   ```
   INSERT INTO <表名>(列1,列2,...) VALUES (值1,值2,...);
   UPDATE <表名> SET <列名>=新值 WHERE <列名>=某值;
   DELETE FROM <表名> WHERE <列名>=某值;
   ```

3. 事务处理语言（TPL: Transaction Processing Language）
   语法：
   
   ```
   BEGIN TRANSACTION、COMMIT和ROLLBACK
   ```

4. 数据控制语言（DCL: Data Control Language）
   语法：
   
   ```
   GRANT、DENY和REVOKE，确定单个用户或用户组对数据库对象的访问权限
   ```

5. 数据定义语言（DDL: Data Definition Language）
   
   ```
   CREATE、ALTER、DROP和TRUNCATE，用于在数据库中创建新表、更新表或删除表，以及为表加入索引等
   ```

6. 指针控制语言（CCL: Cursor Control Language）
   
   ```
   DECLARE CURSOR、FETCH INTO和UPDATE WHERE CURRENT用于对一个或多个表单独行的操作
   ```

## 集群

MariaDB集群是 Galera Cluster
MySQL集群是 Percona XtraDB Cluter（PXC）

[https://blog.csdn.net/qq_39122146/article/details/104070832](https://blog.csdn.net/qq_39122146/article/details/104070832)

复制容器数据库配置文件

```
docker cp mariadb-node02:/etc/mysql /opt/mariadb/conf
```

[https://zhuanlan.zhihu.com/p/346698374](https://zhuanlan.zhihu.com/p/346698374)

## 分库分表

阿里巴巴《Java 开发手册》提出单表行数超过 500 万行或者单表容量超过 2GB，才推荐进行分库分表。
如果预计三年后的数据量根本达不到这个级别，请不要在创建表时就分库分表。

引申出一个问题，为什么按这个标准设计，依据是什么？
思考一下，InnoDB一棵B+树可以存放多少行数据？
简单回答是：约2千万
