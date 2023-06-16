# Redis

## 基础

### Redis简介

#### NoSQL

1. SQL

2. NoSQL

3. SQL和NoSQL比较

   ![image-20230221102738202](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211027983.png)

#### Redis

redis中文网：https://www.redis.net.cn/

参考资料：

* https://blog.csdn.net/hellozpc/article/details/81267030

1. 简介：Redis诞生于2009年全称是Remote Dictionary Server,远程词典服务器，是一个基于内存的键值型NoSQL数据库。

2. 特征：

   * 键值(key-value)型，value支持多种不同数据结构,功能丰富
   * 单线程，每个命令具备原子性
   * 低延迟，速度快(基于内存、10多路复用、良好的编码)。
   * 支持数据持久化。
   * 支持主从集群、分片集群。
   * 支持多语言客户端

3. redis应用场景

   * 缓存
   * 任务队列
   * 消息队列
   * 分布式锁

4. 安装

5. 配置

6. Reids客户端

   * 命令行客户端
   * 图形化客户端

7. key的层级

   ![image-20230221150559429](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211506149.png)

### 数据类型

Redis是一个key-value的数据库， key- 般是String类型，不过value的类型多种多样。

1. 常见数据结构

   ![image-20230221112343749](D:\学习\road-of-coding\java study notes.assets\image-20230221112343749.png)

#### String类型

![image-20230221114914932](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211149092.png)

#### Hash类型

![image-20230221152905957](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211529302.png)

#### List类型

![image-20230221153504668](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211535191.png)

#### Set类型

![image-20230221154227216](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211542836.png)

#### SortedSet类型

![image-20230221183350312](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211833894.png)

### 常见命令

官方参考文档：https://redis.io/commands/

#### 通用命令

![image-20230221114644376](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211146926.png)

#### String类型的常见命令

![image-20230221134053867](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211340328.png)

#### Hash类型的常见命令

![image-20230221153343238](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211533319.png)

#### List类型的常见命令

![image-20230221153711995](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211537923.png)

#### Set类型的常见命令

![image-20230221154642114](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211546072.png)

#### SortedSet类型常见命令

![image-20230221183922957](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211839023.png)

### Redis的java客户端

redis的java客户端很多，官方推荐有三种：

1. Jedis：以Redi s命令作为方法名称，学习成本低，简单实用。但是Jedis实例是线程不安全的，多线程环境下需要基于连接池来使用
2. Lettuce：是基于Netty实现的，支持同步、异步和响应式编程方式，并且是线程安全的。支持Redis的哨兵模式、集群模式和管道模式。
3. Redisson：基于Redis实现的分布式、可伸缩的Java数据结构集合。包含了诸如Map. Queue、Lock、Semaphore、Atomi cLong等强大功能

spring对redis客户端进行了整合，提供了Spring Data Redis。

#### Jedis

1. 快速使用

   ![image-20230221194510804](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211945201.png)

2. jedis连接池

   ![image-20230221200923748](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302212009785.png)

#### SpringDataRedis

1. 简介

   ![image-20230221202228761](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302212022639.png)

2. 快速使用

   ![image-20230221202454506](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302212024218.png)