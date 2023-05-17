# Gorm

[https://github.com/go-gorm/gorm](https://github.com/go-gorm/gorm)

[GORM Guides](https://gorm.io)

[GORM Gen](https://github.com/go-gorm/gen#gormgen)

[乐观锁 Optimistic Lock](https://github.com/go-gorm/optimisticlock)

[GORM 2.0 发布说明](https://gorm.io/zh_CN/docs/v2_release_note.html)

关联设置：

    1 : N （例如：订单详情）
    N : N （例如：产品标签）

关联操作：

    创建
    更新
    删除

关系：

- Belongs To
  - `User` belongs to `Company`, `CompanyID` is the foreign key
- Has One
  - User has one CreditCard, CreditCardID is the foreign key
- Has Many
  - User has many CreditCards, UserID is the foreign key
- Many To Many
  - User has and belongs to many languages, `user_languages` is the join table


## 关联更新

先说问题：若想通过整体结构来更新全部数据，Gorm仅能更新关联关系，无法正确更新关联数据的其他字段，与其实现原理有关。

结合前端场景，来分析整体结构更新的适用场景：
1. 穿梭框，可以直接通过主键设置关联，适用
2. 嵌套表单，无法更新嵌套表单明细，不适用

目前关联更新对自增主键不太友好

推荐的流程：
```
子表更新（创建、更新）
关联关系更新（创建、更新、删除）
主表更新
```

示例
```
db.Model(&user.Car).Update("Year", 2020)
db.Model(&user).Updates(User{Name: "Tom"})
db.Model(&user).Updates(map[string]interface{}{"Name": "Tom"})
```

参考：https://github.com/go-gorm/gorm/issues/3487

## Gen Tool

[https://gorm.io/gen/gen_tool.html](https://gorm.io/gen/gen_tool.html)

```
# 安装工具
go install gorm.io/gen/tools/gentool@latest
# 进入项目目录执行
gentool -dsn "user:pwd@tcp(localhost:3306)/database?charset=utf8mb4&parseTime=True&loc=Local" -tables "orders,doctor"
```

gentool工具的安装依赖cgo，Windows环境，需要提前安装 [TDM-GCC](https://jmeubank.github.io/tdm-gcc/articles/2021-05/10.3.0-release) 并设置环境变量

## 滚动更新

滚动更新的兼容性考虑，基于 [GORM Auto Migration](https://gorm.io/docs/migration.html)

```
// SchemaTest 表结构变迁测试（基于GORM）
// 测试场景：
// 1、新增字段(非约束) 	完全兼容
// 2、新增字段(索引约束) 	不兼容（考虑历史数据，需要加入变迁逻辑）
// 3、删除字段(非约束) 	完全兼容，保留历史字段
// 4、删除字段(索引约束) 	部分兼容（需要同步清理索引）
// 5、修改名称 			完全兼容，保留历史字段
// 6、修改类型 			部分兼容（取决于历史数据能否支持类型转换），原字段修改

// 总结：
// 为了满足兼容性要求，需要做如下约束：
// 字段必须设置非空，并设置默认值，否则影响新增有约束的字段
// 删除有约束的字段，必须同步清理相应的索引，否则影响数据插入
// 新增存在约束字段，当有历史数据，需要拆分Schema变迁步骤（第一步：新增字段；第二步：处理历史数据；第三步：新增约束）否则新增字段失败

type SchemaTest struct {
	BaseModel
	//Code string `gorm:"index:udx_code,unique;column:code;type:varchar(6);default:'';not null;comment:'编码'" json:"code"`
	Name   string `gorm:"column:name;type:varchar(36);default:'';not null;comment:'名称'" json:"name"`
	//NameUpdate   string `gorm:"column:name_update;type:bigint(21) unsigned;default:0;not null;comment:'名称更新'" json:"name_update"`
	UserId uint64 `gorm:"column:user_id;type:bigint(21) unsigned;default:0;not null;comment:'用户ID'" json:"user_id"`
	User   User   `gorm:"constraint:on_update:cascade,on_delete:cascade;"`
}
```

## 秒杀活动

```
// RedPacket
// 创建红包
// 1、新增红包数据记录
// 2、设置缓存红包集合 Redis SAdd
// 3、设置缓存过期时间 Redis Expire (失效时间：1分钟)
type RedPacket struct {
	BaseModel
	Count  uint64 `gorm:"column:count;type:bigint(21) unsigned;default:0;not null;comment:'红包个数'" json:"count"`
	Amount uint64 `gorm:"column:amount;type:bigint(21) unsigned;default:0;not null;comment:'红包总额'" json:"amount"`
}

func (m *RedPacket) TableName() string {
	return "red_packet"
}

// UserRedPacket
// 抢夺红包
// 1、判断是否抢过红包 (防止同一用户抢到多个红包) Redis SETNX (失效时间：5分钟，需要大于红包集合过期时间)
// 2、弹出红包集合元素 (防止用户抢夺超出红包总数) Redis SPOP (红包已经派完；恭喜抢到红包)
// 3、新增红包抢夺记录 (联合唯一限制一人一个红包)
// 第1步和第3步虽然都是限制单人单个红包，但是缺一不可，第一步有分布式锁的作用，可以避免红包集合的元素被并发刷掉；第3步兜底
type UserRedPacket struct {
	BaseModel
	UserId      uint64    `gorm:"index:udx_user_red_packet,unique;column:user_id;type:bigint(21) unsigned;default:0;not null;comment:'用户ID'" json:"user_id"`
	User        User      `gorm:"constraint:on_update:cascade,on_delete:cascade;"`
	RedPacketId uint64    `gorm:"index:udx_user_red_packet,unique;column:red_packet_id;type:bigint(21) unsigned;default:0;not null;comment:'红包ID'" json:"red_packet_id"`
	RedPacket   RedPacket `gorm:"constraint:on_update:cascade,on_delete:cascade;"`
	Amount      uint64    `gorm:"column:amount;type:bigint(21) unsigned;default:0;not null;comment:'红包金额'" json:"amount"`
}

func (m *UserRedPacket) TableName() string {
	return "user_red_packet"
}
```
