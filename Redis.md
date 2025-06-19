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

1. 说明

   * 地球地理位置使用二位经纬度表示
   * 将三维球体转换为二维平面坐标，将二维坐标转换为一维点块，将一维点块转换为二进制再使用base32进行编码

2. 常用命令

   ~~~bash
   # 向指定的地理空间添加一个或多个地理位置（经纬度）。
   GEOADD key longitude latitude member
   
   # 计算两个地理位置之间的距离。unit 可以是 m（米）、km（千米）、mi（英里）、ft（英尺），默认为米。
   GEODIST key member1 member2 [unit]
   
   # 返回一个或多个成员的位置（经纬度）。
   GEOPOS key member [member ...]
   
   # 返回一个或多个成员的地理位置的 Geohash 编码。
   GEOHASH key member [member ...]
   
   # 从指定的地理位置返回一定半径内的成员（按照距离排序）。
   GEORADIUS key longitude latitude radius unit [WITHDIST] [WITHCOORD] [WITHHASH] [COUNT count] [ASC|DESC]
   
   # 与 GEORADIUS 类似，但使用地理位置成员而不是经纬度。
   GEORADIUSBYMEMBER key member radius unit [WITHDIST] [WITHCOORD] [WITHHASH] [COUNT count] [ASC|DESC]
   
   ~~~

   

3. 应用场景

   * 交友软件附近的人
   * 外卖软件附近美食
   * 地图软件附近的xxx

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

> Redis5.0新增的数据结构，可以理解为Redis版消息队列

1. 说明
   * Redis5.0前消息队列方案有List和Pub/Sub模型
   * 作用：实现消息队列，支持消息的持久化，自动生成全局唯一ID，消息ACK确认机制，消费组消费模式
   * 底层：通过一个消息链表串联所有消息，每个消息由唯一ID和对用内容
2. 常用命令
3. 应用场景

#### Bitfield类型

1. 说明
   * 将Redis字符串看作是一个二进制位组成的数组，并对这个数组中任意偏移进行访问。
   * 作用：位域修改、溢出控制

## 持久化

1. 必要性
2. 两种实现方式
   * RDB（Redis Database）：**以指定的时间间隔执行数据集的时间点快照**。即将某一时刻的数据和状态以文件的形式写入磁盘，该快照文件叫做RDB文件（dump.rdb）
   * AOF（Append Only File）：**以日志的形式来记录每个写操作**，将Redis执行过的所有写指令记录下来(读操作不记录)只许追加文件但不可以改写文件，redis启动之初会读取该文件，将写指令从前到后执行一次以完成数据的恢复工作。

### RDB

1. 简介：存储快照

2. 相关配置（redis配置文件中）

   ~~~
   ################################ SNAPSHOTTING  ################################
   
   # Save the DB to disk.
   #
   # save <seconds> <changes> [<seconds> <changes> ...]
   #
   # Redis will save the DB if the given number of seconds elapsed and it
   # surpassed the given number of write operations against the DB.
   #
   # Snapshotting can be completely disabled with a single empty string argument
   # as in following example:
   #
   # save ""
   #
   # Unless specified otherwise, by default Redis will save the DB:
   #   * After 3600 seconds (an hour) if at least 1 change was performed
   #   * After 300 seconds (5 minutes) if at least 100 changes were performed
   #   * After 60 seconds if at least 10000 changes were performed
   #
   # You can set these explicitly by uncommenting the following line.
   #
   # save 3600 1 300 100 60 10000
   
   # By default Redis will stop accepting writes if RDB snapshots are enabled
   # (at least one save point) and the latest background save failed.
   # This will make the user aware (in a hard way) that data is not persisting
   # on disk properly, otherwise chances are that no one will notice and some
   # disaster will happen.
   #
   # If the background saving process will start working again Redis will
   # automatically allow writes again.
   #
   # However if you have setup your proper monitoring of the Redis server
   # and persistence, you may want to disable this feature so that Redis will
   # continue to work as usual even if there are problems with disk,
   # permissions, and so forth.
   stop-writes-on-bgsave-error yes
   
   # Compress string objects using LZF when dump .rdb databases?
   # By default compression is enabled as it's almost always a win.
   # If you want to save some CPU in the saving child set it to 'no' but
   # the dataset will likely be bigger if you have compressible values or keys.
   rdbcompression yes
   
   # Since version 5 of RDB a CRC64 checksum is placed at the end of the file.
   # This makes the format more resistant to corruption but there is a performance
   # hit to pay (around 10%) when saving and loading RDB files, so you can disable it
   # for maximum performances.
   #
   # RDB files created with checksum disabled have a checksum of zero that will
   # tell the loading code to skip the check.
   rdbchecksum yes
   
   # Enables or disables full sanitization checks for ziplist and listpack etc when
   # loading an RDB or RESTORE payload. This reduces the chances of a assertion or
   # crash later on while processing commands.
   # Options:
   #   no         - Never perform full sanitization
   #   yes        - Always perform full sanitization
   #   clients    - Perform full sanitization only for user connections.
   #                Excludes: RDB files, RESTORE commands received from the master
   #                connection, and client connections which have the
   #                skip-sanitize-payload ACL flag.
   # The default should be 'clients' but since it currently affects cluster
   # resharding via MIGRATE, it is temporarily set to 'no' by default.
   #
   # sanitize-dump-payload no
   
   # The filename where to dump the DB
   dbfilename dump.rdb
   
   # Remove RDB files used by replication in instances without persistence
   # enabled. By default this option is disabled, however there are environments
   # where for regulations or other security concerns, RDB files persisted on
   # disk by masters in order to feed replicas, or stored on disk by replicas
   # in order to load them for the initial synchronization, should be deleted
   # ASAP. Note that this option ONLY WORKS in instances that have both AOF
   # and RDB persistence disabled, otherwise is completely ignored.
   #
   # An alternative (and sometimes better) way to obtain the same effect is
   # to use diskless replication on both master and replicas instances. However
   # in the case of replicas, diskless is not always an option.
   rdb-del-sync-files no
   
   # The working directory.
   #
   # The DB will be written inside this directory, with the filename specified
   # above using the 'dbfilename' configuration directive.
   #
   # The Append Only File will also be created inside this directory.
   #
   # Note that you must specify a directory here, not a file name.
   dir ./
   ~~~

