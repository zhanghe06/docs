# 断线重连 (ReConnection) 

下面介绍几种常用组件的断线重连机制，需要注意的是：不同语言实现机制可能不同，而且不同的客户端支持断线重连的情况也不一样。

## MariaDB

- Golang

依赖模块
```
"github.com/jinzhu/gorm"
_ "github.com/jinzhu/gorm/dialects/mysql"

// Open initialize a new db connection, need to import driver first, e.g:
//
//     import _ "github.com/go-sql-driver/mysql"
//     func main() {
//       db, err := gorm.Open("mysql", "user:password@/dbname?charset=utf8&parseTime=True&loc=Local")
//     }
// GORM has wrapped some drivers, for easier to remember driver's import path, so you could import the mysql driver with
//    import _ "github.com/jinzhu/gorm/dialects/mysql"
//    // import _ "github.com/jinzhu/gorm/dialects/postgres"
//    // import _ "github.com/jinzhu/gorm/dialects/sqlite"
//    // import _ "github.com/jinzhu/gorm/dialects/mssql"
```

支持重连

实现方案

连接池
```
// 连接池配置
DbClient.DB().SetMaxOpenConns(viper.GetInt("mysql.max_open_conns"))                                    // 默认值0，无限制
DbClient.DB().SetMaxIdleConns(viper.GetInt("mysql.max_idle_conns"))                                    // 默认值2
DbClient.DB().SetConnMaxLifetime(time.Duration(viper.GetInt("mysql.conn_max_lifetime")) * time.Second) // 默认值0，永不过期
```

Golang客户端连接配置参考:

db_conf.yaml
```
mysql:
  user: "root"
  password: "123456"
  ip: "127.0.0.1"
  port: "3306"
  name: "gin_project"
  charset: "utf8mb4"
  max_open_conns: 50
  max_idle_conns: 10
  conn_max_lifetime: 500
```


- cli

支持重连

具体表现:
```
MariaDB [test_project]> select 1;
ERROR 2006 (HY000): MySQL server has gone away
No connection. Trying to reconnect...
Connection id:    8
Current database: test_project

+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.79 sec)
```


## Redis

- Golang

依赖模块
```
github.com/go-redis/redis/v8
```

支持重连

实现方案

Golang客户端通过重试策略解决了断线重连问题
```
// Examples:
//      redis://user:password@localhost:6789/3?dial_timeout=3&db=1&read_timeout=6s&max_retries=2
//      is equivalent to:
//      &Options{
//          Network:     "tcp",
//          Addr:        "localhost:6789",
//          DB:          1,               // path "/3" was overridden by "&db=1"
//          DialTimeout: 3 * time.Second, // no time unit = seconds
//          ReadTimeout: 6 * time.Second,
//          MaxRetries:  2,
//      }
```

核心配置是MaxRetries，默认重试3次:
```
// Default is 3 retries; -1 (not 0) disables retries.
MaxRetries int
```

- Python

依赖模块
```
import redis
```

支持重连

实现方案

连接异常，清空失效连接，再次执行send_command
```
class StrictRedis(object):
    ...
    def execute_command(self, *args, **options):
        "Execute a command and return a parsed response"
        pool = self.connection_pool
        command_name = args[0]
        connection = pool.get_connection(command_name, **options)
        try:
            connection.send_command(*args)
            return self.parse_response(connection, command_name, **options)
        except (ConnectionError, TimeoutError) as e:
            connection.disconnect()
            if not connection.retry_on_timeout and isinstance(e, TimeoutError):
                raise
            connection.send_command(*args)
            return self.parse_response(connection, command_name, **options)
        finally:
            pool.release(connection)
```

send_command 会判断当前连接是否存在，不存在则重新创建连接
```
class Connection(object):
    ...
    def send_command(self, *args):
        "Pack and send a command to the Redis server"
        self.send_packed_command(self.pack_command(*args))

    def send_packed_command(self, command):
        "Send an already packed command to the Redis server"
        if not self._sock:
            self.connect()
        ...
```

从源码分析可知：Python客户端采用重试策略解决断线重连问题

Python客户端连接配置参考:

redis_conf.yaml
```
redis:
  host: "127.0.0.1"
  port: 6379
  password: "123456"
  max_connections: 10
  socket_connect_timeout: 1
  retry_on_timeout: true
```

## NSQ

- Golang

依赖模块
```
"github.com/nsqio/go-nsq"
```

支持重连

实现方案
```
go r.rdyLoop()
```

## ETCD

- Golang

依赖模块
```
"go.etcd.io/etcd/clientv3"
```

支持重连

实现方案
```
go client.autoSync()
```
