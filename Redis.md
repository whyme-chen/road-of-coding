# Redis

学习参考：

* https://www.bilibili.com/video/BV1cr4y1671t/?p=1&vd_source=fabefd3fabfadb9324761989b55c26ea

## 基础

### Redis简介

#### NoSQL

1. SQL

2. NoSQL

3. SQL和NoSQL比较

   ![image-20230221102738202](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211027983.png)

#### Redis

redis中文网：https://www.redis.net.cn/

redis官网：https://redis.io/

参考资料：

* https://blog.csdn.net/hellozpc/article/details/81267030

1. 简介：Redis诞生于2009年全称是Remote Dictionary Server,远程词典服务器，是一个基于内存的**键值型**NoSQL数据库。

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

4. 安装和配置

   * Linux
   * Windows

5. Reids客户端

   * 命令行客户端
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

   ![image-20230221112343749](D:\学习\road-of-coding\java study notes.assets\image-20230221112343749.png)

#### 通用命令

![image-20230221114644376](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211146926.png)

#### String类型

![image-20230221114914932](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211149092.png)

![image-20230221134053867](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211340328.png)

#### Hash类型

![image-20230221152905957](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211529302.png)

![image-20230221153343238](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211533319.png)

#### List类型

![image-20230221153504668](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211535191.png)

![image-20230221153711995](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211537923.png)

#### Set类型

![image-20230221154227216](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211542836.png)

![image-20230221154642114](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211546072.png)

#### SortedSet类型

![image-20230221183350312](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211833894.png)

![image-20230221183922957](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211839023.png)

### Redis的java客户端

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

商户查询缓存
优惠券秒杀
达人探店
好友关注
附近的商户
用户签到
UV统计



企业缓存方案

缓存雪崩、穿透等问题

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

主从模式
哨兵模式
集群模式
多级缓存
Redis应用最佳实践

## 原理分析

Redis常见数据类型的底层结构
Redis通信模型
Redis的内存策略