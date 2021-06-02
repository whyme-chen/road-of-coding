# 面向对象编程

1. 面向对象三个特征：

* 封装性
* 继承性
* 多态性

2. 面向对象程序开发三个步骤：

* OOA：面向对象分析
* OOD：面向对象设计
* OOP：面向对象编程

3. 类与对象
   * 类：对某一类事物的共性抽象概念
   * 对象：描述的是一个具体的事物
4. this关键字
   * 使用this调用属性
   * 使用this调用方法

# 数组

### 一维数组

1. 定义语法
2. 使用
3. 遍历（foreach）
4. 注意：数组的下标从0开始，到数组的长度减一结束。

### 二维数组

1. 定义语法
2. 使用
3. 遍历（foreach）
4. 实质：数组的数组，因此每一列的长度可以不一样。

### 相关类库

1. 排序：java.util.Arrays.sort()
2. 拷贝：System.arraycopy(原数组，原数组开始点，新数组，新数组开始点，拷贝长度)
3.  可变参数：实质就是数组

# 集合



# Junit单元测试

1.测试分类

* 黑盒测试
* 白盒测试

2. Junit使用

   步骤：

   * 定义一个测试类
   * 定义测试方法
   * 给方法添加@Test
   * 导入Junit依赖环境

3. 补充：

   * @Before：修饰的方法会在测试方法之前被自动执行
   * @After：修饰的方法会在测试方法执行之后自动执行

# 反射（框架设计的灵魂）

框架：半成品软件。可以在框架的基础上进行软件开发，简化编码。

反射：将类的各个组成部分封装为其他对象，这就是反射机制。

![image-20210202115502782](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210202115502782.png)

1. 获取Class对象的方式：

   * Class.forName("全类名");将字节码文件加载进内存，返回Class对象（多用于配置文件）
   * 类名.class：通过类名的属性class获取（多用于参数传递）
   * 对象.getClass():getClass（）方法

   注意：同一个字节码文件（*.class）在一次程序运行中，只会被加载一次，不论通过哪种方式获得的Class对象都是同一个对象

2. Class对象的功能

   * 获取成员变量

     * Field[ ] getFields():获取所有public修饰的成员变量
     * Field getField(String name)：获取指定名称的public成员变量
     * Field[ ] getDeclaredFields()
     * Field getDeclaredField(String name) 

   * 获取成员方法

     * Method[ ] getMethods()
     * Method getMethod(String name,类<?> parameterTypes)
     * Method[ ] getDeclaredMethods()
     * Method getDeclaredMethod(String name,类<?> parameterTypes)

   * 获取构造方法

     * Constructor<?>[ ] getConstructors()
     * Constructor<T>  getConstructor(类<?> parametertypes)
     * Constructor<T> getDeclaredConstructor(类<?> parameterTypes)
     * Constructor<?>[ ] getDeclaredConsructor()  

   * 获取类名

     getName()

# 注解

1. 注解：一种代码级别的说明

2. JDK中预定义的一些注解

   * @override：检测被该注解标注的方法是否继承自父类
   * @Deprecated：该注解标注的内容，表示已过时
   * @SuppressWarnings：压制警告

3. 自定义注解

   * 格式：

     元注解：用于描述注解的注解

     * @target：描述注解能够作用的位置
     * @Retention：描述注解被保留的阶段
     * @Documented：描述注解是否被抽取到api文档中
     * Inherited：描述注解是否被子类继承

     public @interface 注解名称{}

4. 在程序中解析（使用）注解

# XML

1. XML

   Extensible Markup Language 可扩展标记语言。

   * 可扩展：标签都是自定义的
   * 功能（传输和存储数据）
     * 作为配置文件
     * 在网络中传输
   * XML与HTML的区别（w3c：万维网联盟）
     * XML标签都是自定义的，HTML标签都是预定义的
     * XML的语法严格，HTML语法松散
     * XML是存储数据的，HTML是展示数据的

2. XML用途

   * 把数据从HTML分离
   * 简化数据共享
   * 简化数据传输
   * 简化平台变更
   * 使数据更有用
   * 用于创建新的互联网语言

