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





