# E-commerce

## 商品规格

参考:
-[教你如何设计电商系统商品模块-规格](https://zhuanlan.zhihu.com/p/348346305)

术语概念

- SPU：Standard Product Unit（标准化产品单元），一种商品，各种规格集合，如：iPhone 12；
- SKU：Stock Keeping Unit（库存量单位），也称单品，一种商品的具体规格，如：一部 黑色 128G 的iPhone 12 手机，黑色 + 128G 就是商品的具体规格。

商品模块比较复杂的地方在于商品参数、规格管理

表结构设计

- 分组 group
  - 名称
  - 排序
- 品类 category
  - 组名ID（group_id）
  - 名称
  - 排序
- 商品 production
  - 品类ID（category_id）
  - 名称
  - 单位
  - 轮播图（HasMany）
  - 视频
  - 上架状态
- 规格模板 spec_template
  - 品类ID（category_id）
  - 名称
  - 是否内置（系统内置、客户定制）
- 规格参数 spec_param
  - 模板ID（spec_template_id）
  - 名称
- 规格数值 spec_value
  - 参数ID（spec_param_id）
  - 数值
- 属性
  - 商品ID（production_id）
  - 参数配置（Json格式；）
- 商品规格 production_spec
  - 商品ID（production_id）
  - 规格参数配置 conf_spec_params
  - 规格数值配置 conf_spec_values
  - 名称
  - 图片
  - 成本
  - 售价
  - 库存