3. 触发备份方式与时机

   * 自动触发：Redis根据配置文件进行自动备份
     * 达到配置规则时进行自动快照备份
     * 执行flushall或flushdb命令也会产生dump.rdb文件，但是该文件内容为空
     * 执行shutdown且没有设置开启AOF持久化
     * 主从复制时，主节点自动触发
   * 手动触发：手动执行save或bgsave命令进行备份
     * Save命令会阻塞当前Redis服务器，直到持久化工作完成，生产切记不要使用
     * Bgsave会再后台异步fork一个子进程，由子进程进行持久化备份工作（默认方式）
     * 可以使用LASTSAVE命令获取最后一次成功执行快照的时间

4. 优缺点

   * 优点
     * 适合大规模的数据恢复
     * 定时备份
     * RDB文件再内存中加载速度比AOF文件快
   * 缺点
     * 可能丢失最近最新修改
     * 数据量大的情况下，因为RDB为全量备份也会占用大量内存和CPU资源，可能导致I/O严重影响性能的情况

> 特别说明：
>
> 不可以把备份文件dump.rdb和生产redis服务器放在同一台机器，必须分开各自存储，以防止物理机器损坏导致备份无法恢复。

### AOF

1. 简介：以日志的形式来记录每个写操作，该日志文件为appendonly.aof

   * 默认情况下Redis不开启AOF，需要在配置文件中修改如下配置：

     ~~~shell
     appendonly yes
     ~~~

2. 基本工作流程

   * Redis-Server端持续接收来自Client端的操作命令
   * Redis-server端接收命令后不会直接写入AOF文件，而是先写入AOF缓存（实际为内存中一片区域），当命令数量达到一定量后再根据同步文件的三种写策略将命令写入磁盘
   * 随着AOF写入内容的增加为避免文件膨胀，会根据规则进行命令合并（称为AOF重写），从而起到AOF文件压缩的目的

3. 三种写回策略

   * always：同步写回，每个写命令执行完立刻写入磁盘
   * everysec（默认）：每秒写入
   * no：由操作系统决定何时将缓冲区内容写回磁盘

4. Redis6 Vs Redis7变化

   * 日志文件写入路径配置变化
   * 日志文件名称
     * Redis6中只有一个日志文件，Redis7中采用Multi Part设计日志文件分为三部分BASE、INCR、MAINFEST

5. 优缺点

   * 优点
     * 损失基本再秒级
   * 缺点 
     * AOF 文件通常比相同数据集的等效 RDB 文件大
     * 根据确切的 fsync 策略，AOF 可能比 RDB 慢

6. 重写机制

   * 只保留可以恢复数据的最小指令集（即一个key的最后一次写记录）
   * 触发机制：
     * 自动：根据配置文件执行，默认为同时达到64mb且aof文件增长一倍
     * 手动：使用命令bgrewrite

> 特别说明：
>
> 1. RDB和AOF可以同时使用，此时会优先使用AOF文件进行数据恢复
> 2. 使用配置aof-use-rdb-preamble开启混合方式，yes表示开启，no表示禁用

## 事务

1. 简介
   * 数据库事务：一次事务的多次操作要么全部成功，要么全部失败
   * Redis事务：一次事务中执行一组命令集合，所有命令都会被序列化，按顺序的串行执行而不被其他命令插入。即在一个队列中、一次性、顺序性、排他性的执行一系列命令。不保证原子性，即没有回滚能力
2. 相关命令
   * MULTI：开始一个事务块。该命令之后的所有命令会被排队，直到执行 EXEC。
   * EXEC：执行事务块中的所有命令，并提交事务。
   * DISCARD：放弃事务块中的所有命令，即取消事务。
   * WATCH：监视一个或多个键，事务开始前，如果被监视的键在执行事务命令之前发生了变化，事务将被取消。
     * 支持乐观锁定
   * UNWATCH：取消对所有键的监视。

## 管道

1. 简介
   * Redis基于客户端服务端模式，命令从请求到执行响应过程消耗时间称为RTT
   * 管道(pipeline)可以一次性发送多条命令给服务骗，服务端依次处理完完毕后，通过一条响应一次性将结果返回，通过减少客户端与redis的通信次数来实现降低往返延时时间。
   * pipeline实现的原理是队列，先进先出特性就保证数据的顺序性。
   
