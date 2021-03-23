# 技术文档

在线文档: [https://zhanghe06.github.io/docs/](https://zhanghe06.github.io/docs/)

{% chart %}
{
    "chart": {
        "type": "bar"
    },
    "title": {
        "text": "开发语言流行度 (Programming Language Rating)"
    },
    "xAxis": {
        "title": {
            "text": "开发语言 (Language)"
        },
        "categories": ["C", "Java", "Python", "C++", "C#", "JavaScript", "PHP", "Go"]
    },
    "yAxis": {
        "title": {
            "text": "流行度 (Rating)"
        },
        "labels": {
            "format": "{value}%"
        }
    },
    "series": [{
        "name": "2020年",
        "data": [15.77, 16.89, 9.71, 5.57, 5.35, 2.45, 2.40, 0.90]
    }, {
        "name": "2021年",
        "data": [17.38, 11.96, 11.72, 7.56, 3.95, 2.20, 1.99, 1.41]
    }],
    "tooltip": {
        "pointFormat": "{series.name}: {point.y}%"
    }
}
{% endchart %}


* [云服务 (Cloud Server)](Cloud/README.md)
    * [Aliyun](Cloud/Aliyun.md)
    * [Tencent](Cloud/Tencent.md)
    * [Vultr](Cloud/Vultr.md)
* [组件 (Components)](Components/README.md)
    * [Keepalived](Components/Keepalived.md)
    * [MariaDB](Components/MariaDB.md)
    * [MongoDB](Components/MongoDB.md)
    * [MSSqlServer](Components/MSSqlServer.md)
    * [MySQL](Components/MySQL.md)
    * [PostgreSQL](Components/PostgreSQL.md)
    * [RabbitMQ](Components/RabbitMQ.md)
    * [Redis](Components/Redis.md)
    * [Sqlite](Components/Sqlite.md)
* [算法 (Algorithm)](Algorithm/README.md)
    * [快速排序 (QuickSort)](Algorithm/QuickSort.md)
    * [归并排序 (MergeSort)](Algorithm/MergeSort.md)
    * [先验算法 (Apriori)](Algorithm/Apriori.md)
    * [协同过滤 (RecsysCF)](Algorithm/RecsysCF.md)
    * [素数应用 (Prime)](Algorithm/Prime.md)
* [架构 (Architecture)](Architecture/README.md)
    * [缓存系统 (Cache System)](Architecture/Cache.md)
    * [集群系统 (Cluster System)](Architecture/Cluster.md)
    * [数据模型 (Data Model)](Architecture/DataModel.md)
    * [幂等设计 (Idempotent)](Architecture/Idempotent.md)
    * [消息队列 (Message Queue)](Architecture/MessageQueue.md)
    * [微服务 (Micro Service)](Architecture/MicroService.md)
    * [迁移系统 (Migration System)](Architecture/Migration.md)
    * [监控系统 (Monitoring System)](Architecture/Monitoring.md)
    * [多任务系统 (Multi Task)](Architecture/MultiTask.md)
    * [通知系统 (Notification System)](Architecture/Notification.md)
    * [并行并发 (Parallel Concurrence)](Architecture/ParallelConcurrence.md)
    * [处理模型 (Process Model)](Architecture/ProcessModel.md)
    * [生产消费 (Producer Consumer)](Architecture/ProducerConsumer.md)
    * [配额系统 (Quota System)](Architecture/Quota.md)
    * [状态系统 (Status System)](Architecture/Status.md)
    * [任务系统 (Task System)](Architecture/Task.md)
* [信息安全 (Security)](Security/README.md)
    * [CC攻击 (CC Attack)](Security/CCAttack.md)
    * [点击劫持 (Click Jacking)](Security/ClickJacking.md)
    * [DDoS攻击 (DDoS Attack)](Security/DDoSAttack.md)
    * [永恒之蓝 (Eternalblue)](Security/Eternalblue.md)
    * [重放攻击 (Replay Attack)](Security/ReplayAttack.md)
    * [慢速攻击 (Slow Attack)](Security/SlowAttack.md)
    * [Sql注入 (Sql Injection)](Security/SqlInjection.md)
* [网络 (Network)](Network/README.md)
    * [ShadowSocks](Network/ShadowSocks.md)
    * [Tcpdump](Network/Tcpdump.md)
* [前端 (FrontEnd)](FrontEnd/README.md)
    * [色彩 (Color)](FrontEnd/Color.md)
    * [层叠样式 (CSS)](FrontEnd/CSS.md)
* [深度学习 (Deep Learning)](DeepLearning/README.md)
    * [语音识别 (ASR)](DeepLearning/ASR.md)
    * [语音合成 (TTS)](DeepLearning/TTS.md)
    * [文本识别 (OCR)](DeepLearning/OCR.md)
* [GitBook操作指南](GitBook.md)