3. XML树结构

   一个文档实例：

   ~~~xml
   <?xml version="1.0" encoding="UTF-8"?><!--xml声明,声明版本和字符编码-->
   <note><!--根元素-->
       <to>Tove</to><!--子元素-->
       <from>Jani</from><!--子元素-->
       <heading>Reminder</heading><!--子元素-->
       <body>Don't forget me</body><!--子元素-->
   </note>
   ~~~

   说明：

   * xml文档必须包含根元素，该元素是所有其他元素的父元素。
   * 所有的元素都可以有子元素。
   * 所有元素都可以有文本内容和属性。
   * ![DOM node tree](https://www.runoob.com/wp-content/uploads/2013/09/nodetree.gif)

4. 语法

   * 基本语法

     xml文档的后缀名为.xml

     xml第一行必须定义文档声明

     xml文档中有且仅有一个根标签

     属性值必须使用引号引起

     标签必须正确关闭

     xml标签名称区分大小写

     xml必须正确嵌套

     xml属性值必须加引号

     **实体引用**（在xml中有五个预定义的实体引用）

     | &lt;   | <    | less than      |
     | ------ | ---- | -------------- |
     | &gt;   | >    | greater than   |
     | &amp;  | &    | ampersand      |
     | &apos; | '    | apostrophe     |
     | &quot; | "    | quotation mark |

     xml的注释：<!--注释内容-->

     xml中空格会被保留（不同于HTML）

     xml以LF存储换行

   * 组成部分

     * 文档声明

       * 格式：<?xml 属性列表 ?>
       * 属性列表
         * version：版本号，必须的属性
         * encoding：编码方式，告知解析引擎当前文档使用的字符集，默认：ISO-8859-1
         * standalone：是否独立

     * 指令

     * 标签

       * xml命名规则
         * 名称可以包含字母，数字和其他字符
         * 名称不能以数字或者标点符号开始
         * 名称不能以xml开始
         * 名称不能包含空格

     * 属性（在 XML 中，您应该尽量避免使用属性。如果信息感觉起来很像数据，那么请使用元素吧。）

     * 文本

       CDATA区：在该区域中的数据会被原样展示

       * 格式：<![CDATA[数据]]>

   * 约束：规定xml文档的书写规则

     * 分类
       * DTD：一种简单的约束技术
       * Schema：一种复杂的约束技术

5. XML验证

   合法的 XML 文档是"形式良好"的 XML 文档，这也符合文档类型定义（DTD）的规则

   ~~~xml
   <?xml version="1.0" encoding="ISO-8859-1"?>
   <!DOCTYPE note SYSTEM "Note.dtd"><!--声明对外部DTD文件的引用-->
   <note>
   <to>Tove</to>
   <from>Jani</from>
   <heading>Reminder</heading>
   <body>Don't forget me this weekend!</body>
   </note>
   ~~~

   DTD的目的是定义XML文档的结构，它使用一系列合法的元素来定义文档的结构。

   ~~~dtd
   <!DOCTYPE note
   [
   <!ELEMENT note (to,from,heading,body)>
   <!ELEMENT to (#PCDATA)>
   <!ELEMENT from (#PCDATA)>
   <!ELEMENT heading (#PCDATA)>
   <!ELEMENT body (#PCDATA)>
   ]>
   ~~~

   **XML验证器**

6. XML查看

7. 解析XML（XML解析器把XML文档转换为XML DOM对象）

   1. 解析：操作xml文档，将文档中的数据读取到内存中

   2. 解析xml方式：

   * DOM：将标记语言文档一次性加载进内存，在内存中形成一棵dom树
     * 优点：操作方便，可以对文档进行CRUD所有操作
     * 缺点：占内存
   * SAX：逐行读取，基于事件驱动
     * 优点：不占内存
     * 缺点：只能读取，不能增删改

   3. xml常见的解析器：

      * JAXP：sun公司提供的解析器，支持dom和sax两种思想
      * DOM4J：一款非常优秀的解析器
      * Jsoup：
      * PULL：Android操作系统内置解析器

      Jsoup使用

      Jsoup对象的使用：

      * Jsoup：工具类，可以解析
      * Document：文档对象。代表内存中的dom树
      * Elements：元素Element对象的集合，
      * Node：结点对象

8. XML JavaScript

   1. XMLHttpRequest对象（用于在后台与服务器交换数据）

   ~~~xml
   <!--创建XMLHttpRequest对象-->
   xmlhttp=new XMlHttpRequest();
   ~~~

   2. XML

# Tomcat

### web相关概念回顾

1. 软件架构

   * C/S：客户端/服务器端
   * B/S：浏览器/服务器端

2. 资源分类

   * 静态资源：所有用户访问后，得到的结果都是一样的，称为静态资源。静态资源可以直接被浏览器直接解析

     ​				如：html，css，javaScricpt

   * 动态资源：每个用户访问相同资源后，得到的结果可能不一样，称为动态资源。动态资源被访问后需要先转换为静态资源，再返回给浏览器

     ​				如：Servlet，jsp，php，asp

3. 网络通信的三要素

   * IP：电子设备（计算机）在网络中的唯一标识。
   * 端口：应用程序在计算机中的唯一标识（0~65536）
   * 传输协议：规定了数据传输的规则
     * 基础协议
       * tcp：安全协议，三次握手。速度稍慢
       * udp：不安全协议。速度快

### web服务器软件

1. 服务器：安装了服务器软件的计算机。

2. 服务器软件：接受用户的请求，处理请求，做出响应。

3. web服务器软件：接受用户的请求，处理请求，做出响应。

   ​	在web服务器软件中，可以部署web项目，让用户通过浏览器来访问该项目

4. 几款与java相关的常见web服务器软件：

   * webLogic：oracle公司，大型的JavaEE（java语言在企业级开发中使用的技术规范的总和，一共规定了13项大的规定）服务器，支持所欲JavaEE规范，是收费的。
   * webSphere：IBM公司，大型的JavaEE服务器，支持所有的JavaEE规范，收费的
   * JBoss：JBoss公司，大型的JavaEE服务器，支持所有的JavaEE规范，收费的
   * Tomcat：Apache基金组织，中小型的JavaEE服务器，仅仅支持少量的JavaEE规范

### Tomcat

1. 下载：官网下载即可
2. 安装：解压安装包即可
3. 卸载：删除安装文件即可
4. Tomcat目录结构

![image-20210206095655879](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210206095655879.png)

5. 启动、访问

   bin/startup.bat双击

6. 关闭

   * 正常关闭：shutdown.bat
   * 强制关闭

7. 配置

   * 部署项目的方式：

     * 直接将项目放到webapps目录即可

       简化部署：将项目打包成war包，再讲war包放置到webapps目录中（war包会自动解压缩）

     * 配置conf/server.xml文件

       在<Host>标签体中配置<Context docBase="D:\hello" path="/hehe"/>

       docBase：项目存放路径

       path：虚拟目录

     * 在conf\Catalina\localhost创建任意名称xml文件，xml文件中写入配置

   * 静态项目和动态项目

     * 目录结构

       * java动态项目的目录结构：

         --项目根目录

         ​	--WEB-INF目录：

         ​		--web.xml：web项目的核心配置文件

         ​		--classes目录：放置字节码文件的目录

         ​		--lib目录：放置依赖jar包

     * 将tomcat集成到IDEA中




### IDEA与Tomcat的相关配置

1. IDEA会为每一个tomcat部署的项目单独建立一份配置文件
2. 工作空间项目和tomcat部署的web项目
   * tomcat真正访问的是“tomcat部署的web项目”，“tomcat部署的web项目”对应着工作空间中的web目录下的所有资源
   * WEB—INF目录下的资源不能被浏览器直接访问

# Servlet

### 一、概念

运行在服务器端的小程序。

Servlet本质上就是一个接口，定义了java类被浏览器访问到（tomcat识别）的规则

### 二、快速入门

1. 创建javaEE项目

2. 定义一个类，实现Servlet接口

3. 实现接口中的抽象方法

4. 配置Servlet

   在web xml中配置

   ```
   <servlet>
       <servlet-name>demo1</servlet-name>
       <servlet-class>cn.itcast.web.servlet.ServletDemo1</servlet-class>
   </servlet>
   <servlet-mapping>
       <servlet-name>demo1</servlet-name>
       <url-pattern>/demo1</url-pattern>
   </servlet-mapping>
   ```

**底层逻辑执行原理**

![image-20210208095117534](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210208095117534.png)

1. 当服务器接收到客户端浏览器的请求后，会解析请求URL路径，获取访问的Servlet资源路径
2. 查找web,xml文件，是否有对象的<utl-pattern>标签内容
3. 如果有，则再找到对应的<servlet-class>全类名
4. tomcat会将字节码文件加载进内存，并且创建其对象
5. 调用其方法



**servlet的生命周期**

1. 被创建：执行init()方法，只执行一次

   * 默认情况下，第一次被访问时，Servlet被创建

   * 可以配置执行Servlet的创建时间

     ```
     <!--        指定servlet的创建时间
                 1.第一次被访问时，创建
                     <load-on-startup>的值为负数
                 2.在服务器启动时，创建
                     <load-on-startup>的值为0或正整数
     -->
     ```

   * servler的init方法只执行一次说明一个Servlet在内存中只存在一个对象

     * 多个用户同时访问时，可能存在线程安全问题

       解决：尽量不要再Servlet中定义成员变量，即使定义了成员变量，也不要修改值

2. 提供服务：执行service方法，执行多次

3. 被销毁：执行destroy方法，只执行一次

   * 只有服务器正常关闭时，才会执行destroy方法
   * destroy方法在Servlet被销毁之前执行，一般用于释放资源



**Servlet3.0**

1. 支持注解配置。可以不需要web.xml

2. 使用步骤：

   1. 创建JavaEE项目，选择Servlet的版本3.0以上，可以不创建web.xml

   2. 定义一个类，实现Servle接口

   3. 重写方法

   4. 在类上使用@WebServlet注解，进行配置

      @WebServlet(“资源路径”)

### 三、Servlet体系结构

Servlet --接口

​		|

GenericServlet --抽象类

​		|

HttpServlet --抽象类

* GenericServlet：将Servlet接口中其他的方法做了默认空实现，只将service90将来定义Servlet类时，可以继承GenericServlet，实现service方法即可
* HttpServlet：对http的一种封装，简化操作
  * 定义类继承HTTPServlet
  * 复写doGet/doPost方法



# HTTP协议

# Maven

## 一、Maven简介

### 1.什么是Maven

项目管理工具

### 2. Maven能解决你什么问题

* 导入jar包
* 编译代码
* 自动运行单元测试
* 打包、生成报表
* 部署项目

### 3. Maven的安装

* 下载Maven压缩包，并解压
* 环境配置
  * 系统变量，变量名：MAVEN_HOME
  * 系统变量，路径：maven所在目录
  * path变量中，%MAVEN_HOME%\bin
* 安装确认：命令行中输入mvn -v

#### 补充：

##### 1. Maven安装包目录结构

* bin：mvn.cmd主要用来构建项目
* boot：Maven自身运行所需的配置文件
* conf
* lib：Maven自身运行所需的jar包
* LICENSE
* NOTICE
* README.txt

##### 2.maven标准目录结构

* stc\main\java目录：核心代码
* src\main\resources：配置文件部分
* src\test\java：测试代码部分
* stc\test\resources：测试配置文件
* stc\main\webapp：页面资源（js,css,图片等资源）

### 4. Maven仓库

* 本地仓库
* 远程仓库（私服）
* 中央仓库

### 5. Maven常用命令

### 6. Maven的生命周期









# Spring

## 一、Spring简介

1. spring是什么

   spring是分层的的javaSE/EE应用full-stack**轻量级开源框架**，以IOC（inverse of control:反转控制）和AOP（aspect oriented programing:面向切面编程）为内核。提供了展现层SpringMVC和持久层Spring JDBCTemplate以及业务层事务管理等众多的企业级应用技术，还能整合开源世界众多著名的第三方框架和类库，逐渐成为使用最多的JavaEE企业应用开源框架。

2. Spring发展历程

   1997年，IBM提出了EJB的思想

3. Spring的优势

   * 方便解耦，简化开发
   * AOP编程的支持
   * 声明式事务的支持
   * 方便程序的测试
   * 方便集成各种优秀框架
   * 减低JavaEE API的使用难度
   * java源码经典学习范例

4. SPring的体系结构

   ![image-20210201105122446](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210201105122446.png)

## 二、Spring快速入门

1. Spring程序开发步骤
   * 导入Spring开发的基本包坐标
   * 编写Dao接口和实现类
   * 创建Spring核心配置文件
   * 在Spring配置文件中配置UserDapImpl
   * 使用Spring的API获得Bean实例

## 三、Spring配置文件

1. Bean标签的基本配置

   用于配置对象交由Spring来创建。默认情况下它调用的是类中的无参构造函数，如果没有无餐构造函数则不能创建成功。

   基本属性：

   * id：Bean实例在Spring容器中的唯一标识
   * class：Bean的全限定名

2. Bean标签的范围配置

   scope：指定对象的作用范围，取值如下：

   | 取值范围  | 说明                                                         |
   | --------- | ------------------------------------------------------------ |
   | singleton | 默认值，单例的                                               |
   | prototype | 多例的                                                       |
   | request   | web项目中，spring创建一个Bean对象，将对象存入到request域中   |
   | session   | web项目中，spring创建一个Bean的对象，将对象存入到session域中 |
   | global    | web项目中，应用在protlet环境中，如果没有protlet环境，那么相当于session |

   总结：

   * 当scope的取值为singleton时，Bean的实例化个数为1个，Dean的实例化时机为当Spring核心文件被加载时，实例化配置的Bean实例。Bean的生命周期：
     * 对象创建：当应用加载，创建容器时，对象就被创建了
     * 对象运行：只要容器在，对象就一直活着
     * 对象销毁：当应用卸载，销毁容器时，对象就被销毁了
   * 当scope的取值为prototype时，Bean的实例个数是多个，Bean的实例化时机是当调用getBean()方法时实例化Bean。Bean的生命周期：
     * 对象创建：当使用对象时，创建新的对象实例
     * 对象运行：只要对象在使用中，就一直活着
     * 对象销毁：当对象长时间不用时，被java的立即回收机制回收

3. Bean生命周期配置
   * init-method:指定类中的初始化方法名称
   * destroy-method：指定类中销毁方法名称

4. Bean实例化三种方式
   * 无参构造方法实例化
   * 工厂静态方法实例化
   * 工厂实例方法实例化

# git和GitHub

### 版本控制

### 1. 版本控制工具应该具备的功能

* 协同修改
* 数据备份
* 版本管理
* 权限控制
* 历史记录
* 分支管理

#### 常见的版本控制工具

* GIt
* SVN(Subversion)
* CVS(Concurrent Version System)
* VSS(Micorosoft Visual SourceSafe)
* TFS(Team Fundation Server)
* Visual Studio Online

### 2. git的发展史

#### 版本控制分类

* 本地版本控制
* 集中版本控制
* 分布式版本控制

### 3. git的优势

### 4. git结构和基本原理

#### 工作区域

![image-20210214224116700](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210214224116700.png)

![image-20210515173624772](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210515173624772.png)

![image-20210515174224821](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210515174224821.png)

![image-20210515174352872](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210515174352872.png)

### 5. git和代码托管中心

* 局域网环境下
  * GitLab
* 外网环境下
  * GitHub
  * 码云

![image-20210215095248914](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210215095248914.png)

![image-20210215095712362](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210215095712362.png)

### 6. git环境配置

~~~~
# git配置
git config

* 形式
  * 用户名
  * email地址
* 作用：区分不同开发人员的身份
* 命令
  * 项目级别/仓库级别：仅在当前本地库范围有效
    * git config user.name 用户名
    * git config user.email 邮箱名
  * 系统用户级别：登录当前操作系统的用户范围
    * git config --global user.name 用户名
    * git config --global user.email 邮箱名
* 注意：信息保存在.git/config中

### 7. 命令行操作

#### 常用的Linux命令

​~~~ 1.
1. cd 进入一个目录
2. cd.. 退出一个目录
3. pwd 显示当前所在目录
4. ls 列出当前目录下的所有文件
5. touch 新建一个文件
6. rm 删除一个文件
7. mkdir 创建一个目录
8. rm -r 删除一个文件夹
9. mv 移动文件
10. reset 重新初始化终端
11. clear 清屏
12. history 查看命令历史
13. help 帮助
14. exit 退出
15. # 表示注释

1. 本地库操作

~~~
* 本地库初始化

  * git init：
  * git clone 【url】;

* 基本操作

  * 状态查看操作

    git status

    查看工作区、暂存区状态

  * 添加操作

    git add 【file name】

    将工作区的新建/修改添加到暂存区

  * 提交操作

    git commit -m "commit message " 【file name】

  * 查看历史记录操作

  * 删除文件并找回

  * 比较文件差异

  * 命令帮助

* 分支管理
~~~

2. ![image-20210516162735858](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210516162735858.png)
3. 远程库操作



# 案例应用

## 1. 百度地图的原理与案例应用