2. 快速使用

   **Python脚本实现批量写入**

   安装 Redis 客户端。

   ```
   pip install redis
   ```

   准备数据文件 `data.txt` 

   ```
   key1 value1
   key2 value2
   key3 value3
   ```

   编写脚本，Python 示例如下。

   ```
   import redis
   
   # 创建 Redis 连接
   r = redis.StrictRedis(host='localhost', port=6379, db=0)
   
   # 打开文件并逐行读取
   with open('data.txt', 'r') as file:
       # 使用管道进行批量写入
       pipe = r.pipeline()
   
       for line in file:
           # 假设每行格式为 "key value"
           key, value = line.strip().split()
           # 将 SET 命令加入管道
           pipe.set(key, value)
   
       # 执行管道中的所有命令
       pipe.execute()
   
   print("数据已成功写入 Redis！")
   ```

   - `r.pipeline()`：创建一个管道对象，这个对象会缓存你通过它发出的所有 Redis 命令。
   - `pipe.set(key, value)`：将每个 `SET` 命令添加到管道中，而不是立即执行。这些命令会被批量发送。
   - `pipe.execute()`：一旦所有命令都加入管道，通过调用 `execute()` 方法一次性将所有命令发送到 Redis。Redis 会同时处理这些命令，从而显著提高写入效率。

   **Redis-cli客户端使用管道模式实现批量写入**

   准备数据文件data.txt。

   ~~~
   set key1 value1
   set key2 value2
   set key3 value3
   ~~~

   使用管道模式写入。

   ~~~bash
   cat data.txt | redis-cli --pipe
   
   # 若数据不带set命令，可如下操作
   awk '{print "SET", \$1, \$2}' data.txt | redis-cli --pipe
   ~~~

   * `redis-cli --pipe` 是 Redis 提供的一种高效的批量操作模式，它允许你通过管道将多个命令批量发送到 Redis，避免了多次连接和等待响应的过程，从而提高性能。
   * `cat data.txt` 会读取 `data.txt` 文件的内容，将每一行的数据传递给 `redis-cli`。
   * `--pipe` 模式会自动将文件中的每行转换为 Redis 的 `SET` 命令，并批量发送给 Redis 执行

## java客户端

官方文档：https://www.redis.net.cn/clients/

redis的java客户端很多，官方推荐有三种：

1. Jedis：以Redis命令作为方法名称，学习成本低，简单实用。但是Jedis实例是线程不安全的，多线程环境下需要基于连接池来使用
2. Lettuce：是基于Netty实现的，支持同步、异步和响应式编程方式，并且是线程安全的。支持Redis的哨兵模式、集群模式和管道模式。
3. Redisson：基于Redis实现的分布式、可伸缩的Java数据结构集合。包含了诸如Map. Queue、Lock、Semaphore、Atomi cLong等强大功能

   spring对redis客户端进行了整合，提供了Spring Data Redis。（可以兼容jdeis和lettuce）

### Jedis

1. 快速使用

   ![image-20230221194510804](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302211945201.png)

2. jedis连接池

   ![image-20230221200923748](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302212009785.png)

### SpringDataRedis

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

## 架构模式与设计

### 主从模式（Replica）

1. 简介

   * 通过主从复制模式实现读写分离，当master库数据变化时自动异步同步到slave库
   * 通过主从复制模式实现数据备份，容灾恢复
   * 通过主从复制模式实现水平扩容支撑高并发

2. 快速使用

   Redis 的主从模式（Master-Slave）配置主要是通过指定从节点（Slave）连接到主节点（Master）来实现数据复制。主从模式可以提供读写分离、负载均衡等功能，也能增强数据的可用性。不过，如果需要高可用性和自动故障转移，可以考虑使用 Redis Sentinel 或 Redis Cluster。常用的主从架构有：

   * 一主二从：两个从库同时从属与一台主库
   * 链式：从库1从属于主库，后续从库依次从属与从库1

   以下是配置主从模式的基本步骤：

   **配置主节点**

   主节点的配置不需要做特别修改，默认就是主节点。你只需确保主节点的配置文件中没有 `slaveof` 指令。

   1. 打开主节点的 Redis 配置文件（通常是 `redis.conf`）。
   2. 确保以下配置项没有被修改或注释掉：
      ```bash
      # master节点一般使用默认配置，不需要特别配置
      ```

   **配置从节点**

   从节点需要配置连接到主节点，来实现数据的复制。

   1. 打开从节点的 Redis 配置文件（`redis.conf`）。
   2. 设置 `slaveof` 指令，指向主节点的 IP 和端口：
      ```bash
      slaveof <master-ip> <master-port>
      ```
      例如：
      ```bash
      slaveof 127.0.0.1 6379
      ```

   3. 可选地，可以设置从节点的 `masterauth` 参数，用于认证主节点：
      ```bash
      masterauth <password>
      ```

   4. 确保 `protected-mode` 配置项设置为 `no`（如果需要的话），以便可以从远程访问：
      ```bash
      protected-mode no
      ```

   5. 启动从节点的 Redis 实例。

   **配置密码认证（可选）**

   > 强烈建议配置，生产环境必须配置

   如果你的 Redis 实例启用了密码认证，可以在主从配置中加上认证设置：

   1. 在主节点的配置文件中启用密码：
      ```bash
      requirepass <password>
      ```

   2. 在从节点的配置文件中，添加认证设置：
      ```bash
      masterauth <password>
      ```

   **启动 Redis 实例**

   - 启动主节点：直接执行 `redis-server /path/to/redis.conf` 启动。
   - 启动从节点：执行 `redis-server /path/to/redis.conf` 启动。

   **验证主从同步**

   一旦配置完成，启动 Redis 实例后，可以通过以下命令来验证主从同步：

   - 连接到主节点：
     ```bash
     redis-cli -h <master-ip> -p <master-port>
     ```

   - 执行 `info replication`，检查主从关系：
     ```bash
     info replication
     ```
     你应该能看到类似下面的输出：
     ```
     role:master
     connected_slaves:1
     slave0:ip=<slave-ip>,port=<slave-port>,state=online,offset=12345,lag=0
     ```

   - 然后连接到从节点：
     ```bash
     redis-cli -h <slave-ip> -p <slave-port>
     ```
     执行 `info replication`，你应该会看到：
     ```
     role:slave
     master_host=<master-ip>
     master_port=<master-port>
     master_link_status:up
     ```

   **其他配置（可选）**

   - 设置从节点为只读：默认情况下，从节点的数据是只读的。你可以通过设置 `slave-read-only` 来强制从节点处于只读状态。
     ```bash
     slave-read-only yes
     ```

   - 配置复制延迟：在从节点和主节点之间存在一定的延迟，确保你的应用能够容忍这种延迟。

   **相关问题**

   * 从机可以进行写操作吗？
   * 主机shutdown后，从机会变为主机吗？主机重启后，从机是否可以顺利同步？
   * 从机shutdown后重启，是否可以从主机中正常同步复制？

