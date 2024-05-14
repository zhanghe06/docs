# Elasticsearch

[https://github.com/elastic/elasticsearch](https://github.com/elastic/elasticsearch)

[official Go client](https://github.com/elastic/go-elasticsearch)

## 排错

创建索引失败，没有分片成功，显示在Unassigned中

```
curl -X GET http://localhost:9200/_cluster/allocation/explain
```

```
{
    "note": "No shard was specified in the explain API request, so this response explains a randomly chosen unassigned shard. There may be other unassigned shards in this cluster which cannot be assigned for different reasons. It may not be possible to assign this shard until one of the other shards is assigned correctly. To explain the allocation of other shards (whether assigned or unassigned) you must specify the target shard in the request to this API.",
    "index": "face_index",
    "shard": 0,
    "primary": true,
    "current_state": "unassigned",
    "unassigned_info": {
        "reason": "INDEX_CREATED",
        "at": "2024-05-09T09:15:26.533Z",
        "last_allocation_status": "no"
    },
    "can_allocate": "no",
    "allocate_explanation": "Elasticsearch isn't allowed to allocate this shard to any of the nodes in the cluster. Choose a node to which you expect this shard to be allocated, find this node in the node-by-node explanation, and address the reasons which prevent Elasticsearch from allocating this shard there.",
    "node_allocation_decisions": [
        {
            "node_id": "Vyal4UyzTPayvHfJYOyArA",
            "node_name": "elasticsearch",
            "transport_address": "172.17.0.6:9300",
            "node_attributes": {
                "ml.allocated_processors": "14",
                "ml.max_jvm_size": "4110417920",
                "ml.allocated_processors_double": "14.0",
                "xpack.installed": "true",
                "ml.machine_memory": "8221278208"
            },
            "node_decision": "no",
            "weight_ranking": 1,
            "deciders": [
                {
                    "decider": "disk_threshold",
                    "decision": "NO",
                    "explanation": "the node is above the high watermark cluster setting [cluster.routing.allocation.disk.watermark.high=90%], having less than the minimum required [5.8gb] free space, actual free: [2.7gb], actual used: [95.2%]"
                }
            ]
        }
    ]
}
```

通过日志看出磁盘空间不足，Elasticsearch正常运行所需的最小可用空闲空间是5.8gb。

测试环境是MacOS，查看Docker配置，确实是空间不足，默认分配空间是64G，调高至128G，重启Docker，es容器启动之后自动完成分片
