# Apriori

```
from apyori import apriori
```

Apriori算法采用了迭代的方法

1. 先搜索出候选1项集及对应的支持度，剪枝去掉低于支持度的1项集，得到频繁1项集。
2. 对剩下的频繁1项集进行连接，得到候选的频繁2项集，筛选去掉低于支持度的候选频繁2项集，得到真正的频繁二项集，
3. 以此类推，迭代下去，直到无法找到频繁k+1项集为止，对应的频繁k项集的集合即为算法的输出结果


## 关联规则（Association Rules）

算法名称	| 算法描述
--- | ---
Apriori	| 关联规则最常用也是最经典的挖掘频繁项集的算法，<br>其核心思想是通过连续产生候选像及其支持度然后通过剪枝生成频繁项集
FT-Tree	| 针对Apriori算法固有的多次扫描事务数据集的缺陷，<br>提出的不产生候选频繁项集的方法
Eclat | 一种深度优先算法，采用垂直数据表示形式，<br>在概念格理论的基础上利用基于前缀的等价关系将搜索空间划分为较小的子空间
灰色关联法 | 分析和确定各因素之间的影响程度<br>或是若干子因素对主因素的贡献度而进行的一种分析方法