3. 工作流程&原理

   * **建立连接**：从服务器启动后，通过 `replicaof` 命令连接主服务器。
   * **发送同步命令**：从服务器发送 `SYNC`（全量同步）或 `PSYNC`（部分同步）命令。
   * **生成RDB快照**：主服务器执行 `BGSAVE` 后台生成 RDB 快照文件。
   * **缓冲写命令**：主服务器在生成 RDB 期间，将新写入命令存入 **复制缓冲区**。
   * **发送RDB文件**：主服务器将 RDB 文件传输给从服务器。
   * **加载RDB文件**：从服务器清空旧数据，载入 RDB 文件恢复主服务器快照状态。
   * **发送缓冲命令**：主服务器将复制缓冲区中的写命令发送给从服务器执行。
   * **持续同步**：进入稳定阶段，主服务器实时推送新写命令给从服务器（基于长连接）。

4. 缺点

   * 因为所有写操作都是现在主节点进行，所以这在一定程度上会增加主节点的压力，第二从节点的数据存在延迟，而且随着从节点的数量增多延迟会随之增大
   * 当主节点宕机后，默认从节点不会替代成为主节点

### 哨兵模式（Sentinel）

1. 简介

   * 产生原因：因为主从复制模式和过程中当主节点宕机后，从节点不会主动成为主节点，导致Redis服务不可用，需要手动将从节点备份数据恢复到主节点。
   * Redis 官方提供的高可用性（HA）解决方案，用于**管理 Redis 主从架构**，实现**自动故障转移**和**系统监控**。

2. 作用

   * 主从监控
   * 消息通知
   * 故障转移
   * 配置中心

3. 架构

   * **Redis 节点**
     - 1 个主节点（Master）
     - N 个从节点（Replica）
   * **Sentinel 集群**
     - **至少 3 个节点**（推荐奇数个）
     - 分布式部署避免单点故障
     - 节点间通过 Gossip 协议通信

   ~~~mermaid
   flowchart TD
       C[客户端] --> S[Sentinel集群]
       S -->|监控| M[Redis Master]
       M -->|复制| R1[Redis Replica 1]
       M -->|复制| R2[Redis Replica 2]
       S -->|监控| R1
       S -->|监控| R2
       S1[Sentinel 1] <-->|通信| S2[Sentinel 2]
       S2 <-->|通信| S3[Sentinel 3]
   ~~~

4. 运行流程（选举原理）

   * **主观下线（SDOWN）**
     - 单个 Sentinel 检测到主节点无响应（默认 30 秒超时）
   * **客观下线（ODOWN）**
     - 多个 Sentinel 确认主节点故障（需 `quorum` 数量同意）
     -  `quorum` 表示最少需要有几个哨兵认同故障迁移的法定票数
     - 配置参数：`sentinel monitor <master> <ip> <port> <quorum>`
   * **领导者选举**
     - 使用`Raft`算法选出故障转移执行者
     - 需要多数 Sentinel 节点同意（`N/2 + 1`）
   * **从节点晋升**
     - 筛选标准（按优先级）：
       1. `redis.conf`配置文件中slave-priority或replica-priority最高节点（数据越小优先级越高）
       2. 复制偏移量最新的节点
       3. 运行 ID 最小的节点（字典序，ASCII码）
     - 执行 `SLAVEOF NO ONE` 提升为主节点
   * **重新配置集群**
     - 其他从节点复制新主节点
     - 旧主节点恢复后变为从节点

   ~~~platuml
   sequenceDiagram
       participant S as Sentinel集群
       participant M as Master
       participant R as Replicas
       
       Note over S: 监控阶段
       S ->> M: 定期发送 PING（每1秒）
       alt 主节点响应超时
           M-->>S: 无响应（>30秒）
           S->>S: 标记主节点为 SDOWN<br>（主观下线）
       end
       
       Note over S: 共识阶段
       S->>S: 广播投票请求
       alt 多数Sentinel同意
           S->>S: 标记 ODOWN<br>（客观下线）
       end
       
       Note over S: 选举阶段
       S->>S: Raft算法选举领导者
       activate S
       Note right of S: 领导者负责故障转移
       
       Note over S,R: 故障转移阶段
       S->>R: 筛选最佳从节点
       S->>R: 执行 SLAVEOF NO ONE
       S->>R: 重新配置其他从节点
       S->>S: 更新主节点配置
       deactivate S
       
       Note over S: 通知阶段
       S->>Clients: 发布新主节点地址
       S->>Other Redis: 更新配置
   ~~~

