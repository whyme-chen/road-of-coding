#  Redis

学习参考：

* https://www.bilibili.com/video/BV1cr4y1671t/?p=1&vd_source=fabefd3fabfadb9324761989b55c26ea
* https://www.bilibili.com/video/BV13R4y1v7sP?spm_id_from=333.788.player.switch&vd_source=fabefd3fabfadb9324761989b55c26ea&p=19

## 基础

### Redis简介

#### NoSQL

1. SQL

2. NoSQL

3. SQL和NoSQL比较

   ![image-20230221102738202](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211027983.png)

#### Redis

Redis官网：https://redis.io/

Redis中文网：https://www.redis.net.cn/

Redis源码：https://github.com/redis/redis

参考资料：

* https://blog.csdn.net/hellozpc/article/details/81267030

1. 简介：Redis诞生于2009年，全称是**Remote Dictionary Server（远程字典服务器）**，是一个完全开源的使用ANSIC语言编写遵守BSD协议的，基于内存的**键值型**NoSQL数据库。

   * 支持事务、持久化、Lua脚本、发布/订阅、缓存淘汰、流技术等多种功能特性；
   * 提供主从模式、Redis Sentinel和Redis Cluster架构方案；
   * Redis之父——安特雷兹
     * Github：https://github.com/antirez
     * 个人博客：https://antirez.com/latest/0

2. 特征：

   * 键值(key-value)型，value支持多种不同数据结构,功能丰富
   * 单线程，每个命令具备原子性
   * 低延迟，速度快(基于内存、IO多路复用、良好的编码)。
   * 支持数据持久化。
   * 支持主从集群、分片集群。
   * 支持多语言客户端

3. redis应用场景

   * 缓存
   * 任务队列
   * 消息队列
   * 分布式锁

4. 安装和配置

   * 安装

     * Linux
     * Windows

     * Docker

       * 参考：https://zhuanlan.zhihu.com/p/625765918

   * 配置

     ~~~shell
     # daemonize 改为 yes
     # protected-mode 改为 no
     # bind 127.0.0.1 注释掉该配置
     # 去除requirepass配置注释并添加自己密码
     ~~~

   > 下载地址：https://redis.io/downloads/
   >
   > 版本命名规则：
   >
   > * 版本号第二位数为奇数，则为非稳定版本，例如：3.1
   > * 版本号第二位数为偶数，则为稳定版本，例如：3.2

5. Reids客户端&工具

   * redis-benchmark：性能测试工具
   * redis-check-aof：修复有问题的AOF文件
   * redis-check-dump：修复有问题的dump.rdb文件
   * redis-sential：redis集群使用
   * redis-server：redis服务器启动器

   * redis-cli：命令行客户端
   * 图形化客户端
     * RedisDesktopManager
     * RDM
     * Another Redis Desktop Manager
   * 编程客户端

6. key的层级

   ![image-20230221150559429](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211506149.png)

### 数据类型及常用命令

官方参考文档：https://redis.io/commands/

Redis是一个key-value的数据库， key- 般是String类型，不过value的类型多种多样。

1. 常见数据结构

   * 字符串（String）
   * 列表（List）
   * 哈希表（Hash）
   * 集合（Set）
   * 有序集合（ZSet）
   * 地理空间（GEO）
   * 基数统计（HyperLog）
   * 位图（bitmap）
   * 位域（bitfiled）
   * 流（Stream）
   
   ![image-20230221112343749](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202312052129167.png)

#### 通用命令

![image-20230221114644376](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211146926.png)

~~~shell
# 查看所有key
keys *
# 查看key类型
type key
# 删除key
del key
# 非阻塞删除
unlink key
# 查看过期时间
ttl key
# 设置过期时间
expire key 秒
# 切换使用库
select dbindex
# 移动数据到指定库，库范围【0-15】
move key dbindex
# 查看当前库key个数
dbsize
# 清空当前库
flushdb
# 清空全部库
flushall
~~~

> 注意：
>
> * 命令不区分大小写，但是键区分大小写 

#### String类型

1. 说明
2. 常用命令
   * `get`
   * `set`
   * `mset`
   * `mget`
   * `getrange`
   * `incr`
   * `incrby`
   * `decr`
   * `decrby`
   * `strlen`
   * `apend`
   * `setnx`
   * `setex`
   * `getset`

![image-20230221114914932](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211149092.png)

![image-20230221134053867](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211340328.png)

#### Hash类型

![image-20230221152905957](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211529302.png)

![image-20230221153343238](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211533319.png)

#### List类型

1. 说明
   * 底层结构是一个双端链表，容量为2^32 -1个元素（约40多亿）
   * 常用于栈、队列、消息队列等场景
