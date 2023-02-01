# MySQL 学习

学习视频：https://www.bilibili.com/video/BV1Kr4y1i7ru/?spm_id_from=333.999.0.0&vd_source=fabefd3fabfadb9324761989b55c26ea

参考链接：https://blog.csdn.net/fannyoona/article/details/105565198

## 概述

1. 基本概念

   ![image-20220929184318530](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291843086.png)

2. 目前主流的数据库管理系统

3. mysql的安装及启动

   * 版本
   * 安装
   * 启动
   * 连接

4. 数据模型

   * 二维表

## SQL语句

1. 通用语法

   ![image-20220929185932212](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291859003.png)

2. SQL语句的分类

   ![image-20220929190026906](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291900741.png)

3. mysql数据类型

   * 数值类型

     ![image-20220929192216973](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291922020.png)

   * 字符串类型

     ![image-20220929192405663](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291936879.png) 

   * 日期类型

     ![image-20220929193610041](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291936189.png)

4. 图形化界面

   * sqlyog
   * Navicat
   * DataGrip

### DDL

1. 数据库操作

   ![image-20220929190845682](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291909371.png)

2. 表操作

   ![image-20220929191028497](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291910688.png)

   ![image-20220929191929527](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291919876.png)

   ![image-20220929195033414](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291950632.png)

   ![image-20220929195114357](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291951052.png)

   ![image-20220929195213082](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291952213.png)

   ![image-20220929195324785](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291953147.png)

3. 小结：

   ![image-20220929195550259](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209291955107.png)

### DML

1. 添加数据（insert）

   ![image-20220930183201553](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301832066.png)

2. 修改数据（update）

   ![image-20220930184320840](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301843301.png)

3. 删除数据（delete）

   ![image-20220930184520139](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301845289.png)

### DQL

1. 基础查询

   ![image-20220930184903204](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301849223.png)

   ![image-20220930185018702](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301850330.png)

2. 条件查询

   ![image-20220930185806321](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301858782.png)

3. 聚合函数

   ![image-20220930190708198](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301907635.png)

4. 分组查询

   ![image-20220930191026093](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301910187.png)

5. 排序查询

   ![image-20220930191553376](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301915129.png)

6. 分页查询

   ![image-20220930191951888](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301919617.png)

7. DQL语句执行顺序

   ![image-20220930192506277](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301925589.png)

8. 小结

   ![image-20220930192826816](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301928109.png)

### DCL

1. 管理用户

   ![image-20220930193235515](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301932090.png)

2. 权限控制

   ![image-20220930193601788](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301936081.png)

   ![image-20220930193701408](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209301937630.png)

## 函数

1. 概念：函数是指一段可以直接被另一段程序调用的程序或代码。

2. 字符串函数

   ![image-20221117185754047](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211171858195.png)

3. 数值函数

   ![image-20221117190537640](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211171905738.png)

4. 日期函数

   ![image-20221117191308114](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211171913400.png)

5. 流程函数

   ![image-20221117193120191](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211171931769.png)

## 约束

1. 概念：约束是作用于表中字段上的规则，用于限制存储在表中的数据。

2. 目的：保证数据库中数据的正确、有效性和完整性。

3. 分类

   ![image-20221117193229448](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211171932772.png)

4. 外键约束

   * 外键用来让两张表的数据之间建立连接,从而保证数据的一致性和完整性。

   * 语法

     ![image-20221117194730658](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211171947413.png)

   * 删除/更新行为

     ![image-20221117195653639](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211171958957.png)

## 多表查询

1. 多表间基本关系
   * 一对一
   * 一对多
   * 多对多
   
2. 笛卡尔积

   1. 多表查询的分类

   * 连接查询
     * 内连接：相当于查询A、B交集部分数据
     * 外连接
       * 左外连接：查询左表所有数据，以及两张表交集部分数据
       * 右外连接：查询右表所有数据，以及两张表交集部分数据
     * 自连接：当前表与自身的连接查询，自连接必须使用表的别名
   * 子查询

4. 内连接

   ![image-20221117204115574](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211172046948.png)

5. 外连接

   ![image-20221117204620913](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211172046393.png)