5. 哨兵使用建议

   * 哨兵数量应该多个，最好为奇数，本身构成集群
   * 各个哨兵版本、配置应该一致
   
6. 缺点

   * 不解决数据分片问题（需 Cluster 模式）
   * 故障转移期间可能丢失数据（异步复制）
   * 客户端需要 Sentinel 支持

### 集群模式（Cluster）

1. 定义：
   * Redis 提供的一种分布式架构方式，用于实现数据的分片（sharding）和高可用性（high availability）。
   * 在 Redis 集群中，数据会分布在多个 Redis 节点上，并且集群能够自动管理节点之间的故障转移。即一个提供在多个Redis节点间共享数据的程序集
2. 特点
   * **数据分片**：
     - Redis集群通过**哈希槽**（hash slots）将数据分布在不同的节点上，Redis 集群有 16384 个哈希槽，所有的数据键（key）通过通过CRC16校验后通过哈希算法映射到某个哈希槽，再将哈希槽映射到集群中的节点。（建议1000个）
     - 数据不会存储在单个节点中，集群中的每个节点只负责管理部分数据。
   * **高可用性**：
     - Redis集群具有内建的高可用机制，能够在节点故障时进行自动故障转移（failover）。
     - 如果一个节点发生故障，集群会自动选举一个从节点（slave）提升为主节点（master），确保服务的连续性。
   * **自动分片与负载均衡**：
     - Redis集群会自动将数据根据哈希槽分布到不同的节点上，因此它能够有效地支持水平扩展，增加新的节点可以增加集群的容量。
     - 数据自动在各个节点之间均衡，减少了某个节点的负载压力。
   * **无共享架构**：
     - 与传统的 Redis 主从复制架构不同，Redis集群是无共享的，意味着集群中的每个节点都可以独立处理请求，不依赖于中心节点的协调。
   * **透明性**：
     - 对客户端而言，Redis集群通过分布式协议自动将请求路由到正确的节点。客户端不需要知道数据是存储在哪个节点上的，集群会自动处理这些路由。
   * **一致性与故障处理**：
     - Redis集群支持复制机制，主节点有一个或多个从节点，在主节点发生故障时，从节点会自动接管工作。
     - 但需要注意的是，Redis集群采用的是“最终一致性”，而不是强一致性。
3. slot槽位映射
   * 哈希取余分区：直接对节点数进行取余简单粗暴有效，但是不易扩缩容
   * 一致性哈希算法分区
     * 一致性哈希算法在1997年由麻省理工学院中提出的，设计目标是**为了解决分布式缓存数据变动和映射问题**。简单说就是若某个机器宕机了，分母数量改变了，自然取余数方法将导致计算结果不一致
     * 步骤
       * 算法构建一致性哈希环
       * 服务器IP节点映射
       * key落到服务器的落键规则
     * 一致性哈希的优点是容错性，缺点是会产生数据倾斜，即数据不均匀
   * 哈希槽分区
     * 哈希槽实质就是一个数组，数组[0,2^14-1]形成hash slot空间。
   * 为什么槽位个数的16384个？

### 多级缓存

### 发布订阅

1. 简介
   * 一种消息传递机制，允许客户端通过订阅频道接收其他客户端发布的消息。
   * 该功能常用于需要实时消息推送和事件通知的场景。
   * Redis 的发布/订阅模式非常适合高效且实时的数据交换，但需要注意的是，它并不保证消息的持久化。如果消息在客户端订阅之前发布，它将丢失。
2. 常用场景：适用于短期内需要实时处理的场景。
   * **实时消息通知系统**：使用 Redis 的发布/订阅模式，可以构建实时通知系统。例如，聊天应用、社交媒体、或者任何需要即时通知用户的场景，可以通过订阅特定频道来实时推送消息。
   * **事件驱动架构**：在微服务架构中，发布/订阅模式可以用来实现事件驱动的通信。当某个服务发生特定事件时，它可以发布一条消息，其他服务通过订阅该消息来做出响应。
   * **实时数据推送**：例如，股票价格、天气变化、游戏数据等需要实时推送给用户的应用场景。Redis 可以用来在后台推送数据到多个订阅者。
   * **日志收集与处理**：可以将应用的日志信息通过发布/订阅模式传递到多个订阅者，进行日志处理、实时监控或记录。
   * **消息队列**：Redis 的发布/订阅可以用于构建简单的消息队列系统，多个客户端订阅同一个频道，然后可以消费和处理消息。
   * **实时数据同步**：多个系统或客户端可以通过 Redis Pub/Sub 进行实时数据同步。例如，多个用户在一个共享文件或数据表上进行操作时，系统可以推送更新给所有订阅者。
   * **缓存失效通知**：当缓存数据更新或失效时，可以发布通知消息，其他系统或应用程序订阅并获取这些变化，进行相应的数据更新或重新加载。

## 应用场景实践

### 短信登录-共享Session

#### 基于Session实现登录

1. 短信验证码登录流程

   ![image-20230704215604631](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202307042156639.png)

#### 基于Redis实现

