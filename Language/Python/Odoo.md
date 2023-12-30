# Odoo

[官方文档](https://www.odoo.com/documentation/16.0/zh_CN/)

[安装手册](https://www.odoo.com/documentation/16.0/zh_CN/administration/install/install.html)

[官方镜像](https://hub.docker.com/_/odoo/)

[在线演示](https://demo.odoo.com/)

[https://github.com/odoo/odoo.git](https://github.com/odoo/odoo.git)

[社区联盟 Odoo Community Association](https://github.com/OCA)

[开发指南](https://juejin.cn/post/7202211586676408379)

```
$ docker run -d -v odoo-db:/var/lib/postgresql/data -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name erp-db postgres:13
$ docker run -v odoo-data:/var/lib/odoo -v odoo-conf:/etc/odoo -v odoo-addons:/mnt/extra-addons -d -p 8069:8069 --name erp-web --link erp-db:db -t odoo:16.0

$ docker stop erp-web
$ docker start -a erp-web

# 创建模块
docker exec erp-web sh -c "ls -alh"
docker exec erp-web sh -c "odoo scaffold book_store ."
```

mkdir odoo_project

[http://localhost:8069](http://localhost:8069)
[http://localhost:8069/web/database/manager](http://localhost:8069/web/database/manager)

| 配置名称            | 配值                       |
| --------------- | ------------------------ |
| Master Password | 4j7q-td3g-iyug           |
| Database Name   | erp                      |
| Email           | zhang_he06@163.com       |
| Password        | 123456                   |
| Phone number    | 13818732593              |
| Language        | Chinese(Simplified)/简体中文 |
| Country         | China                    |
| Demo data       |                          |

## 开发环境搭建

```
git clone https://github.com/odoo/odoo.git -b 16.0 --depth=1
```

## 版本对照

- [Odoo社区版](https://github.com/odoo/odoo.git) （开源）
- [Odoo企业版](https://github.com/odoo/enterprise.git) （授权）

[https://www.odoo.com/zh_CN/page/editions](https://www.odoo.com/zh_CN/page/editions)

企业版源码下载，需要订阅支持客制化的企业版

https://aishu1.odoo.com/
