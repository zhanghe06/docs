# Helm

Helm的三大概念

- Chart: chart代表一个helm的包，这个包里会包含一切在k8s上运行某个应用、工具、服务所需要的资源定义。
- Repository: 资料库，就是在远端存chart的地方
- Release: 代表一个正运行在k8s上的chart实例，同一个chart可以有多个实例

常用命令

```
# 查看版本
helm version

# 创建工程
helm create demo

# 静态检查
helm lint ./demo

# 构建打包
helm package demo/

# 查看当前安装的charts
helm list | grep capp

# 新增仓库
helm repo list
helm repo add acr https://acr.aishu.cn/chartrepo/as

# 更新仓库（chart资源）
helm repo update
helm search capp # 模糊匹配

# 拉取离线文件
helm fetch acr/capp-model

# 查看模板
helm template capp-model-1.0.1.tgz

# 安装服务
helm install -n capp-model --namespace anyshare capp-model-1.0.1.tgz
或
tar -zxvf capp-model-1.0.1.tgz
helm install -n capp-model --namespace anyshare capp-model/

# 查看状态
helm status capp-model

# 查看内容
helm get manifest capp-model

# 回滚服务
helm hist capp-model
helm rollback capp-model 2

# 卸载服务
helm delete --purge capp-model
```

Helm v2 v3 的差异

```
Helm3 移除了Tiller，主要是为了解决多租户场景下的权限控制问题
v2中ServiceAccount拥有整个集群的权限
v3通过kubeconfig预设
```

| v2                 | v3              | 说明                      |
| ------------------ | --------------- | ----------------------- |
| helm serve         | 移除              | 临时搭建本地 Chart Repository |
| helm delete        | helm uninstall  | 旧版命令仍然可用                |
| helm inspect       | helm show       | 旧版命令仍然可用                |
| helm fetch         | helm pull       | 旧版命令仍然可用                |
| helm install -n 名称 | helm install 名称 | 旧版安装需要-n参数              |