1. 集群部署的session共享问题：多台tomcat服务器件无法共享session

2. 使用Redis解决集群部署下共享session问题

   ![image-20230716181322597](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202307161813066.png)

3. 使用拦截器实现token刷新

### 查询缓存&双写

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

   **通用查询缓存示例**

   ~~~java
   import redis.clients.jedis.Jedis;
   
   public class RedisCacheExample {
   
       private static Jedis jedis = new Jedis("localhost", 6379);
   
       // 模拟从数据库查询数据
       public static String queryFromDatabase(String queryKey) {
           try {
               // 模拟数据库查询延迟
               Thread.sleep(2000);
           } catch (InterruptedException e) {
               e.printStackTrace();
           }
           return "Data for " + queryKey;
       }
   
       public static String getData(String queryKey) {
           // 尝试从缓存中获取数据
           String cachedData = jedis.get(queryKey);
   
           if (cachedData != null) {
               System.out.println("Cache hit");
               return cachedData;
           }
   
           // 如果缓存中没有数据，查询数据库
           System.out.println("Cache miss");
           String data = queryFromDatabase(queryKey);
   
           // 将查询结果存入缓存，缓存有效期设置为 5 分钟
           jedis.setex(queryKey, 300, data);
   
           return data;
       }
   
       public static void main(String[] args) {
           String result = getData("user:123");
           System.out.println(result);
       }
   }
   ~~~

   **高并发下查询缓存示例**

   在高并发环境下，为防止缓存击穿，我们使用 **双重检查锁** 和 Redis 的 **setnx** 命令来保证只有一个请求会查询数据库，并更新缓存。其他请求则会从缓存中读取数据。

   ~~~java
   import redis.clients.jedis.Jedis;
   
   public class RedisCacheWithLockExample {
   
       private static Jedis jedis = new Jedis("localhost", 6379);
   
       // 锁的前缀
       private static final String LOCK_PREFIX = "lock:";
   
       // 模拟从数据库查询数据
       public static String queryFromDatabase(String queryKey) {
           try {
               // 模拟数据库查询延迟
               Thread.sleep(2000);
           } catch (InterruptedException e) {
               e.printStackTrace();
           }
           return "Data for " + queryKey;
       }
   
       public static String getDataWithLock(String queryKey) {
           // 尝试从缓存中获取数据
           String cachedData = jedis.get(queryKey);
   
           if (cachedData != null) {
               System.out.println("Cache hit");
               return cachedData;
           }
   
           // 如果缓存中没有数据，尝试获取锁
           String lockKey = LOCK_PREFIX + queryKey;
           if (jedis.setnx(lockKey, "locked") == 1) {
               try {
                   // 如果获得锁，第二次检查缓存
                   cachedData = jedis.get(queryKey);
                   if (cachedData != null) {
                       System.out.println("Cache hit after lock");
                       return cachedData;
                   }
   
                   // 如果缓存中没有数据，查询数据库
                   System.out.println("Cache miss and querying database");
                   String data = queryFromDatabase(queryKey);
   
                   // 将查询结果存入缓存，缓存有效期设置为 5 分钟
                   jedis.setex(queryKey, 300, data);
                   return data;
               } finally {
                   // 释放锁
                   jedis.del(lockKey);
               }
           } else {
               // 如果没有获得锁，稍作等待后重试
               System.out.println("Cache miss, waiting for lock");
               try {
                   Thread.sleep(100);  // 等待 100 毫秒后重试
               } catch (InterruptedException e) {
                   e.printStackTrace();
               }
               return getDataWithLock(queryKey);
           }
       }
   
       public static void main(String[] args) {
           // 模拟高并发查询
           Thread thread1 = new Thread(() -> {
               String result = getDataWithLock("user:123");
               System.out.println(result);
           });
   
           Thread thread2 = new Thread(() -> {
               String result = getDataWithLock("user:123");
               System.out.println(result);
           });
   
           thread1.start();
           thread2.start();
       }
   }
   ~~~

   双检锁优势如下：

   - **减少数据库查询**：通过缓存机制和锁机制，确保每次查询只有一个请求会访问数据库并更新缓存，避免缓存穿透。
   - **提高并发性能**：即使在高并发环境下，只有一个请求会去查询数据库并更新缓存，其他请求会从缓存中读取数据，减少数据库压力。

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
   
