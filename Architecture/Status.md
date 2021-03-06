# 状态系统 (Status System)

通常，我们与第三方系统进行交互式，往往会涉及状态的处理

系统异常，会导致状态同步不一致，需要一套有效的机制控制数据一致

## 通用状态
- pending 准备请求（本地）
- waiting 等待结果（本地）
- process 正在进行（远程）
- success 结果成功
- failure 结果失败

## 业务流程

创建、更新、删除

注意：用户请求，参数校验失败，不更新状态，做失败处理

### 同步流程

1、同步流程 - 业务处理

序号 | 业务动作 | 状态设置
:---: | --- | ---
1 | 参数校验 | -
2 | - | 准备
3 | 接口调用 | -
4 | 接口返回 | -
5 | - | 成功、失败


### 异步流程

1、异步流程 - 请求发起

序号 | 业务动作 | 状态设置
:---: | --- | ---
1 | 参数校验 | -
2 | - | 准备
3 | 接口调用 | -
4 | - | 等待

2、异步流程 - 接口处理

3、异步流程 - 结果处理

序号 | 业务动作 | 状态设置
:---: | --- | ---
1 | 结果查询 | -
2 | - | 成功、失败、进行

以上过程，调用接口这一步，即使是异步操作，依然存在阻塞，如果需要非阻塞，需要改造成[任务系统](Task.md)


## 异常处理

请求过程，经常出现下列异常情况：

1、参数校验成功，调用接口失败  
2、调用接口成功，状态设置失败

以上2种情况，状态没有设置，我们是不知道接口是否调用的，即使调用也不清楚调用是否成功。

## 并发冲突