2. 常用命令
   * `lpush`
   * `rpush`
   * `lrange`

![image-20230221153504668](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211535191.png)

![image-20230221153711995](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211537923.png)

#### Set类型

1. 说明
2. 常用命令
   * `sintercard`
3. 应用场景
   * 可能认识的人
   * 共同好友

![image-20230221154227216](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211542836.png)

![image-20230221154642114](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211546072.png)

#### SortedSet类型

1. 说明
2. 应用场景
   * 排行榜

![image-20230221183350312](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211833894.png)

![image-20230221183922957](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211839023.png)

#### Geo类型

#### Bitmap类型

1. 说明
   * 由0和1状态表现的二进制位的比特数组
   * 用String类型作为底层数据结构实现的一种统计二值状态的数据类型，本质为数组
   * BitMap最大支持位数为2^32
2. 常用命令
   * setbit
   * getbit
   * strlen
     * 统计占据字节数，8位一组
   * bitcount
   * bitop

#### Bitfield类型

#### HyperLogLog类型

1. 说明
   * 用于做基数统计的算法
   * 有点在于输入元素数量或体积非常非常大时，计算基础所需的空间总是固定且小的
   * 在Redis中，每个HyperLogLog键只需要12KB内存，就可以计算接近2^64个不同元素的基数
2. 常用命令
3. 应用场景
   * 统计某个网站或文章的UV（独立访客浏览量）
   * 用户搜索网站关键词的数量
   * 统计用户每天搜索不同词条个数

#### Stream流

### 持久化

### 事务

### 管道

### java客户端

官方文档：https://www.redis.net.cn/clients/

redis的java客户端很多，官方推荐有三种：

1. Jedis：以Redis命令作为方法名称，学习成本低，简单实用。但是Jedis实例是线程不安全的，多线程环境下需要基于连接池来使用
2. Lettuce：是基于Netty实现的，支持同步、异步和响应式编程方式，并且是线程安全的。支持Redis的哨兵模式、集群模式和管道模式。
3. Redisson：基于Redis实现的分布式、可伸缩的Java数据结构集合。包含了诸如Map. Queue、Lock、Semaphore、Atomi cLong等强大功能

   spring对redis客户端进行了整合，提供了Spring Data Redis。（可以兼容jdeis和lettuce）

#### Jedis

1. 快速使用

   ![image-20230221194510804](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211945201.png)

2. jedis连接池

   ![image-20230221200923748](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302212009785.png)

#### SpringDataRedis

1. 简介

   官网地址：

   ![image-20230221202228761](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302212022639.png)

2. 相关API

   ![image-20230221202454506](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302212024218.png)

3. 快速使用

   springboot已经提供了对SpringDataRedis的支持，可以通过导入下列依赖快速集成。

   ~~~xml
    <!-- redis依赖 -->
       <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-data-redis</artifactId>
       </dependency>
   
       <!-- 连接池依赖 -->
       <dependency>
         <groupId>org.apache.commons</groupId>
         <artifactId>commons-pool2</artifactId>
       </dependency>
   ~~~

   然后在springboot配置文件中进行数据源连接的相关配置。

   ~~~yml
   spring:
     redis:
       host: 192.168.175.130
       port: 6379
       password: 4112
       jedis:
         pool:
           # 最大连接
           max-active: 8
           # 最大空闲连接
           max-idle: 8
           # 最小空闲连接
           min-idle: 0
           # 最长连接等待时间
           max-wait: 100
   ~~~

   接下来就可以使用RedisTemplate对象进行相关操作。

   ~~~java
   @SpringBootTest
   class SpringDataRedisDemoApplicationTests {
   
       @Resource
       private RedisTemplate redisTemplate;
   
       @Test
       void testString(){
           redisTemplate.opsForValue().set("username","chenwenjian");
           System.out.println(redisTemplate.opsForValue().get("username"));
       }
   }
   ~~~

4. SpringDataRedis的序列化方式

   RedisTemplate使用Object接收任意的值写入到redis中，写入前会默认使用jdk方式序列化key和value，该方式可读性较差，内存占用更高，并可能造成bug隐患。

   通过查看RedisTemplate的源码，发现RedisSerializer有如下实现类。

   ![image-20230702232236331](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202307022322490.png)

   于是可以通过如下代码，自定义RedisRemplate的序列化方式。

   ~~~java
   @Configuration
   public class RedisConfig {
   
       @Bean
       public RedisTemplate<String,Object> getRedisTemplate(RedisConnectionFactory redisConnectionFactory){
   
           // 创建RedisTemplate对象
           RedisTemplate<String, Object> template = new RedisTemplate<>();
           // 设置连接工厂
           template.setConnectionFactory(redisConnectionFactory);
           // 创建Json序列化工具
           GenericJackson2JsonRedisSerializer genericJackson2JsonRedisSerializer = new GenericJackson2JsonRedisSerializer();
           // 设置key的序列化
           template.setKeySerializer(RedisSerializer.string());
           template.setHashKeySerializer(RedisSerializer.string());
           // 设置value的序列化
           template.setValueSerializer(genericJackson2JsonRedisSerializer);
           template.setHashValueSerializer(genericJackson2JsonRedisSerializer);
           return template;
       }
   }
   ~~~