6. Redis与数据库数据一致性

   **缓存更新策略**

   缓存更新策略主要用于保持 Redis 和 MySQL 之间的数据一致性。常见的策略有：

   * **写入穿透 (Write Through Cache)**：在写入数据时，先写入缓存，再写入数据库。这意味着每次修改数据时，都会同时更新缓存和数据库。
     * 优点：
       - **一致性**：缓存和数据库始终保持同步。
       - **简化读取逻辑**：每次查询都能从缓存中直接读取最新的数据。
     * 缺点：
       - **性能瓶颈**：每次写入都要同时更新 Redis 和 MySQL，可能会影响写入性能。
       - **写操作复杂**：如果写入数据库失败，可能导致缓存与数据库的不一致。
   * **写后回写 (Write Behind / Lazy Write)**：在写入数据时，首先只写入缓存，而数据库更新会延迟到缓存中的数据有一定的失效或过期时，定期批量更新数据库。
     * 缺点：
       - **数据一致性问题**：由于数据库的更新是延迟的，可能会导致数据库和缓存数据不一致。
       - **复杂的管理**：需要额外的机制来确保最终一致性，并处理数据回写的失败情况。
     * 优点：
       - **提高性能**：减少了写数据库的频率，可以有效减轻数据库负载。
       - **减少写数据库的延迟**：提高了系统的响应速度，特别是对于高并发的写操作。
   * **定时更新 (Scheduled Updates)**：通过定时任务定期同步 Redis 中的数据到 MySQL，通常适用于一些不频繁更新的场景。
     * 优点：
       - **简单高效**：实现简单，通过定时任务定期同步，不需要在每次写操作时同时操作数据库。
       - **减少数据库写压力**：减少了每次操作时的数据库写入压力。
     * 缺点：
       - **数据不一致**：在同步前，缓存中的数据可能与数据库中的数据不一致，尤其是在短时间内有大量数据变动时。
       - **延迟性**：数据更新的延迟较大，可能导致某些实时性要求较高的场景下出现问题。
   * **删除缓存 (Cache Eviction)**：每当数据更新时，直接删除缓存中的数据，然后下次读取时再从数据库中获取并重新缓存。这种方式常用于数据更新时不会马上同步到缓存，而是缓存过期后才重新加载。
     * 优点：
       - **一致性保证**：避免了缓存和数据库的不一致问题，每次查询都会获取最新的数据库数据。
       - **简单易实现**：不需要复杂的同步机制，只需要简单的缓存删除操作。
     * 缺点：
       - **缓存穿透问题**：如果缓存数据频繁删除，可能会造成大量的数据库读取请求，影响数据库性能。
       - **缓存命中率低**：频繁删除缓存导致缓存命中率较低，降低了性能优化的效果。

   **缓存与数据库的脱钩策略**

   在高并发系统中，有时我们会选择让 Redis 与 MySQL 之间完全脱钩，避免在每次更新时同时操作两个系统。

   * **延迟双删 (Double Deletion)**：在更新数据时，先删除缓存，再将更新写入数据库，之后再次删除缓存。这是一个常用的方式，特别是在高并发的系统中，防止缓存数据与数据库数据不一致。
     * 优点：
       - **简单有效**：即使缓存有时没有及时失效，也能通过第二次删除来保证缓存一致性。
       - **提高缓存命中率**：缓存删除后，下次查询时从数据库重新获取数据并缓存，能保证数据的一致性。
     * 缺点：
       - **可能出现延迟**：虽然有双重删除机制，但在高并发的场景下，仍可能出现缓存和数据库不一致的现象。
       - **执行开销大**：每次更新时，删除缓存需要额外的操作，可能带来性能开销。
   * **异步更新 (Asynchronous Update)**：更新操作将变成异步操作。即，数据在写入数据库后，不会马上同步到缓存，而是通过异步消息队列或者后台线程来更新缓存。
     * 优点：
       - **减少响应延迟**：可以提高写操作的响应速度，不会阻塞等待缓存更新。
       - **数据库负载较低**：避免每次写操作都直接写缓存，减少缓存的同步压力。
     * 缺点：
       - **数据一致性问题**：由于缓存更新是异步的，可能会出现短时间内缓存和数据库数据不一致的情况。
       - **系统复杂性增加**：需要处理异步任务、消息队列或后台更新，增加了系统的复杂性。

   | **策略**                           | **优点**                         | **缺点**                                           | **适用场景**                                           |
   | ---------------------------------- | -------------------------------- | -------------------------------------------------- | ------------------------------------------------------ |
   | **写入穿透 (Write Through)**       | 数据一致性强，查询简单           | 写入性能受影响，每次操作都需要同步写缓存和数据库   | 数据更新频繁且一致性要求较高的场景                     |
   | **写后回写 (Write Behind)**        | 提高性能，减少数据库负载         | 数据一致性问题，可能导致数据丢失或更新延迟         | 高性能、高并发写操作的场景，适合非实时的数据更新       |
   | **定时更新 (Scheduled Updates)**   | 实现简单，减少数据库压力         | 数据可能存在延迟，缓存和数据库可能不一致           | 数据更新不频繁，对实时性要求不高的场景                 |
   | **删除缓存 (Cache Eviction)**      | 数据一致性好，简化了更新逻辑     | 可能造成缓存穿透，增加数据库的查询压力             | 缓存不频繁变动，数据更新时不需要立刻同步到缓存的场景   |
   | **延迟双删 (Double Deletion)**     | 简单有效，减少数据不一致问题     | 执行开销大，可能导致数据更新延迟                   | 高并发写操作需要避免缓存和数据库的不一致时使用         |
   | **异步更新 (Asynchronous Update)** | 提高性能，减少响应延迟，避免阻塞 | 需要处理异步任务，增加了系统复杂性，数据一致性问题 | 需要高性能和高并发的场景，数据更新不需要立刻同步到缓存 |

#### Canal

github：https://github.com/alibaba/canal

### 数据分析统计

1. 典型场景
   * 用户签到小案例（BitMap数据统计功能）
   * UV统计（HyperLogLog的统计功能）
   * 附近的商户（GEO实现）
2. 

### 分布式锁

1. 典型场景
   * 秒杀

## 原理&问题分析

### 单线程 vs 多线程

> Redis4之后才慢慢支持多线程，直到Redis6/7才稳定