6. 自连接

   ![image-20221117205212885](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211172052309.png)

7. 联合查询

   ![image-20221117205448015](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211172054517.png)

8. 子查询

   * 标量子查询(子查询结果为单个值)
     * 常用操作符：=、>=、<=
   * 列子查询(子查询结果为一列
     * 常用的操作符: IN、NOT IN、ANY、 SOME、ALL
   * 行子查询(子查询结果为一行)
   * 表子查询(子查询结果为多行多列

   > 注意：子查询的位置可以在where、from、select之后

## 事务

1. 概念：事务是一组操作的集合，它是一个不可分割的工作单位，事务会把所有的操作作为一一个整体一起向系统提交或撤销操作请求，即这些操作要么同时成功，要么同时失败。

2. 基本操作

   * 方式一：

     ![image-20221117213224636](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301131453535.png)

   * 方式二：

     ![image-20221117213306222](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211172133460.png)

3. 四大特性(CIAD)

   * 原子性. (Atomicity) ：事务是不可分割的最小操作单元，要么全部成功，要么全部失败。
   * 一致性(Consistency) ：事务完成时，必须使所有的数据都保持一致状态。
   * 隔离性(Isolation)：数据库系统提供的隔离机制，保证事务在不受外部并发操作影响的独立环境下运行。
   * 持久性(Durability) ：事务一旦提交或回滚，它对数据库中的数据的改变就是永久的。

4. 并发事务

   * 引发的问题

     * 脏读
   
     * 不可重复读

       ![image-20230124094712069](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301240947657.png)

     * 幻读

     ![image-20221117214004968](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211172140596.png)

   * 事务的隔离级别

     * 类型

       ![image-20221117214200429](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211172142141.png)
   
     * 操作
   
       ![image-20221117214316834](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211172144698.png)

## 存储引擎

### MYSQL体系结构

![image-20221118204613913](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182046122.png)

![image-20221118204717244](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182047687.png)

### 存储引擎

1. 存储引擎：存储引擎就是存储数据、建立索弧更新/查询数据等技术的实现方式。**存储引擎是基于表的**，而不是基于库的,所以存储引擎也可被称为表类型。

2. 查看当前数据库支持的存储引擎

   ~~~sql
   show engines;
   ~~~

3. 在创建表时，指定存储引擎

   ~~~sql
   create table 表名(
       # 字段
   	...
   ) engine = INNODB;
   ~~~

4. 存储引擎特点

   * INNODB

     ![image-20221118210239601](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182108215.png)

     ![image-20221118210838607](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182108992.png)

   * MYISAM

     ![image-20221118211056369](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182110733.png)

   * Memory

     ![image-20221118211131982](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182111068.png)

   ![image-20221118211217014](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182112545.png)

   > 注：MySQL中存储引擎为INNODB的表的文件在目录C:\ProgramData\MySQL\MySQL Server 8.0\Data中（Windows），可以通过cmd命令行命令ibd2sdi提取查看文件数据

5. 存储引擎的选择

   ![image-20221118211341200](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182113097.png)

### INNODB

## 索引

### 概述

1. 索引：索引(index)是帮助MySQL高效获取数据的**数据结构**(有序)。

2. 优缺点

   ![image-20221125203610782](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211252036399.png)

### 索引结构

1. MySQL的索引是在存储引擎层实现的，不同的存储引擎有不同的结构，主要包含以下几种:

   ![image-20221125203708806](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211252037696.png)

   ![image-20221125203802196](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211252038644.png)

#### B-Tree

* 特性
  * 允许一个结点包含过个key
  * 对于M阶B树，每个结点最多有M-1个key并以升序排列，每个结点最多有M个子结点，根结点至少有两个子结点。

![image-20221125204507836](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211252045218.png)

#### B+树

* 特性：B树的变形
  * 非叶结点仅具有索引作用（即非叶子结点只存储key不存储value）
  * 树的所有叶结点构成一个有序链表，即可以按照key排序的次序遍历全部数据

#### B+树索引

1. 二叉树结构的缺点：顺序插入时，会形成-一个链表, 查询性能大大降低。大数据量情况下，层级较深,检索速度慢。

2. 平衡二叉树结构的缺点：大数据量情况下，层级较深，检索速度慢。

4. B+Tree

   * 相对于B-Tree的区别
     * 所有数据都会出现在叶子节点
     * 叶子节点形成一个单向链表

   ![image-20221125204806093](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211252048354.png)

5. mysql中的B+Tree：MySQL索引数据结构对经典的B+Tree进行了优化。在原B+Tree的基础. 上,增加一个指向相邻叶子节点的链表指针，就形成了带有顺序指针的B+Tree,提高区间访问的性能。

   ![image-20221125205030347](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211252050009.png)

#### Hash索引

1. 哈希索引就是采用一-定的hash算法，将键值换算成新的hash值，映射到对应的槽位上,然后存储在hash表中。
2. 特点
   * Hash索引只能用于对等比较(=，in)， 不支持范围查询(between, >，<, ..
   * 无法利用索引完成排序操作
   * 查询效率高，通常只需要- -次检索就可以了 ，效率通常要高于B+tree索引
3. 支持的存储引擎：在MySQL中，支持hash索引的是Memory引擎, 而InnoDB中具 有自适应hash功能，hash索引是存储引擎根据B+Tree索引在指定条件下自动构建的。

### 索引分类

![image-20230124113618926](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301241136671.png)

在InnoDB存储引擎中，根据索引的存储形式，又可以分为以下两种：

![image-20230124113741695](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301241137594.png)

聚集索引的选取规则：

* 如果存在主键，主键索引就是聚集索引。
* 如果不存在主键，将使用第一价唯一(UNIQUE) 索引作为聚集索引。
* 如果表没有主键，或没有合适的唯一索引， 则InnoDB会自动生成-个rowid作为隐藏的聚集索引。

![image-20230124114228364](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301241142549.png)

![image-20230124114341385](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301241143026.png)

### 索引语法

![image-20230125221021096](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301252210103.png)



## SQL优化

## 视图

## 存储过程

## 触发器

## 锁

## MYSQL管理

## 常用操作汇总

### 1. 常用命令

~~~ mysql
show databases;//查看当前所有的数据库
use+库名;//打开指定的库
（只要用了use你就在那个库中了）
select database();//查看当前所在库
show tables;//查看当前库所有的表
show tables from 库名;//查看其他库所有的表
create table 表名(
	列名 列类型，
	列名 列类型，
	...
)//创建表
desc 表名;//查看表的结构
查看服务器的版本：
方式一：登录到mysql服务端
select version();
方式二：没有登录到mysql服务端
mysql --version或mysql --V
~~~

### 2. 条件查询

~~~ sql
1.按条件表达式筛选
	条件运算符: > < = != <>(不等于) >= <=
2.按逻辑表达式筛选
	逻辑运算符：&& || !
		    and or not
	作用：连接条件表达式
3.模糊查询
		like(通配符：% 表示任意多个字符		_表示单个任意字符)
		between ... and ...（包含临界值）
		in ...
		is null
~~~

### 3. 排序查询

~~~ sql
select 查询列表 from 表名 [where 筛选条件] order by 排序列表 [ASC|DESC];
说明：
	1. ASC代表升序，DESC代表降序，默认为升序排列
	2、order by子句中可以支持单个字段、多个字段、表达式、函数、别名
	3、order by子句一般是放在查询语句的最后面，limit子句除外
~~~

### 4. 常用函数

~~~sql
select 函数名(实参列表) [from 表(根据需要)];
说明：
	分类：
	1）单行函数（字符函数，数学函数，日期函数，其他函数，流程控制函数）
	如concat、length、ifnull等
	2）分组函数
	功能：做统计使用，又称为统计函数、聚合函数、组函数
	----------------------------------------------------------------
	常见函数：
	字符函数:length  concat substr
	instr trim upper lower
	lpad rpad replace
	
	数学函数： round ceil floor truncate mod
	
	日期函数：now curdate curtime year month monthname 
	day hour minute second str_to_date  date_format
	
	其他函数：version database user
	
	控制函数: if case
~~~

### 5. 分组查询

~~~sql
select 分组函数（max，min这些），列（要求出现在group by后面）
	from 表
	【where 筛选条件】
	group by 分组的列表
	【order by】子句
注意：查询列表必须特殊，要求是分组函数和group by后出现的字段。
	1）分组查询中的筛选条件分为两类（筛选的数据源不同
                        数据源           位置		    关键字
	分组前筛选：    原始表	   group by子句前面	    where
	分组后筛选：分组后的结果集   group by子句后面	    having
	①分组函数做条件，肯定是放在having子句中
	②能用分组前筛选的，优先考虑用分组前筛选
	2）group by子句支持单个字段分组，多个字段分组，
	（多个字段之间用逗号隔开无顺序要求），表达式或函数（用的较少）
	3）可添加排序（放在group by后）
~~~

### 6. 连接查询

~~~sql
1. 连接查询：又称多表查询，当查询的字段来自多个表，就会用到连接查询
2. 分类：
	内连接：等值连接，非等值连接，自连接
	外连接：左外连接，右外连接，全外连接
	交叉连接
3.各连接详细解读
	1）等值连接
    ①多表等值连接的结果为多表的交集部分
    ②n表连接，至少需要n-1个连接条件
    ③多表的顺序无要求
    ④一般需要为表起别名
    ⑤可以搭配前面介绍的所有查询子句使用，比如排序，分组，筛选
    2）非等值连接
    3）自连接
    4）内连接
    select 查询列表
    from 表1 别名
    inner join 表2 别名
    on 连接条件；
    5）外连接
    应用场景：用于查找一个表中有，另一个表中没有的记录
     i.外连接的查询结果为主表中所有的记录
       如果从表中有和它匹配的，则显示匹配的值
       如果从表中没有和它匹配的，则显示null
       外连接查询结果=内连接结果+主表中有而从表中没有的记录
    ii.左外连接：left jon左边的是主表
       右外连接：right join右边的是主表
    iii.左外和右外交换两个表的顺序，可以实现同样的效果
    iV.全外连接=内连接结果+表1有但表2没有+表2有但表1没有
~~~

### 7. 子查询

~~~sql
1.子查询：出现在其他语句内部的select语句，称为子查询或内查询
外部的查询语句，称为主查询或外查询
2.分类：
按子查询出现的位置：
	     select后面：仅仅支持标量子查询
	     from后面：支持表子查询
      ☆ where或者having后面：标量子查询，列子查询，行子查询
	     exists后面（相关子查询）：表子查询
按结果集的行列数不同：
	    标量子查询（结果集只有一行一列）
		列子查询（结果集只有一列多行）
		行子查询（结果集有一行多列）
		表子查询（结果集一般为多行多列）
		
3.解释：
1)where或者having后面
	特点：
①子查询放在小括号内
②子查询一般放在条件右侧
③标量子查询，一般搭配单行操作符使用
> < >= <= = <>
列子查询一般搭配多行操作符使用
IN/NOT IN、ANY/SOME、ALL
④子查询的执行优先于主查询执行
2)select后面
3）from 后面
4）exists后面
~~~

### 8. 分页查询

~~~sql
1.应用场景：当要显示的数据一页显示不全，需要分页提交sql请求
2.语法：
		select 查询列表
		from 表
		【join type join 表2
		where 筛选条件
		group by 分组字段
		having 分组后的筛选
		order by 排序的字段】
		limit offset，size;
	说明：offset:要显示条目的起始索引，起始索引从0开始
		size：要显示的条目数
		①limit语句放在查询语句的最后
		②公式
		要显示的页数 page，每页的条目数size
		select 查询列表
		from 表
		limit (page-1)*size,size;
~~~

### 9. 表数据相关（DML）

~~~sql
1. 插入语句insert
    方式一：insert into 表名(列名,...) values(值1，...);
    方式二：insert into 表名 set 列名=值，列名=值...
2. 删除语句delete
	update 表名
    set 列=新值,列=新值,...
    where 筛选条件;
3. 更新语句update
	delete from 表名 where 筛选条件
~~~

### 10. 数据库或表结构相关（DDL语句）

~~~sql
常见约束

CREATE TABLE 表名(
	字段名 字段类型 列级约束
	字段名 字段类型，
	表级约束
);

含义：一种限制，用于限制表中的数据，为了保证表中数据的准确性和可靠性

分类：六大约束
	not null:非空，用于保证该字段的值不能为空。比如姓名、学号等
	default：默认，用于保证该字段有默认值。比如性别
	primary key：主键，用于保证该字段的值有唯一性，并且非空。比如学号
	unique：唯一，保证该字段的值有唯一性，可以为空。比如座位号
	check：检查约束【mysql不支持】，比如年龄性别
	foreign key：外键，用于限制两个表的关系，保证该字段值必须来自于主表关联列的值
		    在从表添加外键约束，用于引用主表中某列的值
		    比如：员工表的部门编号、工种号

添加约束的时间：
	1、创建表时
	2、修改表时
约束的添加分类：
	1、列级约束：六大约束语法上都支持，但外键约束没有效果
	2、表级约束：除了非空、默认约束，其他都支持
~~~

### 12. 事务

事务：一个或一组sql语句组成一个执行单元，这个执行单元要么全部执行，要么全部不执行。如果单元中某条sql语句一旦执行失败或产生错误，整个单元将会回滚。
~~~sql
/*
事务的创建

1、隐式事务：事务没有明显的开启和结束的标记
比如insert、update、delete语句

delete from 表 where id=1；

2、显式事务：事务具有明显的开启和结束的标记
前提：必须先设置自动提交功能为禁用
SHOW VARIABLES LIKE '%autocommit%';
set autocommit=0;

步骤1：开启事务
set autocommit=0;
start transaction;#可选的

步骤2：编写事务中的sql语句(select,insert,update,delete增删改查，不包括create，drop这些)
语句1;
语句2;
...

步骤3：结束事务
commit;提交事务
rollback;回滚事务
save point 节点名;#设置保存点

*/

CREATE DATABASE test;

CREATE TABLE account(
	id INT PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(20),
	balance DOUBLE
);
INSERT INTO account(username,balance)
VALUES('张无忌',1000),('赵敏',1000);

#演示事务的使用步骤
SET autocommit=0;
#编写一组事务的语句
UPDATE account SET balance=500 WHERE username='张无忌';
UPDATE account SET balance=1500 WHERE username='赵敏';

#结束事务
#commit;
ROLLBACK;#把500,1500改成1000,1000，执行回滚，发现还是500,1500

SELECT * FROM account;

#演示savepoint的使用
SET autocommit=0;
START TRANSACTION;

DELETE FROM account WHERE id=1;
SAVEPOINT a;#设置保存点
DELETE FROM account WHERE id=2;

ROLLBACK TO a;#回滚到保存点
SELECT * FROM account;#1号删了，2号没删
~~~

### 13. 存储过程

含义：
一组预先编译好的sql语句的集合，理解成批处理语句

好处：
1、提高代码的重用性
2、简化操作
3、减少了编译次数，并且减少了和数据库服务器的连接次数，提高了效率

~~~sql
#一、创建语法

CREATE PROCEDURE 存储过程名(参数列表)
BEGIN
	存储过程体（一组合法的SQL语句）
END

注意：
1、参数列表包含三部分
参数模式 参数名 参数类型
举例：
IN stuname VARCHAR(20)

参数模式：
IN:该参数可以作为输入，即需要调用方传入值
OUT:参数可以作为输出，即可以作为返回值
INOUT:该参数既可以作为输入又可以作为输出，也就是既需要传入值，又可以返回值

2、如果存储过程体只有一句话, BEGIN END 可以省略
存储过程体中每条sql语句结尾必须加分号
存储过程的结尾可以使用 DELIMITER 重新设置
语法：
DELIMITER 结束标记
例如：
DELIMITER $

#二、调用语法
CALL 存储过程名(实参列表);
~~~

### 14. 函数

~~~sql
#一、创建语法
CREATE FUNCTION 函数名(参数列表) RETURNS 返回类型
BEGIN
	函数体
END
/*
注意：
1、参数列表包含两部分-----参数名 参数类型

2、函数体：肯定会有return语句，如果没有会报错
如果return语句没有放在函数体最后也不报错，但不建议

return 值;

3、当函数体只有一句话可以省略begin，end

4、使用delimiter语句设置结束标记

*/

#二、调用语法
SELECT 函数名(参数列表)
~~~

### 代码示例

~~~sql
# 1.query one field from a table
select last_name from employees;

# 2.query fields from a table
select last_name,salary,email from employees;

# 3.query all fields from a table
select * from employees;

# 4.query const values
select 100;

-- 5.give an alias
# use as for the keyword
select last_name as 姓 from employees;
select last_name 姓 from employees;

# 6. 去重
# 查询员工表中所有涉及到的部门编号
select distinct department_id from employees;

# 查询员工姓和名连接成一个字段，并显示为姓名
select concat(last_name,first_name) 姓名 from employees;
# 判断是否为空,为空返回0
select IFNULL(commission_pct,0) 奖金率,commission_pct from employees;

======================================================================
-- 1. 查询工资>12000的员工信息
select * from employees where salary>12000;

-- 2. 查询部门编号不等于90号的员工名和部门编号
select last_name,department_id from employees where department_id!=90;

-- 3. 查询工资在10000到20000之间的员工名，工资和奖金
select 
	last_name,
	salary,
	commission_pct
from
	employees
where
	salary between 10000 and 20000;
	

select 
	last_name,
	salary,
	commission_pct
from
	employees
where
	salary>=10000 and salary<=20000;
	
	-- 4. 查询部门编号不在90-110之间，或者工资高于15000的员工信息
	select
		*
	from 
		employees
	where
		department_id not in(90,110) or salary>15000;
		
	select
		*
	from 
		employees
	where
		department_id<90 or department_id>110 or salary>15000;
		
-- 5. 查询员工名中包含字符a的员工信息
	select * from employees where last_name like '%a%';
	
-- 6. 查询员工名中第3个字符为n，第五个字符为l的员工名和工资
	select
		last_name,
		salary
	from
		employees
	where
		last_name like '__n_l%';
		
-- 7. 查询员工名中第二个字符为_的员工名（转义字符）
	select
		last_name
	from
		employees
	where
		last_name like '_\_%';
		
-- 8. 查询员工编号在100到120之间的员工信息
	select
		*
	from
		employees
	where
		employee_id between 100 and 120;
		
		
-- 9. 查询员工的工种编号是 IT_PROT, AD_VP, AD_PRES中的一个的员工名和工种编号
	select
		last_name,
		job_id
	from
		employees
	where
		job_id in('IT_PROT', 'AD_VP','AD_PRES');
		
		
-- 10. 查询没有奖金的员工名和奖金率
	select
		last_name,
		commission_pct
	from
		employees
	where
		commission_pct is null;
#安全等于  <=>  is null可以换成<=> null

-- 11. 查询员工信息，要求工资从高到低排序
select * from employees order by salary DESC;

-- 12. 查询部门编号>=90的员工信息，按入职时间的先后进行排序
select * from employees where department_id>=90 order by hiredate;

-- 13. 按年薪高低显示员工的信息和年薪[按表达式排序]
select *,12*salary 年薪 from employees order by 12*salary;

-- 14. 按姓名的长度显示员工的姓名和工资 [按函数排序]
select last_name,salary from employees order by LENGTH(last_name);

-- 15.查询员工信息，要求先按工资升序，再按员工编号降序 [按多个字段排序]
select * from employees order by salary ASC,employee_id DESC;


-- 16.length 获取参数值的字节个数
select length('hnon');

-- 17.concat 拼接字符串（用下划线拼接）
select concat(last_name,'.',first_name) from employees;

-- 18.变大写，变小写
select upper('tom');
select lower('TOM');

-- 19.substr,substring
# 注意：索引从1开始
select substr('chenwenjian',5);
select substr('chenwenjian',5,3);

-- 20.instr 返回子串的起始索引，找不到返回0
select instr('chenwenjian','wenjian');

-- 21.trim 去掉首尾指定字符
select trim('          chenwenjian     ');
select trim('a'from'aaa aabbbchenwenjianbbbbaaa');

-- 22.lpad 用指定的字符实现左填充指定长度
select lpad('chenwenjian',20,'**');

-- 23.rpad  用指定的字符实现右填充指定长度
select rpad('chen',10,'++++');

-- 24.replace 替换
select replace('chenwenjian','wen','whymechen');

-- 25.round 四舍五入
select round(3.14);
#1.57,小数点后保留2位
SELECT ROUND(1.567,2);

-- 26. ceil 向上取整，返回>=该参数的最小整数
select ceil(5.6);

-- 27.floor 向下取整，返回<=该参数的最大整数
select floor(5.6);

-- 28.truncate 截断
select truncate(1.6897438297423,5);

-- 29.mod 取余
select mod(10,-3);

-- 30.now 返回当前系统日期加时间
select now();

-- 31.curdate 返回当前系统日期，不包含时间
select curdate();

-- 32.返回当前系统日期，不包含时间
select year(now());

-- 33.str_to_date 将日期格式字符串转换成指定格式日期
-- %Y 四位的年份
-- %y 2位的年份
-- %m 月份 （01,02，...12）
-- %c 月份（1,2，..., 12）
-- %d 日
-- %H小时（24）%h（12）
-- %i 分钟  %s秒
select str_to_date('2020-5-8','%Y-%m-%d');

-- 33.date_format 将日期转换成字符
select date_format(now(),'%Y/%m/%d');

-- 34.if
select if(6>9,'true','false');

-- 35.查询员工的工资：要求
-- 部门号=30，显示的工资为1.1倍
-- 部门号=40，显示的工资为1.2倍
-- 部门号=50，显示的工资为1.3倍
-- 其他部门显示原工资
SELECT salary,department_id,
CASE department_id
WHEN 30 THEN salary*1.1
WHEN 40 THEN salary*1.2
WHEN 50 THEN salary*1.3
ELSE salary
END AS 新工资
FROM employees;

-- 36.sum 求和、avg平均值、max、min、count计算个数
select sum(salary) from employees;
select avg(salary) from employees;
select max(salary) from employees;
SELECT min(salary) from employees;
select count(salary) from employees;

-- 37.查询每个工种的最高工资
select max(salary),job_id from employees group by job_id;

-- 38.查询每个位置上的部门个数
select count(*),department_id from departments group by location_id;

-- 39.查询邮箱中包含a字符的，每个部门的平均工资
select avg(salary) from employees where email like '%a%' group by department_id;
-- select avg(salary) from employees group by department_id having email like '%a%';

-- 40.查询有奖金的每个领导手下员工的最高工资

-- 41.查询哪个部门的员工个数大于2
select department_id,count(*) from employees group by department_id having count(*)>2;

-- 42.查询员工名和对应的部门名
select last_name,department_name from employees,departments where employees.department_id=departments.department_id;

-- 43.查询员工名和上级的名称
select e.last_name 员工名字,m.last_name 上级名字 from employees e,employees m where e.manager_id=m.department_id;

-- 44.查询员工名，部门名
select e.last_name,d.department_name from employees e inner join departments d on e.department_id=d.department_id;

-- 45.查询部门个数>3的城市名和部门个数（添加分组+筛选）
select l.city,count(*) 部门个数 
from departments d 
inner join locations l 
on d.location_id=l.location_id 
group by city 
having count(*)>3;

-- 46.查询哪个城市没有部门
select locations.city from locations left join departments on departments.location_id=locations.location_id where departments.department_id is null;


-- 47.谁的工资比Abel高
select last_name from employees where salary>(select salary from employees where last_name='Abel');

-- 48.返回job_id与141号员工相同，salary比143号员工多的员工姓名，
-- job_id和工资
select last_name,job_id,salary from employees where salary>(select salary from employees where employee_id=143) and job_id=(select job_id from employees where employee_id=141);

-- 49.返回location_id是1400或1700的部门中所有员工姓名
select last_name from employees where department_id in(select distinct department_id from departments where location_id=1400 or location_id= 1700);

-- 49.返回其他工种中比job_id为‘IT_PROG'部门任一工资低的员工信息
select * from employees where salary<all(select distinct salary from employees where job_id='IT_PROG') and job_id <> 'IN_PROG';

-- 50.查询员工编号最小并且工资最高的员工信息
select * from employees where employee_id=(select min(employee_id) from employees) and salary=(select max(salary) from employees);

-- 51.查询每个部门的员工个数
select department_name,(select count(*) from employees where employees.department_id=departments.department_id) from departments;

-- 52.查询有员工的部门名
select department_name from departments where exists(select * from employees where departments.department_id=employees.department_id);

-- 53.查询第11条——第25条员工信息
select * from employees limit 11,15; 
~~~

## SQL语句练习

常用SQL语句练习案例链接：https://www.cnblogs.com/Diyo/p/11424844.html

牛客网：https://www.nowcoder.com/？

# 《SQL必知必会》学习笔记

## 数据库基础

### 基本概念

1. 数据库

   保存有组织的数据的容器

2. 表

   某种特定类型数据的结构化清单

3. 列和数据类型

   列：表中的一个字段，所有的表都是由一个或多个列组合而成。

   数据类型：每个列都有相应的数据类型来限制该列中存储的数据

4. 行

   表中的一个记录。

5. 主键

   一列（或一组列），其值可以唯一标识表中每一行。

   主键应该满足如下条件：

   > + 任意两行都不具有相同的主键值
   > + 每一行都必须具有一个主键值（主键值列不允许NULL值）
   > + 主键列中的值不允许修改或更新
   > + 主键值不能重复（如果某行从表中删除，它的主键不能赋给以后的新行）

### 什么是SQL

SQL是结构化查询语言（Structured Query Language）的缩写。SQL是一种专门用来与数据库沟通的语言。

## 检索数据

### SELECT语句

1. 检索单个列

   ~~~sql
   SELECT 列名 FROM 表名;
   ~~~

   注意：SQL语句是不区分大小写的。

   ​			在处理SQL语句时，其中所有空格都是被忽略的。

2. 检索多个列

   ~~~sql
   SELECT 列名1,列名2,.... FROM 表名;
   ~~~

3. 检索所有列

   ~~~sql
   SELECT * FROM 表名;
   ~~~

4. 检索不同的值

   ~~~sql
   SELECT DISTINICT 列名 FROM 表名; 
   ~~~

   注意：distinct关键字作用于所有列，而不是只作用域紧跟其后的一列。

5. 限制结果

   ~~~sql
   //SQL Server和Access中，使用top关键字来限定返回结果的行数
   SELECT TOP 行数 列名 FROM 表名;
   //DB2中
   SELECT 列名 FROM 表名 FETCH FIRST 行数 ROWS ONLY;
   //Oracle中，基于ROWNUM（行计数器）实现
   SELEct 列名 FROM 表名 WHERE ROWNUM <=行数;
   //MySQL、MariaDB、PostgreSQL、SQLite，使用LIMIT子句实现
   SELECT 列名 FROM 表名 LIMIT 行数;
   SELECT 列名 FROM 表名 LIMIT 行数 OFFSET 起始行;//注意：第一个被检索的是0行，而非1行
   ~~~

6. 注释

   使用--（两个连字符）或者#

   /**/进行多行注释

## 排序检索数据

### 排序数据

1. 使用子句order by对检索出的数据进行排序。

   ~~~sql
   SELECT 列名 FROM 表名 ORDER BY 列名;
   ~~~

   注意：在指定一条order by子句时，应该保证它是select语句中的最后一条子句。否则，会出现错误。

2. 按多个列排序

   ~~~sql
   SELECT 列名 FROM 表名 ORDER BY 列名1,列名2,...;
   ~~~

3. 按列位置排序

### 指定排序方向

使用关键字DESC来实现指定降序排序。 

~~~sql
SELECT 列名 FROM 表名 ORDER BY 列名 DESC;
~~~

+++

## 过滤数据

使用where子句指定搜索条件。

### 使用where子句

~~~sql
SELECT 列名 FROM 表名 WHERE 条件;
~~~

### where子句操作符

## 高级数据过滤

## 使用存储过程

### 什么是存储过程



### 为什么要使用存储过程



### 怎么使用存储过程







