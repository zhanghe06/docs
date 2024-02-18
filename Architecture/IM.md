# 即时通讯 (IM)

参考：[https://developer.redis.com/howtos/chatapp/](https://developer.redis.com/howtos/chatapp/)

用户 (user)
```
# 创建用户
# 1、检查是否重复（响应结果：0-用户重复；1-创建成功）
SETNX user:name:{username} 0
# 2、生成用户编号
INCR user:count
# 3、设置用户编号
SET user:name:{username} {userId}

# 设置用户
HSET user:{userId} username {username} password {password}

# 查看用户
HGETALL user:{userId}

# 用户上线
SADD user:online {userId}

# 用户离线
SREM user:online {userId}

# 在线状态
SISMEMBER user:online {userId}

# 在线用户
SMEMBERS user:online

# 在线人数
SCARD user:online

# 用户总数
INCRBY user:count 0
```

房间 (room)
```
# 创建房间
INCR room:count

# 设置房间
HSET room:{roomId} name {roomName} note {roomNote} type {rootType(dialog|groups)}

# 关联房间
SADD user:{userId}:rooms {roomId}
# SADD user:1:rooms 1
# SADD user:2:rooms 1

# 场景一：临时对话
# 当用户1主动发起对话时，仅仅关联此用户的房间，不需要关联其他成员的房间；并将两人加入当前房间
# 当用户1执行发送消息时，遍历当前房间所有成员，并为其成员设置关联的房间；

# 场景二：群组消息
# 当用户1主动发起对话时，除了关联此用户的房间，还需要关联其他成员的房间；并将成员加入当前房间

# 房间列表
SMEMBERS user:{userId}:rooms

# 加入成员
ZADD room:{roomId}:users {timestamp} {userId}

# 移除成员
ZREM room:{roomId}:users {userId}

# 成员总数
ZCARD room:{roomId}:users

# 在线成员
SINTER room:{roomId}:users user:online

# 成员列表
ZREVRANGE room:{roomId}:users {offset_start} {offset_end}
```

消息 (message)
```
# 消息编号
INCR message:count

# 消息存储
HSET message:{messageId} time {timestamp} room {roomId} from {userId} data {message}
# HSET message:100 time 1615480369 room 1 from 1 data 'Hello'
# 消息存储的好处：
# 1、便于敏感内容过滤
# 2、支持存储方案变更

# 关联消息
ZADD room:{roomId}:messages {timestamp} {messageId}
# ZADD room:1:messages 1615480369 1

# 删除消息
# 1、完全删除
ZREM room:{roomId}:messages {messageId}
# 2、标记删除
ZADD room:{roomId}:messages 0 {messageId}

# 消息列表
ZREVRANGE room:{roomId}:messages {start} {stop}
# ZREVRANGE room:1:messages 0 50

# 过滤消息
ZRANGEBYSCORE room:{roomId}:messages {min} {max} WITHSCORES LIMIT {offset} {count}
# ZRANGEBYSCORE room:1:messages 1 +inf WITHSCORES LIMIT 0 10

# 消息总数
ZCARD room:{roomId}:messages
# ZCARD room:1:messages

# 新消息数
ZCOUNT room:{roomId}:messages {min} {max}
# ZCOUNT room:1:messages 1615480369 +inf
```

广播消息
```
PUBLISH message "{'serverId': 4132, 'type':'message', 'data': {'from': 1, 'date': 1615480369, 'message': 'Hello', 'roomId': '1'}}"
```