1. 单线程：Redis命令工作线程是单线程，但整个Redis是多线程的。
   * 单线程主要是指Redis的网络IO和键值对读写是由一个线程来完成的，Redis在处理客户端的请求时包括获取(socket 读)、解析、执行、内容返回(socket 写)等都由一个顺序串行的主线程处理，这就是所谓的“单线程”。这也是Redis对外提供键值存储服务的主要流程。
   * 但是Redis的其他功能，如RBD、AOF、集群数据同步等是由其他线程完成。
   * 单线程问题（为什么使用多线程）
     * 大key删除问题（解决方案：惰性删除，将某些高耗时操作交给子线程处理，极大地减少主线程的阻塞问题）
2. 相关配置
   * Redis6.0及以后，多线程机制默认时关闭的

### bigkey问题

1. 相关面试题

   * 生产环境如何限制keys * /flushdb/flushall等危险操作，防止误删数据
     * 在Redis配置中对相关命令做重命名配置等
   * 如何在海量数据中查询某一固定前缀的key
     * 使用SCAN，HSCAN，SSCAN，ZSSCAN相关命令
   * 多大算大key，如何发现，如何删除

2. bigkey定义

   * bigkey 是指占用大量内存的键，通常是一些大字符串、大哈希表、大列表或大集合等。但通常大的不是key本身，而是对应的value内容
   * 《阿里云Redis开发规范》定义，String类型控制在10KB以内，hash、list、set、zset元素个数不要超过5000，非字符串大key，不要使用del删除

3. bigkey问题（潜在危险）

   * 内存不均、集群迁移困难
   * 网络流量阻塞
   * 超时删除

4. bigkey发现（排查常用手段）

   **方法 1：使用 `redis-cli` 的 `MEMORY USAGE` 命令**

   `MEMORY USAGE` 命令可以返回指定键占用的内存大小。你可以遍历 Redis 中的所有键，使用这个命令来检查每个键的内存占用情况。

   1. **列出所有键**： 使用 `SCAN` 命令（而不是 `KEYS`，因为 `KEYS` 会阻塞 Redis）遍历 Redis 中的所有键：

      ```
      redis-cli --scan
      ```

      或者使用 `SCAN` 命令来手动遍历键空间：

      ```
      redis-cli SCAN 0
      ```

   2. **检查每个键的内存使用情况**： 使用 `MEMORY USAGE <key>` 命令来查看每个键占用的内存。例如：

      ```
      redis-cli MEMORY USAGE key1
      ```

   3. **编写脚本自动化检查**： 可以编写一个脚本来自动扫描所有键并返回占用内存最多的键。例如，以下是一个简单的 Python 脚本，利用 `redis-py` 库扫描 Redis 键并检查它们的内存使用：

      ```
      import redis
      
      r = redis.StrictRedis(host='localhost', port=6379, db=0)
      
      # 获取所有键
      cursor, keys = r.scan(cursor=0)
      
      # 记录最大内存使用的键
      max_key = None
      max_memory = 0
      
      for key in keys:
          memory = r.memory_usage(key)
          if memory > max_memory:
              max_memory = memory
              max_key = key
      
      print(f"The key with the most memory usage is {max_key} with {max_memory} bytes")
      ```

   **方法 2：使用 `redis-bigkey` 工具**

   `redis-bigkey` 是一个第三方工具，用于扫描 Redis 数据库并找出占用大量内存的键。使用方法：

   1. **安装 `redis-bigkey`**： 你可以通过 `pip` 安装 `redis-bigkey`：

      ```
      bashCopy Codepip install redis-bigkey
      ```

   2. **运行工具**： 运行 `redis-bigkey` 来扫描 Redis 并找出 bigkey。假设你的 Redis 服务器在本地，端口是 6379：

      ```
      bashCopy Coderedis-bigkey --host 127.0.0.1 --port 6379
      ```

      它会输出 Redis 数据库中占用内存最多的键及其内存使用情况。

   **方法 3：使用 `redis-stat` 工具**

   `redis-stat` 是另一个常用的 Redis 监控工具，它可以帮助你查看 Redis 中的各类统计信息，包括内存占用情况。使用方法：

   1. **安装 `redis-stat`**：

      ```
      bashCopy Codegem install redis-stat
      ```

   2. **运行 `redis-stat`**：

      启动监控：

      ```
      bashCopy Coderedis-stat -h 127.0.0.1 -p 6379
      ```

      它会提供 Redis 性能的实时监控数据，包括内存占用。

### 缓存命中性问题

缓存雪崩

缓存击穿

缓存穿透

1. **缓存穿透**： 缓存穿透是指当针对某个特定的 key，无论是缓存中不存在还是后端存储中都不存在，恶意请求可以绕过缓存直接访问后端存储，导致大量请求直接落到数据库或其他存储系统上，引起数据库压力过大甚至宕机。
2. **缓存穿透攻击**： 缓存穿透攻击是一种利用缓存穿透漏洞进行的恶意攻击。攻击者会故意发送一些缓存中肯定不存在的数据请求，以绕过缓存系统直接查询数据库，从而消耗系统资源或者获取敏感信息。这种攻击可能导致系统负载过高、数据库压力增大甚至拖垮整个系统。
3. 造成原因：缓存穿透通常是由恶意请求或者程序错误引起的。
4. 解决方法：
   * 通常是对于不存在的 key 值也进行缓存
   * 使用**布隆过滤器**等数据结构来过滤非法请求
   * 对请求参数进行校验

### 性能问题分析

Redis性能主要存在三个方面：CPU、内存、网络

Redis常见数据类型的底层结构
Redis通信模型
Redis的内存策略