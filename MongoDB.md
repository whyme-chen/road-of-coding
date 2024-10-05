# MongoDB
参考：
* [MongoDB](https://www.mongodb.com/)
* [MongoDB 教程](https://www.runoob.com/mongodb/mongodb-tutorial.html)

## 简介

1. 简介
   * MongoDB是一个开源、高性能、无模式的**文档型数据库**，是NoSQL数据库产品的一种。
   * 支持的数据结构非常松散，使用JSON风格的BSON格式来存储数据。
   * MongoDB的记录是一个文档，由字段和值对（filed：value）组成，类似于JSON对象，即一个文档认为就是一个对象。字段的数据类型是字符串，值除了基本类型外还可以包括其他文档、普通数组和文档数组。
2. 特点
   * 高性能
   * 高可用
   * 高扩展
   * 丰富的查询支持
3. 应用场景
   * MongoDB支持高效的查询、索引、和水平扩展，适用于需要处理大量数据和灵活结构的应用程序。
   * 价值较低，对事务性要求不高的应用程序数据。
4. 体系结构

## 环境部署

### 单机部署

1. 环境搭建步骤（windows）
   * 下载压缩包解压
   * 启动
     * 命令行中使用`mongod`命令
     * 配置文件
2. 使用方式
   * 命令行使用`mongo`命令
   * 使用图形化客户端
     * `MongoDB Compass`
     * `Navicate`
     * `DataGrip`

## 数据类型

## 基本操作

### 数据库操作
1. 连接数据库

   连接语法：
    * mongobd://：协议头
    * [username:password@]：（可选）认证信息，包括用户名和密码 
    * host1[:port1][,...hostN[:portN]]：服务器地址和端口，可以是一个或多个 MongoDB 服务器的地址和端口。 
    * /[defaultauthdb]：（可选）默认认证数据库。
    * [?options]：（可选）连接选项。
    ~~~shell
   `mongodb://[username:password@]host1[:port1][,...hostN[:portN]]][/[database][?options]]`
    ~~~

2. 创建数据库 
3. 删除数据库

### 集合操作
1. 创建集合 
2. 更新集合名 
3. 删除集合

### 文档操作

1. 插入文档
2. 更新文档
3. 删除文档
4. 查询文档

## SpringBoot集成MongoDB
参考：
* [SpringBoot集成MongoDB](https://blog.csdn.net/qq_46112274/article/details/117425532)

SpringBoot提供了MongoTemplate和MongoRepository两种方式访问MongoDB。
* MongoTemplate操作灵活
* MongoRepository操作简单

### 快速接入

1. 创建SpringBoot项目
2. 引入依赖
~~~xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-mongodb</artifactId>
    </dependency>
</dependencies>
~~~
2. 配置数据源
~~~yaml
spring:
  data:
    mongodb:
      # ip:port替换为对应的ip和端口
      uri: mongodb://rwuser:PNZxfClIS#LdUibcs6*QeahjT6Qr@ip:port/dev?authSource=admin
~~~
3. 创建实体类
4. 创建Repository 