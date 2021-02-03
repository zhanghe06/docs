# 配额系统 (Quota System)

配额系统往往应用于计费项目

计费的边界：项目

## 表设计

### 配额配置（quota_conf）

字段名称 | 字段类型 | 示例
--- | --- | ---
配置编号 | 主键 | 1
资源类型 | 字符 | CPU
所属项目 | 字符 | 教育、工业
配额单位 | 字符 | 核心
配额总数 | 数值 | 4
预留总数 | 数值 | 1
消耗总数 | 数值 | 1

可用配额 = 配额总数 - 预留总数 - 消耗总数

### 预留明细（quota_reserved）

字段名称 | 字段类型 | 示例
--- | --- | ---
预留编号 | 主键 | 1
资源类型 | 字符 | CPU
预留项目 | 字符 | 教育
预留数量 | 数值 | 1
预留时间 | 时间 | 2019-01-01 00:00:00

需要定期清理预留记录，还原预留总数

### 消耗明细（quota_consumed）

字段名称 | 字段类型 | 示例
--- | --- | ---
消耗编号 | 主键 | 1
资源编号 | 数值 | 1
资源类型 | 字符 | CPU
分配项目 | 字符 | 教育
分配数量 | 数值 | 1

## 考虑因素

- 创建资源前置检查
- 删除资源配额回收

## 基本设计
1. 创建资源配额检查成功，新增预留
2. 创建资源配额检查失败，流程结束
3. 创建资源成功，扣除预留、新增消耗
4. 创建资源失败，扣除预留、消耗不变
5. 删除资源成功，扣除消耗
6. 删除资源失败，消耗不变

## 防御性设计

1. 删除资源，先删除资源，再操作配额
2. 如果创建资源时，新增消耗失败，后面删除资源扣除消耗数量不能小于零值，业务不需要报错
3. 定期对账