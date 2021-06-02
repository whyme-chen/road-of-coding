# SQL必知必会读书笔记

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

+++

### 什么是SQL

SQL是结构化查询语言（Structured Query Language）的缩写。SQL是一种专门用来与数据库沟通的语言。

+++

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

+++

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





# MySQL 知识总结

参考链接：https://blog.csdn.net/fannyoona/article/details/105565198

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



经典查询案例链接：https://www.cnblogs.com/Diyo/p/11424844.html