5. StringRedisTemplate

   为了节省内存空间，我们并不会使用JSON序列化器来处理value，而是统一使用String序列化器，要求只能存储String类型的key和value。当需要存储Java对象时，手动完成对象的序列化和反序列化。

   Spring默认提供了一个StringRedisTemplate类，它的key和value的序列化方式默认就是String方式。省去了我们自定义RedisTemplate的过程：

## 应用场景

### 短信登录-共享Session

#### 基于Session实现登录

1. 短信验证码登录流程

   ![image-20230704215604631](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202307042156639.png)

#### 基于Redis实现

1. 集群部署的session共享问题：多台tomcat服务器件无法共享session

2. 使用Redis解决集群部署下共享session问题

   ![image-20230716181322597](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202307161813066.png)

3. 使用拦截器实现token刷新

### 查询缓存

1. 缓存：数据交换的缓冲区(称作Cache)，是存贮数据的临时地方，一般读写性能较高。计算机软硬件各级缓存：

   ![image-20231206082216266](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202312060822856.png)

2. 缓存作用：

   * 降低后端负载
   * 提高读写效率，降低响应时间

3. 缓存成本

   * 数据一致性成本
   * 代码维护成本
   * 运维成本

4. 添加缓存

   ![image-20231206083220688](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202312060832148.png)
   
5. 缓存更新策略

   * 内存淘汰
   * 超时剔除
   * 主动更新
     * **Cache Aside Pattern**（常用）：由缓存的调用者，在更新数据库的同时更新缓存。主动操作数据库和缓存时存在以下三个常见问题：
       * 删除缓存还是更新缓存？
         * 更新缓存：每次更新数据库都更新缓存，无效写操作较多
         * 删除缓存：更新数据库时让缓存失效，查询时再更新缓存（推荐）
       * 如何保证缓存与数据库的操作同时成功或失败？
         * 单体系统，将缓存与数据库操作放在一个事务
         * 分布式系统，利用TCC等分布式事务方案
       * 先操作缓存还是先操作数据库？
         * 先删除缓存，再操作数据库
         * 先操作数据库，再删除缓存（推荐）
     * Read/Write Through Pattern：缓存与数据库整合为一个服务由服务来维护一致性。调用者调用该服务，无需关心缓存一致性问题。
     * Write Behind Caching Pattern：调用者只操作缓存，由其它线程异步的将缓存数据持久化到数据库，保证最终一致。

   ![image-20231209173826751](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202312091738758.png)

商户查询缓存
优惠券秒杀
达人探店
好友关注
附近的商户
用户签到
UV统计



企业缓存方案

缓存雪崩

缓存穿透

1. **缓存穿透**： 缓存穿透是指当针对某个特定的 key，无论是缓存中不存在还是后端存储中都不存在，恶意请求可以绕过缓存直接访问后端存储，导致大量请求直接落到数据库或其他存储系统上，引起数据库压力过大甚至宕机。
2. **缓存穿透攻击**： 缓存穿透攻击是一种利用缓存穿透漏洞进行的恶意攻击。攻击者会故意发送一些缓存中肯定不存在的数据请求，以绕过缓存系统直接查询数据库，从而消耗系统资源或者获取敏感信息。这种攻击可能导致系统负载过高、数据库压力增大甚至拖垮整个系统。
3. 造成原因：缓存穿透通常是由恶意请求或者程序错误引起的。
4. 解决方法：
   * 通常是对于不存在的 key 值也进行缓存
   * 使用**布隆过滤器**等数据结构来过滤非法请求
   * 对请求参数进行校验

秒杀中Redis的应用

* Redis计数器
* 分布式锁
* 消息队列的应用

社交APP中Redis的应用

Redis特殊数据结构的应用



点赞列表、排行榜小案例

关注、取关、共同关注、消息推送小案例

用户签到小案例（BitMap数据统计功能）

附近商户小案例（GeoHash的应用）

UV统计（HyperLogLog的统计功能）

## 设计及优化

### 主从模式

### 哨兵模式

### 集群模式

### 多级缓存

Redis应用最佳实践

## 原理分析

Redis常见数据类型的底层结构
Redis通信模型
Redis的内存策略