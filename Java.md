# 简介&基础语法

Java：https://docs.oracle.com/en/java/index.html

JDK：[JDK Builds from Oracle (java.net)](https://jdk.java.net/)

JavaSE 8：https://docs.oracle.com/javase/8/index.html

JavaEE7：https://docs.oracle.com/javaee/7/index.html

Jakarta（Java EE）：https://jakarta.ee/

## java技术体系

java技术体系：JVM、Java类库、Java框架（Spring、Mybatis ...）

![image-20230903090434672](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202309030904027.png)

Java SE（Java Platform, Standard Edition）和 Java EE（Java Platform, Enterprise Edition）是 Java 平台的两个不同版本，它们之间有着密切的关系，但用途和功能有所不同。

JavaSE（Java Platform, Standard Edition）：**Java SE** 是 Java 平台的标准版，提供了开发和运行 Java 应用程序的基本 API 和工具。它包含了核心的 Java 类库和 Java 虚拟机（JVM），**适用于桌面应用程序、控制台应用程序、嵌入式系统等**。Java SE 包含的主要组件和功能：

- 核心语言语法和 API：如 java.lang、java.util、[java.io](http://java.io/) 等。
- GUI 工具包：如 Swing 和 AWT，用于开发图形用户界面应用。
- 网络编程：如 [java.net](http://java.net/) 包。
- 多线程和并发处理：如 java.util.concurrent 包。
- 数据库连接：通过 JDBC（Java Database Connectivity）实现。

JavaEE（Java Platform, Enterprise Edition）：**Java EE** 是 Java 平台的企业版，**基于 Java SE 构建**，并在其基础上增加了一系列用于开发和部署企业级应用的 API 和功能。Java EE **适用于分布式计算、大规模业务系统、Web 应用程序和服务端应用等**。Java EE 包含的主要组件和功能：

- Web 容器：如 Servlet 和 JSP，用于开发动态 Web 内容和 Web 服务。
- 企业级服务：如 EJB（Enterprise JavaBeans），用于构建可扩展、事务性的分布式应用。
- Web 服务：如 JAX-RS 和 JAX-WS，用于构建 RESTful 和 SOAP Web 服务。
- 持久化框架：如 JPA（Java Persistence API），用于简化数据库操作。
- 消息服务：如 JMS（Java Message Service），用于消息传递和异步通信。
- 安全性管理：如 JAAS（Java Authentication and Authorization Service）。

> JavaEE8 开始正式更名为Jakarta EE8。Java EE原本由Oracle官方维护，api包名通常为：`Javax.规范名.xxx`，更名后由Eclipse基金会维护，并因版权问题，将命名空间变为：`jakarta.xxx`
>
> 对于Jakarta EE中规范的实现通常包含两种，一种为api实现（需要对规范定义的功能及其注解进行实现），一种为逻辑实现（只实现功能，并对规范进行兼容，比如Spring IOC容器就是逻辑实现，对于@Resource这个Java原生注解也同样能够注入Spring容器）。
>
> 由于规范坐标的特殊性，实现在Maven中央仓库的依赖管理通常不是强（编译）依赖，而是由开发者在使用规范实现时自行引入对应的规范。例如使用`hiberate-validation`时需要自行引入对应规范`jakarta.validation-api`。

## java发展史

> [JDK版本新特性](https://mp.weixin.qq.com/s/GPMHkH7eJ02yWReeQVTEtg)

1. 1995年5月23日，Oak语言改名为java，并在SunWorld大会上正式发布java1.0版本。
2. 1996年1月23日Sun Microsystems发布了JDK 1.0。
3. 1998年，JDK 1.2版本发布。同时，Sun发布了JSP/Servlet、 EJB规范，以及将Java分成了J2EE、 J2SE和J2ME。这表明 了Java开始向 企业、桌面应用和移动设备应用3大领域挺进。
4. 1999年4月27日，HotSpot虚拟机诞生。
5. 2000年，JDK 1.3发布，Java HotSpot Virtual Machine正式发布，成为
   Java的默认虚拟机。
6. 2002年，JDK 1.4发布，古老的Classic虛拟机退出历史舞台。T
7. 2003年年底，Java平台的Scala正式发布，同年Groovy也加入了Java阵 营。
8. 2004年，JDK 1.5发布。同时JDK 1. 5改名为JavaSE 5.0。
9. 2006年，JDK 6发布。同年，Java开源并建立了OpenJDK。 顺理成章，Hotspot虚拟机也成为了OpenJDK中 的默认虛拟机。
10. 2007年，Java平台迎来了新伙伴Clojure。
11. 2008年，Oracle收购了BEA, 得到了JRockit 虛拟机。
12. 2009年，Twitter宣布把后台大部分程序从Ruby迁移到Scala，这是Java平台的又一次大规模应用。
13. 2010年，Oracle收购了Sun，获得Java商标和最具价值的Hotspot虞拟机。此时，Oracle拥有市场占用率最高的两款虚拟机HotSpot和JRockit，并计划在未来对它们进行整合: HotRockit
14. 2011年，JDK7发布。在JDK 1. 7u4中，正式启用了新的垃圾回收器G1。
15. 2017年，JDK9发 布。将G1设置为默认GC，替代CMS，同年，IBM的J9开源，形成了现在的Open J9社区
16. 2018年，Android的Java侵权案判决，Google赔 偿Oracle计88亿美元
    同年，Oracle宣告JavaEE成为历史名词，JDBC、JMS、 Servlet赠 予Eclipse基金会。同年，JDK11发 布，LTS版本的JDK,发布革命性的ZGC,调整JDK授权许可
17. 2019年，JDK12发 布，加入RedHat领导开发的Shenandoah GC

## java特性

1. 封装
2. 继承
3. 多态

## 开发环境

1. JDK

2. JRE

3. JVM

4. JVM&JRE&JDK关系

5. Oracle JDK & [Open JDK](https://openjdk.org/)

   | 特征                   | Oracle JDK                                                   | OpenJDK                                               |
   | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------- |
   | **来源和授权**         | 由Oracle公司发布，部分功能是闭源的，商业支持需付费           | 由OpenJDK社区维护，完全开源，免费使用                 |
   | **发布模式**           | 提供商业许可和长期支持（LTS），有定期的安全更新              | 免费提供各个版本，由多个渠道提供长期支持和更新        |
   | **功能**               | 包含标准OpenJDK功能外，可能有商业功能（如JFR、Mission Control） | 包含标准Java SE功能，通常不包含Oracle JDK的商业特性   |
   | **更新频率和安全补丁** | 提供商业支持客户定期的安全和功能更新                         | 开源社区提供安全补丁和更新，由Linux发行版提供打包发布 |
   | **使用场景**           | 适合需要商业支持和附加功能的企业客户或特定功能需求的开发者   | 大多数开发者和组织，注重免费和开源性质的使用场景      |

## 注释与关键字

### 注释

1. 单行注释

2. 多行注释

3. 文档注释

4. JavaDoc

   JavaDoc 是一种用于生成 API 文档的注释规范。以下是 JavaDoc 注释的一些常见规范：

   * 类、接口和枚举的注释：
     * 使用 `/** ... */` 多行注释格式。
     * 在注释的开头，使用一个概要描述该类、接口或枚举的功能。
     * 如果有必要，在概要之后提供更详细的描述。
     * 使用 `@author` 标签指定作者的姓名。
     * 使用 `@version` 标签指定版本信息。
   
     ~~~java
     /**
      * 描述类、接口或枚举的功能。
      * 
      * 更多详细描述...
      *
      * @author Your Name
      * @version 1.0
      */
     public class MyClass {
         // 类的代码...
     }
     ~~~

   * 方法的注释：
     * 使用 `/** ... */` 多行注释格式。
     * 在注释的开头，使用一个概要描述该方法的功能。
     * 如果有必要，在概要之后提供更详细的描述。
     * 对于每个参数，使用 `@param` 标签指定参数名称和描述。
     * 使用 `@return` 标签指定方法的返回值描述。
     * 使用 `@throws` 标签指定可能抛出的异常及其描述。
   
     ~~~java
     /**
      * 描述方法的功能。
      * 
      * @param a 参数a的描述
      * @param b 参数b的描述
      * @return 返回值的描述
      * @throws Exception 可能抛出的异常及其描述
      */
     public int calculate(int a, int b) throws Exception {
         // 方法的代码...
     }
     ~~~

   * 字段和常量的注释：
     * 使用单行注释 `//` 或多行注释 `/* ... */` 格式。
     * 在注释中描述该字段或常量的作用。
   
     ~~~java
     public class MyClass {
         /**
          * 描述字段的作用。
          */
         private int myField;
     
         /**
          * 描述常量的作用。
          */
         public static final int MY_CONSTANT = 10;
     }
     ~~~

   * 引用其他类或方法：
     
  * 使用 `{@link}` 或`{@linkplain}`标签来引用其他类、方法、变量等。@link用于创建超链接并显示链接的文本，而@linkplain用于创建链接并显示自定义的文本。@link还可以与@since和@version一起使用来指定链接的版本信息。
    
     ~~~java
     /**
      * 引用其他类：{@link OtherClass}
      * 引用其他方法：{@link OtherClass#otherMethod()}
      * 引用其他变量：{@link OtherClass#OTHER_CONSTANT}
      */
     public class MyClass {
         // ...
     }
     ~~~

### 关键字

Java关键字是**编程语言中预定义的具有特殊含义和用途的词汇**，它们在语法规则中有特定的作用，用于定义程序结构、控制流程、数据类型等。以下是Java中常见的关键字及其作用：

1. | 关键字       | 用途和描述                                    |
   | ------------ | --------------------------------------------- |
   | abstract     | 声明抽象类和方法。                            |
   | assert       | 用于调试目的，在代码中做断言。                |
   | boolean      | 定义布尔类型变量或方法返回值。                |
   | break        | 退出循环或switch语句。                        |
   | byte         | 定义字节类型变量。                            |
   | case         | 标记switch语句中的代码块。                    |
   | catch        | 处理try块中生成的异常。                       |
   | char         | 定义字符类型变量。                            |
   | class        | 声明类。                                      |
   | const        | 已废弃，曾用于定义常量。                      |
   | continue     | 跳过当前循环的迭代。                          |
   | default      | 指定switch语句或接口方法的默认情况。          |
   | do           | 在条件为真时执行一系列语句的循环。            |
   | double       | 定义双精度浮点类型变量。                      |
   | else         | 如果if语句的条件表达式为假，则执行代码。      |
   | enum         | 声明枚举类型。                                |
   | extends      | 表示一个类正在继承另一个类。                  |
   | final        | 防止类、方法和变量的修改。                    |
   | finally      | 无论异常是否发生，都执行try-catch块后的代码。 |
   | float        | 定义单精度浮点类型变量。                      |
   | for          | 初始化一个循环，由三个可选表达式组成。        |
   | goto         | 已废弃，在Java中不使用。                      |
   | if           | 根据条件表达式的布尔结果执行语句。            |
   | implements   | 类实现接口。                                  |
   | import       | 从其他包含中导入类。                          |
   | instanceof   | 测试对象是否是特定类或接口的实例。            |
   | int          | 定义整数类型变量。                            |
   | interface    | 声明接口。                                    |
   | long         | 定义长整数类型变量。                          |
   | native       | 表示方法使用JNI在本地代码中实现。             |
   | new          | 创建新对象。                                  |
   | null         | 表示空引用。                                  |
   | package      | 定义包。                                      |
   | private      | 将方法和变量的访问限制在同一类内。            |
   | protected    | 允许同一包和子类访问方法和变量。              |
   | public       | 允许任何其他类访问方法和变量。                |
   | return       | 退出当前方法，可选择返回值。                  |
   | short        | 定义短整数类型变量。                          |
   | static       | 表示方法或变量属于类，而不是类的实例。        |
   | strictfp     | 确保浮点计算在不同平台上一致。                |
   | super        | 引用当前对象的超类。                          |
   | switch       | 根据多个条件执行一个语句。                    |
   | synchronized | 控制多线程对共享资源的访问。                  |
   | this         | 引用当前对象。                                |
   | throw        | 抛出异常。                                    |
   | throws       | 指定方法可能抛出的异常。                      |
   | transient    | 防止变量序列化。                              |
   | try          | 实现对代码块的错误处理。                      |
   | void         | 指定方法不返回值。                            |
   | volatile     | 表示变量可能异步修改。                        |
   | while        | 当指定条件为真时执行一系列代码块。            |

## 数据类型

### 基本数据类型&包装类

1. `byte`
2. `char`
3. `short`
4. `int`
5. `long`
6. `float`
7. `double`
8. `boolean`

### 类型转换

1. 强制类型转换
2. 隐式类型转换

## 运算符

## 控制逻辑

### 条件控制

1. `if`
2. `switch`
   * 从 Java 7 开始，可以在 switch 条件判断语句中使用 String 对象。

### 循环控制

1. `while`
2. `do while`
3. `for`

# 面向对象编程

1. 面向对象三个特征：
* 封装性

* 继承性

* 多态性
  
  * 编译时多态：主要指方法的重载
  * 运行时多态：
    * 指程序中定义的对象引用所指向的具体类型在运行期间才确定。
    * 三个条件：继承、重写（覆盖）、向上转型
2. 面向对象程序开发三个步骤：
* OOA：面向对象分析

* OOD：面向对象设计

* OOP：面向对象编程
3. 类与对象
   
   * 类：对某一类事物的共性抽象概念
   * 对象：描述的是一个具体的事物

4. 构造器
   
   ![image-20220914202459869](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209142025665.png)

5. this关键字：
   
   * 代表当前对象的地址
   * 使用this调用属性（当前对象的成员变量、方法）
   * 使用this调用方法

6. static关键字
   
   * 静态代码块
     
     ![image-20220915134158463](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209151342732.png)
   
   > 注意：
   > 
   > * 静态方法只能访问静态的成员,不可以直接访问实例成员。
   > * 实例方法可以访问静态的成员，也可以访问实例成员。
   > * 静态方法中是不可以出现this关键字的。

## 类

### 数据表与简单java类映射关系

* 数据实体表设计 = 类的定义
* 表中的字段 =  类的成员属性
* 表的外键 = 引用关联
* 表的一行记录 = 类的一个实例化对象
* 表的多行记录 = 对象数组

### 封装性（包装类）

1. 包装类的本质：将基本数据类型进行包装使其可以像对象一样进行引用传递

2. 包装类的类型
   
   * 对象包装类
   * 数值包装类
   
   ![image-20210731093833499](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210731093833499.png)

3. 装箱与拆箱操作

注意：从JDK1.9开始对于所有包装类之中提供的构造方法变为了过期处理，不建议用户继续使用。因为从JDK1.5之后提供了自动的装箱和拆箱操作。

### 继承性

1. 继承的实现：在java程序中使用extends来实现继承关系。

2. 继承的目的：继承的实现目的是子类可以重用父类的代码并且扩充父类的功能。

3. 子类实例化流程
   
   ```java
   class Person{
       public Person(){
           System.out.println("父类实例化对象产生了。");
       }
   }
   
   class Student extends Person{
       public Student(){
           System.out.println("子类实例化对象产生了。");
       }
   }
   
   public class Test{
       public static void main(String[] args){
           new Student();
       }
   }
   
   /*
   运行结果：
   父类实例化对象产生了。
   子类实例化对象产生了。
   */
   ```
   
   子类实例化的过程必然会先实例化父类（即调用父类的构造方法），this调用的是本类构造方法。因此super和this不能同时出现。

4. 继承定义限制
   
   * java中不允许多重继承，只允许多层继承
   * 在进行继承关系的定义时，实际上子类可以继承父类中所有的操作结构。（即私有的也可以继承）

#### 覆盖重写

1. 方法覆写：子类中与父类拥有相同方法定义
2. 属性覆盖
3. 覆写的限制：被覆写的方法不能比父类拥有更为严格的访问控制权限

**Override和Overllading的区别**

| 区别   | Override          | Overloading  |
| ---- | ----------------- | ------------ |
| 中文含义 | 重写                | 重载           |
| 概念   | 方法名、参数列表和返回值都相同   | 方法名相同，参数列表不同 |
| 权限   | 被重写的方法不能有更严格的权限控制 | 没有权限限制       |
| 范围   | 发生在继承关系类中         | 在一个类中        |

#### final关键字

* 表达的是一种终结器的概念
* 可以利用final定义常量

### 多态性

1. Java中多态性的两种实现模式：
   * 方法的多态性
     * 方法的重写
     * 方法的重载
   * 对象的多态性：父子实例之间的转换处理
     * 对象向上转型
     * 对象向下转型
2. instanof关键字：保证对象向下转型的正确性

### JavaBean

![image-20220914203132422](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209142031407.png)

### Object类

1. Object类是所有类的父类。

2. 常用方法
   
   参考文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/Object.html#method.summary

### 类图

1. 泛化关系：用来描述继承关系，在 Java 中使用 extends 关键字。
   
   ![img](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211301307206.png)

2. 实现关系：用来实现一个接口，在 Java 中使用 implements 关键字。
   
   ![img](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211301308200.png)

3. 聚合关系：表示整体由部分组成，但是整体和部分不是强依赖的，整体不存在了部分还是会存在。
   
   ![img](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211301308330.png)

4. 组合关系：和聚合不同，组合中整体和部分是强依赖的，整体不存在了部分也不存在了。
   
   ![组合关系](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211301307859.png)

5. 关联关系：表示不同类对象之间有关联，这是一种静态关系，与运行过程的状态无关，在最开始就可以确定。
   
   ![img](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211301309291.png)

6. 依赖关系：和关联关系不同的是，依赖关系是在运行过程中起作用的。A 类和 B 类是依赖关系主要有三种形式:
   
   - A 类是 B 类中的(某中方法的)局部变量；
   - A 类是 B 类方法当中的一个参数；
   - A 类向 B 类发送消息，从而影响 B 类发生变化；

## 字符串

### 实质

字符串的实质是对数组的特殊包装。在JDK1.8以前使用的是字符数组，在1.9以后使用的字节数组。

### 字符串的相等比较

对于字符串的相等比较应该注意“==”比较的是字符串的对象地址，而若要比较字符串内容应该使用equals()方法进行。

### String类

#### String类两种实例化方式

* 直接赋值的对象实例化模式：只会产生一个实例化对象并且会自动保存到对象池中，以实现字符串实例重用
* 使用构造方法的实例化模式：会产生两个实例对象并且不会自动入池，无法实现对象重用，但是可以利用intern()方法实现手动入池

#### String对象（常量）池

对象池的主要目的是实现数据的共享处理。java中对象（常量）池实际上可以分为两种

* 静态常量池：指的是程序在加载时会自动将此程序之中保存的字符串、普通的常量、类和方法的信息，全部进行分类；
* 运行时常量池：当一个程序加载之后，里面可能包含变量

```java
//静态常量池示例
public class StringDemo{
    public static void mian(String[] args){
        String strA="www.baidu.com";
        String strB="www."+"baidu."+"com";
        System.out.println(strA==strB);//程序输出结果为true
    }
}
```

```java
//运行时常量池示例
public class StringDemo{
    public static void mian(String[] args){
        String info="baidu";
        String strA="www.baidu.com";
        String strB="www."+info+".com";
        System.out.println(strA==strB);//程序输出结果为false,因为程序加载时不确定info的内容
    }
}
```

#### 常用方法

API文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/String.html#method.summary

1. 字符串与字符
   
   | 方法                  | 类型  | 描述  |
   | ------------------- | --- | --- |
   | String(char[] data) | 构造  |     |
   |                     | 普通  |     |

2. 字符串与字节

3. 字符串比较

4. 字符串查找
   
   | 方法                                     | 类型  | 描述                     |
   | -------------------------------------- | --- | ---------------------- |
   | public boolean contains(String s)      | 普通  | 判断子字符串是否存在             |
   | public int indexOf(String str)         | 普通  | 从头查找指定字符串的位置           |
   | int indexOf(String str, int fromIndex) | 普通  | 从指定位置开始查找指定字符串第一次出现的位置 |
   | int lastIndexOf(String str)            | 普通  | 从后查找指定字符串的位置           |

5. 字符串替换
   
   | 方法                                                    | 类型  | 描述                  |
   | ----------------------------------------------------- | --- | ------------------- |
   | String replace(char oldChar, char newChar)            | 普通  | 替换字符串中指定的字符         |
   | String replaceAll(String regex, String replacement)   | 普通  | 替换字符串中能所有满足正则表达式的子串 |
   | String replaceFirst(String regex, String replacement) | 普通  | 替换字符串中第一个满足条件的子串    |

6. 字符串拆分
   
   | 方法                                      | 类型                  | 描述  |
   | --------------------------------------- | ------------------- | --- |
   | String[] split(String regex)            | 按指定条件拆分字符串          |     |
   | String[] split(String regex, int limit) | 按指定条件将字符串拆分为指定个数的子串 |     |

7. 字符串截取
   
   | 方法                                             | 类型  | 描述               |
   | ---------------------------------------------- | --- | ---------------- |
   | String substring(int beginIndex)               | 普通  | 从指定位置开始截取        |
   | String substring(int beginIndex, int endIndex) | 普通  | 从指定位置开始截取到指定结束位置 |

8. 字符串格式化
   
   | 方法                                                            | 类型  | 描述            |
   | ------------------------------------------------------------- | --- | ------------- |
   | static String format(String format, Object... args)           | 静态  | 根据指定形式进行文本格式化 |
   | static String format(Locale l, String format, Object... args) | 静态  |               |
   
   ```java
   public class Test{
       public static void main(String[] args){
           String name="张三";
           int age=18;
           double grade=98.34567;
           System.out.println(String.format("name:%s,age:%d,grade:%5.2f",name,age,grade));
       }
   }
   ```

9. 其他操作方法

| 方法                        | 描述           |
| ------------------------- | ------------ |
| String concat(String str) | 拼接两个字符串      |
| boolean isEmpty()         | 判断是否为空字符串    |
| String intern()           | 字符串入池        |
| String trim()             | 去除字符串左右的空格信息 |
| String toLowerCase()      | 字符串转小写       |
| String toUpperCase()      | 字符串转大写       |

## 数组

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

### 类库相关方法

1. 排序：java.util.Arrays.sort()
2. 拷贝：System.arraycopy(原数组，原数组开始点，新数组，新数组开始点，拷贝长度)
3. 可变参数：实质就是数组

## 抽象类

1. 抽象类的定义和使用
   * 定义时，使用abstract修饰类
   * 抽象类使用时必须拥有子类并且该子类覆写抽象类中所有抽象方法
   * 抽象类一定不能使用final关键字修饰（因为抽象类必须有子类才能使用）
   * 抽象类中可以没有抽象方法，但是即使没有抽象方法也无法直接使用new关键字进行实例化
   * 抽象类中允许有static方法（static永远不受到实例对象的结构影响）

## 接口

1. 接口的定义和使用
   
   * java中使用interface关键字来定义接口
   * 接口需要被子类实现，使用implements关键字，并且一个子类可以实现多个父接口
   * 如果子类不是抽象类，那么一定要覆写接口中所有的抽象方法
   * 接口对象可以利用子类对象的向上转型进行实例化
   * 接口中定义的变量默认为public static final修饰
   
   在JDK1.8开始，为解决接口设计缺陷，在接口中允许定义普通方法。
   
   * 普通方法需要使用default修饰（该操作一般属于挽救功能，不应作为设计首选）
   * 允许定义static方法

2. 实际开发中，接口的常用使用形式：
   
   * 进行标准设置
   * 表示一种操作的能力
   * 暴露远程方法视图（常用于RPC分布式开发中使用 ）

3. **抽象类和接口的区别**
   
   | 区别   | 抽象类                                                               | 接口                        |
   | ---- | ----------------------------------------------------------------- | ------------------------- |
   | 定义   | abstract关键字                                                       | interface关键字              |
   | 权限   | 各种权限                                                              | 只能使用public                |
   | 子类使用 | 子类通过extends关键字只能继承一个抽象类                                           | 子类通过implements关键字可以实现多个接口 |
   | 两者关系 | 抽象类可以实现若干个接口                                                      | 接口不允许继承抽象类，但是可以继承多个接口     |
   | 使用   | 1. 抽象类或接口必须定义子类；2. 子类一定要覆写抽象类或接口中的所有抽象方法；3. 通过子类的向上转型实现抽象类或接口的实例化 |                           |

4. 抽象类和接口的选择
   
   * 使用接口:
     * 需要让不相关的类都实现一个方法，例如不相关的类都可以实现 Compareable 接口中的 compareTo() 方法；
     * 需要使用多重继承。
   * 使用抽象类:
     * 需要在几个相关的类中共享代码。
     * 需要能控制继承来的成员的访问权限，而不是都为 public。
     * 需要继承非静态和非常量字段。

## 枚举类

参考：[java枚举类详解_java内部枚举类-CSDN博客](https://blog.csdn.net/weixin_43604021/article/details/126242933)

java从JDK1.5之后才提出枚举的定义。枚举的主要作用是用于定义有限个数对象的一种结构。

Java中使用关键字enum来定义枚举类。示例如下：

```java
enum Color{
    RED,GREEN,BULE;
}

public class Client{
    public static void main(String[] args){
        Color c=Color.RED;
        System.out.println(c);
    }
}
```

### Enum类

文档参考地址：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/Enum.html

常用方法：

| 方法                                       | 类型  | 描述     |
| ---------------------------------------- | --- | ------ |
| protected Enum(String name, int ordinal) | 构造  | 实例名和序号 |
| public String name()                     | 普通  | 获得到实例名 |
| public int ordinal()                     | 普通  | 获得实例序号 |

## 内部类

1. 普通内部类（成员内部类）
2. 静态内部类
3. 方法中定义内部类（局部内部类）
4. 匿名内部类

## 常用类

### Objcet类

参考文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/Object.html#method.summary

##### 常用方法

1. equals（）

2. hashCode（）

3. toString（）

4. clone（）
   
   * clone() 是 Object 的 protected 方法，它不是 public，一个类不显式去重写 clone()，其它类就不能直接去调用该类实例的 clone() 方法。
   
   * clone() 方法并不是 Cloneable 接口的方法，而是 Object 的一个 protected 方法。Cloneable 接口只是规定，如果一个类没有实现 Cloneable 接口又调用了 clone() 方法，就会抛出 CloneNotSupportedException。
   
   * 浅拷贝：拷贝对象和原始对象的引用类型引用同一个对象。
   
   * 深拷贝：拷贝对象和原始对象的引用类型引用不同对象。
   
   * 使用 clone() 方法来拷贝一个对象即复杂又有风险，它会抛出异常，并且还需要类型转换。Effective Java 书上讲到，最好不要去使用 clone()，可以使用拷贝构造函数或者拷贝工厂来拷贝一个对象。

### Scanner类

### Math类

### String、StringBuffer和StringBuilder

String类是所有项目中都会使用到的一个功能类，这个类拥有如下特性：

* 每一个字符串的常量都属于一个String类的匿名对象，并且不可更改
* String类有两个常量池：静态常量池、运行时常量池
* String类对象实例化建议使用直接复制的形式完成，这样可以保证对象的重用

但是其弊端也非常明显就是字符串内容不允许修改，为了解决这个问题，专门提出StringBuffer类来对字符串内容进行修改。

**StringBuffer和StringBuilder比较**

StringBuilder类的功能和StringBuffer类的功能相同，但是StringBuffer类中的方法属于线程安全的。

文档参考：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/StringBuffer.html

### CharSequence接口

描述字符串结构的接口，在这个接口中发现有三种常用子类：

* String类
* StringBuffer类
* StringBuilder类

文档参考：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/CharSequence.html

### AutoCloseable接口

AutoCloseable主要用于日后惊喜你资源开发的处理上，以实现资源的自动关闭。

文档参考：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/AutoCloseable.html

### Runtime类

Runtime描述的是运行时的状态，也就是说在整个JVM中，Runtime类是唯一一个与JVM运行状态有关的类。

文档参考：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/Runtime.html

### Comparable接口和Comparator接口

参考资料：https://www.jb51.net/article/93973.htm

### System类

* 常用方法
  * 数组拷贝：static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length)
  * 获取当前日期时间数值：public static long currentTimeMills();
  * 垃圾回收：public static void gc();

参考文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/System.html

### Cleaner类

### Arrays

### 日期与时间相关类

[【黑马磊哥】一听就懂 JDK8新增的日期时间、Java日期时间API、LocalDateT](https://www.bilibili.com/video/BV1wG4y1h7j4?spm_id_from=333.1245.0.0)

#### calendar system

* [ISO-8601](https://www.joda.org/joda-time/cal_iso.html)、[Joda-Time](https://www.joda.org/joda-time/index.html)
* proleptic Gregorian calendar system

java中jdk8之前传统的与时间相关类主要有：

* Date
* SimpleDateFormat
* Calendar

在jdk8中新增的时间相关类有：

* LocalDate:年、月、日
* LocalTime:时、分、秒
* LocalDateTime: 年、月、日时、分、秒
* ZoneId :时区
* ZonedDateTime:带时区的时间
* Instant:时间戳/时间线
* DateTimeFormatter:用于时间的格式化和解析
* Duration:时间间隔 (时、分、秒，纳秒)
* Period:时间间隔 (年，月，日)

在实际开发中，推荐使用 `java.time` 包中的新日期和时间 API（Java 8+）。例如 `LocalDateTime`、`LocalDate` 等类，它们提供了更简洁、易用且线程安全的日期和时间处理方式。其中可以使用`LocatDate`、`LocatDateTime`、`LocalDateTime`、`ZoneId`、`ZoneDateTime`来代替原`Calendar`，使用`Instant`代替`Date`，使用`DateTimeFormatter`代替`SimpleDateFormat`。

> jdk8以前的时间api，设计不合理，使用不方便很多都被淘汰了；都是可变对象，修改后会丢失最开始的时间信息并且是线程不安全；在精度上只能精确到毫秒。jak8+的相关时间api能精确到毫秒、纳秒，在不可变的同时也是线程安全的。

#### Date

参考文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/util/Date.html

1. Date类对象在java中代表当前所在系统的此刻日期时间

#### SimpleDateFormat

参考文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/text/SimpleDateFormat.html

1. 作用：将Date对象或时间毫秒值格式化为想要的格式。同时也可以把字符串的时间形式解析成日期对象

2. 使用

   ![image-20211228204316451](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211228204316451.png)

   3. 格式化的时间形式

      ![image-20211228204547690](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211228204547690.png)

#### Calendar

`java.util.Calendar` 类是 Java 中处理日期和时间的核心类之一。它提供了一组方法，用于操作日期、时间和日历字段。

该类中常用的字段和方法如下：

- `YEAR`：年份字段
- `MONTH`：月份字段（注意从0开始，即0表示一月）
- `DATE`：日期字段
- `HOUR_OF_DAY`：24小时制的小时字段
- `MINUTE`：分钟字段
- `SECOND`：秒字段
- `MILLISECOND`：毫秒字段
- `DAY_OF_WEEK`：星期几字段（1表示星期日，2表示星期一，以此类推）
- `AM_PM`：上午/下午字段（0表示上午，1表示下午）
- `getInstance()`：返回一个默认时区和语言环境的 Calendar 实例
- `set(int field, int value)`：设置给定字段的值
- `get(int field)`：获取给定字段的值
- `add(int field, int amount)`：根据日历的规则，将指定字段的值增加或减少指定的时间量
- `getTime()`：返回一个表示 Calendar 所代表的日期的 Date 对象
- `setTime(Date date)`：使用给定的 Date 设置此 Calendar 的时间

> 注意: **calendar是可变对象，一旦修改后其对象本身表示的时间将产生变化。**

---

#### LocalDate

`LocalDate` 表示不带时区的日期，包括年、月、日等信息。它是一个不可变的类，每个实例都代表一个特定的日期。

1. 常用方法：

   * `now()`：获取当前系统日期
   * `of(int year, int month, int dayOfMonth)`：根据指定的年份、月份和日期创建 LocalDate 对象
   * `parse(CharSequence text)`：将字符串解析为 LocalDate 对象，例如 `LocalDate.parse("2021-08-06")`
   * `plusYears(long years)`：增加指定的年数
   * `minusYears(long years)`：减少指定的年数
   * `plusMonths(long months)`：增加指定的月份数
   * `minusMonths(long months)`：减少指定的月份数
   * `plusDays(long days)`：增加指定的天数
   * `minusDays(long days)`：减少指定的天数

2. `java.time.LocalDate`vs`java.util.Date`

   * java.util.Date和SimpleDateFormatter都是线程不安全的，而java.time.LocalDate和java.time.LocalTime与最String一样，是不可变的，因此可以说是线程安全的。以下是API文档中的解释：

     > LocalDate is an immutable date-time object that represents a date, often viewed as year-month-day.  Other date fields, such as day-of-year, day-of-week and week-of-year, can also be accessed.  For example, the value "2nd October 2007" can be stored in a LocalDate.

   * java.util.Date月份是从0开始，一月是0，十二月是11。java.time.LocalDate月份和星期都改成了enum（分别为java.time.DayOfWeek和java.time.Month）。

   * java.util.Date推算时间（比如往前推几天/往后推几天/推算某年某月第一天等等）要结合Calender编写代码，相当麻烦，而java.time.LocaDate只需要调用对应的方法即可。

#### LocalTime

`LocalTime` 表示不带时区的时间，包括小时、分钟、秒、毫秒等信息。与 `LocalDate` 类似，它也是一个不可变的类。

1. 常用方法：
   * `now()`：获取当前系统时间
   * `of(int hour, int minute)`：根据指定的小时和分钟数创建 `LocalTime` 对象
   * `parse(CharSequence text)`：将字符串解析为 `LocalTime` 对象，例如 `LocalTime.parse("12:00:00")`
   * `plusHours(long hours)`：增加指定的小时数
   * `minusHours(long hours)`：减少指定的小时数
   * `plusMinutes(long minutes)`：增加指定的分钟数
   * `minusMinutes(long minutes)`：减少指定的分钟数
   * `plusSeconds(long seconds)`：增加指定的秒数
   * `minusSeconds(long seconds)`：减少指定的秒数

#### LocalDateTime

`LocalDateTime` 表示不带时区的日期和时间，包括年、月、日、小时、分钟、秒、毫秒等信息。它是 `LocalDate` 和 `LocalTime` 的合集，也是一个不可变的类。

1. 常用方法：
   * `now()`：获取当前系统日期和时间
   * `of(int year, int month, int dayOfMonth, int hour, int minute, int second)`：根据指定的年、月、日、小时、分钟和秒数创建 `LocalDateTime` 对象
   * `parse(CharSequence text)`：将字符串解析为 `LocalDateTime` 对象，例如 `LocalDateTime.parse("2021-08-06T12:00:00")`
   * `plusYears(long years)`：增加指定的年数
   * `minusYears(long years)`：减少指定的年数
   * `plusMonths(long months)`：增加指定的月份数
   * `minusMonths(long months)`：减少指定的月份数
   * `plusDays(long days)`：增加指定的天数
   * `minusDays(long days)`：减少指定的天数
   * `plusHours(long hours)`：增加指定的小时数
   * `minusHours(long hours)`：减少指定的小时数
   * `plusMinutes(long minutes)`：增加指定的分钟数
   * `minusMinutes(long minutes)`：减少指定的分钟数
   * `plusSeconds(long seconds)`：增加指定的秒数
   * `minusSeconds(long seconds)`：减少指定的秒数

#### ZoneId

由于世界各个国家与地区的经度不同，各地区的时间也有所不同，因此会划分为不同的时区。

#### ZoneDateTime

`ZonedDateTime` 表示带时区的日期和时间，包括年、月、日、小时、分钟、秒、毫秒等信息，并且还包括时区信息。它也是一个不可变的类。

1. 常用方法：
   * `now()`：获取当前系统日期和时间，以系统默认时区为准
   * `of(LocalDateTime localDateTime, ZoneId zone)`：根据指定的日期时间和时区创建 `ZonedDateTime` 对象
   * `parse(CharSequence text)`：将字符串解析为 `ZonedDateTime` 对象，例如 `ZonedDateTime.parse("2021-08-06T12:00:00+08:00")`
   * `withZoneSameInstant(ZoneId zone)`：返回一个新的 `ZonedDateTime` 对象，其时区与指定时区相同，但日期时间不变
   * `withZoneSameLocal(ZoneId zone)`：返回一个新的 `ZonedDateTime` 对象，其时区与指定时区相同，但本地日期时间不变
   * `plusYears(long years)`：增加指定的年数
   * `minusYears(long years)`：减少指定的年数
   * `plusMonths(long months)`：增加指定的月份数
   * `minusMonths(long months)`：减少指定的月份数
   * `plusDays(long days)`：增加指定的天数
   * `minusDays(long days)`：减少指定的天数
   * `plusHours(long hours)`

#### DateTimeFormatter

#### Duration

`Duration` 类用于表示时间上的持续时间，以秒和纳秒为单位。

1. 常用方法：
   * `ofDays(long days)`、`ofHours(long hours)`、`ofMinutes(long minutes)`、`ofSeconds(long seconds)` 等：创建一个指定持续时间的 `Duration` 对象。
   * `between(Temporal startInclusive, Temporal endExclusive)`：计算两个 `Temporal` 对象之间的持续时间。
   * `plus(Duration duration)` 和 `minus(Duration duration)`：添加或减去指定的持续时间。
   * `getSeconds()` 和 `getNano()`：获取持续时间的秒数和纳秒数。
   * `toMinutes()`、`toHours()` 和 `toDays()`：将持续时间转换为分钟、小时或天数。

#### Period

`Period` 类用于表示日期上的持续时间，以年、月和日为单位。

1. 常用方法：
   * `ofYears(int years)`、`ofMonths(int months)`、`ofDays(int days)` 等：创建一个指定持续时间的 `Period` 对象。
   * `between(LocalDate startDateInclusive, LocalDate endDateExclusive)`：计算两个 `LocalDate` 对象之间的持续时间。
   * `plus(Period period)` 和 `minus(Period period)`：添加或减去指定的持续时间。
   * `getYears()`、`getMonths()` 和 `getDays()`：获取持续时间的年数、月数和天数。

#### Instant

`Instant` 类是 Java 8 引入的用于表示时间戳的类，以便在机器和人类可读的格式之间进行转换。该时间由两部分组成:从1970-01-01 00:00:00 开始走到此刻的总秒数 + 不够1秒的纳秒数

1. 常用方法：
   * `now()`：获取当前的时间戳。
   * `ofEpochSecond(long epochSecond)` 和 `ofEpochMilli(long epochMilli)`：创建一个 `Instant` 对象，表示从 1970 年 1 月 1 日开始的秒数或毫秒数。
   * `getEpochSecond()` 和 `toEpochMilli()`：获取秒数或毫秒数表示的时间戳。
   * `plus(Duration amountToAdd)` 和 `minus(Duration amountToSubtract)`：添加或减去指定的持续时间。
   * `isBefore(Instant other)` 和 `isAfter(Instant other)`：判断一个 `Instant` 是否在另一个之前或之后。
   * `atZone(ZoneId zone)`：在指定时区转换为 `ZonedDateTime` 对象。

## 包的定义及使用

1. 包的定义：为了避免类名的重复，方便类的管理于是引入了包的概念。其实质就是目录。

2. 包的导入：利用关键字import进行导包。包的导入实质就是包之间类的相互引用。

3. 包的静态导入

4. 系统常用包
   
   java语言从发展至今一直提供有大量的类库，这些类库一般由两部分组成：
   
   * java自身提供的（JDK和一些标准）
   * 第三方厂商提供的
   
   常用的包列举如下：
   
   * java.lang：包含String、Number、Object等常用类
   * java.lang.reflect：反射机制处理包，所有的设计从此开始
   * java.util：工具类的定义，包括数据结构的定义
   * java.io：输入输出流操作的程序包
   * java.net：网络程序开发的程序包
   * java.sql：进行数据库编程的开发包
   * java.applet：java的最原始的使用形式，直接嵌套在网页上执行的程序包
   * java.awt、javax.swing：java的图形界面开发包（GUI），其中awt属于重量级的组件，而swing是轻量级的组件

### 访问控制权限

java中一共定义由四种访问控制权限分别为：public、default（不写）、protected、private。它们的区别如下：

| 访问范围    | public | default | protected | private |
| ------- | ------ | ------- | --------- | ------- |
| 同一包中同一类 | √      | √       | √         | √       |
| 同一包中不同类 | √      | √       | √         |         |
| 不同包的子类  | √      |         | √         |         |
| 不同包所有类  | √      |         |           |         |

### 生成jar文件

当一个项目完成后会存在大量* .class文件，那么此时对于这些文件的管理可以利用一种特殊压缩结构的形式进行处理。这种结构在java中就被称为jar文件。如果想要将程序打包为jar文件可以直接利用jdk中提供的jar命令进行处理。（使用“jar --help”命令查看相关命令）

**jar的使用和配置操作示例：**

1. 编写程序代码
   
   ```java
   package cn.chen.sort;
   import java.util.*;
   public class SortTest{
       public static void main(String[] args){
           int[] arr={2,4,2,1,3,7,8,5,6,9};
           // bubbleSort(arr);
           selectionSort(arr);
           System.out.println(Arrays.toString(arr));
       }
   
       /*
           Bubble Sort
       */
       public static void bubbleSort(int[] arr){
           for(int i=0;i<arr.length;i++){
               for(int j=0;j<arr.length-i-1;j++){
                   if(arr[j]>arr[j+1]){
                       int temp=arr[j];
                       arr[j]=arr[j+1];
                       arr[j+1]=temp;
                   }
               }
           }
       }
   
       /*
           选择排序
       */
       public static void selectionSort(int[] arr){
           int min,temp;
           for(int i=0;i<arr.length;i++){
               min=i;
               for(int j=i+1;j<arr.length;j++){
                   if(arr[j]<arr[min]){
                       min=j;
                   }
               }
               temp=arr[i];
               arr[i]=arr[min];
               arr[min]=temp;
           }
       }
   
       /*
           插入排序
       */
       public static void insertSort(int[] arr){
   
       }
   }
   ```

2. 对程序进行编译与打包
   
   * 编译：javac -d . SortTest.java
   * 编译完成后生成相应cn的包，包内包含相应的子包和*.class文件
   * 将其打包为chen.jar命令为“jar -cvf chen.jar cn”。命令参数解释如下：
     * “-c”：创建一个新的jar包
     * “-v”：得到一个详细输出
     * “-f”：设置生成的jar文件名称，本处定义为chen.jar

3. jar包的使用：每一个jar包都是一个独立的程序路径，若要在java程序中使用此路径，则需要通过CLASSPATHj进行配置“SET CLASSPATH=.;C:\Users\hp\Desktop\排序测试\chen.jar”

参考文档：https://docs.oracle.com/en/java/javase/16/docs/specs/jar/jar.html

# Lambda表达式与函数式编程

参考：https://www.bilibili.com/video/BV1Gh41187uR/?spm_id_from=333.337.search-card.all.click

## 函数式编程

参考：

* https://www.finclip.com/news/f/38498.html
* [深入浅出聊聊Java函数式编程思想](https://juejin.cn/post/7056354222689746974)

1. 优势
   * 大数量下处理集合效率高
   * 代码可读性高
   * 消灭嵌套地狱
   
2. 函数式编程思想
   
   * 面向对象思想需要关注用什么对象完成什么事情。函数式编程思想主要关注的是对数据进行了什么操作。
   
3. 函数式接口：只用一个抽象方法的接口

   JDK的函数式接口都加上了@FunctionalInterface注解进行标识。但是无论是否加上该注解只要接口中只有一个抽象方法, 都是函数式接口。

4. 方法引用

   在使用lambda时,如果方法体中只有一个方法的调用(包括构造方法)，我们可以用方法引用进一步简化代码。

   语法格式如下：

   ~~~java
   类名或对象名::方法名
   ~~~

   引用类的静态方法：如果我们在重写方法的时候，方法体中只有一-行代码,并且这行代码是调用了某个类的静态方法，并且我们把要重写的抽象方法中所有的参数都按照顺序传入了这个静态方法中，这个时候我们就可以引用类的静态方法。

   引用对象的实例方法：如果我们在重写方法的时候，方法体中只有一行代码， 并且这行代码是调用了某个对象的成员方法，并且我们把要重写的抽象方法中所有的参数都按照顺序传入了这个成员方法中，这个时候我们就可以引用对象的实例方法。

   引用类的实例方法：如果我们在重写方法的时候，方法体中只有一行代码，并粗这行代码是**调用了第一个参数的成员方法**,并组我们把要重写的抽象方法中剩余的所有的参数都按照顺序传入了这个成员方法中，这个时候我们就可以引用类的实例方法。

   构造引用：如果我们在重写方法的时候，方法体中只有一行代码， 并粗这行代码是调用了某个类的构造方法，并且我们把要重写的抽象方法中的所有的参数都按照顺序传入了这个构造方法中，这个时候我们就可以引用构造器。

## 语法糖

1. 定义：指编程语言为了方便程序员开发程序而设计的一种**特殊语法**，这种语法对编程语言的功能并没有影响。实现相同的功能，基于语法糖写出来的代码往往更简单简洁且更易阅读。
2. Java常见语法糖：
   * 泛型
   * 自动拆装箱
   * 变长参数
   * 枚举
   * 内部类
   * 增强 for 循环
   * try-with-resources 语法
   * lambda 表达式

## Lamba表达式

参考：https://objcoding.com/2019/03/04/lambda/

### 基本使用

1. 概述：从JDK1.8开始为简化使用者进行代码开发，专门提供有Lambda表达式的支持（语法糖）。对于函数式编程比较著名的语言：haskell、Scala。
2. 要求：Lambda表达式如果要使用，必须有一个重要的实现要求：SAM（Single Abstract Method）,只有一个抽象方法。
3. 格式：Lambda表达式提供有如下几种格式：
   * 方法没有参数：()->{}
   * 方法有参数：(argument)->{}
   * 如果只有一行语句返回：(参数，参数)->语句
4. 省略规则
   * 参数类型可以省略
   * 方法体只有一句代码时大括号return和唯一-句代码的分号可以省略
   * 方法只有-个参数时小括号可以省略
   * 以上这些规则都记不住也可以省略不记

利用Lambda表达式可以摆脱传统面向对象只用关于结构的限制，使得代码更加简便。

~~~java
package com.chen.lambda;

public class LambdaDemo1 {
    public static void main(String[] args) {
        Thread thread1 = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println(Thread.currentThread().getName());
            }
        },"thread1");

        Thread thread2 = new Thread(() -> {
            System.out.println(Thread.currentThread().getName());
        }, "Thread2");

        Thread thread3 = new Thread(() -> System.out.println(Thread.currentThread().getName()), "Thread3");

        thread1.start();
        thread2.start();
        thread3.start();
    }
}
~~~

```java
package com.chen.lambda;

import java.util.function.IntBinaryOperator;

public class LambdaDemo2 {
    public static void main(String[] args) {
        int calculate1 = calculate(new IntBinaryOperator() {
            @Override
            public int applyAsInt(int left, int right) {
                return left + right;
            }
        });
        System.out.println(calculate1);
        System.out.println("============");

        int calculate2 = calculate((int left, int right) -> {
            return left + right;
        });
        System.out.println(calculate2);
        System.out.println("============");

        int calculate3 = calculate(Integer::sum);
        System.out.println(calculate3);
    }

    public static int calculate(IntBinaryOperator operator){
        int a =10;
        int b=20;
        return operator.applyAsInt(a,b);
    }

}
```

```java
package com.chen.lambda;

import java.util.Objects;
import java.util.function.IntPredicate;

public class LambdaDemo3 {
    public static void main(String[] args) {
        printNum(new IntPredicate() {
            @Override
            public boolean test(int value) {
                return value%2==0;
            }
        });
        System.out.println("=================");
        printNum((int value) -> {return value%2!=0;});
    }

    public static void printNum(IntPredicate intPredicate){
        int[] arr = {1,2,3,4,5,6,7,8,9,10};
        for (int i :
                arr) {
            if (intPredicate.test(i)) {
                System.out.println(i);
            }
        }
    }
}
```

### JVM层面的Lambda

## Stream流

参考：

* https://blog.csdn.net/m0_64355285/article/details/122194444
* https://heapdump.cn/article/4481824

1. 概述：Java8的Stream使用的是函数式编程模式，如同它的名字一样，它可以被用来对集合或数组进行链状流式的操作。可以更方便的让我们对集合或数组操作。

2. 优势

   Stream相较于传统的foreach的方式处理，Stream流代码更加简洁、逻辑间解耦，并行流场景效率比迭代器逐个循环更高。但同时也存在一些缺点就是在代码调试时相没有那么方便，并且开发人员需要花费一定时间精力去适应Stream流方式。

3. 常用操作（方法）

   * 创建流

     > 数组：`集合对象.stream()`
     >
     > 单列集合：`Arrays.steam（数组）`或者`Stream.of(数组)`
     >
     > 双列集合：转换为单列集合后创建
     >
     > ~~~java
     > Map<String,Integer> map=new HashMap<>();
     > map.put(1,"chen");
     > map.put(2,"wang");
     > map.put(3,"li");
     > Stream<Map<String,Integer>> steam = map.entrySet().stream();
     > ~~~

   * 中间操作

     * filter：可以对流中的元素进行条件过滤，符合过滤条件的才能继续留在流中。
     * map：可以把对流中的元素进行计算或转换。
     * distinct：可以去除流中的重复元素。 distinct方法是依赖Object的equals方法来判断是否是相同对象的。所以需要注意重写equals方法。
     * sorted：可以对流中的元素进行排序。
     * limit：可以设置流的最大长度，超出的部分将被抛弃。
     * skip：跳过流中的前n个元素,返回剩下的元素
     * flatMap：map只能把一个对象转换成另一 个对象来作为流中的元素。而flatMap可以把一 个对象转换成多 个对象作为流中的元素。
     * peek：对stream流中的每个元素进行逐个遍历处理，返回处理后的stream流

   * 终结操作

     * forEach：对流中的元素进行遍历操作，我们通过传入的参数去指定对遍历到的元素进行什么具体操作。
     * count：可以用来获取当前流中元素的个数。
     * max&min：可以来或者流中的最值。
     * **collect**：把当前流转换成一个集合。
     * 查找与匹配
       * allMatch：可以用来判断是否有任意符合匹配条件的元素，结果为boolean类型。
       * anyMatch：可以用来判断是否都符合匹配条件，结果为boolean类型。 如果都符合结果为true,否则结果为false。
       * noneMatch：可以判断流中的元素是否都不符合匹配条件。如果都不符合结果为true,否则结果为false
       * findAny：获取流中的任意一个元素。 该方法没有办法保证获取的一定是流中的第一个元素。
       * findFirst：获取流中的第一个元素。
     * **reduce**：对流中的数据按照你制定的计算方式计算出一个结果。reduce的作用是把stream中的元素给组合起来,我们可以传入一个初始值,它会按照我们的计算方式依次拿流中的元素和在初始化值的基础_上进行计算,计算结果再和后面的元素计算。

   ~~~java
   public class StreamDemo1 {
       public static void main(String[] args) {
           List<Author> authors = StreamDemo.getAuthors();
   
           // filter
           // 打印所有名字长度大于3的作者名字
           authors.stream()
                   .filter(author -> author.getName().length()>3)
                   .forEach(author -> System.out.println(author.getName()));
           // map
           // 对所有人年龄+5
           authors.stream()
                   .map(author -> author.getAge())
                   .map(age -> age+5)
                   .forEach(age -> System.out.println(age));
           // distinct
           // sorted
           // 按年龄进行排序
           authors.stream()
                   .sorted((o1, o2) -> o1.getAge()-o2.getAge())
                   .forEach(author -> System.out.println(author.toString()));
           // limit
           // skip
           // flatMap
           // 打印所有书籍的名字
           authors.stream()
                   .flatMap((Function<Author, Stream<?>>) author -> author.getBooks().stream())
                   .forEach(o -> System.out.println(o.toString()));
       }
   }
   
   ~~~

   ```java
   public class StreamDemo2 {
       public static void main(String[] args) {
           List<Author> authors = StreamDemo.getAuthors();
   
           // forEach
           // count
           // max或min
           System.out.println(authors.stream()
                   .map(author -> author.getAge())
                   .max((i1, i2) -> i1 - i2)
                   .get());
   
           // collect
           // 获取-一个存放所有作者名字的List集合。
           List<String> collect = authors.stream()
                   .distinct()
                   .map(author -> author.getName())
                   .collect(Collectors.toList());
           System.out.println(collect);
   
           // 获取一个所有书名的Set集合。
           List<Book> bookList = authors.stream()
                   .flatMap((Function<Author, Stream<Book>>) author -> author.getBooks().stream())
                   .distinct()
                   .collect(Collectors.toList());
           System.out.println(bookList);
           
           // 获取一个map集合，map的key为作者名, value为List<Book>
           Map<String, List<Book>> map = authors.stream()
                   .distinct()
                   .collect(Collectors.toMap(author -> author.getName(), author -> author.getBooks()));
           for (Map.Entry<String, List<Book>> stringListEntry : map.entrySet()) {
               System.out.println(stringListEntry.getKey()+"-"+stringListEntry.getValue());
           }
   
       }
       
       // allMatch
           // 判断是否有年龄在29岁以上的作家
           System.out.println(authors.stream()
                   .anyMatch(author -> author.getAge() > 29));
           // anyMatch
           System.out.println(authors.stream()
                   .allMatch(author -> author.getAge() > 40));
           // noneMatch
           System.out.println(authors.stream()
                   .noneMatch(author -> author.getAge() > 50));
           // findAny
           // findFirst
   
           // reduce 归并
           // 使用reduce求所有作者年龄的和
           Integer sumAge = authors.stream()
                   .distinct()
                   .map(author -> author.getAge())
                   .reduce(0, (result, element) -> result + element);
           System.out.println(sumAge);
           // 使用reduce求所有作者中年龄的最大值
           Integer maxAge = authors.stream()
                   .distinct()
                   .map(author -> author.getAge())
                   .reduce(Integer.MIN_VALUE, (result, element) -> result < element ? element : result);
           System.out.println(maxAge);
           // 使用reduce求所有作者中年龄的最小值
   }
   ```

4. 并行流

   Stream.parallel方法（可以使用peek方法进行调试）

5. 注意事项

   * 惰性求值(如果没有终结操作，中间操作是不会得到执行的)
   * 流是一次性的(一旦一个流对象经过一 个终结操作后。这个流就不能再被使用)
   * 不会影响原数据(我们在流中可以多数据做很多处理。但是正常情况下是不会影响原来集合中的元素的。这往往也是我们期望的)

## 常用类和接口

### Optional

参考：https://blog.csdn.net/aaaPostcard/article/details/123596787

1. 概述

   在java编码过程中经常出现空指针异常，为了解决这个问题，通常的做法是在使用该变量前进行非空判断。但当变量为对象且其内部属性也为对象时，非常容易造成大片的非空判断语句，造成代码整体非常臃肿。使用Optional类可以写出更优雅的代码避免空指针异常。Optional就好像是包装类,可以把我们的具体数据封装Optional对象内部。然后我们去使用Optiona中封装好的方法操作封装进去的数据就可以非常优雅的避免空指针异常。
   
2. 常用操作

   * 创建

     ~~~java
     Optional.ofNullable(对象); // 建议使用
     Optional.empty(); // 创建一个null对象
   Optional.of(对象); // 若对象为null则会抛出NullpointerException
     ~~~

     > 在实际开发中我们的数据很多是从数据库获取的。Mybatis从3.5版本可以也已经支持Optiona了。我们可以直接把dao方法的返口值类型定义成Optional类型，MyBastis 会自己把数据封装成Optional对象返回。封装的过程也不需要我们自己操作。

   * 判断是否包含值

     ~~~java
      Optional.ifPresent();
      Optional.iSPresent();
     ~~~
<<<<<<< HEAD
     

=======
  ~~~
   
>>>>>>> e1548b195f9c5f09bd269381183b2bc95cd270d4
   * 安全获取值
   
     ~~~java
     Optional.Get(); // 如果Optional为空，调用get()方法会抛出NoSuchElementException异常
     Optional.orElse(); // 
     Optional.orElseGet(); // 如果Optional为空，则执行一个函数并返回结果
     Optional.orelseThrow();
     Optional.map(); // 如果Optional不为空，则执行一个函数并返回结果
     Optional.flatMap(); // 如果Optional不为空，则执行一个函数并返回一个Optional对象
  ~~~

   * 过滤
   
     ~~~java
     Optional.filter();//如果原本是有数据的，但是不符合判断，也会变成一个无数据的Optional对象。
     ~~~
   
      * 数据转换
### java.util.function包

参考文档：

* [API文档](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/function/package-summary.html)
* [java.util.function包详解-Lambda](https://zhuanlan.zhihu.com/p/423809261)

四大类

* Consumer：accept方法对传入的实体参数进行处理

* Supplier：get方法创建实体类型并返回

* Predicate：test方法确定实体T是否满足约束，返回boolean
* Function：apply方法对类型T实体进行相应的操作并返回类型为R的实体

# 正则表达式

1. 作用：用于验证字符串合法性

2. 验证规则
   
   参考文档：[Pattern (Java SE 16 &amp; JDK 16)](https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/util/regex/Pattern.html)
   
   ![image-20211229104328005](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211229104328005.png)

# 异常捕获和处理

参考：https://pdai.tech/md/java/basic/java-basic-x-exception.html

## 异常的类型

![img](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202212022314508.png)

* Throwable： Java 语言中所有错误与异常的超类。包含了其线程创建时线程执行堆栈的快照，它提供了 printStackTrace() 等接口用于获取堆栈跟踪数据等信息。
* Error：程序中无法处理的错误，表示运行应用程序中出现了严重的错误，由JVM抛出。
* Exception：程序本身可以捕获并且可以处理的异常。Exception 这种异常又分为两类：运行时异常和编译时异常。
* checked exception和unchecked exception
  * RuntimeException及其子类和Error均属于unchecked exception
  * 除RuntimeException及其子类外的异常都属于checked exception

## 基本结构和处理流程

在java中通过try、catch和finally、throw和throws关键词来实现异常的捕获和处理，常用基本结构如下：

* try-catch
* try-catch-finally
* try-finally
* try-with-resource

```java
try{
    //可能出现异常的语句
}catch(//异常类型 异常对象){
    //异常处理
}finally{
    //不管是否出现异常，都执行的代码
    //只有finally块，执行完成之后，才会回来执行try或者catch块中的return或者throw语句，如果finally中使用了return或者throw等终止方法的语句，则就不会跳回执行，直接停止。

}
```

## 自定义异常类

习惯上，定义一个异常类应包含两个构造函数，一个无参构造函数和一个带有详细描述信息的构造函数（Throwable 的 toString 方法会打印这些详细信息，调试时很有用）。

```java
public class MyException extends Exception{
    public MyException(){

    }
    public MyException(String msg){
        super(msg);
    }
    //....
}
```

## assert断言

从JDK1.4之后开始追加一个断言的功能，确定代码执行到某行之后一定是所期待的结果。在实际开发之中，断言不一定是准确的，也有可能出现偏差，但是这种偏差不应该影响程序的执行。

# 泛型

参考：

* [JavaSE强化教程泛型，由点到面的讲解了整个泛型体系](https://www.bilibili.com/video/BV1xJ411n77R/?spm_id_from=333.337.search-card.all.click&vd_source=fabefd3fabfadb9324761989b55c26ea)
* [Java 基础 - 泛型机制详解](https://pdai.tech/md/java/basic/java-basic-x-generic.html)

1. 泛型的引出
   
   泛型是JDK1.5之后开始使用的，其主要目的是**为了解决ClassCastException的问题**。java中向下转型始终都有可能存在安全隐患，因此希望通过泛型来慢慢解决此类问题。泛型提供了编译时类型安全监测机制，该机制允许我们在编译时检测到非法的类型数据结构。**泛型的本质是类型参数化**，也就是所操作的数据类型被指定为一个参数。

   泛型的优点：
   
   * 类型安全：编译时就可以发现类型的不一致性
   * 消除了强制类型转换
   
2. 泛型的定义

   * 泛型中只允许使用引用类型，若要使用基本类型则必须进行包装
   * 泛型可以定义在类、接口和方法上

3. 泛型通配符

   * 通配符（？）
     
     > ?可以在”使用泛型“的时候代表一切类型(可以理解为T,V,K,E等实在定义时使用)

   * 泛型上限

   * 泛型下限

   ```java
   package generics;
   
   import java.util.ArrayList;
   
   /**
    * 泛型通配符？
    * 在“使用”的时候代表一切类型
    * 假设要开发一个极品飞车游戏，是所有赛车都可以参加比赛
    */
   public class GenericsWildCard {
       public static void main(String[] args) {
           ArrayList<BENGCI> bengcis = new ArrayList<>();
           ArrayList<BAOMA> baomas = new ArrayList<>();
   
           compete(bengcis);
           compete(baomas);
   
       }
   
       public static void compete(ArrayList<? extends Car> cars){
   
       }
       }
   
   class Car{
   
   }
   
   class BENGCI extends Car{
   
   }
   
   class BAOMA extends Car{
   
   }
   ```

4. 泛型类

   * 常用的泛型标识：T、E、K、V（这些字母没有什么具体含义，只是通常会用这些字母进行标识）
   * 从JDK1.7开始，泛型对象实例化可以简化。例如由`ArrayList<String> list = new ArrayList<String>()`简化为`ArrayList<String> list = new ArrayList<>()`，编译器可以通过变量类型来推断泛型实例对象的类型。
   * 泛型类在实例化时若没有指定类型则按照Object类型实例化。
   * 同一泛型类，根据不同的数据类型创建的对象，本质上是同一类型。
   * 从泛型类派生子类时，若子类也是泛型类，子类和父类的泛型要保持一致；若子类不是泛型类，则父类要明确泛型的数据类型。

   ```java
   package generics;
   
   /**
    * 泛型类
    在类的名字后加上泛型标识
    */
   public class MyArrayList<E> {
       
       private E list;
       
       public void add(E e){
   
       }
   
       public void remove(E e){
   
       }
   
   }
   // 子类是泛型类，则子类的泛型（标识）需要与父类泛型（标识）保持一致
   public MyChildrenList<T> extends MyArrayList<T>{
       
   }
   
   // 子类不是泛型类，父类要明确泛型数据类型
   public MyChildrenList extends MyArrayList<String{
       
   }
   ```

5. 泛型接口

   ```java
   package generics;
   
   public interface Date<T> {
       public void add(T t);
       public void delete(T t);
   }
   ```

6. 泛型方法

   ```java
       /**
        * 泛型方法
        * 作用：方法中可以使用泛型接受一切实际类型的参数，方法更具备通用性
        * 形式：
        *  public <T> void print(T t){}
        *
        *  自定义一个打印数组的方法
        * @param arr
        */
       public static <E> void print(E[] arr){
           if (arr!=null){
               StringBuilder builder = new StringBuilder("[");
               for (int i = 0; i < arr.length; i++) {
                   builder.append(arr[i]).append(i==arr.length-1?"":",");
   
               }
               System.out.println(builder.append("]").toString());
           }else {
               System.out.println(arr);
           }
       }
   ```

7. 类型擦除

8. 泛型和数组

9. 泛型和反射

# 集合

## 集合概述

1. 体系结构
   
   Collection体系（单列集合）
   
   ![Collection](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220109124008792.png)
   
   Collection常用API
   
   ![](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220110164632701.png)
   
   Map体系（双列集合）

2. 使用场景

   * 数据个数不确定，需要进行增删元素的场景

3. 常见数据结构
   
   * 栈、队列
   * 数组
   * 链表
   * 二叉树、二叉查找树
   * 平衡二叉树（任意结点的左右子树高度差不超过1）
   * 红黑树

## Collection集合

1. 简介：单列集合的顶层接口、无法使用new关键字直接创建，需要使用多态的方式来实现。

2. 常用方法
   
   ![image-20230218152511044](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181525037.png)

3. 遍历：使用迭代器进行遍历。

## 迭代器及遍历

参考文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/util/Iterator.html

1. 迭代器
   
   ![image-20230218152649500](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181526220.png)
   
   > 注意：
   > 
   > 1. 增强for循环：自jdk1.5开始出现，内部原始是Iterator迭代器。
   > 2. 实现了Iterator接口的类才可以使用迭代器和增强for循环。

2. iterator的fail-fast和fail-safe机制
   
   * fail-fast机制：且发现遍历的同时其它人来修改，则立刻抛异常
   * fail-safe机制：发现遍历的同时其它人来修改，应当能有应对策略，例如牺牲一致性 来让整个遍历运行完成
   
   > ArrayList是fail-fast的典型代表，遍历的同时不能修改
   > CopyOnWriteArrayList是fail-safe的典型代表，遍历的同时可以修改，原理是读写分离

## List

元素有序、可重复、有索引

### ArrayList

1. 常用方法
   
   ![image-20220914211516448](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209142115036.png)

2. 底层实现原理
   
   > * 底层基于Object[]数组实现，根据索引定位元素快，但是增删元素时需要做移位操作
   > 
   > * 初始化时，若调用无参构造则初始容量为0，
   > 
   > * 扩容规则：
   >   
   >   * 调用add()方法添加元素时，默认初次扩容长度为10，第二次开始扩容为原来的1.5倍
   >   * 调用addAll方法时，初次扩容元素长度若小于10则扩容后长度为10，若初次扩容长度大于10则为扩容元素的长度。（或者说是元素长度和10二者之间的较大值）
   >   
   >   ![image-20230218144311632](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181443509.png)

3. 遍历
   
   ArrayList采用fail-fast机制，遍历是不允许修改，否则会抛出异常。

4. ListIterator
   
   ![image-20230218153725584](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181537846.png)

### LinkedList

1. 常用方法

   ![image-20220402170854567](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220402170854567.png)

2. 底层原理

   * 底层数据结构为双链表，查询慢，但是首位操作快，故新增了许多首位操作的特有功能
   * LinkedList可以完成栈和队列的操作

3. ArrayList和LinkedList的比较

   ![image-20230218150626703](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181506765.png)

~~~java
import java.util.LinkedList;

public class LinkedListDemo {
    public static void main(String[] args) {
        /*栈*/
        LinkedList<String> stack = new LinkedList<>();

        /*入栈*/
        stack.addFirst("第1颗子弹");
        stack.addFirst("第2颗子弹");
        stack.addFirst("第3颗子弹");
        stack.addFirst("第4颗子弹");
        stack.push("第5颗子弹");
        System.out.println(stack.toString());

        /*出栈*/
        stack.removeFirst();
        stack.pop();
        System.out.println(stack.toString());


        /*队列*/
        LinkedList<String> queue = new LinkedList<>();

        /*入队*/
        queue.addLast("排第1");
        queue.addLast("排第2");
        queue.addLast("排第3");
        queue.addLast("排第4");
        queue.offerLast("排第4");
        System.out.println(queue.toString());

        /*出队*/
        queue.removeFirst();
        System.out.println(queue.toString());
    }
}
~~~

### Vector

## Set

* 元素无序、不重复、无索引
* Set的实现类是基于Map来实现的

### 哈希值

![image-20230218154116983](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181541747.png)

### HashSet

1. 特点

   * 对集合的迭代顺序不作任何保证，也就是说不保证存储和取出的元素顺序一致
   * 没有带索弓|的方法，所以不能使用普通for循环遍历
   * 由于是Set集合，所以是不包含重复元素的集合

2. 底层原理
   
   * 底层数据结构是HashMap
     
   * 保证元素唯一性
     
     要保证元素唯一性， 需要重写hashCode()和equals()。
     
     ![image-20230218154652172](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181546683.png)

#### LinkedHashSet

> 注意：LinkedHashSet是有序、不重复、无索引

1. 特点
   * 哈希表和链表实现的Set接口，具有可预测的迭代次序
   * 由链表保证元素有序,也就是说元素的存储和取出顺序是一致的
   * 由哈希表保证元素唯一，也就是说没有重复的元素
2. 底层原理
   * 底层通过`LinkedHashMap`实现

### TreeSet

1. 特点

   * TreeSet按照大小默认升序排序、是不重复、无索引的。

   ![image-20230218182847835](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181828513.png)

2. 底层实现

   * 底层是红黑树（自平衡的二叉排序树）

3. Comparable接口和Compartor类

   * 用TreeSet集合存储自定义对象，无参构造方法使用的是自然排序对元素进行排序的自然排序，就是让元素所属的类实现Comparable接口，重写compareTo(T o)方法重写方法时，-定要注意排序规则必须按照要求的主要条件和次要条件来写
   * 用TreeSet集合存储自定义对象，带参构造方法使用的是比较器排序对元素进行排序的比较器排序,就是让集合构造方法接收Comparator的实现类对象，重写compare(T o1,T o2)方法

## Queue

### PriorityQueue

### DelayQueue

### ArrayDeque

1. 底层
   * 可扩容动态数组

## Map

参考链接：https://www.cnblogs.com/haimishasha/p/10790508.html#autoid-4-2-0

### HashMap

参考：https://zhuanlan.zhihu.com/p/21673805

1. 特点

2. 底层原理
   
   * HashMap在jdk1.7中底层数据结构使用的是数组+链表。在jdk1.8中使用的是数组+链表或红黑树
   * 链表过长解决方法：
     * 扩容
     * 树化
       * 只有当链表长度超过树化阈值8，且数组长度大于64才会尝试树化
   * 树化后退化
     * 在扩容时如果拆分树时，树元素个数<= 6则会退化链表,
     * remove树节点时，若root、root.left、 root.right、 root.left.left 有一一个为null ,也会退化为链表

3. 常见面试
   
   ![image-20230219120133521](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191201564.png)
   
   ![image-20230219181151936](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191811015.png)
   
   ![image-20230219211521433](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302192115430.png)

4. 常用方法
   
   ![image-20230219105815926](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191058116.png)
   
   ![image-20230219105909038](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191059258.png)

#### LinkedHashMap

### TreeMap

### HashTable

# I/O操作

参考：

* [Java I/O, NIO, and NIO.2](https://docs.oracle.com/javase/8/docs/technotes/guides/io/index.html)
* https://www.bilibili.com/video/BV1gz4y1C7RK/?spm_id_from=333.788.recommend_more_video.2&vd_source=fabefd3fabfadb9324761989b55c26ea

## File类

1. File类：位于java.io.File包中，代表操作系统中文件对象（文件及文件夹）

2. File类的创建
   
   ![image-20211227210216574](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211227210216574.png)

3. 常用API
   
   参考文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/io/File.html
   
   ![image-20211227211734081](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211227211734081.png)
   
   ![image-20211227213211148](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211227213211148.png)

4. 小案例
   
   * 搜索文件

## 字符集

1. 相关概念
2. ASCII
3. GBK
4. Unicode

## I/O流基础

### 概述

1. 流：是一种抽象概念，是对数据传输的总称。也就是说数据在设备间的传输称为流，流的本质是数据传输。I0流就是用来处理设备间数据传输问题的。
2. 常见的应用：文件复制;文件上传;文件下载
3. 分类
   * 按照数据操作分
     * 文件
     * 数组
     * 管道
     * 基本数据类型
     * 缓冲操作
     * 打印
     * 对象序列化和反序列化
     * 转换
   * 按照数据类型分
     * 字节流
       * 字节输入流（InputStream）
         * ByteArrayInputStream
         * PipedInputStream
         * FileInputStream
         * FilterInputStream
           * BufferedInputStream
           * DataInputStream
       * 字节输出流（OutputStream）
         * ByteArrayOutputStream
         * PipedOutputStream
         * FileOutputStream
         * FilterOutputStream
           * BufferedOutputStream
           * DataOutputStream
           * PrintStream
         * ObjectOutputStream
     * 字符流
       * 字符输入流（Reader）
         * CharArrayReader
         * PipedReader
         * FilterReader
         * BufferedReader
         * InputStreamReader
           * FileReader
       * 字符输出流（Writer）
         * CharArrayWriter
         * PipedWriter
         * FilterWriter
         * BufferedWriter
         * OutputStreamWriter
           * FileWriter
         * PrintWriter
     * 字节流和字符流的区别：
       * 字节流读取单个字节，字符流读取单个字符(一个字符根据编码的不同，对应的字节也不同，如 UTF-8 编码中文汉字是 3 个字节，GBK编码中文汉字是 2 个字节。) 
       * 字节流用来处理二进制文件(图片、MP3、视频文件)，字符流用来处理文本文件(可以看做是特殊的二进制文件，使用了某种编码，人可以阅读)。

![image-20230418222346754](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202304182223037.png)

* FileInputStream 和 FileOutputStream：用于从文件中读取或向文件中写入字节。
* ByteArrayInputStream 和 ByteArrayOutputStream：在内存中的字节数组上进行读写操作。
* BufferedInputStream 和 BufferedOutputStream：提供缓冲机制以提高性能。
* DataInputStream 和 DataOutputStream：支持读写基本数据类型（如 int, float 等）。
* ObjectInputStream 和 ObjectOutputStream：用于对象的序列化和反序列化。
* FileReader 和 FileWriter：用于从文件中读取或向文件中写入字符。
* CharArrayReader 和 CharArrayWriter：在字符数组上进行读写操作。
* BufferedReader 和 BufferedWriter：提供缓冲机制以提高性能。
* InputStreamReader 和 OutputStreamWriter：作为桥梁，将字节流转换为字符流，反之亦然，同时负责字符编码转换。
* PrintWriter：提供方便的方法来格式化输出，类似于 System.out.println()。

### 字节输出流（OutputStream）

1. 常用实现类
   
   * FileOutputStream
   * BufferedOutputStream

2. 常用方法
   
   ![image-20221228181241689](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202212281812241.png)

3. 空间

### 字节输入流（InputStream）

1. 常用实现类
   * FileInputStream
   * BufferedInputStream

### 字符输入流(InputStreamReader)

1. 常用类
   
   * InputStreamReader
   * FileReader
   * BufferedReader

2. 读数据的2种方式
   
   ![image-20221230180301466](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202212301803038.png)

### 字符输出流（OutputStreamWriter）

1. 写数据的5种方式
   
   ![image-20221230175500549](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202212301755663.png)

```java
package com.chen.file;

/**
 * @author WenJianChen
 * @version 1.0
 * @date 2022/12/30 17:43
 */
public class InputStreamReaderDemo {
    public static void main(String[] args) throws IOException {
//        InputStreamReader inputStreamReader = new InputStreamReader(new FileInputStream("InputAndOutput\\test.txt"), StandardCharsets.UTF_8);
//        int len;
//        while ((len=inputStreamReader.read())!=-1){
//            System.out.print((char) len);
//        }
//        inputStreamReader.close();


//        InputStreamReader inputStreamReader = new InputStreamReader(new FileInputStream("InputAndOutput\\src\\com\\chen\\file\\BufferedInputStreamDemo.java"));
//        OutputStreamWriter outputStreamWriter = new OutputStreamWriter(new FileOutputStream("InputAndOutput\\test.java"));
//
//        char[] ch = new char[1024];
//        int len;
//        while((len=inputStreamReader.read(ch))!=-1){
//            outputStreamWriter.write(ch,0,len);
//            outputStreamWriter.flush();
//        }
//
//        inputStreamReader.close();
//        outputStreamWriter.close();

        FileReader fileReader = new FileReader("InputAndOutput\\src\\com\\chen\\file\\BufferedInputStreamDemo.java");
        FileWriter fileWriter = new FileWriter("InputAndOutput\\test.java");

        char[] chars = new char[1024];
        int len;
        while ((len=fileReader.read(chars))!=-1){
            fileWriter.write(chars,0,len);
            fileWriter.flush();
        }

        fileReader.close();
        fileWriter.close();

        BufferedReader bufferedReader = new BufferedReader(new FileReader("InputAndOutput\\test.java"));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("InputAndOutput\\test2.java"));

        String line;
        while((line=bufferedReader.readLine())!=null){
            bufferedWriter.write(line);
            bufferedWriter.newLine();
            bufferedWriter.flush();
        }

        bufferedReader.close();
        bufferedWriter.close();
    }
}
```

### 应用：文件复制

1. 复制文件
   
   ```java
   public static void copyFile(File srcFile,File destFile) throws IOException {
           BufferedInputStream bis = new BufferedInputStream(new FileInputStream(srcFile));
           BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(destFile));
   
           byte[] bytes = new byte[1024];
           int len;
           while ((len=bis.read(bytes))!=-1){
               bos.write(bytes,0,len);
           }
   
           bis.close();
           bos.close();
       }
   ```

2. 异常处理
   
   ![image-20230105090357888](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301050904199.png)
   
   ```java
   public static void copyFile(File srcFile,File destFile) throws IOException {
           BufferedInputStream bis = new BufferedInputStream(new FileInputStream(srcFile));
           BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(destFile));
   
           byte[] bytes = new byte[1024];
           int len;
           while ((len=bis.read(bytes))!=-1){
               bos.write(bytes,0,len);
           }
   
           bis.close();
           bos.close();
       }
   
       /**
        * 常规异常处理
        * @param srcFile
        * @param destFile
        */
       public static void copyFile2(File srcFile,File destFile) {
           BufferedInputStream bis = null;
           BufferedOutputStream bos = null;
           try {
               bis = new BufferedInputStream(new FileInputStream(srcFile));
               bos = new BufferedOutputStream(new FileOutputStream(destFile));
   
               byte[] bytes = new byte[1024];
               int len;
               while ((len=bis.read(bytes))!=-1){
                   bos.write(bytes,0,len);
               }
           } catch (IOException e) {
               e.printStackTrace();
           } finally {
               if (bis!=null){
                   try {
                       bis.close();
                   } catch (IOException e) {
                       e.printStackTrace();
                   }
               }
               if (bos!=null){
                   try {
                       bos.close();
                   } catch (IOException e) {
                       e.printStackTrace();
                   }
               }
           }
       }
   
       /**
        * JDK7 处理
        * @param srcFile
        * @param destFile
        */
       public static void copyFile3(File srcFile,File destFile) {
           try (BufferedInputStream bis = new BufferedInputStream(new FileInputStream(srcFile));
           BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(destFile));){
   
               byte[] bytes = new byte[1024];
               int len;
               while ((len=bis.read(bytes))!=-1){
                   bos.write(bytes,0,len);
               }
           } catch (IOException e) {
               e.printStackTrace();
           }
       }
   
       /**
        * JDK9 处理
        * @param srcFile
        * @param destFile
        */
   //    public static void copyFile4(File srcFile,File destFile) {
   //        BufferedInputStream bis = new BufferedInputStream(new FileInputStream(srcFile));
   //        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(destFile));
   //        try (bis;bos){
   //            byte[] bytes = new byte[1024];
   //            int len;
   //            while ((len=bis.read(bytes))!=-1){
   //                bos.write(bytes,0,len);
   //            }
   //        } catch (IOException e) {
   //            e.printStackTrace();
   //        }
   //    }
   ```

### 特殊操作流

#### 标准输入输出流

![image-20230105093202370](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301050932510.png)

![image-20230105093242144](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301050932224.png)

#### 打印流

1. 分类
   
   * 字节打印流：PrintStream
   * 字符打印流：PrintWriter

2. 特点
   
   * 只负责输出数据，不负责读取数据
   * 有特有方法

3. 字节打印流（PrintStream）
   
   * PringStream(String fileName)：使用指定的文件名创建新的打印流
   * 使用继承父类的方法写数据，查看的时候会转码，使用自己特有方法写数据原样输出

4. 字符打印流
   
   * 构造方法
     
     ![image-20230105094225259](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301050942091.png)

### 对象序列化

jdk序列化Api文档：https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/package-summary.html

1. 概念：对象序列化是指将对象保存到磁盘中或者在网络中传输对象。这种机制就是使用一个字节序列表示一个对象，该字节序列包含：对象的类型、对象的数据和对象中存储的属性等信息。字节序列写到文件之后，相当于文件中持久保存了一个对象信息。要实现序列化和反序列化就要使用对象序列化流和对象反序列化流。

2. 对象序列化流（ObjectOutputStream）
   
   ![image-20230105100920603](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051009928.png)
   
   ```java
           ObjectOutputStream objectOutputStream = new ObjectOutputStream(new FileOutputStream("InputAndOutput\\ObjectOutputStream.txt"));
   
           objectOutputStream.writeObject(new Student("00001","whymechen",22));
   
           objectOutputStream.close();
   ```

3. 对象反序列化流（ObjectInputStream）
   
   ![image-20230105101507054](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051015801.png)
   
   ```java
           ObjectInputStream objectInputStream = new ObjectInputStream(new FileInputStream("InputAndOutput\\ObjectOutputStream.txt"));
           Student student = (Student) objectInputStream.readObject();
   
           System.out.println(student.toString());
   
           objectInputStream.close();
   ```

4. 常见问题及解决
   
   ![image-20230105102330823](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051023459.png)

### Properties

1. 概述：Properties是一个Map体系的集合类。Properties可以保存到流中或从流中加载。

2. 特有方法
   
   ![image-20230105134657581](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051346314.png)

3. 与IO流结合
   
   ![image-20230105135440885](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051354966.png)

```java
public class PropertiesDemo {
    public static void main(String[] args) throws IOException {
//        Properties properties = new Properties();
//        properties.put("0001","xiaoming");
//        properties.put("0002","zhangsan");
//        properties.put("0003","lisi");
//
//        for (Object key : properties.keySet()) {
//            Object value = properties.get(key);
//            System.out.println(key+" "+value);
//        }

        //Properties特有方法
//        Properties properties = new Properties();
//        properties.setProperty("chen","25");
//        properties.setProperty("wang","22");
//        properties.setProperty("li","23");
//
//        System.out.println(properties.getProperty("chen"));
//        System.out.println("======================================");
//
//        for (String name : properties.stringPropertyNames()) {
//            System.out.println(name+" "+properties.getProperty(name));
//        }

//        myStore();
        myLoad();
    }

    private static void myLoad() throws IOException {
        Properties properties = new Properties();
        //文件中的数据保存到集合
        BufferedReader bufferedReader = new BufferedReader(new FileReader("InputAndOutput\\propertiesDemo.txt"));
        properties.load(bufferedReader);

        System.out.println(properties);

        bufferedReader.close();
    }

    private static void myStore() throws IOException {
        //集合中的数据保存到文件
        Properties properties = new Properties();
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("InputAndOutput\\propertiesDemo.txt"));

        properties.setProperty("0001","张三");
        properties.setProperty("0002","李四");
        properties.setProperty("0003","王五");

        properties.store(bufferedWriter,null);

        bufferedWriter.close();
    }
}
```

## 序列化与反序列化

1. 定义
2. 应用场景
   * 网络传输
   * 文件存储
   * 数据库存储
   * 内存读写
3. 常见序列化协议
   * Hessian
   * Kryo
   * Protobuf
   * ProtoStuff
4. SerialVersionUID
5. `transient`关键字

### Kryo

项目地址：https://github.com/EsotericSoftware/kryo

1. 简介
   * Kryo 是一个高性能的序列化/反序列化工具
   * 由于其变长存储特性并使用了字节码生成机制，拥有较高的运行速度和较小的字节码体积

### Protobuf

项目地址：https://github.com/protocolbuffers/protobuf

文档地址：https://protobuf.dev/

1. 简介
   * Protobuf 包含序列化格式的定义、各种语言的库以及一个 IDL 编译器。正常情况下你需要定义 proto 文件，然后使用 IDL 编译器编译成你需要的语言

### ProtoStuff

项目地址：https://github.com/protostuff/protostuff

### Hessian

## IO模型

UNIX 系统下， IO 模型一共有 5 种：**同步阻塞 I/O**、**同步非阻塞 I/O**、**I/O 多路复用**、**信号驱动 I/O** 和**异步 I/O**。

### Java BIO

### Java NIO

1. 简介：Java 中的 NIO 于 Java 1.4 中引入，对应 `java.nio` 包，提供了 `Channel` , `Selector`，`Buffer` 等抽象。

2. 与传统IO的区别

   * 传统 IO 基于字节流和字符流进行操作（面向流），而 NIO 基于 Channel 和 Buffer(缓冲区)进行操作（面向缓冲区），数据总是从通道读取到缓冲区中，或者从缓冲区写入到通道中。

   * Selector(选择区)用于监听多个通道的事件（比如：连接打开，

     数据到达）

3. 核心部分

   * Channel(通道)
   * Buffer(缓冲区)
   * Selector

4. nio包

   ![image-20230418223501025](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202304182235383.png)
   
5. 零拷贝

### Java AIO

AIO 也就是 NIO 2。Java 7 中引入了 NIO 的改进版 NIO 2,它是异步 IO 模型。

## 设计模式应用

1. 装饰器模式
2. 适配器模式
3. 工厂模式
4. 观察者模式

# 多线程

多线程技术通常用于异步编程、并发编程。详情见：[并发编程](./并发编程.md)

多线程技术可以用于实现并发执行任务，提高程序的运行效率。它可以用于实现以下几种场景：  

* 响应式编程：多线程可以用于实现快速响应用户请求，提高用户体验。 
* 并发计算：多线程可以用于实现多个任务同时执行，提高计算效率。
* 并发I/O操作：多线程可以用于实现多个I/O操作同时进行，提高I/O效率。 
* 延迟操作：多线程可以用于实现需要等待一定时间才能执行的操作，例如定时任务。 
* 并发访问共享资源：多线程可以用于实现多个线程并发访问共享资源，提高资源利用率。

## 进程

window的时代开启了多进程设计，在一个时间段可以同时运行多个程序并进行资源的轮流抢占。但是在一个时间点只会有一个进程在执行。

## 线程

线程是在进程基础上创建并且使用的，所以线程依赖于进程的支持，但是线程的启动速度要比进程快得多。

> Java中与线程有关的包：
>
> - `java.lang` 包：该包中包含与线程直接相关的类，如 `Thread`、`Runnable`、`ThreadGroup` 等。其中，`Thread` 类用于创建和操作线程；`Runnable` 接口定义了线程执行的任务；`ThreadGroup` 类用于管理线程组。
>   - `java.lang.Thread`：表示一个线程，可以通过继承 `Thread` 类或实现 `Runnable` 接口来创建线程。
>   - `java.lang.Runnable`：定义了线程要执行的任务，通常作为参数传递给 `Thread` 类的构造方法。
>   - `java.lang.ThreadGroup`：表示一组线程的集合，可以对这组线程进行统一地管理。
> - `java.util.concurrent` 包：该包中提供了更高级别的线程管理工具和并发编程的支持类。其中，常用的类包括 `Executor`、`ExecutorService`、`ThreadPoolExecutor`、`Future` 等，它们提供了线程池、异步执行任务、并发控制等功能，简化了多线程编程的复杂性。
>   - `java.util.concurrent.Executor`：定义了执行任务的接口，可以将任务提交给执行器来异步执行。
>   - `java.util.concurrent.ExecutorService`：继承自 `Executor` 接口，提供了更多的任务执行控制方法，如提交任务、关闭执行器等。
>   - `java.util.concurrent.ThreadPoolExecutor`：实现了 `ExecutorService` 接口，是线程池的具体实现。
>   - `java.util.concurrent.Future`：表示一个可能还未完成的异步任务的结果。

### 多线程的定义

在java中实现多线程的定义，需要有一个专门的线程主体类进行线程的定义，必须实现特定的接口或继承特定的父类。

#### 继承Thread类实现多线程

在java中提供了一个java.lang.Thread的程序类，只要一个类继承了此类就表示这个类为线程的主体类。在该主体类中覆盖重写run()方法，多线程要执行的功能都应该再run()方法内部进行定义。需要说明的是：正常情况下只需产生一个实例化对象，然后调用类中提供的方法。但是run()方法是不能被直接调用的，而是需要使用start()方法来启动多线程实现线程的调度。

* 优点：编码简单
* 缺点：因为该类已继承Thread类，无法继承其他类，故不利于扩

```java
class MyThread extends Thread{
    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println(this.getName()+":"+i);
        }
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        MyThread myThread=new MyThread();
        MyThread myThread1=new MyThread();
        MyThread myThread2=new MyThread();

        myThread.start();
        myThread1.start();
        myThread2.start();
    }
}
```

#### 基于Ruanable接口实现多线程

* 优点：可以继承其他类和实现其他接口，扩展性强
* 缺点：编码较为复杂，多次封装

```java
package test;

/*
    使用Runnable接口实现多线程
    1.创建一个MyRunnable类来实现Runnable接口，在这个类中重写run方法
    2.创建一个MyRunnable类的对象和Thread类的对象，将MyRunnable的对象作为参数传输Thread类的构造方法中
    3.启动线程
*/
public class ThreadDemo2 {
    public static void main(String[] args) {
        Thread thread1 = new Thread(new MyRunnable());
        thread1.start();

        //匿名内部类形式
        Thread thread2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 100; i++) {
                    System.out.println("son2 thread: "+i);
                }
            }
        });
        thread2.start();

        //lambda表达式形式
        Thread thread3 = new Thread(()->{
            for (int i = 0; i < 100; i++) {
                System.out.println("son3 thread: "+i);
            }
        });
        thread3.start();

        for (int i = 0; i < 100; i++) {
            System.out.println("father thread: "+i);
        }
    }
}

class MyRunnable implements Runnable{
    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            System.out.println("son1 thread: "+i);
        }
    }
}
```

#### Thread和Runnable关系

实现多线程有两种方式：Thread类和Runnable接口。但是从结构上来讲使用Runnable接口更方便。因为其避免了单继承的局限，同时也可以更好的对功能进行扩充。但是通过观察Thread类的定义

```java
public class Thread extends Object implements Runnable {}
```

可以发现Thread类是Runnable接口的子类，那么在继承Thread类是覆盖重写的run()方法实际上还是Runnable接口的run()方法。

多线程之中，使用了代理设计模式的结构。用户自定义的线程主体只是负责项目核心功能的实现，而所有的辅助实现全部交由Thread类实现。

![image-20210718210459721](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210718210459721.png)

多线程开发的本质实质上就是多个线程可以进行同一资源的抢占，那么Thread主要描述的是线程，而资源的描述是通过Runnable。

![image-20210718211447972](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210718211447972.png)

#### Callable实现多线程

传统的多线程实现是依靠Runnable接口，但是Runnable接口有一个缺点：线程执行完毕后无法获取一个返回值。从JDK1.5之后提出了一个新的线程实现接口：java.util.concurrent.Callable。

![image-20220909233414588](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209092337483.png)

* 优点：扩展性强
* 缺点：编码较为复杂

![image-20210721211443958](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210721211443958.png)

```java
import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;

class MyThread implements Callable<String>{
    @Override
    public String call() throw Exception{
        for(int i=0;i<10;i++){
            System.out.println("***********线程执行:x="+x);
        }
        return "线程执行完毕");
    }
}

public class ThreadDemo{
    public static void mainf(String[] args) throw Exception{
        FutureTask<String> task=new FutureTask<>(new MyThread());
        new Thread(task).start();
        System.out.println("【线程返回数据】："+task.get());
    }
}
```

### 线程运行状态

![image-20210721212820134](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210721212820134.png)

![image-20230220221305153](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302202213059.png)

![image-20220913202914929](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209132029314.png)

![image-20220913203242411](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209132032460.png)

### 线程常用方法

1. 线程的命名与取得
   
   * 构造方法：public Thread(Runnable target,String name)
   * 设置名字：publid final void setName(String name)
   * 取得名字：public final String getName()

2. 线程控制
   
   * public static void sleep(long millis)：使当前正在执行的线程停留（暂停执行）指定的毫秒数
   * void join()：等待这个线程死亡
   * void setDaemon(boolean on)：将此线程标记为守护线程，当运行的线程都是守护线程时，java虚拟机将退出

3. 线程中断

4. 线程调度
   
   * 常用的线程调度方式有两种：
     
     * 分时调度模型
     * 抢占式调度模型
     
     **java使用的线程调度方式是抢占式调度模型。**
   
   * 设置和获取线程优先级
     
     * public final int getPriority()：返回此线程的优先级
     * public final void setPriority(int newPriority)：更改线程的优先级
   
   注意：线程默认优先级为5；线程优先级的范围是：1-10；线程优先级高仅仅表示线程获取的CPU时间片的几率高，但是要在次数比较多或者多次运行的时候才能看到想要的效果。
   
   ![image-20220910173947436](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209101739700.png)

### 线程安全

1. 线程安全问题： 多个线程同时操作同一个共享资源的时候可能出现的业务安全问题。

2. 出现原因：
   
   * 存在多线程并发
   * 同时访问共享资源
   * 存在修改共享资源的行为(可破坏)

3. 模拟案例
   
   ```java
   /**
    *
    * An account simulation class
    *
    * @author WenJianChen
    * @version 1.0
    * @date 2022/9/10 17:54
    *
    */
   public class Account {
       private int cardID;
       private int money;
   
       /**
        * draw money
        * @param money
        * @return
        */
       public void drawMoney(int money){
           String name = Thread.currentThread().getName();
           if (money<=this.money){
               System.out.println(name+"draw money successfully");
               this.money-=money;
               System.out.println("balance: "+this.money);
           }else {
               System.out.println("sorry,"+name+" Insufficient balance");
           }
       }
   
       @Override
       public String toString() {
           return "Account{" +
                   "cardID=" + cardID +
                   ", money=" + money +
                   '}';
       }
   
       public Account() {
           this.cardID = cardID;
           this.money = money;
       }
   
       public int getCardID() {
           return cardID;
       }
   
       public void setCardID(int cardID) {
           this.cardID = cardID;
       }
   
       public int getMoney() {
           return money;
       }
   
       public void setMoney(int money) {
           this.money = money;
       }
   }
   ========================================
   /**
    * @author WenJianChen
    * @version 1.0
    * @date 2022/9/10 18:25
    */
   public class ThreadDemo5 {
       public static void main(String[] args) {
           Account account = new Account();
           account.setCardID(1);
           account.setMoney(100000);
   
           new DrawMoney(account,"小明").start();
           new DrawMoney(account,"小红").start();
       }
   }
   
   class DrawMoney extends Thread{
       private Account account;
   
       public DrawMoney(Account account,String threadName){
           super(threadName);
           this.account=account;
       }
   
       @Override
       public void run() {
           account.drawMoney(100000);
       }
   }
   ```

4. 常见的线程安全的类
   
   * StringBuffer
   * Vector
   * HashTable
   
   ![image-20230220224942536](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302202249194.png)

### 线程同步

1. 同步思想
   
   * 加锁： 多个线程依次访问共享资源
     
     * 同步代码块
       
       > 理论上： 锁对象只要对于当前同时执行的线程来说是同一个对象即可。
       > 
       > 规范上：建议使用共享资源作为锁对象。对于实例方法建议使用this作为锁对象，对于静态方法建议使用字节码（类名.class）对象作为锁对象。
       > 
       > **synchronized（同步锁对象）{**
       > 
       > ​    **操作共享资源的代码**
       > 
       > **}**
     
     * 同步方法
       
       > * 同步方法其实底层也是有隐式锁对象的，只是锁的范围是整个方法代码。
       > * 如果方法是实例方法:同步方法默认用this作为的锁对象。但是代码要高度面向对象!
       > * 如果方法是静态方法:同步方法默认用类名.class作为的锁对象。
       > 
       > **修饰符 synchronized 返回值类型 方法名称（形参列表）{**
       > 
       > ​    **操作共享资源的代码**        
       > 
       > **}**
     
     * Lock锁
       
       > ![image-20220910231502796](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209102315950.png)

### 线程通信

1. 线程通信：线程相互发送数据

2. 常见模型
   
   * 生产者与消费者模型
     
     ![image-20230220225229649](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302202252952.png)
     
     ![image-20220912130658196](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209121307430.png)

### 线程池

参考：[JavaSE基础强化，深入学习线程池](https://www.bilibili.com/video/BV18J41157DX?spm_id_from=333.1245.0.0)

#### 基础

1. 线程池：**可以复用线程的技术**

   * 线程池其实就是一种多线程处理形式，处理过程中可以将任务添加到队列中，然后在创建线程后自动启动这些任务。
   * 使用线程池的原因：
     * 可以根据系统的需求和硬件环境灵活的控制线程的数量,且可以对所有线程进行统一的管理和控制，从而提高系统的运行效率,降低系统运行运行压力。
     * 线程和任务分离，提升线程重用性
     * 制线程并发数量，降低服务器压力，统一管理所有线程
     * 提升系统响应速度，假如创建线程用的时间为T1，执行任务用的时间为T2，销毁线程用的时间为T3，那么使用线程池就免去了T1和T3的时间
   * 常见应用场景：
     * 网购商品秒杀
     * 云盘文件上传和下载
     * 12306网上购票系统等

2. 基本原理

   ![image-20220912131231401](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209121312471.png)

#### 内置线程池

* `ExecutorService`
* `ThreadPoolExcutor`
* `Excetors`

![image-20220912131322867](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209121313452.png)

1. `ExecutorService`

   * api文档：https://docs.oracle.com/javase/8/docs/api/
   * java内置的线程池接口

2. `ThreadPoolExecutor` 

   * api文档：https://docs.oracle.com/javase/8/docs/api/
   * 构造器：

   ![image-20220912131429879](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209121314545.png)

   ![image-20220913191802427](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209131918792.png)

   ![image-20220913191826706](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209131918660.png)

![image-20220913194838758](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209131948194.png)

注意：

* 新任务提交时发现核心线程都在忙，任务队列也满了，并且还可以创建临时线程，此时才会创建临时线程。
* 核心线程和临时线程都在忙，任务队列也满了，新的任务过来的时候才会开始任务拒绝。

#### 自定义线程池

1. 重要参数

   * 核心线程数量
   * 任务队列大小
     * 一般可以设置为，核心线程数/单个任务执行时间*2;
   * 最大线程数（maximumPoolThread）
   * 最大空闲时间（keepAliveTime）

2. 简单示例

   ```java
   package thread_pool;
   
   import java.util.Collections;
   import java.util.LinkedList;
   import java.util.List;
   
   /**
    * 一个自定义的线程池类;
    * 成员变量:
    * 1:任务队列集合，需要控制线程安全问题
    * 2:当前线程数量
    * 3:核心线程数量
    * 4:最大线程数量
    * 5:任务队列的长度
    * 成员方法
    * 1:提交任务;
    * 将任务添加到集合中，需要判断是否超出了任务总长度2:执行任务;
    * 判断当前线程的数量，决定创建核心线程还是非核心线程
    *
    * @author whymechen
    * @version 1.0
    * @date 2023/11/9 22:04
    **/
   public class ThreadPoolDemo {
   
       /**
        * 任务队列集合
        */
       private List<Runnable> taskQueue = Collections.synchronizedList(new LinkedList<>());
   
       /**
        * 任务队列的长度
        */
       private Long taskQueueSize = 20L;
   
       /**
        * 核心线程数量
        */
       private Long corePoolSize = 10L;
   
       /**
        * 最大线程数量
        */
       private Long maximumPoolSize = 20L;
   
       /**
        * 当前线程数量
        */
       private Long currentPoolSize = 0L;
   
       /**
        * 任务提交
        *
        * @param runnable 任务
        */
       public void submit(Runnable runnable) {
           //判断任务队列是否满了
           if (taskQueue.size() >= taskQueueSize) {
               System.out.println("任务队列已满，无法添加任务");
               return;
           }
           //添加任务
           taskQueue.add(runnable);
           executeTask(runnable);
       }
   
       /**
        * 执行任务
        *
        * @param runnable 任务
        */
       private void executeTask(Runnable runnable) {
           //判断当前线程数量是否小于核心线程数量
           if (currentPoolSize < corePoolSize) {
               //创建核心线程
               new ThreadWorkerDemo("core thread" + currentPoolSize,taskQueue).start();
               currentPoolSize++;
           } else {
               //创建非核心线程
               if (currentPoolSize < maximumPoolSize) {
                   new ThreadWorkerDemo("non-core thread" + currentPoolSize,taskQueue).start();
                   currentPoolSize++;
               }else {
                   //如果当前线程数量大于最大线程数量，则将任务添加到任务队列中
                   System.out.println("当前线程数量已达到最大值，将任务添加到任务队列中");
               }
           }
       }
   }
   ```

   ```java
   package thread_pool;
   
   import java.util.List;
   
   /**
    * @author whymechen
    * @version 1.0
    * @date 2023/11/9 21:56
    **/
   public class ThreadWorkerDemo extends Thread{
   
       private String threadName;
   
       private List<Runnable> tasks;
   
       public ThreadWorkerDemo(String threadName, List<Runnable> tasks) {
           this.threadName = threadName;
           this.tasks = tasks;
       }
   
       @Override
       public void run() {
           while (true){
               synchronized (tasks){
                   if (tasks.size() == 0){
                       System.out.println(threadName + "任务队列为空，退出");
                       break;
                   }
                   Runnable task = tasks.remove(0);
                   System.out.println(threadName + "开始执行任务：" + task);
                   try {
                       Thread.sleep(1000);
                   } catch (InterruptedException e) {
                   }
               }
           }
       }
   }
   ```

### 定时器

1. 定时器：一种控制任务延时调用，或者周期调用的技术。可用于闹钟、定时邮件的发送。

2. 实现方式
   
   * Timer
   * ScheduleExecutorService
   
   ![image-20220913200705966](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209132007407.png)
   
   ![image-20220913201527702](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202209132015465.png)

3. 代码演示
   
   ```java
       public static void main(String[] args) {
           Timer timer = new Timer();
           timer.schedule(new TimerTask() {
               @Override
               public void run() {
                   System.out.println(Thread.currentThread().getName()+"输出了");
               }
           },3000,3000);
       }
   ======================================
   public static void main(String[] args) {
           ScheduledExecutorService pool = Executors.newScheduledThreadPool(3);
   
           pool.scheduleAtFixedRate(new TimerTask() {
               @Override
               public void run() {
                   System.out.println(Thread.currentThread().getName()+" 输出了");
               }
           },0,2, TimeUnit.SECONDS);
       }
   ```

## ThreadLocal类

从ava官方文档中的描述: ThreadLocal类用来提供线程内部的局部变量。这种变量在多线程环境下访问(通过get和set方法访问)时能保证各个线程的变量相对独立于其他线程内的变量。ThreadLocal实例通常来说都是
private static类型的,用于关联线程和线程上下文。

> * 线程并发:在多线程并发的场景下
> * 传递数据:我们可以通过ThreadLocal在同一线程，不同组件中传递公共变量
> * 线程隔离每个线程的变量都是独立的，不会互相影响

### 常用方法

## 锁

# 反射

1. 简介：**反射是框架设计的灵魂。**

   * 框架：半成品软件。可以在框架的基础上进行软件开发，简化编码。

     反射：将类的各个组成部分封装为其他对象，这就是反射机制。

2. 优缺点

   * 优点：代码更加灵活、为各种框架提供开箱即用的功能提供了便利。
   * 缺点：主要为安全性问题，比如可以无视泛型参数的安全检查（泛型参数的安全检查发生在编译时）。

## Class类

![image-20210202115502782](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210202115502782.png)

![image-20221201133204597](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202212011332544.png)

如果想要实现反射的处理操作，那么首先要采用的就是Object中所提供的的一个方法获取Class对象信息：public final Class<?> getClass();

1. 反射中所有的核心操作都是通过Class类对象展开的，获取Class对象的三种方式：
   
   * **【class类支持】**Class.forName("全类名")：将字节码文件加载进内存，返回Class对象（多用于配置文件）
   * **【JVM直接支持】**类名.class：通过类名的属性class获取（多用于参数传递）
   * **【Object类支持】**对象.getClass()：通过Object类提供的getClass（）方法获取
   
   注意：同一个字节码文件（*.class）在一次程序运行中，只会被加载一次，不论通过哪种方式获得的Class对象都是同一个对象

2. Class类方法（获取类结构信息）
   
   * 获取包名
     
     * Package getPackage()
   
   * 获得父类信息
     
     * Class<? super T> getSuperclass() 
   
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
     
     * getName()

```java
package reflect;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

/**
 * 方法演示
 * @author WenJianChen
 * @version 1.0
 * @date 2022/12/1 13:36
 */
public class ReflectDemo {
    public static void main(String[] args) throws ClassNotFoundException {
        Person person = new Person();
        person.setName("chen");
        person.setId("123456789");
        Class<? extends Person> personClass = person.getClass();
//        Class<?> personClass = Class.forName("reflect.Person");
//        Class<Person> personClass = Person.class;
        System.out.println("成员变量");
        for (Field field : personClass.getFields()) {
            System.out.println(field);
        }

        System.out.println("--------------------");
        System.out.println("成员方法");
        for (Method method : personClass.getMethods()) {
            System.out.println(method.toString());
        }

        System.out.println("--------------------");
        System.out.println("构造方法");
        for (Constructor<?> constructor : personClass.getConstructors()) {
            System.out.println(constructor.toString());
        }

                System.out.println("===================================");
        Field name = personClass.getDeclaredField("name");
        //暴力反射，忽略访问权限安全检查
        name.setAccessible(true);
        System.out.println(name.get(person));

        name.set(person,"wang");
        System.out.println(person.getName());

                System.out.println("-------------------------------");

        Constructor<? extends Person> noParameterConstructor = personClass.getConstructor();
        //创建对象
        Person person2=noParameterConstructor.newInstance();
        person2.setId("987654321");
        person2.setName("LiMing");
        System.out.println(person2);

        System.out.println("----------------------");
        Method eatMethod = personClass.getMethod("eat");
        //执行方法
        eatMethod.invoke(person);
    }
}
```

```java
package reflect;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Properties;

/**
 * 案例：创建任意类的对象并执行任意方法
 * 实现方式：
 *      * 设置配置文件，将需要创建的全类名和需要执行的方法进行定义说明
 *      * 读取配置文件
 *      * 利用反射加载类文件后创建对象并执行方法
 *
 * @author WenJianChen
 * @version 1.0
 * @date 2022/12/1 14:30
 */
public class ReflectDemo2 {
    public static void main(String[] args) throws IOException, InstantiationException, IllegalAccessException, InvocationTargetException {
        Properties properties = new Properties();
        //获得类加载器
        ClassLoader classLoader = ReflectDemo2.class.getClassLoader();
        properties.load(classLoader.getResourceAsStream("property.properties"));

        //获取文件数据
        String className = properties.getProperty("className");
        String methodName = properties.getProperty("methodName");

        Class<?> aClass = null;
        try {
            aClass = Class.forName(className);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            System.out.println("没有指定的类，请检查配置文件是否错误或创建指定类");
        }

        Object instance = aClass.newInstance();

        Method method = null;
        try {
            method = aClass.getMethod(methodName);
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
            System.out.println("没有指定方法，请检查配置文件是否错误或在指定类中创建指定方法");
        }

        method.invoke(instance);

    }
}
```

## 反射实例化对象

* 在JDK1.9以前的实例化：public T newInstance() throws InstantiationException,IllegalAccessException
* 在JDK1.9后：clazz.getDeclareConstructor().newInstance();

```java
package test;

public class Person {
    public Person() {
        // TODO Auto-generated constructor stub
        System.out.println("person object");
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "i am a interesting";
    }

}

+++++++++++++++++++++++++++++++++++++++++++++++++++++++

package test;

public class Test04 {
    public static void main(String[] args) throws ClassNotFoundException, InstantiationException, IllegalAccessException {
        Class<?> cls=Class.forName("test.Person");
        Object object=cls.newInstance();
    }
}

+++++++++++++++++++++++++++++++++++++++++++++++++++++
package test;

import java.lang.reflect.InvocationTargetException;

public class Test04 {
    public static void main(String[] args) throws ClassNotFoundException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException {
        Class<?> cls=Class.forName("test.Person");
        Object object=cls.getDeclaredConstructor().newInstance();
    }
}
```

## 反射与工厂设计模式

1. 代码示例

2. 优势：利用反射实现工厂设计模式最大的优势在于，对于接口子类的扩充将不再影响到工厂类的定义。
   
   ![image-20210831103603429](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210831103603429.png)

## 动态代理

1. 为什么需要代理：实现无侵入式的给对象增强功能

2. 代码实现
   
   ![image-20230216231907501](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302162319458.png)

### 代理模式

参考博客：https://blog.csdn.net/qq_43478882/article/details/124191700

# 注解（Annoation）

参考资料：https://pdai.tech/md/java/basic/java-basic-x-annotation.html

1. 注解：一种代码级别的说明。JDK1.5之后提出的一个新的开发技术结构，利用annoation可以有效减少程序配置的代码并且可以利用annoation进行一些结构化定义。(可以简单理解为就是给计算机看的注释)

2. 作用
   
   * 编写文档：通过代码里标识的元数据生成文档（生成doc文档）
   * 代码分析：通过代码里标识的元数据对代码进行分析（使用反射）
   * 编译检查：通过代码里标识的元数据让编译器能够实现基本的编译检查

3. 分类
   
   * 预定义注解
   * 元注解
   * 自定义注解

4. JDK中预定义的一些注解

   * @Override：检测被该注解标注的方法是否继承自父类
   * @Deprecated：该注解标注的内容，表示已过时
   * @SuppressWarnings：压制警告（一般传递参数all）

5. 元注解：用于描述注解的注解

   * `@Retention`用于标明注解被保留的阶段
   * `@Target`用于标明注解使用的范围
   * `@Inherited`用于标明注解可继承
   * `@Documented`用于标明是否生成javadoc文档
   * `@Repeatable`
   * `@Native`

   > 前四个jdk1.5提供，后两个jdk1.8提供

6. 自定义注解

   * 本质：注解本质上就是一个接口，该接口默认继承Annoation接口
     
     ~~~java
     public interface MyAnnoation extends java.lang.annoation.Annoation{}
     ~~~
     
   * 格式：

     > * @target：描述注解能够作用的位置
     >
     >   * ElementType取值：
     >       * TYPE：可以作用于类、接口、枚举上
     >     * METHOD：可以作用于方法上
     >     * FILED：可以作用于成员变量上（包括枚举变量）
     >     * PARAMETER：方法参数
     >     * CONSTRUCTOR：构造方法
     >     * LOCAL_VARIABLE：局部变量
     >     * ANNOTATION_TYPE：注解类
     >     * PACKAGE：可用于修饰包
     >     * TYPE_PARAMETER：类型参数，JDK 1.8 新增
     >     * TYPE_USE：使用类型的任何地方，JDK 1.8 新增
     >
     > * @Retention：描述注解被保留的阶段
     >
     >   * RetentionPolicy.SOURCE（源码级别保留）：被标注的注解仅在编译阶段存在，编译后不会包含在生成的字节码中，对运行时没有影响。这种注解**通常用于提供给编译器或其他工具使用**，而不会影响实际的程序运行。
     >   * RetentionPolicy.CLASS（类级别保留）：被标注的注解会被保留到编译后的字节码文件中，并被JVM读取，但在运行时不可访问。这是**默认的保留策略**，如果没有显式指定@Retention，默认使用该策略。
     >   * RetentionPolicy.RUNTIME（运行时级别保留）：被标注的注解会被保留到编译后的字节码文件中，并在运行时可以通过反射机制访问到。这种注解**通常用于运行时的动态操作，例如自定义注解处理器、框架的扩展、依赖注入等**
     >
     > * @Documented：描述注解是否被抽取到api文档中
     >
     > * @Inherited：描述注解是否被子类继承
     >
     > public @interface 注解名称{}

   * 属性：接口中的抽象方法
     
     * 属性的返回值类型
       
       > * 基本数据类型
       > * String
       > * 枚举
       > * 注解
       > * 以上类型的数组
     
     * 使用注解时需要为其属性赋值
       
       * 可有使用default关键字给属性默认初始化值
       * 若只有一个属性要赋值且属性名称是value，则可以省略

7. 解析注解：获取注解中定义的属性值，通过接口`java.lang.reflect.AnnotatedElement`提供的方法读取

   *  `AnnotatedElement` 接口是所有可以包含注解的程序元素（如类、方法、字段等）的通用超接口，它定义了一些常见的方法来获取和操作注解信息。常用方法：
     * `T getAnnotation(Class<T> annotationClass)`：返回指定类型的注解对象，如果该注解不存在，则返回 null。
     * `Annotation[] getAnnotations()`：返回该元素上存在的所有注解的数组，包括从父类继承而来的注解。
     * `Annotation[] getDeclaredAnnotations()`：返回该元素上直接存在的所有注解的数组，不包括从父类继承而来的注解。
     * `boolean isAnnotationPresent(Class<? extends Annotation> annotationClass)`：判断该元素上是否存在指定类型的注解。
     *  `getAnnotationByType`
     * `getDeclaredAnnotationByType` 
   * 获取注解定义位置的对象
   * 获取指定的注解（getAnnoation（Class））
   * 调用注解中的抽象方法获取属性值

   ![image-20211227202726241](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211227202726241.png)

   ```java
   @Property(className = "reflect.Person",methodName = "eat")
   public class ReflectDemo {
       public static void main(String[] args) throws IOException, InstantiationException, IllegalAccessException, InvocationTargetException {
           Class<ReflectDemo> reflectDemoClass = ReflectDemo.class;
           Property annotation = reflectDemoClass.getAnnotation(Property.class);
           String className = annotation.className();
           String methodName = annotation.methodName();
           System.out.println(className);
           System.out.println(methodName);
       }
   }
   ```

8. 原理

   参考：
   
   * [java注解的本质以及注解的底层实现原理](https://blog.csdn.net/qq_20009015/article/details/106038023)
   
   当我们在Java代码中使用注解时，Annotation Processor（注解处理器）可以在编译时扫描源代码中的注解，并根据注解的定义生成额外的代码。注解处理器是Java编译器的一部分，它们负责在编译期间对注解进行处理。
   
   注解处理器通过继承 `javax.annotation.processing.AbstractProcessor` 类，并重写其中的方法来实现自定义的注解处理逻辑。通常，我们需要重写 `process()` 方法来处理特定的注解，并生成相应的代码。
   
   在编译过程中，Java编译器会检测源代码中是否存在使用了特定注解的元素（类、方法、字段等），如果有，就会调用相应的注解处理器来处理这些注解。注解处理器可以读取和分析注解及其相关元素的信息，然后根据处理逻辑生成新的代码文件。
   
   使用Annotation Processor可以帮助我们减少重复的、机械性的编码工作，提高开发效率，同时保证生成的代码的正确性和一致性。Lombok和MapStruct就是利用Annotation Processor的能力，通过注解来生成简化代码，如自动生成getter/setter方法、构造函数等。
   
   需要注意的是，Annotation Processor是在编译期间执行的，它不会改变源代码的内容，而是在编译过程中生成额外的代码文件。生成的代码文件将会被编译成字节码，并与原始代码一起打包到最终的可执行文件中。

# SPI机制

参考：

* [Java SPI机制详解](https://javaguide.cn/java/basis/spi.html)

# 网络编程

1. 网络编程：在网络通信协议下，实现网络互连的不同计算机上运行的程序可以进行数据交换。

2. 三要素
   
   * IP地址
     * IPv4和Ipv6
     * 常用命令
       * ipconfig
       * ping
   * 端口
   * 协议
     * TCP
     * UDP

## UDP协议通信

UDP协议通信

* java提供DataGramSocket类作为基于UDP协议的Socket

* 发送数据
  
  > ①创建发送端的Socket对象(DatagramSocket)
  > ②创建数据， 并把数据打包
  > ③调用DatagramSocket对象的方法发送数据
  > ④关闭发送端

* 接受数据
  
  > ①创建接收端的Socket对象(DatagramSocket)
  > ②创建一个数据包， 用于接收数据
  > ③调用DatagramSocket对象的方法接收数据
  > ④解析数据包, 并把数据在控制台显示
  > ⑤关闭接收端

```java
//接受数据
public class Demo1 {
    public static void main(String[] args) throws IOException {
        DatagramSocket datagramSocket = new DatagramSocket(10086);
        //创建数据包
        byte[] bytes = new byte[1024];
        DatagramPacket datagramPacket = new DatagramPacket(bytes,bytes.length);
        //接受数据
        datagramSocket.receive(datagramPacket);
        //解析数据并在控制台显示
        byte[] data = datagramPacket.getData();
        System.out.println(new String(data,0,data.length));
    }
}

//=========================================
//发送数据
public class Demo {
    public static void main(String[] args) throws IOException {
//        InetAddress hostName = Inet4Address.getByName("192.168.137.1");
//        InetAddress localHost = Inet4Address.getLocalHost();
//        System.out.println(hostName);
//        System.out.println(localHost.getHostAddress());

        DatagramSocket datagramSocket = new DatagramSocket();
        byte[] bytes = "hello world".getBytes(StandardCharsets.UTF_8);
        InetAddress localHost = InetAddress.getLocalHost();
        DatagramPacket datagramPacket = new DatagramPacket(bytes, bytes.length, localHost, 10086);
        datagramSocket.send(datagramPacket);
        datagramSocket.close();
    }
```

## TCP协议通信

TCP协议通信

* Java对基于TCP协议的的网络提供了良好的封装，使用Socket对象来代表两端的通信端口， 并通过Socket产生I0流来进行网络通信
  Java为客户端提供了Socket类,为服务器端提供了ServerSocket类

* 发送数据
  
  > ①创建客户端的Socket对象(Socket)
  > ②获取输出流， 写数据
  > ③释放资源

* 接收数据
  
  > ①创建服务器端的Socket对象(ServerSocket)
  > ②监听客户端连接, 返回一个Socket对象
  > ③获取输入流， 读数据,并把数据显示在控制台
  > ④释放资源

```java
public class TcpClient {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket(InetAddress.getByName("192.168.137.1"),10086);
        //获得输出流，写数据
        OutputStream outputStream = socket.getOutputStream();
        outputStream.write("hello world!server......".getBytes());

        InputStream inputStream = socket.getInputStream();
        byte[] bytes = new byte[1024];
        int len = inputStream.read(bytes);
        System.out.println(new String(bytes,0,len));

        socket.close();
    }
}

//============================================
public class TcpServer {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(10086);

        Socket accept = serverSocket.accept();

        InputStream inputStream = accept.getInputStream();
        byte[] bytes = new byte[1024];
        int len = inputStream.read(bytes);
        System.out.println(new String(bytes, 0, len));

        OutputStream outputStream = accept.getOutputStream();
        outputStream.write("hello client..".getBytes());

        accept.close();
        serverSocket.close();
    }
}
```

## Http/Https

参考：https://www.runoob.com/http/http-tutorial.html

1. Hyper Text Transfer Protocol（超文本传输协议）

   * 定义了客户端和服务器端通信时，发送数据的格式
   * 特点：
     * 基于TCP/IP的高级协议
     * 默认端口是8080
     * 基于请求响应模型
     * 无状态的：每次请求之间是相互独立的，不能交互数据
   * 历史版本

2. 请求消息数据格式（四部分）

   * **请求行**

     请求方式 请求url 请求协议/版本

     例：GET /login.html http/1.1

     * 请求方式
       * HTTP协议有7种请求方式，常用的有2种：
         * GET：请求参数在请求行中，请求的url长度有限制，不太安全
         * POST：请求参数在请求体中，请求的url长度没有限制，相对安全

   * **请求头**

     请求头名称：请求头值

     * 常见请求头：
       * user-Agent：浏览器告诉服务器，访问时使用的浏览器版本信息（可以在服务器端获取该头的信息，解决浏览器的兼容性问题）
       * Referer：告诉服务器，当前请求从哪里来（可以用于防盗链和统计工作）
         * 防盗链
         * 统计工作
       * Connection

   * **请求空行**

   * **请求体（正文）**

3. 响应消息数据格式(四部分)

   * **响应行**
     * 组成：协议/版本 响应状态码  状态码描述
     * 响应状态码：服务器告诉客户端浏览器本次请求和响应的一个状态
       * 状态码都是3位数字
       * 分类：
         * 1xx：服务器接收客户端消息，但没有接收完成，等待一段时间后发送1xx状态码
         * 2xx：成功。
         * 3xx：重定向。代表：302（重定向），304（访问缓存）
         * 4xx：客户端错误。代表：404（没有请求路径对应的资源），405（请求方式没有对应的处理方法）
         * 5xx：服务器端错误。代表：500（服务器内部出现异常）
   * **响应头**
     * 格式：头名称：值
     * 常见响应头
       * Context-Type：服务器告诉客户端本次响应体数据格式以及编码方式
       * Context-disposition：服务器告诉客户端以什么格式打开响应体数据
         * 值：
           * in-line：默认值，在当前页面打开
           * attachment;filename=xxx:以附件形式打开响应体，文件下载
   * **响应空行**
   * **响应体**

## WebSocket

# java Web概述

1. 相关技术栈
   * 数据库相关
     * mysql
     * jdbc
     * mybatis
   * 前端网页相关
     * HTML+CSS
     * JavaScript
     * ajax
     * Vue
     * ElementUI
   * javaWeb核心
     * Tomcat+HTTP+Servlet
     * JSP
     * Cookie+Session
     * Filter+Lister

![image-20221104200959033](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211042010915.png)

# MySQL数据库

## 概述及环境准备

1. 常见的数据库软件
   
   * Oracle
   * MySQL
   * SQL Server
   * DB2
   * MongDB

2. MySQL的安装

3. 编码问题
   
   * 查看mysql数据库编码
     
     ```sql
     show variables like 'char%';
     ```

## DDL语句（数据定义）

1. 操作数据库（CRUD）
   
   ```sql
   1. C（Create）：创建
   * 创建数据库
   create database 数据库名称;
   
   * 创建数据库并判断是否已存在
   create database if not exists 数据库名称;
   
   * 创建数据库并设置字符集
   create database character set 字符集;
   
   2. R（Retrieve）：查询
   * 查询所有数据库的名称
   show databases；
   
   * 查询某个数据库的字符集（实际查看某个数据库的创建语句）
   show create database 数据库名称;
   
   3. U（Update）：修改
   * 修改数据库字符集
   alter database 数据库名称 character set 字符集名称;
   
   4. D（Delete）：删除
   * 删除数据库
   drop database 数据库名称
   
   * 删除数据库如果存在
   drop database if exists 数据库名称;
   
   * 查询当前正在使用的数据库名称
   select  database（）;
   
   * 使用数据库
   use 数据库名称;;
   ```

2. 操作表
   
   ```sql
   1. 创建
   * 创建表
   create table 表名(
       列名1 数据类型1，
       列名n 数据类型n
   );
   
   * 复制表
   create table 表名 like 表名;
   
   * 数据库数据类型：
   int
   double
   date（只包含年月日）
   datetime（包含年月日时分秒）
   timestamp（时间戳类型）
   varchar（字符串）
   
   2. 查询
   * 查询某个数据库中的所有表名称
   show tables;
   
   * 查询表结构
   desc 表名
   show create table 表名
   
   3. 修改
   * 修改表名
   alter table 表名 rename to  表名
   
   * 修改表的字符集
   show create table 表名 character set 字符集
   
   * 添加列
   alter table 表名 add 列名 数据类型;
   
   * 修改列名称  类型
   alter table 表名 change  列名 新列名 新数据类型
   alter table 表名 modify 列名 新数据类型
   
   * 删除列
   alter table 表名 drop 列名;
   
   4. 删除
   drop table if exists 表名 ;
   ```

## DQL语句（数据查询）

1. 条件查询（where）
   
   ```sql
   select 查询列表 from 表名 where 条件判断;
   ```

2. 模糊查询（like）
   
   ```sql
   select 查询列表 from 表名 where 查询列 like 条件;
   
   注意：%表示任意个任意字符，——表示一个任意字符。
   ```

3. 排序查询（order by）

4. 聚合函数
   
   ```sql
   * count()
   * sum()
   * avg()
   * max()
   * min()
   ```

5. 分组查询（group by）

6. 分页查询（limit）
   
   ```sql
   select 查询列表 from 表名 limit 范围;
   例：select * from student limit 0,2;
   
   分页公式：（当前页数-1）*每页记录数
   ```

## DML语句（数据操作）

## DCL语句（数据控制）

1. 管理用户
   
   ```sql
   * 增加用户
   create user 用户名@主机名 identified by 密码;
   (注意：当主机名为%时，用户可以在任意IP地址上登录)
   
   * 删除用户
   drop user 用户名@主机名
   
   * 查询用户
   
   * 修改秘密
   update user set password=password('新密码','用户名');
   set password for 'root'@'localhost'=password('新密码');
   ```

2. 权限管理
   
   ```sql
   * 查询权限
   show grants for 用户名@主机名
   
   * 授予权限
   grant 权限 on 数据库名称.* to 用户名@主机名;
   (注意：若权限为all，则表示给用户授予该数据库的所有权限)
   
   * 撤销授权
   revoke 权限 on 数据库.* from 用户名@主机名;
   ```

## 约束

1. 概念：对表中数据进行限定，保证数据的正确性，有效性和完整性。

2. 分类
   
   * 主键约束（primary key）
     
     > 主键：非空且唯一，一张表中只能有一个字段为主键，主键就是表中记录的唯一标识
     >    删除主键（alter table 表名 drop primary key;）
     > 
     > 自动增长：如果某一列是数值类型的，使用auto_ncreament可以完成值的自动增长
   
   * 非空约束
   
   * 唯一约束
   
   * 检查约束
   
   * 默认约束
   
   * 外键约束
   
   ![image-20221104202706822](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211042027411.png)
   
   > 注意：mysql不支持检查约束

3. 添加约束

## 数据库备份和恢复

1. 数据库导出sql脚本
   
   ```sql
   mysqldump
   ```

2. 执行sql脚本

## 事务

1. 概念：如果一个包含多个步骤的业务操作，被事务管理，那么这些操作要么同时成功，要么同时失败。

2. 操作：
   
   1. 开启事务start transaction
   2. 回滚rollback
   3. 提交commit

3. mysql数据库中事务默认自动提交。事务提交有两种方式（自动提交和手动提交，mysql就是自动提交），查询事务的默认提交方式可以使用 select @@atuocoommit; （1代表自动提交，0代表手动提交）。修改事务的默认提交方式可以使用set @@autocommit;

4. 四大特征
   
   * **原子性**：不可分割的最小操作操作单位，要么同时成功，要门同时失败。
   * **持久性**：当事务提交或回滚后，数据库会持久化的保存数据。
   * **隔离性**：多个事务之间，相互独立。
   * **一致性**：事务操作前后，数据总量不变。

5. 隔离级别
   
   * 概念：多个事务间是隔离的，相互独立的，但是如果多个事务操作同一批数据，则会引发一些问题，设置不同的隔离级别就可以解决这些问题。
   
   * 存在问题：
     
     * 脏读：一个事务，读取到另一个事务中没有提交的数据
     * 不可重复读（虚读）：在同一个事务中，两次读取到的数据不一样
     * 幻读：一个事务操作数据表中所有记录，另一个事务添加了一条数据，则第一个事务查询不到自己的修改。
   
   * 隔离级别：
     
     * read uncommitted（可能产生脏读、不可重复读、幻读）
     * read commited（可能产生不可重复读、幻读）
     * repeatable read（可能产生幻读）
     * serializable（可以解决所有问题）
   
   注意：隔离界别从小到大安全性越来越高当时效率越来越低。mysql数据库默认为repeatable read，oracle默认为read commited
   
   * 数据库查询隔离级别：select @@ tx_isolation;
   
   * 数据库设置隔离级别：set global transaction isolation level 级别字符串;

## 数据库设计

### 范式

1. 概念：设计关系数据库时，遵从不同的规范要求，设计出合理的关系型数据库,这些不同的规范要求被称为不同的范式，各种范式**呈递次规范**,越高的范式数据库冗余越小。目前关系数据库有六种范式:第-范式(1NF) 、第二范式(2NF)、第三范式(3NF)、巴斯科德范式(BCNF) 、第四范式(4NF)和第五范式(5NF,又称完美范式)。
2. 分类
   * 第一范式（1NF）：每一列都是不可分割的原子数据项
   * 第二范式（2NF）：在1NF的基础上，非码属性必须完全依赖于候选码
     * 函数依赖：如果通过A属性(属性组)的值，可以确定唯- -B属性的值。则称B依赖于A
     * 完全函数依赖
     * 部分函数依赖
     * 传递函数依赖
   * 第三范式（3NF）：在2NF的基础上，任何非主属性不依赖于其他非主属性（消除传递依赖）

# JDBC

## 基本操作

1. 概念：Java DataBase Connectivity。java数据库连接，java语言操作数据库。
   
   * 本质：一套操作所有关系型数据库的接口，各个数据库产商去实现这套接口，提供数据库驱动jar包。我们使用这套接口进行编程，真正执行代码的是驱动jar包中的实现类。

2. 快速入门
   
   > 1. 导入驱动jar包
   > 2. 注册驱动
   > 3. 获取数据库连接对象Connection
   > 4. 定义sql
   > 5. 获取执行sql语句对象Statement
   > 6. 执行sql，接受返回结果
   > 7. 处理结果
   > 8. 释放资源
   
   ```sql
   package cn.itcast.jdbc;
   
   import java.sql.*;
   
   public class JDBCDemo1 {
       public static void main(String[] args) throws ClassNotFoundException, SQLException {
   //        1. 导入驱动jar包
   //        2. 注册驱动
           Class.forName("com.mysql.cj.jdbc.Driver");
   //        3. 获取数据库连接对象Connection
           Connection connection = DriverManager.getConnection(
                   "jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC",
                   "root", "4112");
   //        4. 定义sql
           String sql = "update user set password='654321' where username='admin'";
   //        5. 获取执行sql语句对象Statement
           Statement statement = connection.createStatement();
   //        6. 执行sql，接受返回结果
           long result = statement.executeLargeUpdate(sql);
   //        7. 处理结果
           System.out.println(result);
   //        8. 释放资源
           connection.close();
           statement.close();
       }
   }
   ```

3. JDBC各接口和类详解
   
   * DriverManger：驱动管理对象
     
     * 功能：
       * 注册驱动(mysql5后的驱动jar包可以省略注册驱动步骤)
         * static void registerDriver(Driver driver)
         * Class.forName(“com.mysql.cj.jdbc.Driver”)（Driver类中的静态代码块执行）
       * 获取数据库连接
         * 方法：Static Connection getConnection(String url,String user,String password)
         * 参数：
           * url：jdbc:mysql://ip地址:端口号/数据库名称?serverTimezone=UTC
           * user：用户名
           * password：密码
   
   * Connection：数据库连接对象
     
     * 功能：
       
       * 获取执行sql对象
         
         * Statement createStatement（）
         * PreparedStatement PreparedStatement（String sql）
       
       * 管理事务
         
         * 开启事务：
           
           ```
           void setAutoCommit(boolean autoCommit)
           ```
         
         * 提交事务：
           
           ```
           void commit()
           ```
         
         * 回滚事务：
           
           ```
           void rollback()
           ```
   
   * Statement：执行sql对象
     
     * 执行sql
       
       > boolean execute(String sql)
       > int executeUpdate(String sql)//执行DML、DDL语句
       > ResultSet executeQuery(String sql)//执行DQL语句
   
   * ResultSet：结果集对象，封装查询结果
     
     * next（）方法：游标向下移动一行
     * getxxx（参数）方法：xxx代表数据类型，参数可以代表列编号或列名称（从1开始）
     
     ```java
     package cn.itcast.jdbc;
     
     import java.sql.*;
     
     public class JDBCDemo4 {
         public static void main(String[] args) {
             Connection connection = null;
             Statement statement = null;
             ResultSet resultSet = null;
             try {
                 Class.forName("com.mysql.cj.jdbc.Driver");
                 connection = DriverManager.getConnection("jdbc:mysql:///user_login?serverTimezone=UTC", "root", "4112");
                 statement = connection.createStatement();
                 String sql = "select * from user";
                 resultSet = statement.executeQuery(sql);
                 //处理结果集
                 while (resultSet.next()){
                     int id = resultSet.getInt("id");
                     String username = resultSet.getString("username");
                     String password = resultSet.getString("password");
                     System.out.println(id+" "+username+" "+password);
     
                 }
             } catch (ClassNotFoundException e) {
                 e.printStackTrace();
             } catch (SQLException e) {
                 e.printStackTrace();
             }finally {
                 if (resultSet!=null){
                     try {
                         resultSet.close();
                     } catch (SQLException e) {
                         e.printStackTrace();
                     }
                 }
                 if (statement!=null){
                     try {
                         statement.close();
                     } catch (SQLException e) {
                         e.printStackTrace();
                     }
                 }
                 if (connection!=null){
                     try {
                         connection.close();
                     } catch (SQLException e) {
                         e.printStackTrace();
                     }
                 }
             }
     
         }
     }
     ```
   
   * PreparedStatement：执行sql对象
     
     * SQL注入问题：在拼接sql时，有一些特殊关键字参与字符串的拼接，会造成安全性问题。
     
     * 解决SQL注入问题：使用PreparedStatement对象执行sql语句
     
     * ```java
       package cn.itcast.jdbc;
       
       import cn.itcast.utils.JDBCUtils;
       
       import java.sql.*;
       
       public class JDBCDemo7 {
       
           public static void main(String[] args) {
               new JDBCDemo7().login("chen","123456");
           }
       
           public boolean login(String username,String password){
               if (username==null||password==null){
                   return false;
               }
               Connection connection =null;
               PreparedStatement preparedStatement = null;
               ResultSet resultSet = null;
               try {
                   connection = JDBCUtils.getConnection();
                   String sql = "select * from user where username = ? and password = ?";
                   preparedStatement = connection.prepareStatement(sql);
                   preparedStatement.setString(1,username);
                   preparedStatement.setString(2,password);
                   resultSet = preparedStatement.executeQuery();
                   System.out.println(resultSet.next());
                   return resultSet.next();
               } catch (SQLException e) {
                   e.printStackTrace();
               }finally {
                   JDBCUtils.close(resultSet,preparedStatement,connection);
               }
               return false;
           }
       
       }
       ```

4. 抽取JDBC工具类：JDBCUtils
   
   * 目的：简写
   
   * 分析：
     
     * 抽取一个方法注册驱动
     
     * 抽取一个方法连接对象
       
       * 需求：不传参数，并保证工具类的通用性
       
       * 解决：配置文件（properities）
         
         ```
         driver=com.mysql.cj.jdbc.Driver
         url=jdbc:mysql:///user_login?serverTimezone
         user=root
         password=4112
         ```
     
     * 抽取一个方法释放资源
   
   * ```java
     package cn.itcast.utils;
     
     import java.io.FileReader;
     import java.io.IOException;
     import java.net.URL;
     import java.sql.*;
     import java.util.Properties;
     
     /**
      * JDBC 工具类
      */
     public class JDBCUtils {
         private static String url;
         private static String user;
         private static String password;
         private static String driver;
     
         /**
          *配置文件的读取，只需要读取一次
          */
         static {
             try {
                 //1.创建Properities集合类
                 Properties properties = new Properties();
                 //获取stc路径下文件的方式ClassLoad
                 ClassLoader classLoader = JDBCUtils.class.getClassLoader();
                 URL res = classLoader.getResource("jdbc.properities");
                 String path = res.getPath();
                 //2.加载文件
                 properties.load(new FileReader(path));
                 //3.获取数据
                 url = properties.getProperty("url");
                 user = properties.getProperty("user");
                 password = properties.getProperty("password");
                 driver = properties.getProperty("driver");
     
                 Class.forName(driver);
             } catch (IOException e) {
                 e.printStackTrace();
             } catch (ClassNotFoundException e) {
                 e.printStackTrace();
             }
     
         }
     
         /**
          * 获取连接对象
          * 需求：不传递参数并且要保证工具类的通用性
          * 解决：使用properities配置文件
          * @return
          */
         public static Connection getConnection() throws SQLException {
             return DriverManager.getConnection(url,user,password);
         }
     
         /**
          * 释放资源
          * @param statement
          * @param connection
          */
         public static void close(Statement statement,Connection connection){
             if (statement!=null){
                 try {
                     statement.close();
                 } catch (SQLException e) {
                     e.printStackTrace();
                 }
             }
             if (connection!=null){
                 try {
                     connection.close();
                 } catch (SQLException e) {
                     e.printStackTrace();
                 }
             }
         }
     
         /**
          * 释放资源
          * @param resultSet
          * @param statement
          * @param connection
          */
         public static void close(ResultSet resultSet,Statement statement, Connection connection){
             if (resultSet!=null){
                 try {
                     resultSet.close();
                 } catch (SQLException e) {
                     e.printStackTrace();
                 }
             }
             if (statement!=null){
                 try {
                     statement.close();
                 } catch (SQLException e) {
                     e.printStackTrace();
                 }
             }
             if (connection!=null){
                 try {
                     connection.close();
                 } catch (SQLException e) {
                     e.printStackTrace();
                 }
             }
         }
     }
     ```

5. JDBC管理事务
   
   * 事务：一个包含多个步骤的业务操作。如果这个业务操作被事务管理，那么这多个步骤要么同时成功，要么同时失败。
   * 操作：
     * 开启事务
     * 提交事务
     * 回滚事务
   * 使用connection对象来管理事务
     * 开启事务：setAutoCommit(boolean autoCommit) 调用该方法，即开启事务
     * 提交事务：commit()
     * 回滚事务：rollback()

## 数据库连接池

1. 概念：一个容器（集合），存放数据库连接的容器。当系统初始化后，容器被创建，容器中会申请一些连接对象，当用户访问数据库时，从容器中获取连接对象，用户访问完后，将对象归还给容器。

2. 实现：
   
   * 标准接口：DataSource
     * 获取连接：getConnection()
     * 归还连接：如果连接对象Connection是从连接池中获取，那么调用connection.close()方法将不再关闭连接，而是归还连接。
   * 数据库产商实现
     * c3p0：
     * druid：阿里巴巴提供


### C3P0

1. C3P0实现

   > 1. 导入jar包（c3p0-0.9.5.2.jar和mchange-commons-java-0.2.12.jar）
   > 2. 定义配置文件
   >    * 名称：c3p0-config.xml or c3p0.properities
   >    * 路径：src目录下即可
   > 3. 创建核心对象：数据库连接池对象（ComboPooledDataSource）
   > 4. 获取连接：getConnection（）

   ```java
   package cn.itcast.c3p0;
   
   import cn.itcast.utils.JDBCUtils;
   import com.mchange.v2.c3p0.ComboPooledDataSource;
   
   import java.sql.Connection;
   import java.sql.PreparedStatement;
   import java.sql.ResultSet;
   import java.sql.SQLException;
   
   /**
    * C3p0演示
    *
    */
   public class C3p0Demo1 {
       public static void main(String[] args) {
           ComboPooledDataSource dataSource = new ComboPooledDataSource();
           Connection connection = null;
           PreparedStatement statement = null;
           ResultSet resultSet = null;
           try {
               connection = dataSource.getConnection();
               String sql ="select * from user";
               statement = connection.prepareStatement(sql);
               resultSet = statement.executeQuery();
               while (resultSet.next()){
                   System.out.println(resultSet.getInt("id"));
                   System.out.println(resultSet.getString("username"));
                   System.out.println(resultSet.getString("password"));
               }
           } catch (SQLException e) {
               e.printStackTrace();
           }finally {
               JDBCUtils.close(resultSet,statement,connection);
           }
       }
   }
   ```


### Druid

GitHub：https://github.com/alibaba/druid

1. druid实现

   > Druid基本使用
   > 
   > 1. 导入jar包 druid-1.0.9.jar
   > 2. 定义配置文件
   >    * 后缀名为properities
   >    * 可以任意名称，放在任意目录
   > 3. 加载配置文件
   > 4. 获取连接池对象：通过工厂来获取（DruidDataSourceFactory）
   > 5. 获取连接：getConnection（）

   ```java
   package cn.itcast.druid;
   
   import com.alibaba.druid.pool.DruidDataSourceFactory;
   
   import javax.sql.DataSource;
   import java.io.IOException;
   import java.io.InputStream;
   import java.sql.Connection;
   import java.sql.PreparedStatement;
   import java.sql.ResultSet;
   import java.util.Properties;
   
   /**
    * Druid演示
    */
   public class DruidDemo {
       public static void main(String[] args) throws Exception {
           //加载配置文件
           Properties properties = new Properties();
           InputStream resourceAsStream =                     DruidDemo.class.getClassLoader().getResourceAsStream("druid.properties");
           properties.load(resourceAsStream);
           //获取连接池对象
           DataSource dataSource = DruidDataSourceFactory.createDataSource(properties);
           //获取连接对象
           Connection connection = dataSource.getConnection();
           String sql = "select * from user";
           PreparedStatement preparedStatement = connection.prepareStatement(sql);
           ResultSet resultSet = preparedStatement.executeQuery();
           while (resultSet.next()){
               System.out.println(resultSet.getString("username")+":"+resultSet.getString("password"));
           }
           //释放资源
           resultSet.close();
           preparedStatement.close();
           connection.close();
       }
   }
   ```

   > Druid工具类
   > 
   > 1. 定义一个JDBCUtils类
   > 2. 定义静态代码块加载配置文件，初始化连接池对象
   > 3. 提供方法
   >    * 获取连接方法：通过数据库连接池获取连接
   >    * 释放资源
   >    * 获取连接池的方法

   ```java
   package cn.itcast.druid;
   
   import com.alibaba.druid.pool.DruidDataSourceFactory;
   
   import javax.sql.DataSource;
   import java.io.IOException;
   import java.io.InputStream;
   import java.sql.Connection;
   import java.sql.ResultSet;
   import java.sql.SQLException;
   import java.sql.Statement;
   import java.util.Properties;
   
   public class JDBCUtils {
       private static DataSource dataSource;
   
       static {
           Properties properties = new Properties();
           InputStream resourceAsStream = JDBCUtils.class.getClassLoader().getResourceAsStream("druid.properties");
           try {
               properties.load(resourceAsStream);
               dataSource = DruidDataSourceFactory.createDataSource(properties);
           } catch (IOException e) {
               e.printStackTrace();
           } catch (Exception e) {
               e.printStackTrace();
           }
       }
   
       public static DataSource getDataSource(){
           return dataSource;
       }
   
       public static Connection getConnection() throws SQLException {
           return dataSource.getConnection();
       }
   
       public static void close(Statement statement,Connection connection){
           if (statement!=null){
               try {
                   statement.close();
               } catch (SQLException e) {
                   e.printStackTrace();
               }
           }
           if (connection!=null){
               try {
                   connection.close();
               } catch (SQLException e) {
                   e.printStackTrace();
               }
           }
       }
   
       public static void close(ResultSet resultSet, Statement statement,Connection connection){
           if (resultSet!=null){
               try {
                   resultSet.close();
               } catch (SQLException e) {
                   e.printStackTrace();
               }
           }
   
           close(statement,connection);
       }
   }
   
   =============================================================================
   
   package cn.itcast.druid;
   
   import java.sql.Connection;
   import java.sql.PreparedStatement;
   import java.sql.SQLException;
   
   /**
    * 使用工具类
    * 在user表中添加一条数据
    */
   public class DruidDemo2 {
       public static void main(String[] args) {
           Connection connection = null;
           PreparedStatement preparedStatement = null;
   
           try {
               connection = JDBCUtils.getConnection();
               String sql = "insert into user value(3,'liXiang','123456')";
               preparedStatement = connection.prepareStatement(sql);
               int i = preparedStatement.executeUpdate();
               System.out.println("affect:"+i);
           } catch (SQLException e) {
               e.printStackTrace();
           }finally {
               JDBCUtils.close(preparedStatement,connection);
   
           }
   
       }
   }
   ```

## Spring JDBC（JDBC Template）

> Spring 框架对JDBC的简单封装
> 
> 使用步骤：
> 
> 1. 导入jar包
> 
> 2. 创建JdbcTemplate对象，依赖于数据源DataSource
>    
>    JdbcTemplate template = newJdbcTemplate（DataSource）；
> 
> 3. 使用JdbcTemplate方法完成CRUD操作
>    
>    * update()：执行增、删、改语句
>    * queryForMap()：查询结果集封装为map集合（查询的结果集长度只能为1）
>    * queryForList()：查询结果集封装为list集合（将每一条记录封装为map集合，在将多条记录封装为list集合）
>    * query()：查询结果集封装为JavaBean对象
>      * 参数：RowMapper（一般使用BeanPropertyRowMapper<类型>(类型.class)实现类来实现数据到JavaBean的自动封装）
>    * queryForObject()：查询结果集封装为对象（一般用于聚合函数的查询）

```java
package cn.itcast.jdbctemplate;

import cn.itcast.druid.JDBCUtils;
import org.springframework.jdbc.core.JdbcTemplate;

/**
 * JDBCTemplate使用
 */
public class JDBCTemplateDemo1 {
    public static void main(String[] args) {
        JdbcTemplate jdbcTemplate = new JdbcTemplate(JDBCUtils.getDataSource());
        String sql = "update user set username = 'Wangwu' where id = 3";
        int update = jdbcTemplate.update(sql);
        System.out.println("affect:"+update);
    }
}
```

```java
package cn.itcast.jdbctemplate;

import cn.itcast.domain.User;
import cn.itcast.druid.JDBCUtils;
import org.junit.Test;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;

public class JDBCTemplateDemo2 {

    private JdbcTemplate jdbcTemplate = new JdbcTemplate(JDBCUtils.getDataSource());

    @Test
    public void test1(){
        String sql = "select * from user";
        List<Map<String, Object>> maps = jdbcTemplate.queryForList(sql);
        for (Map<String, Object> map : maps) {
            System.out.println(map);
        }

    }

    @Test
    public void test2(){
        String sql = "select * from user where id = ?";
        Map<String, Object> stringObjectMap = jdbcTemplate.queryForMap(sql, 1);
        System.out.println(stringObjectMap);
    }

    @Test
    public void test3(){
        String sql = "select * from user";
//        List<User> users = jdbcTemplate.query(sql, new RowMapper<User>() {
//            @Override
//            public User mapRow(ResultSet resultSet, int i) throws SQLException {
//                User user = new User();
//                user.setId(resultSet.getInt("id"));
//                user.setUsername(resultSet.getString("username"));
//                user.setPassword(resultSet.getString("password"));
//                return user;
//            }
//        });
        List<User> users = jdbcTemplate.query(sql, new BeanPropertyRowMapper<User>(User.class));
        for (User u :users) {
            System.out.println(u);
        }
    }

    @Test
    public void test4(){
        String sql = "select count(id) from user";
        Long aLong = jdbcTemplate.queryForObject(sql, Long.class);
        System.out.println(aLong);
    }
}
```

# XML

### XML入门

1. XML简介
   
   Extensible Markup Language 可扩展标记语言。
   
   * 可扩展：标签都是自定义的
   * 功能（传输和存储数据）
     * 作为配置文件
     * 在网络中传输
   * 版本：1.0和1.1（1.1不能向下兼容）
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
   
   ```xml
   <?xml version="1.0" encoding="UTF-8"?><!--xml声明,声明版本和字符编码-->
   <note><!--根元素-->
       <to>Tove</to><!--子元素-->
       <from>Jani</from><!--子元素-->
       <heading>Reminder</heading><!--子元素-->
       <body>Don't forget me</body><!--子元素-->
   </note>
   ```
   
   说明：
   
   * xml文档必须包含根元素，该元素是所有其他元素的父元素。
   * 所有的元素都可以有子元素。
   * 所有元素都可以有文本内容和属性。
   * ![DOM node tree](https://www.runoob.com/wp-content/uploads/2013/09/nodetree.gif)

4. 语法
   
   * xml的文档声明
     
     ```xml
     <?xml version='1.0' encoding='UTF-8'?>
     ```
     
     * xml文档的后缀名为.xml
     * xml第一行必须定义文档声明
     * xml以LF存储换行
   
   * 定义元素
     
     * xml命名规则
       * 名称可以包含字母，数字和其他字符
       * 名称不能以数字或者标点符号开始
       * 名称不能以xml开始
       * 名称不能包含空格
     * xml文档中有且仅有一个根标签
     * 标签必须正确关闭
     * xml标签名称区分大小写
     * xml必须正确嵌套
   
   * 定义属性（在 XML 中，您应该尽量避免使用属性。如果信息感觉起来很像数据，那么请使用元素吧。）
     
     * 属性值必须使用引号引起
     * 一个标签可以有多个属性，但是属性名不能相同
   
   * 注释
     
     * xml的注释：<!--注释内容-->
     * 注释不能嵌套
   
   * 特殊字符
     
     * | 特殊字符   |                |
       | ------ | -------------- |
       | &lt;   | less than      |
       | &gt;   | greater than   |
       | &amp;  | ampersand      |
       | &apos; | apostrophe     |
       | &quot; | quotation mark |
   
   * CDATA区
     
     * 可以解决多个字符都需要转义的问题，在该区域中的数据会被原样展示
     * 格式：<![CDATA[数据]]>
   
   * PI指令（处理指令）
     
     * 可以在xml中设置样式，写法如下（只对英文标签起作用）
       
       ```xml
       <?xml-stylesheet type="text/css" href=""?>
       ```
   
   * 约束：规定xml文档的书写规则
     
     * 分类
       * DTD：一种简单的约束技术
       * Schema：一种复杂的约束技术

### DTD（文档类型定义）

1. dtd快速入门
   
   * 创建一个文件，后缀名为.dtd
   
   * 在xml中有几个元素在dtd文件就写几个<!ELEMENT>
     
     * 若为简单元素（没有子元素），格式如下
       
       ```xml
       <!ELEMENT 元素名 (#PCDATA)>
       ```
     
     * 若为复杂元素（有子元素），格式如下
       
       ```xml
       <!ELEMENT 元素名 (子元素)>
       ```
   
   * 使xml引入该dtd约束文件，格式如下
     
     ```xml
     <!DOCTYPE 根元素名称 SYSTEM “dtd文件的路径”>
     ```
   
   * 非递
   
   注意：使用浏览器打开xml文件，浏览器不负责校验约束
   
   合法的 XML 文档是"形式良好"的 XML 文档，这也符合文档类型定义（DTD）的规则

```xml
?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE note SYSTEM "Note.dtd"><!--声明对外部DTD文件的引用-->
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
```

​    DTD的目的是定义XML文档的结构，它使用一系列合法的元素来定义文档的结构。

```dtd
<!DOCTYPE note
[
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
]>
```

2. dtd的引入方式
   
   * 引入外部dtd文件，使用方法如上所示
   
   * 使用内部dtd文件，使用方法如下所示
     
     ```
     ?xml version="1.0" encoding="ISO-8859-1"?>
     <!DOCTYPE note [
         <!ELEMENT note (to,from,heading,body)>
     ]>
     <note>
         <to>Tove</to>
         <from>Jani</from>
         <heading>Reminder</heading>
         <body>Don't forget me this weekend!</body>
     </note>
     ```
   
   * 使用外部dtd文件（网络上的dtd文件）
     
     ```xml
     <!DOCTYPE 根元素 PUBLIC "DTD名称" "DTD文档的URL">
     ```

3. 使用dtd定义元素
   
   * 语法：<!ELEMENT 元素名 约束>
   
   * 简单元素：没有子元素的元素
     
     ```
     <!ELEMENT 元素名 (#PCDATA)>//(#PCDATA)表示元素内容为字符串
     <!ELEMENT 元素名 EMPTY>//EMPTY表示元素内容为空
     <!ELEMENT 元素名 ANY>//ANY表示内容任意
     ```
   
   * 复杂元素：有子元素的元素
     
     ```
     //表示子元素出现次数
     + 表示一次或多次
     * 表示零次或多次
     ? 表示零次或一次
     //各子元素使用逗号隔开表示元素出现顺序
     例：<!ELEMENT person (name,age,sex)>
     //各子元素使用逗号隔开表示只能出现其中的一个
     例：<!ELEMENT person (name|age|sex)>
     ```

4. 使用dtd定义属性
   
   * 语法：
     
     ```<!ATTLIST
     <!ATTLIST 元素名称
         属性名称 属性类型 属性的约束
     >
     ```
   
   * 属性类型
     
     * CDATA：字符串
     * 枚举
     * ID：只能是字母或下划线开头
   
   * 属性的约束
     
     * #REQUEST：属性必须存在
     * #IMPLIED：属性可有可无
     * #FIXED：表示一个固定值（例：#FIXED “动静”）
     * 直接值：设置默认值（例：ID CDATA ‘’DD‘）

5. 定义实体
   
   * 在dtd中定义，xml中使用（实体需要卸载内部dtd中）
   * 语法：<!ENTITY 实体名称 '实体内容'>

**XML验证器**

1. XML查看

2. 解析XML（XML解析器把XML文档转换为XML DOM对象）
   
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

3. XML JavaScript
   
   1. XMLHttpRequest对象（用于在后台与服务器交换数据）
   
   ```xml
   <!--创建XMLHttpRequest对象-->
   xmlhttp=new XMlHttpRequest();
   ```
   
   2. XML

# Tomcat

### web相关概念回顾

1. 软件架构
   
   * C/S：客户端/服务器端
   * B/S：浏览器/服务器端

2. 资源分类
   
   * 静态资源：所有用户访问后，得到的结果都是一样的，称为静态资源。静态资源可以直接被浏览器直接解析
     
     ​                如：html，css，javaScricpt
   
   * 动态资源：每个用户访问相同资源后，得到的结果可能不一样，称为动态资源。动态资源被访问后需要先转换为静态资源，再返回给浏览器
     
     ​                如：Servlet，jsp，php，asp

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
   
   ​    在web服务器软件中，可以部署web项目，让用户通过浏览器来访问该项目

4. 几款与java相关的常见web服务器软件：
   
   * webLogic：oracle公司，大型的JavaEE（java语言在企业级开发中使用的技术规范的总和，一共规定了13项大的规定）服务器，支持所欲JavaEE规范，是收费的。
   * webSphere：IBM公司，大型的JavaEE服务器，支持所有的JavaEE规范，收费的
   * JBoss：JBoss公司，大型的JavaEE服务器，支持所有的JavaEE规范，收费的
   * Tomcat：Apache基金组织，中小型的JavaEE服务器，仅仅支持少量的JavaEE规范

### Tomcat

4. Tomcat目录结构

![image-20210206095655879](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210206095655879.png)

5. 启动、访问
   
   bin/startup.bat双击

6. 关闭
   
   * 正常关闭：bin/shutdown.bat
   * 强制关闭（关闭窗口）

7. 配置
   
   * **部署项目的方式：**
     
     * 直接将项目放到webapps目录即可
       
       简化部署：将项目打包成war包，再将war包放置到webapps目录中（war包会自动解压缩）
     
     * 配置conf/server.xml文件
       
       在<Host>标签体中配置<Context docBase="D:\hello" path="/hehe"/>
       
       docBase：项目存放路径
       
       path：虚拟目录
     
     * 在conf\Catalina\localhost创建任意名称xml文件，xml文件中写入配置
   
   * 静态项目和动态项目
     
     * 目录结构
       
       * java动态项目的目录结构：
         
         --项目根目录
         
         ​    --WEB-INF目录：
         
         ​        --web.xml：web项目的核心配置文件
         
         ​        --classes目录：放置字节码文件的目录
         
         ​        --lib目录：放置依赖jar包
     
     * 将tomcat集成到IDEA中

### IDEA与Tomcat的相关配置

1. IDEA会为每一个tomcat部署的项目单独建立一份配置文件
2. 工作空间项目和tomcat部署的web项目
   * tomcat真正访问的是“tomcat部署的web项目”，“tomcat部署的web项目”对应着工作空间中的web目录下的所有资源
   * **WEB—INF目录下的资源不能被浏览器直接访问**

# Servlet

### 一、概念

运行在服务器端的小程序。Servlet本质上就是一个接口，定义了java类被浏览器访问到（tomcat识别）的规则。在Servlet通常需要接收请求、处理请求、完成响应。

### 二、快速入门

#### 实现Servlet的三种方式

* 实现java.servlet.Servlet接口
* 继承java.servlet.GenericServlet类
* 继承java.servlet.http.HttpServlet类

+++

1. 创建javaEE项目

2. 定义一个类，实现Servlet接口并重写所有方法

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

#### 底层逻辑执行原理

1. 当服务器接收到客户端浏览器的请求后，会解析请求URL路径，获取访问的Servlet资源路径
2. 查找web.xml文件，是否有对象的<utl-pattern>标签内容
3. 如果有，则再找到对应的<servlet-class>全类名
4. tomcat会将字节码文件加载进内存，并且创建其对象
5. 调用其方法

![image-20230203175027461](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302031806502.png)

#### servlet的生命周期

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
   
   * servler的init方法只执行一次说明一个Servlet在内存中只存在一个对象，Servlet是单例的
     
     * 问题：多个用户同时访问时，可能存在线程安全问题
   
   * 解决：尽量不要再Servlet中定义成员变量，即使定义了成员变量，也不要修改值

2. 提供服务：执行service方法，执行多次

3. 被销毁：执行destroy方法，只执行一次
   
   * 只有服务器正常关闭时，才会执行destroy方法
   * destroy方法在Servlet被销毁之前执行，一般用于释放资源

```java
package cn.itcast.web.servlet;

import javax.servlet.*;
import java.io.IOException;

public class MyServletDemo implements Servlet {

    /**
     * 初始化方法
     * 在Servlet被创建时执行，只会执行一次
     * @param servletConfig
     * @throws ServletException
     */
    @Override
    public void init(ServletConfig servletConfig) throws ServletException {
        System.out.println("【init..........】");
    }

    /**
     * 获取ServletConfig对象，Servlet的配置对象
     * @return
     */
    @Override
    public ServletConfig getServletConfig() {
        return null;
    }

    /**
     * 提供服务的方法
     * 每一次Servlet被访问时执行，执行多次
     * @param servletRequest
     * @param servletResponse
     * @throws ServletException
     * @throws IOException
     */
    @Override
    public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
        System.out.println("【service...........】");
    }

    /**
     * 获取Servlet的一些信息，如：作者，版本
     * @return
     */
    @Override
    public String getServletInfo() {
        return null;
    }

    /**
     * 销毁方法
     * 在服务器正常关闭时执行（服务器销毁前调用该方法，一般用于释放资源）
     */
    @Override
    public void destroy() {
        System.out.println("【destroy............】");
    }
}
```

参考文档：https://docs.oracle.com/javaee/7/api/toc.htm

#### Servlet3.0

1. 支持注解配置。可以不需要web.xml

2. 使用步骤：
   
   1. 创建JavaEE项目，选择Servlet的版本3.0以上，可以不创建web.xml
   
   2. 定义一个类，实现Servle接口
   
   3. 重写方法
   
   4. 在类上使用@WebServlet注解，进行配置，@WebServlet(“资源路径”)

#### Servlet相关配置

1. urlpartten：Servlet访问路径
   * 一个Servlet可以定义多个访问路径：@webServlet（{“/dd”，“ddd”，“dddd”}）
   * 路径定义规则：
     * xxx
     * xxx/xxxx
     * *.后缀名

### 三、Servlet体系结构

Servlet --接口

​        |

GenericServlet --抽象类

​        |

HttpServlet --抽象类

* GenericServlet：将Servlet接口中其他的方法做了默认空实现，只将service(),将来定义Servlet类时，可以继承GenericServlet，实现service方法即可
* HttpServlet：对http的一种封装，简化操作
  * 定义类继承HTTPServlet
  * 复写doGet/doPost方法

### 四、Request对象和Response对象

#### request对象和response对象原理

![image-20230208130455779](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302081305920.png)

注意：

* request对象和response对象是由服务器创建的
* request对象是用来获取请求消息的，response对象是用来设置响应消息的

#### request对象

1. request对象的继承体系
   
   ServletRequest -- 接口
   
   ​        |  继承
   
   HttpServletRequest -- 接口
   
   ​        |
   
   org.apache.catalina.connector.RequestFacade -- 类
   
   ![image-20211122190128811](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211122190128811.png)
   
   ![image-20211122190404767](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211122190404767.png)

2. request功能
   
   * 获取请求消息数据
     * 获取请求行数据
       * 例子：GET day14/demo1?name=zhangsan  HTTP/1.1
       * 方法：
         * 获取请求方法：String getMethod()
         * 获取虚拟目录：String getContextPath()
         * 获取Servlet路径：String getServletPath()
         * 获取get方式请求参数：String getQueryString()
         * 获取请求URI：Sring getRequestURI()，SringBuffer getRequestURL()
           * 统一资源定位符（URL）
           * 统一资源标识符（URI）
         * 获取协议及版本：String getProtocol()
         * 获取客户机的IP地址：String getRemoteAddr()
     * 获取请求头数据
       * 方法
         * 通过请求头的名称获取请求头的值：String getHeader(String name)
         * 获取所有请求头名称：Enumeration<String> getHeaderNames()
     * 获取请求体数据
       * 请求体：只有POST请求方式才有请求体，在请求体中封装了POST请求的请求参数
       * 步骤：
         * 获取流对象：
           * BufferReader getReader()：获取字符输入流，只能操作字符数据
           * ServletInputStream getInputStream()：获取字节输入流，可以操作所有输入类型数据
         * 从流对象中获取数据
   * 其他功能
     * 获取请求参数通用方式
       * String getParameter(String name) ：根据参数名称获取参数值
       * String[ ] getParameterValues(String name) ：根据参数名称获取参数值数组
       * Enumeration<String> getParameterNames()：获取所有请求的参数名称
       * Map<String,String[ ]> getParameterMap()：获取所有参数的map集合
       * 中文乱码问题的解决
         * get方式：tomcat自动解决乱码问题
         * post方式：获取参数前需要设置request编码（request.setCharacterEncoding("utf-8")）
     * 请求转发：一种在服务器内部的资源跳转方式
       * 步骤
         * 通过request对象获取请求转发器对象：RequestDispatcher getDispatcher（String path）
         * 使用RequestDispatcher对象来进行转发：forward（ServletRequest request，ServletResponse response）
       * 特点
         * 浏览器地址栏路径不发生变化
         * 只能转发到当前服务器内部的资源中
     * 共享数据（域对象）
       * 域对象：一个有作用范围的对象，可以在范围内共享数据
       * request域：代表一次请求的范围，一般用于请求转发的多个资源中共享数据
       * 方法：
         * void setAttribute（String name，Object object）：存储数据
         * Object getAttribute（String name）：通过键获取值
         * removeAttribute（String name）：通过键移除键值对
     * 获取ServletContext
       * ServletContext getServletContext（）

3. 案例：**用户登录**
   
   * 需求
     
     > 1. 编写login.html登录页面
     > 2. 使用Druid数据库连接池技术，操作mysql
     > 3. 使用jdbcTemplate技术封装JDBC
     > 4. 登录成功舔砖SuccessServlet展示：登录成功！用户名，欢迎您
     > 5. 登录失败跳转到FailServlet展示：登录失败，用户名或密码错误
   
   * 开发步骤
     
     * 创建项目并导入相关的html页面和jar包
     
     * 创建数据库环境
       
       ```sql
       create database user_login;
       
       use user_login;
       
       create table user(
           id int primary key AUTO_INCREMENT,
           username varchar(32) unique not null,
           password varchar(32) not null
       
       );
       ```
     
     * 创建数据表对应类，cn.itcast.doamin.User
       
       ```sql
       package cn.itcast.domain;
       
       /**
        * 用户的实体类
        */
       public class User {
           private int id;
           private String name;
           private String password;
       
           public int getId() {
               return id;
           }
       
           public void setId(int id) {
               this.id = id;
           }
       
           public String getName() {
               return name;
           }
       
           public void setName(String name) {
               this.name = name;
           }
       
           public String getPassword() {
               return password;
           }
       
           public void setPassword(String password) {
               this.password = password;
           }
       
           @Override
           public String toString() {
               return "User{" +
                       "id=" + id +
                       ", name='" + name + '\'' +
                       ", password='" + password + '\'' +
                       '}';
           }
       }
       ```
     
     * 创建数据库操作类，cn.itcast.dao.UserDao
       
       ```sql
       package cn.itcast.dao;
       
       import cn.itcast.domain.User;
       import org.springframework.jdbc.core.BeanPropertyRowMapper;
       import org.springframework.jdbc.core.JdbcTemplate;
       
       /**
        * 操作数据库中User表的类
        */
       public class UserDao {
       
           //声明JDBCTemplate对象动用
           private JdbcTemplate template = new JdbcTemplate();
       
           /**
            * 登录方法
            * @param loginUser 用户输入的用户名和密码
            * @return 整个用户的所欲信息
            */
           public User login(User loginUser){
               try {
                   String sql="select * from user where username=? and password=?";
                   User user = template.queryForObject(sql,
                           new BeanPropertyRowMapper<User>(User.class),
                           loginUser.getName(), loginUser.getPassword());
                   return user;
               }catch (Exception e){
                   e.getStackTrace();
                   return null;
               }
       
           }
       }
       ```
     
     * 编写cn.itcast.web.servlet.LoginServlet类
       
       ```java
       package cn.itcast.web.servlet;
       
       import cn.itcast.dao.UserDao;
       import cn.itcast.domain.User;
       
       import javax.servlet.ServletException;
       import javax.servlet.annotation.WebServlet;
       import javax.servlet.http.HttpServlet;
       import javax.servlet.http.HttpServletRequest;
       import javax.servlet.http.HttpServletResponse;
       import java.io.IOException;
       
       @WebServlet("/LoginServlet")
       public class LoginServlet extends HttpServlet {
           protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
               //1.设置编码
               request.setCharacterEncoding("utf-8");
               //2.获取请求参数
               String username = request.getParameter("username");
               String password = request.getParameter("password");
               //3.封装User对象
               User loginUser = new User();
               loginUser.setName(username);
               loginUser.setPassword(password);
               //4.调用UserDao的login方法
               UserDao userDao = new UserDao();
               User user = userDao.login(loginUser);
               //判断
               if (user == null){
                   //登录失败                                    request.getRequestDispatcher("/FailServlet").forward(request,response);
               }else {
                   //登录成功
                   request.setAttribute("user",user);           request.getRequestDispatcher("/SuccessServlet").forward(request,response);
               }
               }
       
       protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
           this.doPost(request, response);
       }
       }
       ```

#### response对象

1. 功能：设置响应消息
   
   * 设置响应行
     
     * 设置状态码：setStatus(int sc)
   
   * 设置响应头：setHeader(String name,String value)
     
     * 常见的响应头：
       * Content-Type：服务器告诉客户端本次响应体数据格式及编码格式
       * Content-disposition：告诉客户端以什么格式打开响应体数据
   
   * 设置响应体
     
     * 步骤
     
     > 1. 获取输出流
     >    * 字节输出流：PrintWriter getWriter（）
     >    * 字符输出流：ServletOutputStream getOutputStream（）
     > 2. 使用输出流，将输出到客户端浏览器

2. 设置输出缓冲
   
   > 通常情况下，服务器输出的到客户端的内容不会直接写到客户端，而是先写到一个输出缓冲区，当满足一下条件时才将缓冲区中的内容写入到客户端：
   > 
   > * JSP页面中信息已经全部写入到缓冲区
   > * 缓冲区已满
   > * 调用response对象的flushBuffer()方法或者out对象的flush()方法
   > 
   > response对象

3. 案例一：**重定向**
   
   * 重定向：资源跳转的方式
   
   * 代码实现：
     
     ```java
     package cn.itcast.servlet;
     
     import javax.servlet.ServletException;
     import javax.servlet.annotation.WebServlet;
     import javax.servlet.http.HttpServlet;
     import javax.servlet.http.HttpServletRequest;
     import javax.servlet.http.HttpServletResponse;
     import java.io.IOException;
     
     /**
      * 重定向
      */
     @WebServlet("/ResponseDemo1")
     public class ResponseDemo1 extends HttpServlet {
         protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
             System.out.println("demo1 print");
             //重定向方式一
             /*//设置状态码302
             response.setStatus(302);
             //设置响应头location
             response.setHeader("location","/Servlet_war_exploded/ResponseDemo2");*/
     
             //重定向方式二
             response.sendRedirect("/Servlet_war_exploded/ResponseDemo2");
         }
     
         protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
             this.doPost(request, response);
         }
     }
     
     ================================================================================
     package cn.itcast.servlet;
     
     import javax.servlet.ServletException;
     import javax.servlet.annotation.WebServlet;
     import javax.servlet.http.HttpServlet;
     import javax.servlet.http.HttpServletRequest;
     import javax.servlet.http.HttpServletResponse;
     import java.io.IOException;
     
     @WebServlet("/ResponseDemo2")
     public class ResponseDemo2 extends HttpServlet {
         protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
             System.out.println("demo2 print");
         }
     
         protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
             this.doPost(request, response);
         }
     }
     ```
* 重定向的特点：
  
  > 1. 地址栏发生变化
  > 2. 重定向可以访问其他站点
  > 3. 重定向是两次请求，不能使用request域共享数据

* 转发的特点
  
  > 1. 地址栏路径不变
  > 2. 转发只能访问当前服务器下的资源
  > 3. 转发只是一次请求，能使用request域共享数据
4. 案例二：**服务器输出字符数据到浏览器**
   
   * 乱码问题
     
     > ```
     > //设置流的编码
     > response.setCharacterEncoding("utf-8");
     > //告诉浏览器，服务器消息体使用的编码
     > response.setHeader("content-type","text/html;charset=utf-8");
     > ```
   
   * 代码实现
     
     ```java
     package cn.itcast.servlet;
     
     import javax.servlet.ServletException;
     import javax.servlet.annotation.WebServlet;
     import javax.servlet.http.HttpServlet;
     import javax.servlet.http.HttpServletRequest;
     import javax.servlet.http.HttpServletResponse;
     import java.io.IOException;
     import java.io.PrintWriter;
     
     @WebServlet("/ResponseDemo3")
     public class ResponseDemo3 extends HttpServlet {
         protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
             //设置流的编码
             response.setCharacterEncoding("utf-8");
             //告诉浏览器，服务器消息体使用的编码
             response.setHeader("content-type","text/html;charset=utf-8");
     
             PrintWriter writer = response.getWriter();
             writer.write("hello");
         }
     
         protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
             this.doPost(request, response);
         }
     }
     ```

5. 案例三：**服务器输出字节数据到浏览器**
   
   ```java
   package cn.itcast.servlet;
   
   import javax.servlet.ServletException;
   import javax.servlet.ServletOutputStream;
   import javax.servlet.annotation.WebServlet;
   import javax.servlet.http.HttpServlet;
   import javax.servlet.http.HttpServletRequest;
   import javax.servlet.http.HttpServletResponse;
   import java.io.IOException;
   import java.nio.charset.StandardCharsets;
   
   @WebServlet("/ResponseDemo4")
   public class ResponseDemo4 extends HttpServlet {
       protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
           response.setHeader("content-type","text/html;charset=utf-8");
           ServletOutputStream outputStream = response.getOutputStream();
           outputStream.write("hello".getBytes("utf-8"));
       }
   
       protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
           this.doPost(request, response);
       }
   }
   ```

### 五、ServletContext

1. ServletContext概述：服务器会为每一个应用创建一个ServletContext对象（ServletContext对象在服务器启动时创建，在服务器关闭时销毁，**代表整个web应用**）
   
   * ServletContext对象的作用是在整个web应用的动态资源之间共享数据。

2. 获取：
   
   * 通过request对象获取：request.getServletContext()
   * 通过HttpServlet获取：this.getServletContext()

3. 功能
   
   * 获取MIME类型
     
     > MIME类型：在互联网通信过程中定义的一种文件数据类型
     > 
     > * 格式：大类型/小类型（例：text/html）
     > * 获取：String getMimeType(String file)
   
   * 域对象：共享数据
     
     > * void setAttribute（String name，Object object）：存储数据
     > * Object getAttribute（String name）：通过键获取值
     > * removeAttribute（String name）：通过键移除键值对
     > 
     > ServletContext对象范围：所有用户所有请求的数据
   
   * 获取文件的真实路径（服务器路径）
     
     > getRealPath()
     > 
     > ![image-20230208151221843](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302081512706.png)

### 文件上传和下载

#### 文件上传

1. 文件上传：将本地文件通过流写入到服务器

2. 文件上传技术
   
   * JSPSmartUPload：应用在JSP上的文件上传和下载的组件
   * FileUpload：应用在java环境上的文件上传的功能
   * Servlet3.0：提供文件上传功能
   * Struts2：提供文件上传功能

3. 文件上传要素
   
   > * 表单提交方式为post
   > * 表单中需要有<input type="file">元素，需要有name属性和值
   > * 表单enctype=“multipart/form-data”

4. 原理分析
   
   ![image-20211216231040047](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211216231040047.png)

5. 代码实现
   
   > 1. 导入相关jar包
   >    
   >    * commons-fileupload-1.2.1.jar
   >    * commons-io-1.4.jar
   > 
   > 2. 编写文件上传页面
   >    
   >    ```jsp
   >    <%@ page contentType="text/html;charset=UTF-8" language="java" %>
   >    <html>
   >    <head>
   >        <title>文件上传</title>
   >    </head>
   >    <body>
   >        <form method="post" acttion="" enctype="multipart/form-data">
   >            <label for="file">文件</label>
   >            <input type="file" name="file" id="file"></br>
   >            <input type="submit" value="upload">
   >        </form>
   >    </body>
   >    </html>
   >    ```
   > 
   > 3. 编写文件上传servlet

#### 文件下载

* 需求
  
  > 1. 页面显示超链接
  > 2. 点击超链接后弹出下载提示框
  > 3. 完成图片文件下载

* 分析
  
  > 超链接指向的资源如果能够被浏览器解析，则在浏览器中展示，否则弹出下载提示框
  > 
  > 使用响应头设置资源的打开方式：
  > 
  > content-disposition：attachment；filename=xxx

* 实现
  
  > 1. 定义页面，使超链接的href指向servlet，传递资源名称filename
  > 2. 定义servlet
  >    1. 获取文件名称
  >    2. 使用字节输入流加载文件进内存
  >    3. 指定response的响应头
  >    4. 将数据写入response输出流
  
  ```java
  package cn.itcast.servlet;
  
  import javax.servlet.ServletContext;
  import javax.servlet.ServletException;
  import javax.servlet.ServletOutputStream;
  import javax.servlet.annotation.WebServlet;
  import javax.servlet.http.HttpServlet;
  import javax.servlet.http.HttpServletRequest;
  import javax.servlet.http.HttpServletResponse;
  import java.io.FileInputStream;
  import java.io.IOException;
  
  @WebServlet("/DownloadServlet")
  public class DownloadServlet extends HttpServlet {
      protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
          //获取文件名
          String filename = request.getParameter("filename");
          //使用字节输入流加载文件进内存
          ServletContext servletContext = this.getServletContext();
          String realPath = servletContext.getRealPath("/img/"+filename);
          FileInputStream fileInputStream = new FileInputStream(realPath);
  
          //设置响应头类型
          String mimeType = servletContext.getMimeType(filename);
          response.setHeader("content-type",mimeType);
  
          //设置响应头打开方式
          response.setHeader("content-disposition","attachment;filename"+filename);
          ServletOutputStream outputStream = response.getOutputStream();
          byte[] bytes = new byte[1024 * 8];
          int len = 0;
          while((len=fileInputStream.read(bytes)) != -1){
              outputStream.write(bytes,0,len);
          }
          fileInputStream.close();
      }
  
      protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
          this.doPost(request, response);
      }
  }
  ```

# 会话技术

1. 会话：一次会话中包含多次请求和响应。
2. 会话功能：在一次会话的范围内的多次请求间共享数据。
3. 方式
   * 客户端会话技术：Cookie
   * 服务器端会话技术：Session
   * 令牌技术

## Cookie

1. Cookie：将数据保存到客户端

2. 快速入门：
   
   * 创建Cookie对象，绑定数据
     * new Cookie(String name,String value)
   * 发送Cookie
     * response.addCookie(Cookie cookie)
   * 获取Cookie，拿到数据
     * request.getCookies()
   
   ```java
   package cn.itcast.servlet;
   
   import javax.servlet.ServletException;
   import javax.servlet.annotation.WebServlet;
   import javax.servlet.http.Cookie;
   import javax.servlet.http.HttpServlet;
   import javax.servlet.http.HttpServletRequest;
   import javax.servlet.http.HttpServletResponse;
   import java.io.IOException;
   
   /**
    * Cookie快速入门
    */
   
   @WebServlet("/ServletDemo5")
   public class ServletDemo5 extends HttpServlet {
       protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
                /**创建Cookie对象，绑定数据
                   * new Cookie(String name,String value)
                   * 发送Cookie
                   * response.addCookie(Cookie cookie)
                   * 获取Cookie，拿到数据
                   * request.getCookies()*/
           Cookie cookie = new Cookie("msg","hello");
           response.addCookie(cookie);
   
       }
   
       protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
           this.doPost(request, response);
       }
   }
   
   ================================================================
   package cn.itcast.servlet;
   
   import javax.servlet.ServletException;
   import javax.servlet.annotation.WebServlet;
   import javax.servlet.http.Cookie;
   import javax.servlet.http.HttpServlet;
   import javax.servlet.http.HttpServletRequest;
   import javax.servlet.http.HttpServletResponse;
   import java.io.IOException;
   
   @WebServlet("/ServletDemo6")
   public class ServletDemo6 extends HttpServlet {
       protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
           Cookie[] cookies = request.getCookies();
           if (cookies!=null){
               for (Cookie cs :
                       cookies) {
                   String name = cs.getName();
                   String value = cs.getValue();
                   System.out.println(name+":"+value);
   
               }
           }
       }
   
       protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
           this.doPost(request, response);
       }
   }
   ```

3. 原理：基于响应头set-cookie和请求头cookie实现
   
   ![image-20230208225302569](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302082253382.png)

4. cookie细节
   
   * 一次可不可以发送多个cookie？可以
   * cookie在浏览器中保存多长时间？
     * 默认情况下，浏览器被关闭，cookie被清除
     * 持久化存储：
       * setmaxAge(int seconds)
         * 正数：将Cookie数据写入硬盘文件。
         * 负数：默认值
         * 零：删除Cookie信息
   * cookie能不能存中文？
     * tomcat8以前，不支持
     * tomcat后，支持，但任然不支持特殊字符
   * cookie获取范围多大？（共享问题）
     * setPath(String path)：设置cookie的获取范围。默认情况下，设置当前的虚拟目录。可通过设置path为”/“在多个web项目中共享
     * 不同tomcat服务器之间共享cookie：setDomain(String path)。如果设置一 级域名相同，那么多个服务器之间cookie可以共享

5. cookie的特点
   
   * cookie存储数据在客户端浏览器
   * 浏览器对于单个cookie的大小有限制（4KB）而且对于同一域名下的总cookie数也有限制（20个）
* 移动端APP无法使用Cookie
   * 不安全，用户可以自己禁用Cookie
   * Cookie不能跨域
   
6. cookie的作用
   
   * cookie一般用于存储少量的不太敏感的信息
   * 在不登录的情况下，完成服务器对客户端的身份识别

7. 案例
   
   * 需求
     
     > 设置一个servlet，若为第一次访问则显示欢迎，否则显示上一次登录时间。
   
   * 分析
     
     > 1.可以采用cookie来完成
     > 2.在服务器中的Servlet判断是否有一个名为lastTime的cookie
     > 
     >     有:不是第一次访问
     >         响应数据:欢迎回来，您上次访问时间为:xxx
     >         写回cookie : lastTime=xxx
     >     没有:是第一次访问
     >         响应数据:您好，欢迎您首次访问
     >         写回Cookie : lastTime=xxx
   
   ```java
   package org.example;
   
   import javax.servlet.ServletException;
   import javax.servlet.http.Cookie;
   import javax.servlet.http.HttpServlet;
   import javax.servlet.http.HttpServletRequest;
   import javax.servlet.http.HttpServletResponse;
   import java.io.IOException;
   import java.text.SimpleDateFormat;
   import java.util.Date;
   
   /**
    * @author WenJianChen
    * @version 1.0
    * @date 2023/2/8 18:19
    */
   public class CookieDemo1 extends HttpServlet {
       @Override
       protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
           this.doPost(req, resp);
       }
   
       @Override
       protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
           resp.setContentType("text/html;charset=utf-8");
           Cookie[] cookies = req.getCookies();
           if (cookies!=null&&cookies.length>0){
               SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy年MM月dd日HH:mm:ss");
               for (Cookie cookie : cookies) {
                   //存在名为lastTime的cookie，即不是第一次访问
                   if ("lastTime".equals(cookie.getName())){
                       //响应数据
                       resp.getWriter().write("欢迎回来,您上次访问时间为："+cookie.getValue());
                       //更新cookie
                       cookie.setValue(dateFormat.format(new Date()));
                       resp.addCookie(cookie);
                       return;
                   }
               }
               //不存在名为lastTime的cookie，即为第一次访问
               resp.getWriter().write("您好，欢迎访问！");
               Cookie lastTimeCookie = new Cookie("lastTime",dateFormat.format(new Date()));
               resp.addCookie(lastTimeCookie);
           }
       }
   }
   ```

## Session

1. Session：服务器端会话技术，在一次会话的多次请求中共享数据，将数据保存在服务器端的对象中。

2. 快速入门：（HTTPSession）
   
   * 获取HttpSession对象
     * HttpSession session = request.getSession();
   * 使用HttpSession对象
     * void setAttribute（String name，Object object）：存储数据
     * Object getAttribute（String name）：通过键获取值
     * removeAttribute（String name）：通过键移除键值对
   
   ```java
   package cn.itcast.servlet;
   
   import javax.servlet.ServletException;
   import javax.servlet.annotation.WebServlet;
   import javax.servlet.http.HttpServlet;
   import javax.servlet.http.HttpServletRequest;
   import javax.servlet.http.HttpServletResponse;
   import javax.servlet.http.HttpSession;
   import java.io.IOException;
   
   @WebServlet("/ServletDemo9")
   public class ServletDemo9 extends HttpServlet {
       protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
           HttpSession session = request.getSession();
           session.setAttribute("msg","hehe");
       }
   
       protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
           this.doPost(request, response);
       }
   }
   
   =============================================================
   package cn.itcast.servlet;
   
   import javax.servlet.ServletException;
   import javax.servlet.annotation.WebServlet;
   import javax.servlet.http.HttpServlet;
   import javax.servlet.http.HttpServletRequest;
   import javax.servlet.http.HttpServletResponse;
   import javax.servlet.http.HttpSession;
   import java.io.IOException;
   
   @WebServlet("/ServletDemo10")
   public class ServletDemo10 extends HttpServlet {
       protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
           HttpSession session = request.getSession();
           Object msg = session.getAttribute("msg");
           System.out.println(msg);
       }
   
       protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
           this.doPost(request, response);
       }
   }
   ```

3. 原理：session的实现是依赖于cookie的
   
   ![image-20230209105946957](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302091059318.png)

4. 细节
   
   * 当客户端关闭后，服务器不关闭，两次获取的session是否为同一个？
     * 默认情况下，不是。
   * 客户端不关闭，服务器关闭后，两次获取的session是同一个吗？
     * 不是同一个，但要确保数据不丢失
       * session的钝化：在服务器正常关闭前，将session对象序列化到硬盘上
       * session的活化：在服务器启动后，将session转化为内存中的session对象
   * session的失效时间是多久？（什么时候被销毁）
     * 服务器关闭时，或者默认失效时间30分钟，或者session对象调用invalidate（）方法销毁

5. 特点
   
   * session用于存储一次会话的多次请求数据，存在服务器端
   * session可以存储任意类型，任意大小的数据
   * **服务器集群环境下无法直接使用Session**

## Session vs Cookie

1. session存储在服务器端，Cookie存储在客户端
2. session没有数据大小限制，Cookie有
3. session数据安全，Cookie相对不安全

### 案例：验证码

1. 需求
   
   * 访问带有验证码的页面login.jsp
   * 用户输入哟红户名，密码以及验证码
     * 如果用户名和密码输入有误，跳转登录页面，提示：用户名或密码错误
     * 如果验证码输入有误，跳转登录页面，提示：验证码错误
     * 如果全部输入正确，跳转到主页succcss.jsp，显示：用户名，欢迎您

2. 分析
   
   ![image-20230209111623952](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302091116757.png)

3. 实现
   
   * 验证码servlet
     
     ```java
     package cn.itcast.web.servlet;
     
     import javax.imageio.ImageIO;
     import javax.servlet.ServletException;
     import javax.servlet.annotation.WebServlet;
     import javax.servlet.http.HttpServlet;
     import javax.servlet.http.HttpServletRequest;
     import javax.servlet.http.HttpServletResponse;
     import java.awt.*;
     import java.awt.image.BufferedImage;
     import java.io.IOException;
     import java.util.Random;
     
     @WebServlet("/CheckCodeServlet")
     public class CheckCodeServlet extends HttpServlet {
         protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
             int width = 100;
             int height = 50;
     
             //验证码图片对象
             BufferedImage bufferedImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
     
             //美化图片
             Graphics graphics = bufferedImage.getGraphics();//画笔对象
             graphics.setColor(Color.PINK);
             graphics.fillRect(0,0,width,height);
     
             graphics.setColor(Color.BLUE);
             graphics.drawRect(0,0,width-1,height-1);
     
             String str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
             Random random = new Random();
             StringBuilder stringBuilder = new StringBuilder();
             for (int i = 1; i <= 4; i++) {
                 int index = random.nextInt(str.length());
                 char ch = str.charAt(index);
                 stringBuilder.append(ch);
                 graphics.drawString(ch+"",width/5*i,height/2);
             }
             String checkCode = stringBuilder.toString();
             request.getSession().setAttribute("checkCode",checkCode);
     
             //画干扰线
             graphics.setColor(Color.GREEN);
     
             //随机生成坐标点
             for (int i = 0; i < 10; i++) {
                 int x1 = random.nextInt(width);
                 int x2 = random.nextInt(width);
     
                 int y1 = random.nextInt(height);
                 int y2 = random.nextInt(height);
     
                 graphics.drawLine(x1,y1,x2,y2);
             }
     
             //将图片输出到页面展示
             ImageIO.write(bufferedImage,"jpg",response.getOutputStream());
         }
     
         protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
             this.doPost(request, response);
         }
     }
     ```
   
   * 登录servlet
     
     ```java
     package cn.itcast.web.servlet;
     
     import cn.itcast.dao.UserDao;
     import cn.itcast.domain.User;
     
     import javax.servlet.ServletException;
     import javax.servlet.annotation.WebServlet;
     import javax.servlet.http.HttpServlet;
     import javax.servlet.http.HttpServletRequest;
     import javax.servlet.http.HttpServletResponse;
     import javax.servlet.http.HttpSession;
     import java.io.IOException;
     
     @WebServlet("/LoginServlet")
     public class LoginServlet extends HttpServlet {
         protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
             //1.设置编码
             request.setCharacterEncoding("utf-8");
             //2.获取请求参数
             String username = request.getParameter("username");
             String password = request.getParameter("password");
             String checkCode = request.getParameter("checkCode");
                //获取生成的验证码
         HttpSession session = request.getSession();
         String checkCode_session = (String)session.getAttribute("checkCode");
         session.removeAttribute("checkCode_session");
         //判断验证码是否正确
         if (checkCode_session != null & checkCode_session.equalsIgnoreCase(checkCode)){
             //验证码正确
     
             // 3.封装User对象
             User loginUser = new User();
             loginUser.setUsername(username);
             loginUser.setPassword(password);
     
             //4.调用UserDao的login方法
             UserDao userDao = new UserDao();
             User user = userDao.login(loginUser);
     
             //判断
             if (user == null){
                 //登录失败
                 response.setContentType("text/html;charset=utf-8");
                 response.getWriter().write("登录失败！用户名或密码错误！");
                 request.setAttribute("login_error","登录失败");
                 request.getRequestDispatcher("/login.jsp").forward(request,response);
             }else {
                 //登录成功
                 session.setAttribute("user",user);
                 response.sendRedirect(request.getContextPath()+"/success.jsp");
             }
         }else {
             //验证码错误
             request.setAttribute("cc_error","验证码错误");
             request.getRequestDispatcher("/login.jsp").forward(request,response);
         }
     }
     
     protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
         this.doPost(request, response);
     }
     }
     ```
* login.jsp
  
  ```jsp
  <%@ page contentType="text/html;charset=UTF-8" language="java" %>
  <html>
  <head>
      <title>login</title>
      <script type="text/javascript">
          window.onload = function () {
              document.getElementById("img").onclick = function () {
                  this.src = "/UserLogin/CheckCodeServlet?time="+new Date().getTime();
              }
          }
      </script>
      <style type="text/css" rel="stylesheet">
          div{
              color: red;
          }
      </style>
  </head>
  <body>
      <form action="/UserLogin/LoginServlet" method="post">
          <table>
              <tr>
                  <td>用户名</td>
                  <td><input type="text" name="username"></td>
              </tr>
              <tr>
                  <td>密码</td>
                  <td><input type="password" name="password"></td>
              </tr>
              <tr>
                  <td>验证码</td>
                  <td><input type="text" name="checkCode"></td>
              </tr>
              <tr align="center">
                  <td colspan="2" ><img id="img" src="/UserLogin/CheckCodeServlet"></td>
              </tr>
              <tr align="center">
                  <td colspan="2" ><input type="submit" value="登录"></td>
              </tr>
          </table>
      </form>
      <div><%=request.getAttribute("cc_error") == null ? "" : request.getAttribute("cc_error")%></div>
      <div><%=request.getAttribute("login_error") == null ? "" : request.getAttribute("login_error")%></div>
  </body>
  </html>
  ```

* success.jsp
  
  ```jsp
  <%@ page import="cn.itcast.domain.User" %>
  <%@ page contentType="text/html;charset=UTF-8" language="java" %>
  <html>
  <head>
      <title>success</title>
  </head>
  <body>
      <%
          User user=(User)request.getSession().getAttribute("user");
      %>
      <h1><%=user.getUsername()%>,欢迎您！</h1>
  </body>
  </html>
  ```

## 令牌技术token

参考：

* [什么是JWT？](https://blog.csdn.net/weixin_45410366/article/details/125031959)
* [JWT认证原理、流程整合springboot实战应用](https://www.bilibili.com/video/BV1i54y1m7cP/?spm_id_from=333.337.search-card.all.click&vd_source=fabefd3fabfadb9324761989b55c26ea)
* https://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html
* [面试官：什么是JWT？为什么要用JWT？](https://mp.weixin.qq.com/s/d2yzPfy0D5lqXKZyCTAWSQ)

官网：https://jwt.io/introduction

Token是一种用于身份验证和授权的令牌。在计算机系统中，Token通常是一个字符串，用于标识用户或客户端的身份和权限。 

在身份验证方面，Token可以用于替代传统的用户名和密码验证方式。当用户登录系统时，系统会生成一个Token并返回给用户。用户在后续的请求中，可以通过携带这个Token来证明自己的身份。系统可以验证Token的有效性，并根据Token中的信息来识别用户。

在授权方面，Token可以用于控制用户对系统资源的访问权限。系统可以根据Token中的权限信息，判断用户是否有权访问某个资源或执行某个操作。 

常见的Token类型包括： 

* JSON Web Token (JWT)：一种**开放标准**，定义了一种紧凑且自包含的方式来传输信息，通常用于身份验证和授权。 
* OAuth Token：用于授权第三方应用程序访问用户资源的令牌，常用于实现单点登录和授权码模式等场景。 
* Session Token：在Web应用程序中，用于标识用户会话的令牌，通常存储在服务器端的会话管理中。

Token的使用可以提高系统的安全性和灵活性，同时也减少了对传统的用户名和密码的依赖。

### 简介

1. JWT（Json Web Token）：定义了一种紧凑的、自包含的方式，用于作为 JSON 对象在各方之间安全地传输信息。

2. 设计目的：不需要服务端存储状态，安全的传递非敏感信息。

3. 作用：用于用户登录鉴权

4. 认证方式对比

   * session认证分析
   * token认证分析

5. JWT数据结构

   * Header（头）：记录令牌类型、签名算法等
   * Payload（有效载荷）：携带一些自定义信息，默认信息等，JWT官方提供了7个字段使用：
     * iss (Issuer)：签发者。
     * sub (Subject)：主题。
     * aud (Audience)：接收者。
     * exp (Expiration time)：过期时间。
     * nbf (Not Before)：生效时间。
     * iat (Issued At)：签发时间。
     * jti (JWT ID)：编号。
   * Signature（签名）：防止token被篡改、确保安全性。将header、payload并加入指定密钥通过指定签名算法计算得出

   ![image-20230807233524493](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202308072335260.png)

6. 优点

   * **无需服务器存储状态**：传统的基于会话的认证机制需要服务器在会话中存储用户的状态信息，包括用户的登录状态、权限等。而使用 JWT，服务器无需存储任何会话状态信息，所有的认证和授权信息都包含在 JWT 中，使得系统可以更容易地进行水平扩展。
   * **跨域支持**：由于 JWT 包含了完整的认证和授权信息，因此可以轻松地在多个域之间进行传递和使用，实现跨域授权。
   * **适应微服务架构**：在微服务架构中，很多服务是独立部署并且可以横向扩展的，这就需要保证认证和授权的无状态性。使用 JWT 可以满足这种需求，每次请求携带 JWT 即可实现认证和授权。
   * **自包含**：JWT 包含了认证和授权信息，以及其他自定义的声明，这些信息都被编码在 JWT 中，在服务端解码后使用。JWT 的自包含性减少了对服务端资源的依赖，并提供了统一的安全机制。
   * **扩展性**：JWT 可以被扩展和定制，可以按照需求添加自定义的声明和数据，灵活性更高。

7. 缺点

8. base64编码：[Base64&Base64URL](#base64)

# 模板引擎

1. 简介
   * 模板引擎是一个用于**动态生成 HTML（或其他文本格式）文件**的工具。
   * 通过**将数据（如来自数据库、用户输入或其他来源的信息）与预先定义的模板（通常是 HTML 文件）相结合，生成最终的内容**。这些模板包含了占位符（如变量或逻辑结构），在渲染时被替换为实际数据。
   * 模板引擎在前后端分离架构中的角色相对较小，主要承担静态页面渲染或特定任务的 HTML 模板生成，而在前后端不分离架构中，角色则更为重要，用于在服务器端动态生成页面，直接影响整个页面的生成与渲染过程。
2. 基本工作流程
   * **创建模板**：开发者编写模板文件，模板中通常包含 HTML 标签和动态占位符。
   * **传递数据**：将数据（如用户信息、商品列表等）传递给模板引擎。
   * **渲染模板**：模板引擎通过将数据填充到模板的占位符中，生成最终的 HTML 页面。
   * **输出结果**：最终生成的 HTML 页面将被返回给客户端，供用户浏览器显示。
3. 核心功能
   * **变量替换**：模板引擎允许将动态变量（如数据库中的数据）嵌入到静态模板中，生成个性化的内容。
   * **逻辑控制**：模板引擎通常提供条件语句（如 `if`）、循环语句（如 `for`）等，用来在模板中控制内容的显示方式，增加模板的动态性。
   * **模板继承**：许多模板引擎支持模板继承，使得开发者可以创建基础模板，并在子模板中重用和扩展这些基础模板的结构和样式。
   * **过滤和转义**：模板引擎可以对输出进行过滤（如日期格式化）和转义（如防止 XSS 攻击），确保生成的内容是安全和格式正确的。
4. 分类：模板引擎可以根据不同的编程语言和框架进行分类。
   * **JavaScript 模板引擎**：
     - **Handlebars**：一个非常流行的 JavaScript 模板引擎，支持逻辑控制和模板继承等特性。
     - **EJS**：另一个 JavaScript 模板引擎，语法接近原生 HTML，可以很方便地嵌入 JavaScript 代码。
   * **Python 模板引擎**：
     - **Jinja2**：广泛用于 Python Web 开发，尤其是在 Flask 等框架中，具有强大的功能和灵活的语法。
   * **Java 模板引擎**：
     - **Freemarker**：用于 Java Web 开发中的模板渲染，支持丰富的语法和功能。
   * **Ruby 模板引擎**：
     - **ERB**：Ruby 的默认模板引擎，允许嵌入 Ruby 代码到 HTML 中。
5. 常见Java模板引擎：
   * Thymeleaf：适合需要高度与 Spring 框架集成的应用，且对模板继承和自然模板有较高需求。
   * FreeMarker：适合大型企业级应用，提供丰富的功能和灵活性。
   * Velocity：适合大型企业级应用，提供丰富的功能和灵活性。
   * JSP（JavaServer Pages）：适合传统的 Java EE 应用，但不如现代模板引擎灵活。
   * Mustache：适合简单应用，语法简洁，易于学习。
   * Groovy Templates：适合快速原型开发和小型项目。
   * Pebble：适合现代 Java Web 应用，特别是微服务架构。

## Thymeleaf

1. 简介：

   * Thymeleaf 是一个现代的 Java 模板引擎，用于服务器端的 Web 应用程序开发，特别是在 Spring 框架中常用。
   * Thymeleaf 的设计目标是提供一个既可以在服务器端渲染页面，也可以在开发和调试过程中直接在浏览器中查看的模板引擎。

2. 特点

   * 自然模板：Thymeleaf 模板是有效的 HTML 文件，你可以在浏览器中直接打开并查看。
   * 支持表达式语言（EL）：Thymeleaf 提供了一种丰富的表达式语言，允许你在模板中插入动态内容。
   * 集成Spring框架
   * 支持模板继承
   * 支持条件判断和循环
   * 文件扩展名：Thymeleaf 默认的文件扩展名是 `.html`，但它也支持其他文件类型（如 `.xml`）进行处理。
   * 支持静态内容和动态内容结合

3. 使用（在springboot项目中）

   * 引入依赖

     > ```xml
     > <dependency>
     > <groupId>org.springframework.boot</groupId>
     > <artifactId>spring-boot-starter-thymeleaf</artifactId>
     > </dependency>
     > ```

   * 配置相关项

     > ```yaml
     > # thymeleaf
     > spring:
     > thymeleaf:
     >  prefix: classpath:/templates/ # 渲染的模板文件所在根目录
     >  check-template: true # 是否强制性检查templates目录下是否有待渲染模板文件
     >  suffix: .html # 设定thymeleaf文件后缀名
     >  encoding: UTF-8
     >  servlet:
     >    content-type: text/html # thymeleaf文件的内容类型
     >  cache: false # 禁止使用缓存
     > ```

   * 编写控制器

     ```java
     @Controller
     @RequestMapping("/test")
     public class IndexController {
     
         @GetMapping("/index")
         public String index(Model model){
             model.addAttribute("str","hello thymeleaf!");
             return "index";
         }
     }
     ```

   * 编写页面

     ```html
     <!DOCTYPE html>
     <html lang="en" xmlns:th="http://www.thymeleaf.org">
     <head>
         <meta charset="UTF-8">
         <title>Title</title>
     </head>
     <body>
         <!---->
         <h1 >hello world!</h1>
         <h1 th:text="${str}"></h1>
     </body>
     </html>
     ```

4. 常用语法标签

## FreeMarker

## JSP

### JSP快速入门

1. JSP：Java Server Pages，java服务器端页面，既可以写html代码，也可以写java代码

2. 原理：
   
   * jsp本质是就是一个Servlet
   
   ![image-20230209104054079](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302091040604.png)

3. JSP的脚本：Jsp定义Java代码的方式
   
   * 代码标签<%  %>：定义的java代码在service方法
   * 声明标签<%!  %>：定义的java代码，在jsp转换后为成员变量
   * 表达式标签<%= %>：定义的java代码，相当于输出语句，将内容输出到页面

4. 指令标签
   
   * 作用：用于配置JSP页面，导入资源文件
   
   * 格式
     
     ```
     <%@ 指令名称 属性名1=属性值1 属性名2=属性值2 ......%>
     ```
   
   * 分类
     
     * page：配置页面
       
       > 属性如下
       > 
       > contentType：设置响应体的mime类型以及字符集，设置当前页面的编码
       > 
       > import：导包
       > 
       > language：
       > 
       > errorPage：当前页面发生异常后跳转的页面
       > 
       > isErrorPage：标识当前页面是否为错误页面（若为错误页面则可以使用内置对象exception）
       > 
       > extends
       > 
       > session：该jsp页面是否使用http的session会话对象
       > 
       > buffer
       > 
       > autoFlush
       > 
       > info：该信息可以在Servlet接口的getServletInfo方法中获得
       > 
       > isELIgnored：是否忽略EL表达式的使用
     
     * include：页面包含的，导入页面的资源文件（静态包含，即内容被原样引入）
       
       > 属性
       > 
       > file：
     
     * taglib：导入资源，引用标签库以及制定标签库的前缀
       
       > 属性
       > 
       > prefix：指定标签库的前缀
       > 
       > uri：标签库文件的存放位置

5. 动作标签
   
   > 动作标签在请求处理阶段按照在页面中出现的顺序被执行
   > 
   > 常用动作标签：
   > 
   > * \<jsp:include\>
   >   * page：被包含文件的相对路径
   >   * flush：可选参数，设置是否刷新缓冲区，默认值为false
   > * \<jsp:forward\>
   > * \<jsp:param>：可作为其他标签的子标签，用于传递参数
   >   * name
   >   * value

6. 注释标签
   
   ```
   <%-- --%>
   ```

7. JSP的内置对象：在JSP页面中不需要获取和创建，可以直接使用的对象（共9个）
   
   > 变量名                    真实类型
   > 
   > pageContext        PageContext        当前页面共享数据（可以获取其他八个内置对象）
   > 
   > request                HttpServletRequest        一次请求访问的多次资源（转发）
   > 
   > response            HttpServletResponse        
   > 
   > session                HttpSession        一次会话的多个请求间共享数据
   > 
   > out                        JspWriter        输出对象
   > 
   > ​    response.write输出始终先于out输出
   > 
   > page                    Object        当前页面
   > 
   > application        ServletContext        所有用户间共享数据
   > 
   > exception            Throwable
   > 
   > config                    ServletConfig
   > 
   > 内置对象详解：
   > 
   > 1. request：封装了由客户端生成的HTTP请求的所有细节。
   >    
   >    * getParameter（）：获取请求参数值
   >    
   >    * getParameterValues（）：获取表单提交信息
   >    
   >    * 中文乱码问题
   >    
   >    * 获取客户端相关信息
   >      
   >      ![image-20211112193622070](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211112193622070.png)
   >    
   >    * 在作用域中管理属性：setAttribute（），getAttribute（），removeAttribute（）
   >    
   >    * 获取cookie：getCookies（），
   >    
   >    * 获取国际化信息：getLocale（），getLocales（）
   > 
   > 2. response
   >    
   >    * 重定向网页：sendRedirect（）
   >    
   >    * 设置输出缓冲
   >      
   >      ![image-20211112194500530](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211112194500530.png)
   >    
   >    * 处理HTTP文件头：setContentType（），setHeader（）
   > 
   > 3. session
   >    
   >    * session中常用方法
   >      
   >      ![image-20211112195036752](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211112195036752.png)
   > 
   > 4. out：通过out对象向客户端浏览器输出信息并管理应用服务器的输出缓冲区
   >    
   >    * 向客户端输出数据：print（），println（）
   >    
   >    * 管理相应缓冲区：clear（），clearBuffer（）
   >      
   >      ![image-20211112200846954](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211112200846954.png)
   > 
   > 5. application：用于保存所有应用程序中的共有数据，在服务器启动时自动创建，服务器停止时自动销毁
   >    
   >    * 应用程序初始化参数：getInitParameter（），getAttributeNames（）
   > 
   > 6. pageContext：可以通过该对象获得其他内置对象
   >    
   >    ![image-20211112201007238](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211112201007238.png)
   > 
   > 7. page：代表JSP页面本身，只在JSP页面内才是合法的
   > 
   > 8. config：获得服务器的配置信息
   >    
   >    ![image-20211112201203556](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211112201203556.png)
   > 
   > 9. exception：只用在包含“isErrorPage=true”的页面才可以使用
   >    
   >    ![image-20211112201433931](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211112201433931.png)

### EL表达式

1. EL表达式：Expression Language

2. 作用：替换和简化jsp页面中java代码的编写

3. 语法：${表达式}

4. 注意：
   
   * jsp默认支持EL表达式
   * 忽略EL表达式
     * 设置jsp中page指令的属性isELIgnored=“ture”
     * 或者使用\\${表达式}

5. 使用
   
   * 运算
     
     > 算术运算符
     > 
     > 比较运算符
     > 
     > 逻辑运算符
     > 
     > 空运算符：empty（用于判断字符串、集合、数组对象是否为null并且长度是否为0）
   
   * 获取值
     
     * **el表达式只能从域对象中获取值**
     
     * 语法：
       
       > 1. ${域名称.键名}：从指定域中获取指定键的值
       > 
       > 域名称：
       > 
       > * pageScope->pageContext
       > * requestScope->request
       > * sessionScope->session
       > * applicationScope->application(ServletContext)
       > 2. ${键名}：依次从最小的域中查找是否有该键对应的值
       > 3. 获取对象：List集合，Map集合的值
       >    * 对象：${域名称.键名.属性名}（本质上是调用对象的getter方法）
       >    * List集合：${域名称.键名[索引]}
       >    * Map集合：${域名称.键名.key名称} 或 ​\${域名称.键名[key名称]}
   
   * 隐式对象
     
     > * el表达式中有11个隐式对象
     > * pageContext：获取其他八个内置对象
     >   * ${pageContext.request.contextPath}：多态获取虚拟目录

### JSTL标签

1. JSTL：JavaServer Pages Tag Library。JSP标准标签库（由apache组织提供的开源的jsp标签）

2. 作用：用于简化和替换jsp页面上的java代码

3. 使用
   
   * 导入jstl相关jar包
   * 引入标签库：taglib指令
   * 使用标签

4. 常用标签
   
   * if：相当于java中if语句
     
     ```jsp
     test为必须属性
     ```
   
   * choose：相当于java中的switch语句
   
   * foreach：相当于java中的for语句
     
     ```jsp
     1. 完成重复操作
     属性：
         begin:初始值（包含）
         end:结束值（包含）
         var:临时变量
         step:步长
         varStatus:循环状态
     2. 遍历
     属性：
         items:容器对象
         var:容器对象临时变量
     ```

### javaBean在JSP中的应用

1. \<jsp:useBean\>标签：用于在JSP页面中创建一个JavaBean实例并通过属性设置将实例存放到jsp的指定范围内。
   
2. \<jsp:setProperty\>标签：用于对JavaBean中属性赋值，但JavaBean的属性要提供相应的set方法

3. \<jsp:getProperty\>标签：用于获取JavaBean中属性的值，但JavaBean的属性要提供相应的get方法

# MVC开发模式

1. MVC（Model-View-Controller）
   
   * 模型：完成业务操作
   * 视图：展示数据
   * 控制器：获取用户输入，调用模型，将数据交给视图进行展示
   
   ![image-20220418082619232](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418082619232.png)

2. 优点：
   
   * 耦合性低，方便维护，利于分工
   * 可重用性高

3. 缺点：
   
   * 使得项目架构变得复杂
   
4. controller层设计

   controller层的主要作用包括以下几项：

   - 接收请求并解析参数
   - 调用 Service 执行具体的业务代码（可能包含参数校验）
   - 捕获业务逻辑异常做出反馈
   - 业务逻辑执行成功做出响应


# 软件设计架构

1. 三层架构
   
   * 界面层（表示层）：用户可以通过界面上的组件和服务器进行交互
   * 业务逻辑层：处理业务逻辑
   * 数据访问层：操作数据存储文件
   
   ![image-20211002163015726](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211002163015726.png)


# Filter和Listener

## Filter

1. 过滤器：Java Servlet 规范提供的一种组件，它可以拦截 HTTP 请求和响应。通过过滤器，我们可以对请求进行预处理、对响应进行后处理，甚至根据需要修改请求或响应的内容。

2. 过滤器的作用：一般用于完成通用的操作，例：登录验证，统一编码处理，敏感字符处理。

3. 快速入门
   
   > 实现步骤：
   > 
   > 1. 定义一个类实现Filter接口
   > 
   > 2. 覆写方法
   > 
   > 3. 配置拦截路径
   >    
   >    * xml方式配置
   >    * 注解方式配置
   
   注解配置：
   
   ```java
   package cn.itcast.filter;
   
   import javax.servlet.*;
   import javax.servlet.annotation.WebFilter;
   import java.io.IOException;
   /**
   * 注解方式
   */
   @WebFilter("/*")
   public class FilterDemo1 implements Filter {
       //初始化方法，Web服务器启动，创建Filter时调用， 只调用一次
       @Override
       public void init(FilterConfig filterConfig) throws ServletException {
   
       }
       //销毁方法，服务器关闭时调用，只调用一-次
       @Override
       public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
           System.out.println("filter was been executed.");
   
           //放行
           filterChain.doFilter(servletRequest,servletResponse);
       }
   
       @Override
       public void destroy() {

       }
   }
   ```
   
   > 注意：如果是在springboot项目中使用过滤器，需要在引导类上加@ServletComponentScan开启Servlet组件支持。
   
   web.xml文件中配置：
   
   ~~~xml
   <?xml version="1.0" encoding="UTF-8"?>
   <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
            version="4.0">
   
       <filter>
           <filter-name>demo2</filter-name>
           <filter-class>cn.itcast.filter.FilterDemo2</filter-class>
       </filter>
       <filter-mapping>
           <filter-name>demo2</filter-name>
           <!--        拦截路径-->
           <url-pattern>/*</url-pattern>
       </filter-mapping>
   </web-app>
   ~~~
   
4. 拦截配置

   * 拦截路径配置

     * 具体资源路径，例：/index.jsp
     * 拦截目录，例：/user/*
     * 后缀名拦截，例：*.jsp
     * 拦截所有路径，例：/*

   * 拦截方式配置（资源被访问的方式）

     * 注解配置

       * 设置dispatcherType属性
         * REQUEST：默认值，浏览器直接请求资源
         * FORWARD：转发访问资源
         * INCLUDE：包含访问资源
         * ERROR：错误跳转资源
         * ASYNC：异步访问资源
     * web.xml配置
       * 设置dispatcher标签

5. 过滤器执行流程

   请求到达阶段：

   - 客户端发送一个HTTP请求到Servlet容器。
   - Servlet容器接收到请求后，通过Filter链处理请求之前的预处理阶段。
   - Filter链中的每个Filter都可以对请求进行修改、验证身份、记录日志等操作。
   - 每个Filter在处理完请求之后，可以选择将请求传递给下一个Filter或目标Servlet。

   目标资源阶段：

   - 过滤器链中的最后一个Filter将请求传递给目标Servlet来执行实际的业务逻辑。
   - 目标Servlet对请求进行处理，生成响应。

   响应返回阶段：

   - 目标Servlet生成响应后，响应通过Filter链处理之前的后处理阶段。
   - Filter链中的每个Filter都可以对响应进行修改、添加头信息、压缩内容等操作。
   - 每个Filter在处理完响应之后，可以选择将响应传递给下一个Filter或将响应返回给客户端。

   响应发送阶段：

   - 最后一个Filter将响应返回给Servlet容器。
   - Servlet容器将响应发送给客户端。

6. 过滤器生命周期

   - 初始化阶段：调用`init()`方法，进行一些初始化操作。
   - 请求处理阶段：调用`doFilter()`方法，处理请求和响应。
   - 销毁阶段：调用`destroy()`方法，进行一些清理操作。

7. 过滤器链

   执行顺序：

   * 注解配置：按照类名的字符串比较规则比较，值小的先执行。也可以使用@Order注解来指定Filter的执行顺序，值越小优先级越高。
   * web.xml配置：谁定义在上面谁先执行

8. 核心API

   > 核心接口：Filter，FilterChain，FilterConfig，ServletRequest，ServletResponse，ServletException

      * Filter接口

        ![image-20211122194305974](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211122194305974.png)

      * FilterChain接口

        FilterChain接口位于javax.servlet包中，由容器实现。该接口中只包含一个方法doFilter(ServletRequest request,ServletResponse response)，主要用于将过滤器处理的请求或响应传递给下一个过滤器对象。

9. 常用场景：

   * 认证和授权：检查用户的身份认证状态，并确定其是否有权限访问特定资源。
   * 日志记录：记录请求和响应的详细信息，以便日后进行审计、故障排除或统计分析。
   * 数据压缩：对响应进行压缩，以减少传输的数据量，提升性能。
   * 输入验证和数据清理：检查请求参数的有效性，并清理恶意或不必要的数据（敏感词过滤等）。
   * 缓存控制：根据请求的属性设置响应的缓存策略，以减少网络流量和提高响应速度。

## Listener

1. Listener：
   
   > 事件监听机制：
   > 
   > * 事件
   > * 事件源
   > * 监听器
   > * 注册监听
   
   ![image-20211215190343503](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211215190343503.png)

2. ServletContextListener：监听ServletContext对象的创建和销毁
   
   * 方法
     
     > void contextDestroy(ServletContextEvent sce)：ServletContext对象被销毁之前调用该方法
     > 
     > void contextInitialized(ServletContextEvent sce)：ServletContext对象被创建之前调用该方法
   
   * 步骤
     
     > 1. 定义一个类实现SevletContextListener接口
     > 2. 覆写方法
     > 3. 配置
     >    1. web.xml
     >    2. 注解

# Jakarta EE

参考：[jakarta ee 全套专业级视频攻略](https://www.bilibili.com/video/BV1fF4m1F7ow/?spm_id_from=333.999.0.0&vd_source=fabefd3fabfadb9324761989b55c26ea)

## JSON Binding&Processing

文档：

* [Jakarta JSON Binding](https://jakarta.ee/specifications/jsonb/3.0/)
* [Jakarta JSON Processing](https://jakarta.ee/specifications/jsonp/2.1/)

1. JSON Binding & Yasson
2. JSON Processing & parsson

## Bean Validation

文档：[Validation](https://jakarta.ee/specifications/bean-validation/)

参考：

* https://pdai.tech/md/spring/springboot/springboot-x-interface-param.html
* [JSR303](https://beanvalidation.org/1.0/spec/#d0e32)
* https://www.bilibili.com/video/BV17i4y157Ah/?spm_id_from=autoNext&vd_source=fabefd3fabfadb9324761989b55c26ea

Java API 的规范 `JSR303` 定义了校验的标准 `validation-api` ，其中一个比较出名的实现是 `hibernate validation` ，`spring validation` 是对其的二次封装，常用于 SpringMVC 的参数自动校验，参数校验的代码就不需要再与业务逻辑代码进行耦合了。

1. 简单检验

2. 分组检验

3. @Valid和@Validated比较

   在校验简单的controller入参时@Valid和@Validated基本没有什么区别，但是在分组检验、嵌套检验等场景下两者功能略有不同。

   * @Validated可以根据不同的分组采用不同的验证机制，但是@Valid作为标准JSR-303规范，还没有吸收分组的功能。
   * @Validated可以用在类型、方法和方法参数上，但是不能用在成员属性（字段）上；@Valid可以用在方法、构造函数、方法参数和成员属性（字段）上。

4. 常用的校验注解

5. 自定义Validation

6. `@NotEmpty`和`@NotBlank`

   两者都是Java中常见的用于验证字符串非空性的注解，主要用于校验输入参数或对象字段上的字符串属性。

   区别如下：

   1. `@NotEmpty`注解：
      - 来自于Hibernate Validator，需要导入`org.hibernate.validator.constraints.NotEmpty`。
      - 用于验证字符串非空性，即不能为空字符串和null值都不符合条件。
      - 可以用于集合、数组、Map和CharSequence类型（如String、CharBuffer等）的验证。
   2. `@NotBlank`注解：
      - 来自于Jakarta Bean Validation API，需要导入`javax.validation.constraints.NotBlank`。
      - 继承自`@NotEmpty`注解，但更加严格。
      - 用于验证字符串非空性，即不能为空字符串和null值都不符合条件，而且字符串中至少要有一个非空白字符。
      - 只能用于CharSequence类型（如String、CharBuffer等）的验证。

   总结来说，`@NotEmpty`注解验证字符串非空性，要求字符串不能为null且长度不能为0；而`@NotBlank`注解在`@NotEmpty`的基础上，还要求字符串中至少包含一个非空白字符。

# Mybatis

官网参考文档：

* https://mybatis.org/mybatis-3/zh/getting-started.html
* mybatis-generator：https://mybatis.org/generator/
* mybatis通用Mapper：https://github.com/abel533/Mapper

## Mybatis简介

1. 原始jdbc操作分析
   
   * 硬编码（mybatis使用配置文件解决）
   * 注册驱动，获取连接
     * sql语句
   * 操作繁琐（mybatis自动完成）
     * 手动设置参数
     * 手动封装结果集
   
   ![image-20220420142447641](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420142447641.png)

2. mybatis概述
   
   ![image-20220420142638250](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420142638250.png)

## 快速入门

1. 开发步骤
   
   * 创建数据库表，定义对应POJO类
   * 引入mybatis模块包
   * 编写mybatis核心配置文件
   * 编写sql映射文件
   * 加载核心配置文件获得会话对象执行sql语句
   
   ![image-20220420143426954](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420143426954.png)
   
   ```xml
   <!--UserMapper.xml-->
   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
   <mapper namespace="userMapper">
       <select id="findAll" resultType="org.example.domain.User">
           select * from user
       </select>
   </mapper>
   ```
   
   ```xml
   <!--SQLMapperConfig.xml-->
   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd">
   <configuration>
       <!--数据源环境-->
       <environments default="development">
           <environment id="development">
               <transactionManager type="JDBC"></transactionManager>
               <dataSource type="POOLED">
                   <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
                   <property name="url" value="jdbc:mysql://localhost/test?serverTimezone=UTC"/>
                   <property name="username" value="root"/>
                   <property name="password" value="4112"/>
               </dataSource>
           </environment>
       </environments>
   
       <!--加载映射文件-->
       <mappers>
           <mapper resource="org/example/mapper/UserMapper.xml"></mapper>
       </mappers>
   
   </configuration>
   ```
   
   ```java
   //测试类
   package org.example.test;
   
   import org.apache.ibatis.io.Resources;
   import org.apache.ibatis.session.SqlSession;
   import org.apache.ibatis.session.SqlSessionFactory;
   import org.apache.ibatis.session.SqlSessionFactoryBuilder;
   import org.junit.Test;
   
   import java.io.IOException;
   import java.io.InputStream;
   import java.util.List;
   
   public class MybatisTest {
   
       @Test
       public void test1() throws IOException {
           //获得核心配置文件
           InputStream resourceAsStream = Resources.getResourceAsStream("SqlMapperConfig.xml");
           //获得session工厂对象
           SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(resourceAsStream);
           //获得session会话对象
           SqlSession sqlSession = sqlSessionFactory.openSession();
           //执行操作 参数：namespace+id
           List<Object> userList = sqlSession.selectList("userMapper.findAll");
        System.out.println(userList);
           sqlSession.close();
   
       }
   }
   ```

2. Mybatis映射文件
   
   ![image-20220420144902922](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420144902922.png)

3. Mybatis核心配置文件概述
   
   参考文档：https://mybatis.org/mybatis-3/zh/configuration.html#properties
   
   ![image-20211120114452462](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimgimage-20211120114452462.png)
   
   > * environments标签
   >   
   >   * 事务管理器（transactionManager）
   >     * JDBC：直接使用JDBC的提交和回滚设置，依赖于从数据源得到的连接来管理事务作用域
   >     * MANAGED：几乎没作用，从来不提交或回滚一个连接，而是让容器来管理事务的整个生命周期（比如JEE应用服务器的上下文）。默认情况下它会关闭连接，然而一些容器不希望如此，因此需要将closeConnection属性设置为false来阻止它默认的关闭行为。
   >   * 数据源（dataSource）
   >     * UNPOOLED：这种数据源的实现知识每次被请求时打开和关闭连接
   >     * POOLED：这种数据源的实现利用“池”的概念将JDBC连接对象组织起来
   >     * JNDI：这种数据源的实现是为了能在如EJB或应用服务器这类容器中使用，容器客户集中或在外部配置数据源，然后放置一个JNDI上下文引用。
   >   
   >   ![image-20211120114926933](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimgimage-20211120114926933.png)
   > 
   > * mapper标签：该标签的作用是加载映射，加载方式有如下几种
   >   
   >   * 使用相对于类路径的资源引用， 例如: <mapper resource=" org/mybatis/builder/AuthorMapper.xml"/>
   >   * 使用完全限定资源定位符(URL) ，例如: <mapper url=”file://var/mappers/AuthorMapper.xml"/>
   >   * 使用映射器接口实现类的完全限定类名，例如: <mapper class= "org.mybatis.builder.AuthorMapper"/>
   >   * 将包内的映射器接口实现全部注册为映射器, 例如: <package name=" org.mybatis.builder"/>
   > 
   > * properties标签
   >   
   >   ![image-20211120115019690](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211120115019690.png)
   > 
   > * typeAliases标签：自定义别名
   >   
   >   ![image-20211120115105853](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211120115105853.png)
   > 
   > * typerHandlers标签
   >   
   >   ![image-20220420162953584](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420162953584.png)
   >   
   >   ![image-20220420163107986](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420163107986.png)
   > 
   > * plugins标签
   
   ```xml
   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd">
   <configuration>
       <!--数据源环境-->
       <environments default="development">
           <environment id="development">
               <transactionManager type="JDBC"></transactionManager>
               <dataSource type="POOLED">
                   <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
                   <property name="url" value="jdbc:mysql://localhost/test?serverTimezone=UTC"/>
                   <property name="username" value="root"/>
                   <property name="password" value="4112"/>
               </dataSource>
           </environment>
       </environments>
   
       <!--加载映射文件-->
       <mappers>
           <mapper resource="org/example/mapper/UserMapper.xml"></mapper>
       </mappers>
   
   </configuration>
   ```

4. 相关API
   
   * SqlSessionFactoryBuilder
     
     ![image-20220420152903129](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420152903129.png)
   
   * SqlSessionFactory
     
     ![image-20220420153035158](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420153035158.png)
   
   * SqlSession
     
     ![image-20220420153241622](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420153241622.png)

## Mybatis的基本增删改查操作

1. 插入操作
   
   > ![image-20220420150803384](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420150803384.png)
   
   ```xml
   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
   <mapper namespace="userMapper">
       <!--查询操作-->
       <select id="findAll" resultType="org.example.domain.User">
           select * from user
       </select>
       <!--插入操作-->
       <insert id="save" parameterType="org.example.domain.User">
           insert into user values (#{id},#{username},#{password})
       </insert>
       <!--修改操作-->
       <!--删除操作-->
   </mapper>
   ```
   
   ```java
   package org.example.test;
   
   import org.apache.ibatis.io.Resources;
   import org.apache.ibatis.session.SqlSession;
   import org.apache.ibatis.session.SqlSessionFactory;
   import org.apache.ibatis.session.SqlSessionFactoryBuilder;
   import org.example.domain.User;
   import org.junit.Test;
   
   import java.io.IOException;
   import java.io.InputStream;
   import java.util.List;
   
   public class MybatisTest {
   
       @Test
       public void test1() throws IOException {
           //模拟User对象
           User user = new User();
           user.setUsername("tom");
           user.setPassword("abcd");
   
           //获得核心配置文件
           InputStream resourceAsStream = Resources.getResourceAsStream("SQLMapperConfig.xml");
           //获得session工厂对象
           SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(resourceAsStream);
           //获得session会话对象
           SqlSession sqlSession = sqlSessionFactory.openSession();
           //执行操作 参数：namespace+id
   
   //        List<Object> userList = sqlSession.selectList("userMapper.findAll");
   //        System.out.println(userList);
   
           int insert = sqlSession.insert("userMapper.save", user);
           System.out.println(insert);
   
           /*Mybatis执行更新操作，提交事务*/
           sqlSession.commit();
   
           sqlSession.close();
   
       }
   }
   ```

2. 修改操作
   
   ```xml
   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
   <mapper namespace="userMapper">
       <!--查询操作-->
       <select id="findAll" resultType="org.example.domain.User">
           select * from user
       </select>
       <!--插入操作-->
       <insert id="save" parameterType="org.example.domain.User">
           insert into user values (#{id},#{username},#{password})
       </insert>
       <!--修改操作-->
       <update id="update" parameterType="org.example.domain.User">
           update user set username=#{username},password=#{password} where id=#{id}
       </update>
       <!--删除操作-->
   </mapper>
   ```
   
   ```java
   package org.example.test;
   
   import org.apache.ibatis.io.Resources;
   import org.apache.ibatis.session.SqlSession;
   import org.apache.ibatis.session.SqlSessionFactory;
   import org.apache.ibatis.session.SqlSessionFactoryBuilder;
   import org.example.domain.User;
   import org.junit.Test;
   
   import java.io.IOException;
   import java.io.InputStream;
   import java.util.List;
   
   public class MybatisTest {
   
       @Test
       public void test1() throws IOException {
           //模拟User对象
           User user = new User();
           user.setId(6);
           user.setUsername("Lucy");
           user.setPassword("dcba");
   
           //获得核心配置文件
           InputStream resourceAsStream = Resources.getResourceAsStream("SQLMapperConfig.xml");
           //获得session工厂对象
           SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(resourceAsStream);
           //获得session会话对象
           SqlSession sqlSession = sqlSessionFactory.openSession();
           //执行操作 参数：namespace+id
   
   //        /*Mybatis执行更新操作，提交事务*/
   //        sqlSession.commit();
   
           //修改操作
           int update = sqlSession.update("userMapper.update", user);
           System.out.println(update);
           sqlSession.commit();
   
           sqlSession.close();
   
       }
   }
   ```

3. 删除操作
   
   ```xml
   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
   <mapper namespace="userMapper">
       <!--查询操作-->
       <select id="findAll" resultType="org.example.domain.User">
           select * from user
       </select>
       <!--插入操作-->
       <insert id="save" parameterType="org.example.domain.User">
           insert into user values (#{id},#{username},#{password})
       </insert>
       <!--修改操作-->
       <update id="update" parameterType="org.example.domain.User">
           update user set username=#{username},password=#{password} where id=#{id}
       </update>
       <!--删除操作-->
       <delete id="delete" parameterType="org.example.domain.User">
           delete from user where id=#{id}
       </delete>
   </mapper>
   ```
   
   ```java
   package org.example.test;
   
   import org.apache.ibatis.io.Resources;
   import org.apache.ibatis.session.SqlSession;
   import org.apache.ibatis.session.SqlSessionFactory;
   import org.apache.ibatis.session.SqlSessionFactoryBuilder;
   import org.example.domain.User;
   import org.junit.Test;
   
   import java.io.IOException;
   import java.io.InputStream;
   import java.util.List;
   
   public class MybatisTest {
   
       @Test
       public void test1() throws IOException {
           //模拟User对象
           User user = new User();
           user.setId(6);
           user.setUsername("Lucy");
           user.setPassword("dcba");
   
           //获得核心配置文件
           InputStream resourceAsStream = Resources.getResourceAsStream("SQLMapperConfig.xml");
           //获得session工厂对象
           SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(resourceAsStream);
           //获得session会话对象
           SqlSession sqlSession = sqlSessionFactory.openSession();
           //执行操作 参数：namespace+id
   
           //查询操作
   //        List<Object> userList = sqlSession.selectList("userMapper.findAll");
   //        System.out.println(userList);
   
           //插入操作
   //        int insert = sqlSession.insert("userMapper.save", user);
   //        System.out.println(insert);
   //
   //        /*Mybatis执行更新操作，提交事务*/
   //        sqlSession.commit();
   
           //修改操作
   //        int update = sqlSession.update("userMapper.update", user);
   //        System.out.println(update);
   //        sqlSession.commit();
   
           //删除操作
           int delete = sqlSession.delete("userMapper.delete", user);
           System.out.println(delete);
           sqlSession.commit();
   
           sqlSession.close();
   
       }
   }
   ```

4. 查询操作
   
   > 在进行查询时表的列名和实体类的字段名不一致时，解决方法如下：
   > 
   > * 给列起别名或者使用sql片段
   > * 使用resultMap进行映射

## Mapper代理

1. 传统实现方式：手动对Dao进行实现

2. 代理开发方式：由Mybatis实现Dao接口
   
   > 1.定义与SQL映射文件同名的Mapper接口，并且将Mapper接口和SQL映射文件放置在同- -目录下
   > 2.设置SQL映射文件的namespace属性为Mapper接口全限定名
   > 3.在Mapper接口中定义方法，方法名就是SQL映射文件中sq|语句的id,并保持参数类型和返回值
   > 类型一致
   > 4.编码：通过SqlSession的getMapper方法获取Mapper接口的代理对象。调用对应方 法完成sq的执行
   > 
   > 细节:如果Mapper接口名称和SQL映射文件名称相同,并在同一目录下，则可以使用包扫描的方式简
   > 化SQL映射文件的加载
   
   ```java
   UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
           List<User> users = userMapper.selectAll();
   ```
   
   ![image-20211120112940959](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211120112940959.png)

![image-20220420155719754](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420155719754.png)

## 动态sql

1. if
   
   ![image-20220420162833609](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420162833609.png)

2. foreach

3. sql片段抽取

## 映射文件

## 多表操作

1. 一对一模型
   
   ![image-20220420164024347](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420164024347.png)
   
   方式一：在映射的xml中使用resultMap进行封装
   
   ![image-20220420164917540](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420164917540.png)
   
   方式二：使用association进行配置

2. 一对多模型
   
   ![image-20220420165829725](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420165829725.png)

3. 多对多模型

## 注解开发

1. 常用注解

   ![image-20220420170043582](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420170043582.png)

   ~~~java
   
   1. @Insert：实现新增功能
   @Insert("insert into user(id,name) values(#{id},#{name})")
   public int insert(User user);
   
   2. @Update注解：实现更新功能
   @Update("update user set name= #{name},sex = #{sex},age =#{age} where id = #{id}")
   void updateUserById(User user);
   
   3. @Delete注解：实现删除功能
   @Delete("delete from  user  where id =#{id}")
   void deleteById(Integer id);
   
   4. @Select注解：实现查询功能
   @Select("Select * from user")
   List<User> queryAllUser();
   
   
   1. @Result注解。
   2. @Results注解。
   3. @ResultMap是结果集映射的三大注解。
   
   @Select({"select id, name, class_id from student"})
   @Results(id="studentMap", value={
       @Result(column="id", property="id", jdbcType=JdbcType.INTEGER, id=true),
       @Result(column="name", property="name", jdbcType=JdbcType.VARCHAR),
       @Result(column="class_id ", property="classId", jdbcType=JdbcType.INTEGER)
   })
   List<Student> selectAll();
   
   @Select({"select id, name, class_id from student where id = #{id}"})
   @ResultMap(value="studentMap")
   Student selectById(integer id);
   ~~~

   > 注意：使用注解时，则没有mapper映射文件,但此时应该在核心配置文件中配置加载映射关系。配置如下：
   > 
   > ```xml
   > <!--加载映射关系-->
   > <mappers>
   >     <!--指定接口所在包-->
   >     <package name="com.chen.dao"/>
   > </mappers>
   > ```

## 常见面试题

1. 传参时#和$符号有什么不同？
   
   > \#传入的参数在SQL中显示为字符串（当成一个字符串），会对自动传入的数据加一个双引号。$传入的参数在SqL中直接显示为传入的值。\#可以防止SQL注入的风险（语句的拼接）；但$无法防止Sql注入。一般情况均使用#。

# MybatisPlus

官网地址：https://baomidou.com/pages/226c21/#%E5%88%9D%E5%A7%8B%E5%8C%96%E5%B7%A5%E7%A8%8B

## 简介

1. 简介

2. 特性

3. 架构
   
   ![image-20220420172055210](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420172055210.png)

## 快速开始

（以在springboot项目）

## 通用CRUD操作

1. TableId
2. TableField：常用于解决属性名与字段名不一致问题，属性字段不在表中问题

## 代码生成器

```java
/**
     * 代码生成器
     */
    @Test
    public void testGenerator(){
        FastAutoGenerator.create("jdbc:mysql://localhost:3306/ordering_system?serverTimezone=UTC",
                "root",
                "4112")
                .globalConfig(builder -> {
                    builder.author("whyme-chen") // 设置作者
                            .enableSwagger() // 开启 swagger 模式
                            .outputDir(System.getProperty("user.dir")+"/src/main/java/"); // 指定输出目录
                })
                .packageConfig(builder -> {
                    builder.parent("com.chen") // 设置父包名
                            .entity("pojo")
                            .pathInfo(Collections.singletonMap(OutputFile.xml, "resources/com/example/mapper")); // 设置mapperXml生成路径
                })
                .strategyConfig(builder -> {
                    builder.addInclude("address_book","category","dish","dish_flavor",
                            "employee","order_detail","orders","setmeal","setmeal_dish",
                            "shopping_cart","user"); // 设置需要生成的表名
//                            .addTablePrefix("sys_"); // 设置过滤表前缀
                })
                .templateEngine(new FreemarkerTemplateEngine()) // 使用Freemarker引擎模板，默认的是Velocity引擎模板
                .execute();

    }
```

## 条件构造器

![image-20220504162503272](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220504162503272.png)

![image-20220504162536139](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220504162536139.png)

## 分页插件

1. 配置
   
   ```java
   @Bean
       public MybatisPlusInterceptor mybatisPlusInterceptor(){
           //配置分页插件
           MybatisPlusInterceptor mybatisPlusInterceptor = new MybatisPlusInterceptor();
           mybatisPlusInterceptor.addInnerInterceptor(new PaginationInnerInterceptor());
           return mybatisPlusInterceptor;
       }
   ```

2. 使用
   
   ```java
       /**
        * 分页插件
        */
       @Test
       public void testPagination(){
           Page<User> userPage = new Page<>(1,10);
           Page<User> page = userMapper.selectPage(userPage, null);
           System.out.println("当前页"+page.getCurrent());
           System.out.println("每页大小"+page.getSize());
           System.out.println("总条数"+page.getTotal());
           System.out.println("总页数"+page.getPages());
           System.out.println("数据"+page.getRecords());
       }
   ```

## 其他常用操作

### 逻辑删除

### 自动填充

### 多数据源

### 乐观锁

# JPA

JPA是官方推出的Java持久层操作标准（现主要使用Hibernate实现），使用SpringData技术和JpaRepository接口技术，也可以达到简化数据层的目的。要在SpringBoot中使用SpringDataJPA，需要spring-boot-starter-data-jpa依赖库的支持。

# Spring boot

## 基础入门

### 简介

1. 概述：SringBoot是由Pivtal团队提供的全新框架，其设计目的是用来简化Spring的初始搭建和开发过程。

2. 优势对比

   * Spring程序
     * 依赖设置繁琐
     * 配置繁琐
   * SpringBoot程序优点
     * 起步依赖：提供依赖启动器简化构建配置，可快速构建独立的Spring应用
     * 辅助功能：直接嵌入Tomcat、Jetty和Undertow服务器（无需部署WAR文件）
     * 自动配置：简化常用工程相关配置

### 快速上手

> 注意从SpringBoot3.1.1开始需要java17，spring framework6.0.10及以上版本

3. 创建项目方式
   
   * 借助idea创建（阿里镜像网址：[http://start.aliyun](http://start.aliyun)）
   * 借助官网创建（https://start.spring.io/）
   * 创建Maven项目，手动添加Springboot依赖

4. 入门案例解析
   
   * parent：所有SpringBoot项目要继承的项目，定义了若干坐标版本号（依赖管理，而非依赖）以达到减少依赖冲突的目的。
     
     ![image-20220223170214665](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223170214665.png)
   
   * starter：定义了当前项目使用的所有依赖坐标，以达到减少依赖配置的目的。
   
   * 引导类
     
     ![image-20220223173016842](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223173016842.png)
   
   * 内嵌tomcat
     
     ![image-20220223173832559](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223173832559.png)

5. 热部署
   
   在开发过程中，通常会对一段业务代码不断地修改测试，在修改之后往往需要重启服务，有些服务需要加载很久才能启动成功，这种不必要的重复操作极大的降低了程序开发效率。为此，Spring Boot框架专门提供了进行热部署的依赖启动器，用于进行项目热部署，而无需手动重启项目。
   
   * 添加spring-boot-devtools热部署依赖启动器
     
     ```xml
     <!-- 引入热部署依赖 -->
     <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-devtools</artifactId>
     </dependency>
     ```
   
   * idea工具热部署设置

### 基础配置

#### 全局配置文件

1. 属性配置
   
   配置属性参考：https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#appendix.application-properties
   
   ![image-20220223222016095](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223222016095.png)

   注意：SpringBoot默认配置文件为application.properties，通过键值对配置
   
2. 配置文件分类

   * properties
   * yml(主流)
   * yaml

   ![image-20220223222330450](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223222330450.png)

   > 注意：SpringBootp配置文件的加载顺序（优先级）：**properties>yml>yaml**
   > 
   > 使用idea在yaml文件中配置时，代码提示失效解决方案：
   > 
   > ![image-20220224150428417](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220224150428417.png)

3. yaml文件

   * YAML（YAML Ain‘t Markup Lanuage），一种数据序列化格式

   * 优点：
     
     * 容易阅读
     * 容易与脚本语言交互
     * 以数据为核心，重数据轻格式

   * YAML文件扩展名
     
     * .yml
     * .yaml(主流)

   * yaml语法规则
     
     ![image-20220224150924547](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220224150924547.png)
     
     ![image-20220224151857640](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220224151857640.png)
     
     ![image-20220224152016549](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220224152016549.png)

   * yaml数据读取
     
     ![image-20220224152744940](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220224152744940.png)
     
     * 将全部数据封装到Envirorment对象
       
       ![image-20220224155427033](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220224155427033.png)
     
     * 自定义对象封装指定数据
       
       ![image-20220224160118620](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220224160118620.png)

   * 引用变量
     
     ![image-20220224155032097](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220224155032097.png)

> 总结：
> 
> 1. 读取配置文件数据的方式
>    * 使用Environment对象的getProperty()方法读取
>    * 使用@Value注解
>    * 使用@ConfigurationProperties(prefix = "")注解进行映射

#### 自定义配置文件

1. @PropertySource：在项目启动入口类中使用，将自定义的配置文件加载到项目中（.property或.yml文件）
2. @ImportResource：在项目启动入口类中使用，将自定义配置文件加载到Spring上下文中（.xml文件）
3. @Configuration：

### 高级配置

1. 使用@ConfigurationProperties为第三方bean绑定属性

   ![image-20230528163717624](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281637305.png)

   ![image-20230528164057851](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281641781.png)

2. 松散绑定

   * @CanfigurationProperties绑定属性支持属性名宽松绑定，绑定前缀名命名规范:仅能使用纯小写字母、数字、下划线作为合法的字符
   * 宽松绑定不支持注解@Value引用单个属性的方式

3. 常用计量单位

   ![image-20230528165141032](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281651311.png)

4. 开启Bean数据校验

   * 添加JSR303规范坐标与Hibernate校验框架对应坐标

     ![image-20230528170422423](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281704053.png)

   * 对Bean开启校验功能

     ![image-20230528170501329](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281705453.png)

   * 设置校验规则

     ![image-20230528170521320](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281705729.png)

### 常用注解

参考文章：https://juejin.cn/post/6844904136492711950

1. @SpringBootApplication：
   
   ~~~java
   @Target({ElementType.TYPE})
   @Retention(RetentionPolicy.RUNTIME)
   @Documented
   @Inherited
   @SpringBootConfiguration
   @EnableAutoConfiguration
   @ComponentScan(
       excludeFilters = {@Filter(
       type = FilterType.CUSTOM,
       classes = {TypeExcludeFilter.class}
   ), @Filter(
       type = FilterType.CUSTOM,
       classes = {AutoConfigurationExcludeFilter.class}
   )}
   )
   public @interface SpringBootApplication {
       //......
   }
   ~~~
   
2. @import

   * springboot中@Enable***开头的注解表示开启某项功能，其底层依赖@import注解。
   * @import注解可以向容器中导入类，这些类对象会被注入到容器中
     * 直接导入
     * 导入配置类
     * 导入ImportSelector接口实现类
     * 导入ImportBeanDefinitionRegister接口的实现类
   
3. @ConditionalOnClass&@ConditionOnBean等条件依赖注解

   用于在特定条件下加载或不加载一个Bean或一个配置类。

   `@ConditionalOnClass`: 这个注解用于指定只有在**类路径下存在指定的类**时才会创建被注解的Bean或配置类。如果类路径中不存在指定的类，则不会创建。

   `@ConditionalOnBean`: 这个注解用于指定只有在**Spring容器中存在指定的Bean**时才会创建被注解的Bean或配置类。如果Spring容器中不存在指定的Bean，则不会创建。

   常见的条件依赖注解有：

   | 注解                            | 功能说明                                             |
   | ------------------------------- | ---------------------------------------------------- |
   | @ConditionalOnBean              | 仅在当前上下文中存在某个bean时，才会实例化这个Bean   |
   | @ConditionalOnClass             | 某个class位于类路径上，才会实例化这个Bean            |
   | @ConditionalOnExpression        | 当表达式为true的时候，才会实例化这个Bean             |
   | @ConditionalOnMissingBean       | 仅在当前上下文中不存在某个bean时，才会实例化这个Bean |
   | @ConditionalOnMissingClass      | 某个class在类路径上不存在的时候，才会实例化这个Bean  |
   | @ConditionalOnNotWebApplication | 不是web应用时才会实例化这个Bean                      |
   | @AutoConfigureAfter             | 在某个bean完成自动配置后实例化这个bean               |
   | @AutoConfigureBefore            | 在某个bean完成自动配置前实例化这个bean               |

## 应用

参考：

* https://gitee.com/BiMon/spring-boot-demo

### 导入导出Excel

#### Apache POI

#### hutool

#### EasyPOI

3. 基于EasyPoi导出
   
   参考：https://zhuanlan.zhihu.com/p/426308817
   
   ```java
       /**
        * easypoi实现导出
        * @param map
        * @param request
        * @param response
        */
       @RequestMapping(value = "/exportByEasyPoi", method = RequestMethod.GET)
       public void exportByEasyPoi(ModelMap map,
                                    HttpServletRequest request,
                                    HttpServletResponse response) {
           List<User> users = userMapper.selectList(null);
           ExportParams params = new ExportParams("用户列表", "用户列表", ExcelType.XSSF);
           map.put(NormalExcelConstants.DATA_LIST, users);
           map.put(NormalExcelConstants.CLASS, User.class);
           map.put(NormalExcelConstants.PARAMS, params);
           map.put(NormalExcelConstants.FILE_NAME, "users");
           PoiBaseView.render(map, request, response, NormalExcelConstants.EASYPOI_EXCEL_VIEW);
       }
   
   ==========================================
   /**
   实体类
   */
   package com.example.pojo;
   
   import cn.afterturn.easypoi.excel.annotation.Excel;
   import com.baomidou.mybatisplus.annotation.IdType;
   import com.baomidou.mybatisplus.annotation.TableId;
   import com.baomidou.mybatisplus.annotation.TableName;
   import lombok.AllArgsConstructor;
   import lombok.Data;
   import lombok.EqualsAndHashCode;
   import lombok.NoArgsConstructor;
   
   /**
    * @author whyme-chen
    * @date 2022/4/30 9:30
    */
   @Data
   @TableName(value = "tb_user")
   @AllArgsConstructor
   @NoArgsConstructor
   @EqualsAndHashCode(callSuper = false)
   public class User {
       /*
   * EasyPoi的核心注解@Excel，通过在对象上添加@Excel注解，可以将对象信息直接导出到Excel中去，下面对注解中的属性做个介绍；
       name：Excel中的列名；
       width：指定列的宽度；
       needMerge：是否需要纵向合并单元格；
       format：当属性为时间类型时，设置时间的导出导出格式；
       desensitizationRule：数据脱敏处理，3_4表示只显示字符串的前3位和后4位，其他为*号；
       replace：对属性进行替换；
       suffix：对数据添加后缀。
   * */
   
   @TableId(value = "id",type = IdType.AUTO)
   @Excel(name = "ID",width = 10)
   private Long id;
   
   @Excel(name = "用户名",width = 30)
   private String userName;
   
   @Excel(name = "密码",width = 40)
   private String password;
   
   @Excel(name = "姓名",width = 30)
   private String name;
   
   @Excel(name = "年龄",width = 20,replace = {"男_0", "女_1"})
   private Integer age;
   
   @Excel(name = "邮箱",width = 50)
   private String email;
   }
   ```
   
2. 基于EasyPoi导入

   ~~~java
   @RequestMapping(value = "/importByEasyPoi", method = RequestMethod.POST)
       public String importByEasyPoi(@RequestPart("file") MultipartFile file) {
           ImportParams params = new ImportParams();
           params.setTitleRows(1);
           params.setHeadRows(1);
           try {
               List<User> list = ExcelImportUtil.importExcel(
                       file.getInputStream(),
                       User.class, params);
               return list.toString();
           } catch (Exception e) {
               e.printStackTrace();
               return "导入失败！";
           }
       }
   ~~~

#### EasyExcel

参考：

* [黑马阿里EasyExcel实战教程](https://www.bilibili.com/video/BV1bF411D7M8/?spm_id_from=333.337.search-card.all.click&vd_source=fabefd3fabfadb9324761989b55c26ea)
* [官网](https://easyexcel.opensource.alibaba.com/)

1. EasyExcel
2. 快速入门

### 发送邮件

#### 基本概念

1. SMTP（Simple Mail Transfer Protocol）：简单邮件传输协议，用于发送电子邮件的传输协议
2. POP3（Post Office Protocol - Version 3）：用于接收电子邮件的标准协议
3. IMAP（Interface Mail Access Protocol）：互联网消息协议，是POP3的替代协议

#### 基于JavaMail实现

参考：https://www.cnblogs.com/antLaddie/p/15583991.html

#### 整合JavaMail

1. 导入依赖
   
   ```xml
           <dependency>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-starter-mail</artifactId>
           </dependency>
   ```
   
2. 配置
   
   ```yml
     # 邮箱配置（application.yml中）（开启邮箱的SMTP服务）
     mail:
       host: smtp.qq.com
       username: 2710335790@qq.com
       password: untmkgyrgdjbdhag
   ```

3. 编写代码，发送邮件
   
   ```java
   package com.chen.service.impl;
   
   import com.chen.service.ISendMailService;
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.mail.SimpleMailMessage;
   import org.springframework.mail.javamail.JavaMailSender;
   import org.springframework.mail.javamail.MimeMessageHelper;
   import org.springframework.stereotype.Service;
   
   import javax.mail.MessagingException;
   import javax.mail.internet.MimeMessage;
   import java.io.File;
   
   /**
    * @author whyme-chen
    * @date 2022/5/8 19:52
    */
   @Service
   public class SendMailServiceImpl implements ISendMailService {
   
       @Autowired
       private JavaMailSender javaMailSender;
   
       //邮件发送人
        private String form = "2710335790@qq.com";
       //邮件接收人
       private String to = "2949613269@qq.com";
       // 邮件标题
       private String subject = "测试";
       // 邮件正文
       private String context = "测试邮件发送功能的实现";
       // 邮件正文2
       private String text = "<a href='https://www.baidu.com/'>前往百度</a>";
       /**
    * 发送简单邮件
    */
   @Override
   public void sendMail() {
       SimpleMailMessage simpleMailMessage = new SimpleMailMessage();
       //设置基本信息
       simpleMailMessage.setFrom(form);//whymechen将替代邮箱好+"whymechen"
       simpleMailMessage.setTo(to);
       simpleMailMessage.setSubject(subject);
       simpleMailMessage.setText(context);
   
       javaMailSender.send(simpleMailMessage);
   }
   
   /**
    * 发送多部件邮件
    */
   @Override
   public void sendMultiPartsMail() {
       try {
           MimeMessage mimeMessage =javaMailSender.createMimeMessage();
           MimeMessageHelper helper = new MimeMessageHelper(mimeMessage,true);//true表示是否允许发送附件
   
           helper.setFrom(form);
           helper.setTo(to);
           helper.setSubject(subject);
           helper.setText(text,true);//可以解析html
   
           //添加附件
           File lanqiao = new File("C:\\Users\\hp\\Desktop\\蓝桥常见考点.txt");
           helper.addAttachment(lanqiao.getName(),lanqiao);
   
           javaMailSender.send(mimeMessage);
       } catch (MessagingException e) {
           e.printStackTrace();
       }
   }
   ```
   

### 打包与运维

1. 使用maven打包项目后，可以使用`java -jar 工程名`运行jar包

   ![image-20230524230040792](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305242300813.png)
   
2. 临时属性设置

   ~~~shell
   # 带属性数启动SpringBoot，携带多个属性启动SpringBoot，属性间使用空格分隔
   java –jar springboot.jar –-server.port=80
   ~~~

3. 属性加载顺序

   参考地址：https://docs.spring.io/spring-boot/docs/current/referencehtml/spring-boot-features.htmlboot-features-external-config

4. 配置文件类别：多层级配置文件间的属性采用叠加并覆盖的形式作用于程序

   ![image-20230524231842289](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305242318701.png)

5. 自定义配置文件

   ![image-20230524232149244](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305242321432.png)

   注意：

   * 单服务器项目: 使用自定义配置文件需求较低
   * 多服务器项目: 使用自定义配置文件需求较高，将所有配置放置在一个目录中，统一管理
   * 基于springcloud技术，所有的服务器将不再设置配置文件，而是通过配置中心进行设定，动态加载配置信息

6. 多环境开发

   ![image-20230525221702051](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305252217588.png)

   ![image-20230525221957097](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305252219487.png)

   ![image-20230525222405129](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305252224524.png)

   > 当Maven与SpringBoot同时对多环境进行控制时，以Mavn为主SpringBoot使用@..@占位符读取Maven对应的配置属性值。
   >
   > 基于SpringBoot读取Maven配置属性的前提下，如果在Idea下测工程时pom.xml每次更新需要手动compile方可生效。

### 日志控制

参考：[Spring Boot统一日志框架](http://c.biancheng.net/spring_boot/slf4j-logback.html)

Spring Boot 选用 SLF4J + Logback 的组合来搭建日志系统。

#### 日志配置

1. 日志级别：

   | 序号 | 日志级别 | 说明                                                        |
   | ---- | -------- | ----------------------------------------------------------- |
   | 1    | trace    | 追踪，指明程序运行轨迹。                                    |
   | 2    | debug    | 调试，实际应用中一般将其作为最低级别，而 trace 则很少使用。 |
   | 3    | info     | 输出重要的信息，使用较多。                                  |
   | 4    | warn     | 警告，使用较多。                                            |
   | 5    | error    | 错误信息，使用较多。                                        |

   > 上述日志级别的优先级依次升高。当一条日志信息的级别大于或等于配置文件的级别时，就对这条日志进行记录。

2. 日志输出格式

   | 序号 | 输出格式                     | 说明                                                         |
   | ---- | ---------------------------- | ------------------------------------------------------------ |
   | 1    | %d{yyyy-MM-dd HH:mm:ss, SSS} | 日志生产时间,输出到毫秒的时间                                |
   | 2    | %-5level                     | 输出日志级别，-5 表示左对齐并且固定输出 5 个字符，如果不足在右边补 0 |
   | 3    | %logger 或 %c                | logger 的名称                                                |
   | 4    | %thread 或 %t                | 输出当前线程名称                                             |
   | 5    | %p                           | 日志输出格式                                                 |
   | 6    | %message 或 %msg 或 %m       | 日志内容，即 logger.info("message")                          |
   | 7    | %n                           | 换行符                                                       |
   | 8    | %class 或 %C                 | 输出 Java 类名                                               |
   | 9    | %file 或 %F                  | 输出文件名                                                   |
   | 10   | %L                           | 输出错误行号                                                 |
   | 11   | %method 或 %M                | 输出方法名                                                   |
   | 12   | %l                           | 输出语句所在的行数, 包括类名、方法名、文件名、行数           |
   | 13   | hostName                     | 本地机器名                                                   |
   | 14   | hostAddress                  | 本地 ip 地址                                                 |

3. 常见配置文件选项

   ~~~yml
   
   
   logging:
     # 配置记录器级别
     level:
       org.springframework.web: "debug"
       org.hibernate: "error"
   ~~~

4. 自定义日志配置

   在 Spring Boot 的配置文件 application.porperties/yml 中，可以对日志的一些默认配置进行修改，但这种方式只能修改个别的日志配置，想要修改更多的配置或者使用更高级的功能，则需要通过日志实现框架自己的配置文件进行配置。

   Spring 官方提供了各个日志实现框架所需的配置文件，用户只要将指定的配置文件放置到项目的类路径下即可。

   | 日志框架                | 配置文件                                                     |
   | ----------------------- | ------------------------------------------------------------ |
   | Logback                 | logback-spring.xml、logback-spring.groovy、logback.xml、logback.groovy |
   | Log4j2                  | log4j2-spring.xml、log4j2.xml                                |
   | JUL (Java Util Logging) | logging.properties                                           |

   > 从上可以看出日志框架的配置文件主要分为两类，一类是普通的日志配置文件，即不带spring标识的配置文件，例如logback.xml，一类是带有spring标识的配置文件，例如logback-spring.xml

   logback.xml等项目的类路径不带 spring 标识的普通日志配置文件，会跳过 Spring Boot，直接被日志框架加载。

   ~~~xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!--
   scan：当此属性设置为true时，配置文件如果发生改变，将会被重新加载，默认值为true。
   scanPeriod：设置监测配置文件是否有修改的时间间隔，如果没有给出时间单位，默认单位是毫秒当scan为true时，此属性生效。默认的时间间隔为1分钟。
   debug：当此属性设置为true时，将打印出logback内部日志信息，实时查看logback运行状态。默认值为false。
   -->
   <configuration scan="false" scanPeriod="60 seconds" debug="false">
       <!-- 定义日志的根目录 -->
       <property name="LOG_HOME" value="/app/log"/>
       <!-- 定义日志文件名称 -->
       <property name="appName" value="bianchengbang-spring-boot-logging"></property>
       <!-- ch.qos.logback.core.ConsoleAppender 表示控制台输出 -->
       <appender name="stdout" class="ch.qos.logback.core.ConsoleAppender">
           <!--
           日志输出格式：
      %d表示日期时间，
      %thread表示线程名，
      %-5level：级别从左显示5个字符宽度
      %logger{50} 表示logger名字最长50个字符，否则按照句点分割。
      %msg：日志消息，
      %n是换行符
           -->
           <layout class="ch.qos.logback.classic.PatternLayout">
               <pattern>%d{yyyy-MM-dd HH:mm:ss} [%thread]**************** %-5level %logger{50} - %msg%n</pattern>
           </layout>
       </appender>
   
       <!-- 滚动记录文件，先将日志记录到指定文件，当符合某个条件时，将日志记录到其他文件 -->
       <appender name="appLogAppender" class="ch.qos.logback.core.rolling.RollingFileAppender">
           <!-- 指定日志文件的名称 -->
           <file>${LOG_HOME}/${appName}.log</file>
           <!--
           当发生滚动时，决定 RollingFileAppender 的行为，涉及文件移动和重命名
           TimeBasedRollingPolicy： 最常用的滚动策略，它根据时间来制定滚动策略，既负责滚动也负责出发滚动。
           -->
           <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
               <!--
               滚动时产生的文件的存放位置及文件名称 %d{yyyy-MM-dd}：按天进行日志滚动
               %i：当文件大小超过maxFileSize时，按照i进行文件滚动
               -->
               <fileNamePattern>${LOG_HOME}/${appName}-%d{yyyy-MM-dd}-%i.log</fileNamePattern>
               <!--
               可选节点，控制保留的归档文件的最大数量，超出数量就删除旧文件。假设设置每天滚动，
               且maxHistory是365，则只保存最近365天的文件，删除之前的旧文件。注意，删除旧文件是，
               那些为了归档而创建的目录也会被删除。
               -->
               <MaxHistory>365</MaxHistory>
               <!--
               当日志文件超过maxFileSize指定的大小是，根据上面提到的%i进行日志文件滚动 注意此处配置SizeBasedTriggeringPolicy是无法实现按文件大小进行滚动的，必须配置timeBasedFileNamingAndTriggeringPolicy
               -->
               <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                   <maxFileSize>100MB</maxFileSize>
               </timeBasedFileNamingAndTriggeringPolicy>
           </rollingPolicy>
           <!-- 日志输出格式： -->
           <layout class="ch.qos.logback.classic.PatternLayout">
               <pattern>%d{yyyy-MM-dd HH:mm:ss} [ %thread ] ------------------ [ %-5level ] [ %logger{50} : %line ] -
                   %msg%n
               </pattern>
           </layout>
       </appender>
   
       <!--
     logger主要用于存放日志对象，也可以定义日志类型、级别
     name：表示匹配的logger类型前缀，也就是包的前半部分
     level：要记录的日志级别，包括 TRACE < DEBUG < INFO < WARN < ERROR
     additivity：作用在于children-logger是否使用 rootLogger配置的appender进行输出，
     false：表示只用当前logger的appender-ref，true：
     表示当前logger的appender-ref和rootLogger的appender-ref都有效
       -->
       <!-- hibernate logger -->
       <logger name="net.biancheng.www" level="debug"/>
       <!-- Spring framework logger -->
       <logger name="org.springframework" level="debug" additivity="false"></logger>
   
       <!--
       root与logger是父子关系，没有特别定义则默认为root，任何一个类只会和一个logger对应，
       要么是定义的logger，要么是root，判断的关键在于找到这个logger，然后判断这个logger的appender和level。
       -->
       <root level="info">
           <appender-ref ref="stdout"/>
           <appender-ref ref="appLogAppender"/>
       </root>
   </configuration> 
   ~~~

   Spring Boot 推荐用户使用 logback-spring.xml等带有 spring 标识的配置文件。该类配置文件不会直接被日志框架加载，而是由 Spring Boot 对它们进行解析。这样就可以使用 Spring Boot 的高级功能 Profile，实现在不同的环境中使用不同的日志配置。

#### 日志文件

### 热部署

#### 开启部署

1. 导入依赖

   ~~~xml
   <dependency>
   <groupId>org.springframework.boot</groupId><artifactId>spring-boot-devtools</artifactId></dependency>
   ~~~

2. 重新编译（在IDEA中点击Build Project重新构建项目）

> 可以通过设置IDEA来自动重新编译热部署，而不需要每次手动重新构建项目

#### 热部署范围配置

1. 默认不触发重启的目录列表

   * /META-INF/maven
   * /META-INF/resources
   * /resources
   * /static
   * /public
   * /templates

2. 在springboot文件中配置热部署相关参数

   ~~~yaml
   devtools:
   	restart:
   		exclude: public/**,static/**
   ~~~

3. 设置高优先级属性禁用热部署

   ~~~java
   // 启动类
   public static void main(String[] args) {
   System,setProperty("spring.devtools.restart.enabled"，"false");SpringApplication.run(SSMPApplication.class);}
   ~~~

### 测试

#### 整合JUnit

* 导入测试对应的starter

* 测试类使用@SpringBootTest修饰

  ![image-20220224161459266](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220224161459266.png)

* 使用自动装配的形式添加要测试的对象

> 注意：
>
> * 测试类如果存在与引导类所在包或子包中无需指定引导类
> * 测试类如果不存在于引导类所在的包或子包中需要通过classes属性指定引导类

#### 测试配置

1. 加载测试专用属性（临时属性）

   ![image-20230528171344770](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281713010.png)

   ![image-20230528171404475](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281714883.png)

2. 加载测试专用配置（临时配置）

   ![image-20230528171655411](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281716301.png)

3. Web环境模拟测试

   ![image-20230528172201797](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281722173.png)

   ~~~java
   // 发送虚拟请求
   
   //创建web模拟环境
   @SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
   //开启虚拟mvc调用
   @AutoConfigureMockMvc
   class SpringbootConfigurationApplicationTests {
   
       @Test
       void contextLoads(@Autowired MockMvc mockMvc) throws Exception {
           RequestBuilder requestBuilder = MockMvcRequestBuilders.get("/users");
           mockMvc.perform(requestBuilder);
       }
   
   }
   
   ~~~

4. 数据层测试事务回滚：避免测试的脏数据污染数据库数据

   ![image-20230528174924593](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281749060.png)

5. 测试用例数据设定

   ![image-20230528175417549](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202305281754324.png)

### 数据层解决方案

1. 数据源配置（SpringBoot提供了3种内嵌的数据源对象供开发者选择）
   * HikariCP
   * Tomcat提供DataSource
   * CommonsDBCP
2. 内置持久化技术：jdbcTemplate
3. 数据库选用（SpringBoot提供了3种内嵌数据库供开发者选择，提高开发测试效率）
   * H2
   * HSQL
   * Derby

#### 整合MyBatis

1. 步骤

   > 1. 导入对应依赖（mybatis，数据库驱动）
   > 2. 配置数据源
   > 3. 设计数据表
   > 4. 编写实体类
   > 5. 编写对应Mapper接口与映射

#### 整合MyBatis-Plus

1. 步骤

   > 1. 导入对应依赖（mybatis-plus，数据库驱动）
   > 2. 配置数据源
   > 3. 设计数据表
   > 4. 编写实体类
   > 5. 编写对应Mapper接口与映射，继承BaseMapper

2. 业务层——快速开发

   > 使用MyBatisPlus提供有业务层通用接口 (ISerivce<T>) 与业务层通用实现类 (ServiceImpl<M,T>)
   >
   > 在通用类基础上做功能重载或功能追加
   > 注意重载时不要覆盖原始操作，避免原始提供的功能丢失

#### 整合Druid

#### 整合Redis

#### 整合MongoDB

#### 整合ES（Elasticsearch）

### 监控

1. 监控的意义

   * 监控服务状态
   * 监控服务运行指标（内存、虚拟机、线程、请求）
   * 监控日志
   * 管理服务

2. 监控实施方式

   * 显示监控信息的服务器:用于获取服务信息,并显示对应的信息
   * 运行的服务:启动时主动上报，告知监控服务器自己需要受到监控

3. 可视化监控平台

   * Spring Boot Admin,开源社区项目，用于管理和监控SpringBoot应用程序。客户端注册到服务端后，通过HTTP
     请求方式，服务端定期从客户端获取对应的信息，并通过UI界面展示对应信息。

     > https://github.com/codecentric/spring-boot-admin

4. 监控原理

   * Actuator提供了SpringBoot生产就绪功能，通过端点的配置与访问，获取端点信息
   * 端点描述了一组监控信息，SpringBoot提供了多个内置端点，也可以根据需要自定义端点信息
   * 访问当前应用所有端点信息: /actuator
   * 访问端点详细信息: /actuator/端 点名称

5. 自定义监控指标

#### Spring Boot Admin

项目地址：https://github.com/codecentric/spring-boot-admin

### 缓存

1. 缓存：一种介于数据永久存储介质与数据应用之间的数据临时存储介质

2. 作用：使用缓存可以有效的减少低速数据读取过程的次数(例如磁盘10)，提高系统性能

3. spring缓存使用

   * 引入依赖

     ~~~xml
             <dependency>
                 <groupId>org.springframework.boot</groupId>
                 <artifactId>spring-boot-starter-cache</artifactId>
             </dependency> 
     ~~~

   * 开启缓存功能

     ~~~java
     @SpringBootApplication
     //开启缓存功能
     @EnableCaching
     public class SpringBootCacheApplication {
         public static void main(String[] args) {
             SpringApplication.run(SpringBootCacheApplication.class,args);
         }
     }
     ~~~

   * 标注缓存

     ```java
     @Cacheable(value = "cacheSpace",key = "#id")
     public User getById(Long id) {
         return userMapper.selectById(id);
     }
     ```

4. SpringBoot提供的缓存技术除了提供默认的缓存方案，还可以对其他缓存技术进行整合，统一接口方便缓存技术的开发与管理

   * Generic
   * JCache
   * Ehcache
   * Hazelcast
   * Infinispan
   * Couchbase
   * Redis
   * Caffenine
   * Simple (默认)memcached

### 定时任务

1. 常见业务：

   * 年度报表
   * 缓存统计报告

2. JDK实现：java.util.Timer类和java.util.TimerTask类

3. 市面上流行的定时任务技术框架

   * Quartz
   * Spring Task

4. Cron表达式

   参考：https://zhuanlan.zhihu.com/p/437328366

   >  在线生成工具
   >
   > * https://cron.qqe2.com/
   > * https://www.pppet.net/

#### 整合Quartz

相关概念：

* 工作(Job) :用于定义具体执行的工作
* 工作明细(JobDetail) :用于描述定时工作相关的信息
* 触发器(Trigger) :用于描述触发工作的规则，通常使用cron表达式定义调度规则
* 调度器(Scheduler) :描述了工作明细与触发器的对应关系

1. 导入坐标

   ~~~xml
           <dependency>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-starter-quartz</artifactId>
           </dependency>
   ~~~

2. 定义具体工作，继承QuartzJobBean

   ~~~java
   public class MyQuartz extends QuartzJobBean {
       @Override
       protected void executeInternal(JobExecutionContext context) throws JobExecutionException {
           System.out.println("now is "+new SimpleDateFormat("yyyy年MM月dd日 HH:mm:ss").format(new Date(System.currentTimeMillis())));
       }
   }
   ~~~

3. 配置（定义工作明细与触发器，并绑定对应关系）

   ~~~java
   @Configuration
   public class QuartzConfig {
   
       @Bean
       public JobDetail printJobDetail(){
           // 绑定具体工作
           return JobBuilder.newJob(MyQuartz.class).storeDurably().build();
       }
   
       @Bean
       public Trigger printTrigger(){
           // 绑定对应工作明细
           return TriggerBuilder.newTrigger()
                   .forJob(printJobDetail())
                   .withSchedule(CronScheduleBuilder.cronSchedule("0/5 * * * * ?"))
                   .build();
       }
   }
   ~~~

#### Spring Task

1. 开启定时任务，在启动类中使用@EnableScheduling

   ~~~java
   @SpringBootApplication
   // 开启开启定时任务
   @EnableScheduling
   public class SpringbootTaskApplication {
   
       public static void main(String[] args) {
           SpringApplication.run(SpringbootTaskApplication.class, args);
       }
   
   }
   ~~~

2. 定义定时任务

   ~~~java
   @Component
   public class SpringTaskDemo {
       @Scheduled(cron = "* * * * * ?")
       public void print(){
           System.out.println("spring task is running.....");
       }
   }
   ~~~

3. 相关配置（application配置文件中）

   ~~~yml
   spring:
     task:
       scheduling:
         # 任务调度线程池大小，默认为1
         pool:
           size: 1
         # 调度线程名称前缀，默认scheduling
         thread-name-prefix: task_
         shutdown:
           # 线程池关闭时等待所有任务完成
           await-termination: false
           # 调度线程关闭前最大等待时间，确保最后一定关闭
           await-termination-period: 10s
   
   ~~~

### 消息

1. 消息类型
   * 同步消息
   * **异步消息**
2. 企业级应用中广泛使用的异步消息传递技术
   * JMS（Java Message Service）：一个规范，等同于JDBC规范，提供了与消息服务相关的API接口
     * JMS消息模型
       * peer-2-peer:点对点模型，消息发送到一个队列中，队列保存消息。队列的消息只能被-一个消费者消费，或超时
       * publish-subscribe:发布订阅模型，消息可以被多个消费者消费，生产者和消费者完全独立,不需要感知对方的存在
     * JMS消息种类
       * TextMessage
       * MapMessage
       * BytesMessage
       * StreamMessage
       * ObjectMessage
       * Message ( 只有消息头和属性)
     * JMS实现: ActiveMQ、 Redis、HornetMQ、 RabbitMQ、 RocketMQ (没有完全遵守JMS规范)
   * AMQP（ advanced message queuing protocol） ：一种种协议(高级消息队列协议，也是消息代理规范) ,规范了网络交换的数据格式，兼容jMS
     * 优点：具有跨平台性,服务器供应商，生产者，消费者可以使用不同的语言来实现
     * AMQP消息模型
       * direct exchange
       * fanout exchange
       * topic exchange
       * headers exchange
       * system exchange
     * 消息种类：byte[]
     * AMQP实现：RabbitMQ、 StormMQ、RocketMQ
   * MOTT（Message Queueing Telemetry Transport）：消息队列遥测传输，专为小设备设计，是物联网(I0T) 生态
     系统中主要成分之一

#### 整合ActiveMQ

#### 整合RabbitMQ

#### 整合RocketMQ

#### 整合Kafka

## 原理分析

### 自定义starter

Spring Boot大大简化了项目初始搭建以及开发过程，而这些都是通过Spring Boot提供的starter来完成的。

spring boot 在配置上相比spring要简单许多, 其核心在于spring-boot-starter, 在使用spring boot来搭建一个项目时, 只需要引入官方提供的starter, 就可以直接使用, 免去了各种配置。starter简单来讲就是引入了一些相关依赖和一些初始化的配置。starter坐标本身通常没有任何代码内容，其目的是在中央仓库维护环境依赖。

Spring官方提供了很多starter，第三方也可以定义starter。为了加以区分，starter从名称上进行了如下规范：

* Spring官方提供的starter名称为：spring-boot-starter-xxx，例如Spring官方提供的spring-boot-starter-web
* 第三方提供的starter名称为：xxx-spring-boot-starter，例如由mybatis提供的mybatis-spring-boot-starter

Spring Boot之所以能够帮我们简化项目的搭建和开发过程，主要是基于它提供的**起步依赖**和**自动配置**。

#### 起步依赖

将具备某种功能的坐标打包到一起，可以简化依赖导入的过程。例如，我们导入spring-boot-starter-web这个starter，则和web开发相关的jar包都一起导入到项目中了。

#### 自动配置

自动配置，就是无须手动配置xml，自动配置并管理bean，可以简化开发过程。

Spring Boot自动配置涉及到如下几个关键步骤：

* 基于Java代码的Bean配置
* 自动配置条件依赖
* Bean参数获取：创建配置文件并配置相关属性
* Bean的发现：通过**@EnableAutoConfiguration，借助**@**Import**的支持，收集和注册依赖包中相关的bean定义
* Bean的加载：通过上述自动配置注解从jar包中读取META-INF/spring.factories

##### Bean的加载方式和加载控制

1. bean的加载

   * xml

   * 注解方式

     * xml配置包扫描

       ~~~xml
       <context:component-scan base-package=""/>
       ~~~

     * @Component（@Controller、@Service、@Repository）标识自动以Bean、@Bean标识第三方Bean、@Import、@ImportResources

   * 使用上下文对象在容器初始化完毕后注入bean（Application.registerBean的方式）

   * 导入实现了ImportSelector接口的类，实现对导入源的编程式处理

   * 导入实现了ImportBeanDefinitionRegistrar接口的类，通过BeanDefinition的注册器注册实名bean,实现对容器中bean的裁定，例如对现有bean的覆盖，进而达成不修改源代码的情况下更换实现的效果

2. @Configuration的proxyBeanMethods属性

   ![image-20230623111707253](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202306231117946.png)

3. bean的控制

##### Bean的依赖属性配置

##### 自动配置原理

##### 变更自动配置

# 日志框架

参考：

* [java日志框架](https://www.bilibili.com/video/BV1iJ411H74S?p=1&vd_source=fabefd3fabfadb9324761989b55c26ea)&[搭配资料](https://pan.baidu.com/s/14D3xOqtRkRbA0_MQ1TWPwg?pwd=1902#list/path=%2Fsharelink3232509500-1047205714822206%2FJava%E6%97%A5%E5%BF%97%E7%83%AD%E9%97%A8%E6%A1%86%E6%9E%B6%2F%E8%B5%84%E6%96%99-Java%E6%97%A5%E5%BF%97&parentPath=%2Fsharelink3232509500-1047205714822206)

## 日志概述

1. 日志的概念
   * 日志文件：日志文件是用于记录系统操作事件的文件集合，可分为事件日志和消息日志。具有处理历史数据、诊断问题的追踪以及理解系统的活动等重要作用。
     * 调试日志
     * 系统日志
2. java的日志框架
   * 日志实现：日志门面的具体的实现。
     * 常见日志实现：JUL（java util logging）、logback、log4j、log4j2
   * 日志门面：为 Java 日志访问提供一套标准和规范的 API 框架，其主要意义在于提供接口。类似于JDBC的思想，将定义与实现进行分离。
     * 常见日志门面：JCL（Jakarta Commons Logging）、Slf4j（Simple Logging  Facade fo java）、jboss-logging
3. 日志发展历史：log4j ->JUL-->JCL--> sIf4j --> logback -> log4j2

## JUL

参考：

* https://blog.csdn.net/weixin_43472934/article/details/122024844

* https://docs.oracle.com/javase/8/docs/api/ 

 JUL全称Java util Logging是java原生的日志框架，使用时不需要另外引用第三方类库,相对其他日志框架使用方便，学习简单，能够在小型应用中灵活使用。

1. 架构

   ![image-20230203203450628](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302032034663.png)

   * Loggers：被称为记录器，应用程序通过获取Logger对象，调用其API来来发布日志信息。Logger通常时应用程序访问日志系统的入口程序。
   * Appenders：也被称为Handlers，每个Logger都会关联一组Handlers，Logger会将日志交给关联Handlers处理，由Handlers负责将日志做记录。Handlers在此是一个抽象，其具体的实现决定了日志记录的位置可以是控制台、文件、网络上的其他日志服务或操作系统日志等。
   * Layouts：也被称为Formatters，它负责对日志事件中的数据进行转换和格式化。Layouts决定了数据在一条日志记录中的最终形式。
   * Level：每条日志消息都有一个关联的日志级别。该级别粗略指导了日志消息的重要性和紧迫，我可以将Level和Loggers、Appenders做关联以便于我们过滤消息。
   * Filters：过滤器，根据需要定制哪些信息会被记录，哪些信息会被放过。

2. 快速入门

   ~~~java
   package org.example;
    import org.junit.Test;
   
      import java.io.IOException;
      import java.util.logging.*;
   
      /**
       * Hello world!
       * @author chenwenjian
       */
      public class JulDemo1
      {
          Logger logger = Logger.getLogger("org.example.JulDemo1");
           @Test
      public void quickStart()
      {
          logger.info("这是一个info信息");
          logger.log(Level.INFO,"这是使用logger的log方法输出的info信息");
   
          String name = "chen wen jian";
          int age = 22;
          logger.log(Level.INFO,"用户信息：{0},{1}",new Object[]{name,age});
      }
   
      @Test
      public void testLoggerLevel(){
          logger.severe("severe");
          logger.warning("warning");
          logger.info("info");
          logger.config("config");
          logger.fine("fine");
          logger.finer("finer");
          logger.finest("finest");
      }
   
      @Test
      public void testLoggerConfig() throws IOException {
          //关闭默认配置
          logger.setUseParentHandlers(false);
   
          //自定义配置日志级别
          //创建ConsoleHandle对象
          ConsoleHandler consoleHandler = new ConsoleHandler();
          SimpleFormatter simpleFormatter = new SimpleFormatter();
   
          //进行关联
          consoleHandler.setFormatter(simpleFormatter);
          logger.addHandler(consoleHandler);
   
          logger.setLevel(Level.ALL);
          consoleHandler.setLevel(Level.ALL);
   
          FileHandler fileHandler = new FileHandler("D:/hp/IntelliJIDEAProjects/LoggingDemo/JULDemo/logs/jul.log", true);
          fileHandler.setFormatter(simpleFormatter);
          fileHandler.setLevel(Level.ALL);
          logger.addHandler(fileHandler);
   
          logger.severe("severe");
          logger.warning("warning");
          logger.info("info");
          logger.config("config");
          logger.fine("fine");
          logger.finer("finer");
          logger.finest("finest");
      }
   ~~~
   
3. jul日志级别

   java.util.logging.Level中定义了日志的级别：

   * SEVERE（最高值）
   * WARNING
   * INFO （默认级别）
   * CONFIG
   * FINE
   * FINER
   * FINEST（最低值）

   > 还有两个特殊的级别：
   > OFF，可用来关闭日志记录。
   > ALL，启用所有消息的日志记录。

4. 自定义日志配置

   ~~~java
   @Test
   public void testLogConfig() throws Exception {
   // 1.创建日志记录器对象
   Logger logger = Logger.getLogger("com.itheima.log.JULTest");
   // 一、自定义日志级别
   // a.关闭系统默认配置
   logger.setUseParentHandlers(false);
   // b.创建handler对象
   ConsoleHandler consoleHandler = new ConsoleHandler();
   // c.创建formatter对象
   SimpleFormatter simpleFormatter = new SimpleFormatter();
   // d.进行关联
   consoleHandler.setFormatter(simpleFormatter);
   logger.addHandler(consoleHandler);
   // e.设置日志级别
   logger.setLevel(Level.ALL);
   consoleHandler.setLevel(Level.ALL);
   // 二、输出到日志文件
   FileHandler fileHandler = new FileHandler("d:/logs/jul.log");
   fileHandler.setFormatter(simpleFormatter);
   3.3 Logger之间的父子关系
   JUL中Logger之间存在父子关系，这种父子关系通过树状结构存储，JUL在初始化时会创建一个顶层
   RootLogger作为所有Logger父Logger，存储上作为树状结构的根节点。并父子关系通过路径来关联。
   logger.addHandler(fileHandler);
   // 2.日志记录输出
   logger.severe("severe");
   logger.warning("warning");
   logger.info("info");
   logger.config("config");
   logger.fine("fine");
   logger.finer("finer");
   logger.finest("finest");
   }
   ~~~

   JUL在初始化时会创建一个顶层RootLogger作为所有Logger父Logger，存储上作为树状结构的根节点。并通过路径来关联所有Logger的父子关系。

   默认配置文件路径$JAVAHOME\jre\lib\logging.properties

5. 日志处理流程

   * 初始化LogManager：LogManager加载logging.properties配置，添加Logger到LogManager
   * 从单例LogManager获取Logger
   * 设置级别Level，并指定日志记录LogRecord
   * Filter提供了日志级别之外更细粒度的控制
   * Handler是用来处理日志输出位置
   * Formatter是用来格式化LogRecord的

   ![image-20230712230348170](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202307122303191.png)

## Slf4j

官网：https://www.slf4j.org/

### 概述

1. Slf4j：简单日志门面(Simple Logging Facade For Java) SLF4J主要是为了给Java日志访问提供一套标准、规范的API框架，其主要意义在于提供接口，具体的实现可以交由其他日志框架，例如log4j和logback等。当然slf4j自己也提供了功能较为简单的实现，但是一般很少用到。对于一般的Java项目而言，日志框架会选择slf4j-api作为门面，配上具体的实现框架（log4j、logback等），中间使用桥接器完成桥接。
2. 主要功能
   * 日志框架的绑定
   * 日志框架的桥接

### Slf4j简单内置实现

1. 导入依赖

   ~~~xml
       <!--Slf4j日志门面-->
       <dependency>
         <groupId>org.slf4j</groupId>
         <artifactId>slf4j-api</artifactId>
         <version>2.0.4</version>
       </dependency>
   
       <!--Slf4j简单内置实现-->
       <dependency>
         <groupId>org.slf4j</groupId>
         <artifactId>slf4j-simple</artifactId>
         <version>2.0.4</version>
       </dependency>
   ~~~

2. 使用示例

   ~~~java
   package org.example;
   
   import org.slf4j.Logger;
   import org.slf4j.LoggerFactory;
   
   /**
    * 简单内置实现测试
    * @author chenwenjian
    */
   public class Slf4jTest01
   {
       public static final Logger LOGGER = LoggerFactory.getLogger(Slf4jTest01.class);
   
       public static void main( String[] args ) {
           LOGGER.info("info level............");
           String name = "chenwenjian";
           Integer age = 22;
           LOGGER.info("用户信息：{},{}",name,age);
       }
   }
   ~~~

### 绑定日志实现

![image-20230415165537188](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202304151655635.png)

 在项目中添加slf4j依赖后就可以在项目中使用slf4j的API在项目中进行统一的日志记录。然后绑定具体的实现就可以了（若具体日志框架没有直接实现slf4j，则需要引入相应的适配器）。slf4j有且仅有一个日志实现框架的绑定（如果出现多个默认使用第一个依赖日志实现）。

### 桥接日志框架

![image-20230712233451286](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202307122334844.png)

## logback

官网：https://logback.qos.ch/index.html

1. 概述

   Logback是由log4j创始人设计的另一个开源日志组件，性能比log4j要好。

2. 主要模块

   * logback-core：其它两个模块的基础模块
   * logback-classic：它是log4j的一个改良版本，同时它完整实现了slf4j API
   * logback-access：访问模块与Servlet容器集成提供通过Http来访问日志的功能

3. 快速使用

   导入依赖：

   ~~~xml
   <dependency>
   <groupId>org.slf4j</groupId>
   <artifactId>slf4j-api</artifactId>
   <version>1.7.25</version>
   </dependency>
   <dependency>
   <groupId>ch.qos.logback</groupId>
   <artifactId>logback-classic</artifactId>
   <version>1.2.3</version>
   </dependency>
   ~~~

   配置相关信息，如日志类型，级别等。logback会依次读取以下名字和类型配置文件：

   * 类路径下logback-test.xml
   * 类路径下logback.groovy
   * 类路径下logback.xml 
   * 类路径下寻找文件META-INFO/services/ch.qos.logback.classic.spi.Configurator，该文件的内容为实现了Configurator接口的实现类的全限定类名
   * 如果以上都没有成功，logback会通过BasicConfigurator为自己进行配置（即采用默认配置），并且日志将会全部在控制台打印出来

4. 三类组件：

   * Logger：日志的记录器，把它关联到应用的对应的context后，主要用于存放日志对象，也可以定义日志类型、级别。各个logger 都被关联到一个 LoggerContext，LoggerContext负责制造logger，也负责以树结构排列各 logger。一个 Logger 被当作为一个实体，它们的命名是大小写敏感的，并且遵循以下规则：

     如果一个logger的名字加上一个.作为另一个logger名字的前缀，那么该logger就是另一个logger的祖先。如果一个logger与另一个logger之间没有其它的logger，则该logger就是另一个logger的父级。

     > 举例：
     > 名为cn.itcast的logger是名为cn.itcast.service的logger的父级
     > 名为cn的logger是名为cn.itcast的logger的父级，是名为cn.itcast.service的logger的祖先

     在logback中有一个root logger，它是logger层次结构的最高层，它是一个特殊的logger，因为它是每一个层次结构的一部分。

   * Appender：用于指定日志输出的目的地，目的地可以是控制台、文件、数据库等等。

   * Layout：负责把事件转换成字符串，格式化的日志信息的输出。在logback中Layout对象被封装在encoder中。

5. 日志输出等级

   logback的日志输出等级分为：TRACE, DEBUG, INFO, WARN, ERROR。

   如果一个给定的logger没有指定一个日志输出等级，那么它就会继承离它最近的一个祖先的层级。

   为了确保所有的logger都有一个日志输出等级，root logger会有一个默认输出等级 --- DEBUG。

6. springboot集成logback

   * 依赖引入

   * 在Resource目录下编写logback配置文件

     ```xml
     <?xml version="1.0" encoding="UTF-8"?>
     <included>
         <contextName>logback</contextName>
         <!-- 
     		name的值是变量的名称，value的值时变量定义的值
     		定义变量后，可以使“${}”来使用变量
     	-->
         <property name="log.path" value="d:\\logs" />
     <!-- 彩色日志 -->
     <!-- 彩色日志依赖的渲染类 -->
     <conversionRule 
               conversionWord="clr" 
               converterClass="org.springframework.boot.logging.logback.ColorConverter" />
     <conversionRule 
               conversionWord="wex" converterClass="org.springframework.boot.logging.logback.WhitespaceThrowableProxyConverter" />
     <conversionRule conversionWord="wEx" converterClass="org.springframework.boot.logging.logback.ExtendedWhitespaceThrowableProxyConverter" />
     <!-- 彩色日志格式 -->
     <property name="CONSOLE_LOG_PATTERN" value="${CONSOLE_LOG_PATTERN:-%clr(%d{yyyy-MM-dd HH:mm:ss.SSS}){faint} %clr(${LOG_LEVEL_PATTERN:-%5p}) %clr(${PID:- }){magenta} %clr(---){faint} %clr([%15.15t]){faint} %clr(%-40.40logger{39}){cyan} %clr(:){faint} %m%n${LOG_EXCEPTION_CONVERSION_WORD:-%wEx}}"/>
     
     <!--输出到控制台-->
     <appender name="LOG_CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
         <encoder>
             <Pattern>${CONSOLE_LOG_PATTERN}</Pattern>
             <!-- 设置字符集 -->
             <charset>UTF-8</charset>
         </encoder>
     </appender>
     
     <!--输出到文件-->
     <appender name="LOG_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
         <!-- 正在记录的日志文件的路径及文件名 -->
         <file>${log.path}/logback.log</file>
         <!--日志文件输出格式-->
         <encoder>
             <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{50} - %msg%n</pattern>
             <charset>UTF-8</charset>
         </encoder>
         <!-- 日志记录器的滚动策略，按日期，按大小记录 -->
         <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
             <!-- 每天日志归档路径以及格式 -->
             <fileNamePattern>${log.path}/info/log-info-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
             <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                 <maxFileSize>100MB</maxFileSize>
             </timeBasedFileNamingAndTriggeringPolicy>
             <!--日志文件保留天数-->
             <maxHistory>15</maxHistory>
         </rollingPolicy>
     </appender>
     ```
     ~~~xml
     <?xml version="1.0" encoding="UTF-8"?>
     <configuration>
         <!--引入其他配置文件-->
         <include resource="logback-base.xml" />
         <!--
         <logger>用来设置某一个包或者具体的某一个类的日志打印级别、
         以及指定<appender>。<logger>仅有一个name属性，
         一个可选的level和一个可选的addtivity属性。
         name:用来指定受此logger约束的某一个包或者具体的某一个类。
         level:用来设置打印级别，大小写无关：TRACE, DEBUG, INFO, WARN, ERROR, ALL 和 OFF，
               如果未设置此属性，那么当前logger将会继承上级的级别。
         addtivity:是否向上级logger传递打印信息。默认是true。
          -->
     
         <!--开发环境-->
         <springProfile name="dev">
             <logger name="cn.itcast.controller" additivity="false" level="debug">
                 <appender-ref ref="LOG_CONSOLE"/>
             </logger>
         </springProfile>
         <!--生产环境-->
         <springProfile name="pro">
             <logger name="cn.itcast.controller" additivity="false" level="info">
                 <appender-ref ref="LOG_FILE"/>
             </logger>
         </springProfile>
     
         <!--
         root节点是必选节点，用来指定最基础的日志输出级别，只有一个level属性
         level:设置打印级别，大小写无关：TRACE, DEBUG, INFO, WARN, ERROR, ALL 和 OFF 默认是DEBUG
         可以包含零个或多个元素，标识这个appender将会添加到这个logger。
         -->
         <root level="info">
             <appender-ref ref="LOG_CONSOLE" />
             <appender-ref ref="LOG_FILE" />
         </root>
     </configuration>
     ~~~

   * 编写application.yml配置文件

     ~~~yml
     server:
       port: 9000
     logging:
       #在Spring Boot项目中默认加载类路径下的logback-spring.xml文件
       config: classpath:logback-spring.xml
     spring:
       profiles:
         active: dev
     ~~~

## lombok日志简化

参考：

* [【lombok】Lombok详解(日志记录和简化代码)](https://blog.csdn.net/twotwo22222/article/details/128609038)

# 测试框架

参考：[通义灵码单元测试实践__智能编码助手_AI编程_智能编码助手通义灵码(Lingma)-阿里云帮助中心](https://help.aliyun.com/zh/lingma/use-cases/unit-test-practice-of-tongyi-lingma?scm=20140722.S_help%40%40文档%40%402849258.S_BB2%40bl%2BRQW%40ag0%2BBB1%40ag0%2Bos0.ID_2849258-RL_cont-LOC_doc~UND~ab-OR_ser-V_4-P0_0&spm=a2c4g.11186623.0.i2)

## 基本概念

1. 测试分类
   * 黑盒测试
   * 白盒测试
2. 测试驱动开发（TDD）
3. 行为驱动开发（BDD）
4. 常用的java测试框架
   * JUnit：Java 最流行的单元测试框架，支持编写和执行单元测试用例。
   * TestNG：另一个常用的测试框架，提供更多的功能，如测试分组、参数化测试等。
   * Mockito：用于创建和管理模拟对象，以进行依赖的模拟和注入。

## Junit

参考

* 官方文档：[JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/)

主要内容：

- 如何编写 JUnit 测试用例，包括使用注解和断言。
- 了解 JUnit 的生命周期和运行机制。
- 掌握 JUnit 的高级功能，如参数化测试、异常测试、测试套件等。

### 基本使用

### 生命周期与运行机制

### 参数化测试

### 异常测试

### 测试套件

1. Junit使用（白盒测试）

   步骤：

   * 定义一个测试类
   * 定义测试方法
   * 给方法添加@Test
   * 导入Junit依赖环境

2. 补充：

   * @Before：修饰的方法会在测试方法之前被自动执行
   * @After：修饰的方法会在测试方法执行之后自动执行

## TestNG

TestNG官方文档：https://testng.org/doc/

## Mockito

# API框架

## Swagger/OpenApi

官网：

* https://swagger.io/
* [Home 2024 - OpenAPI Initiative (openapis.org)](https://www.openapis.org/)
* [GitHub - OpenAPITools/openapi-generator: OpenAPI Generator allows generation of API client libraries (SDK generation), server stubs, documentation and configuration automatically given an OpenAPI Spec (v2, v3)](https://github.com/OpenAPITools/openapi-generator)

参考文章：

* https://blog.csdn.net/YR_112233/article/details/122630446
* https://blog.csdn.net/weixin_46645338/article/details/123895447
* [SpringBoot集成Swagger3.0（详细）](https://www.cnblogs.com/antLaddie/p/17418078.html)
* [OpenAPI 规范 | OpenAPI 官方文档中文版 (xiniushu.com)](https://openapi.xiniushu.com/)

### 简介

1. 简介

   Swagger 是一个 RESTful API 的开源框架，它的主要目的是帮助开发者设计、构建、文档化和测试 Web API。Swagger 的核心思想是通过定义和描述 API 的规范、结构和交互方式，以提高 API 的可读性、可靠性和易用性，同时降低 API 开发的难度和开发者之间的沟通成本。

2. 作用
   * 接口文档在线自动生成
   * 功能测试

3. 主要项目
   * Swagger-tools:提供各种与Swagger进行集成和交互的工具。例如模式检验、Swagger 1.2文档转换成Swagger 2.0文档等功能。
   * Swagger-core: 用于Java/Scala的的Swagger实现。与JAX-RS(Jersey、Resteasy、CXF…)、Servlets和Play框架进行集成。
   * Swagger-js: 用于JavaScript的Swagger实现。
   * Swagger-node-express: Swagger模块，用于node.js的Express web应用框架。
   * Swagger-ui：一个无依赖的HTML、JS和CSS集合，可以为Swagger兼容API动态生成优雅文档。
   * Swagger-codegen：一个模板驱动引擎，通过分析用户Swagger资源声明以各种语言生成客户端代码。

4. OpenAPI（OpenAPI Specification）
   * 最初由开发Swagger的团队在2010年推出，从Swagger 2.0开始，Swagger规范被正式更名为OpenAPI规范，是REST API的API描述格式，为REST API定义了一个与语言无关的标准接口
   * OpenAPI规范可以使用YAML或JSON格式进行编写

5. Swagger发展史

   Swagger它最初由Tony Tam在2011年创建，并在之后被SmartBear Software公司收购。在过去几年中，Swagger经历了许多重大的更新和变化，其发展史大概可以分为以下几个阶段：

   * Swagger 1.x 阶段（2011-2014年）

     Swagger最初是一个简单的API文档生成工具，通过对JAX-RS和Jersey注解的支持自动生成API文档，使得API文档的维护变得更加容易。在这个阶段，Swagger还没有完全成熟，只能支持基本的API描述和文档生成。

   * Swagger 2.x 阶段（2014-2017年）
     在Swagger 2.x阶段，Swagger发生了重大变化。它不再仅仅是一个文档生成工具，而是一个完整的API开发和管理平台。Swagger 2.x加入了强大的注解支持，可以描述API的细节信息，如请求参数、返回类型等，以及定义RESTful API的元数据，如API描述、标签等。此外，Swagger 2.x还引入了OpenAPI规范，在API定义方面有了更严格的标准和规则。

   * OpenAPI 阶段（2017-至今）（也被称为Swagger 3.x）
     在2017年，Swagger 2.x的规范成为了Linux基金会旗下的OpenAPI规范。这标志着Swagger从一款工具演变成为了一个开放且标准的API定义框架。OpenAPI规范不仅继承了Swagger 2.x的特性，还提供了更加全面和严格的API定义规范，并且扩展了对非RESTful API的支持

   除了上述几个主要阶段之外，还有一些其他重要的事件和版本，如Swagger UI、Swagger Codegen、SwaggerHub等等。这些工具和服务进一步扩展了Swagger的功能，使其成为了一个更加完整、强大和易于使用的API定义和管理平台。

### SpringBoot集成Swagger（swagger3.0）

### SpringFox

参考：https://blog.csdn.net/weixin_46645338/article/details/123895447

为了简化swagger的使用，Spring框架对swagger进行了整合，建立了Spring-swagger项目，后面改成了现在的Springfox。通过在项目中引入Springfox，可以扫描相关的代码，生成描述文件，进而生成与代码一致的接口文档和客户端代码。

Springfox是一套可以帮助Java开发者自动生成API文档的工具，它是基于Swagger 2.x基础上开发的。Swagger已经成为了RESTful API文档生态系统的事实标准，而**Springfox是一个用于集成Swagger2.x到Spring应用程序中的库**。而且Springfox**提供了一些注解**来描述API接口、参数和返回值，并根据这些信息**生成Swagger UI界面**，从而方便其他开发人员查看和使用您的API接口。此外，Springfox还支持自动生成API文档和代码片段，简化了开发人员的工作量。除了集成Swagger 2.x，Springfox还提供了一些额外功能，例如自定义Swagger文档、API版本控制、请求验证等等。这些功能使得Springfox可以胜任各种类型和规模的应用程序，同时还可以提高代码质量和开发效率。

maven依赖：

```xml
	<dependency>
        <groupId>io.springfox</groupId>
        <artifactId>springfox-boot-starter</artifactId>
        <version>3.0.0</version>
    </dependency>
```
> 随着时间的推移，Swagger2.x终究成为历史，springfox-boot-starter的坐标从3.0.0版本（2020年7月14日）开始就一直没有更新；也得注意的是springfox-swagger2坐标和springfox-boot-start是一样的，但springfox-boot-start只有3.0.0版本。因此不推荐你使用springfox

配置：

```java
package com.example.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.oas.annotations.EnableOpenApi;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;

/**
 * @author whyme-chen
 * @date 2022/4/28 11:02
 */
@EnableOpenApi
@Configuration
public class SwaggerConfiguration {
    /**
     *创建Docket对象，并交给Spring容器管理
     *
     * @return Docket对象：是Swagger中的全局配置
     */
    @Bean
    public Docket docket(){
        return new Docket(DocumentationType.OAS_30)
                .apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.controller"))//设定扫描包
                .paths(PathSelectors.any())
                .build();
    }

    /**
     *
     * @return Api帮助文档的描述信息
     */
    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .contact(new Contact(
                        "whyme-chen",//文档发布者的名称
                        "http://localhot:8080",//文档发布者的网站
                        "2710335790@qq.com"//文档发布者的邮箱
                ))
                .title("Swagger学习帮助文档")
                .description("Swagger学习帮助文档........")
                .version("1.0")
                .build();
    }
}
```

### SpringDoc（推荐）

springdoc-openapi

* 官网：https://springdoc.org/
* Github仓库：https://github.com/springdoc/springdoc-openapi
* Maven仓库：https://mvnrepository.com/artifact/org.springdoc/springdoc-openapi-ui

SpringDoc除了可以生成Swagger UI风格的接口文档，还提供了ReDoc的文档渲染方式，可以自动注入OpenAPI规范的JSON描述文件，支持OAuth2、JWT等认证机制，并且**支持全新的OpenAPI 3.0规范**。

> SpringDoc是基于OpenAPI 3.0规范构建的，因此推荐在Spring Boot 2.4及以上版本中使用springdoc-openapi-ui库来集成Swagger3.x。在这些版本中，springdoc-openapi-ui库已被广泛应用，并且得到了社区的大力支持和推广。而在Spring Boot 2.3及其以下版本，可以使用springfox-boot-starter库来集成Swagger2.x。

坐标依赖：

~~~xml
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-ui</artifactId>
    <version>1.7.0</version>
</dependency>
~~~

> 说明：上面的坐标内部导入了Swagger3.0的原生依赖（我们只需要在SpringBoot导入springdoc-openapi-ui即可）
>     ①：io.swagger.core.v3:swagger-core:2.2.9
>         Swagger Core是Swagger 3.x规范的核心实现，提供了一组Java API，用于生成和处理OpenAPI规范文件。
>         它包括Swagger的核心功能，例如Model、Schema、Parameter、Response等，是构建Swagger API的必要条件。
>     ②：io.swagger.core.v3:swagger-annotations:2.2.9
>         Swagger Annotations是一个用于编写Swagger API文档的Java注解库，提供了一组注解，用于描述API元数据。
>         例如，@Operation、@Parameter、@ApiResponse等注解基本包含了OpenAPI规范中的所有元素。
>     ③：io.swagger.core.v3:swagger-models:2.2.9
>         Swagger Models是Swagger 3.x规范的Java模型库，提供了一组Java模型类，用于表示OpenAPI规范文件。
>         它包含了OpenAPI规范中的所有数据模型，例如PathItem、Operation、Parameter、Components等。

### 常用注解

swagger2.0常用注解如下：

![img](https://img2020.cnblogs.com/blog/2088791/202112/2088791-20211229104433596-25349310.png)

OpenAPI3.0（Swagger3.0）常用注解：

| 注解                   | 说明                                              |
| ---------------------- | ------------------------------------------------- |
| `@OpenAPIDefinition`   | 定义全局的OpenAPI文档信息，包括标题、描述、版本等 |
| `@Info`                | 定义API文档的标题、描述、版本等                   |
| `@Server`              | 定义服务端的URL和描述                             |
| `@Paths`               | 定义多个API路径以及对应的操作                     |
| `@Operation`           | 定义一个操作，包括HTTP方法、摘要、描述等          |
| `@Parameter`           | 定义请求参数，包括名称、位置、类型、描述等        |
| `@RequestBody`         | 定义请求体的内容和描述                            |
| `@ApiResponse`         | 定义操作的响应，包括状态码、描述、返回类型等      |
| `@Schema`              | 定义数据模型，包括属性、类型、格式等              |
| `@Example`             | 定义示例值                                        |
| `@Tag`                 | 定义API标签，用于分组和组织API                    |
| `@SecurityScheme`      | 定义安全方案，如OAuth2、ApiKey等                  |
| `@SecurityRequirement` | 定义操作所需的安全要求                            |
| `@Extension`           | 定义扩展属性，可在OpenAPI规范中添加自定义属性     |

## knife4j

knife4j是为Java MVC框架集成Swagger生成Api文档的增强解决方案,前身是swagger-bootstrap-ui,取名knife4j是希望它能像一把匕首一样小巧,轻量,并且功能强悍。其底层是对Springfox的封装，使用方式也和Springfox一致，只是对接口文档UI进行了优化。

1. 核心功能
   - **文档说明**：根据Swagger的规范说明，详细列出接口文档的说明，包括接口地址、类型、请求示例、请求参数、响应示例、响应参数、响应码等信息，对该接口的使用情况一目了然。

   - **在线调试**：提供在线接口联调的强大功能，自动解析当前接口参数,同时包含表单验证，调用参数可返回接口响应内容、headers、响应时间、响应状态码等信息，帮助开发者在线调试。

# 工具

## Maven

> Maven相关内容具体参考：[BuildTools](./BuildTools.md)

## Gradle

> Gradle相关内容具体参考：[BuildTools](./BuildTools.md)

## IDEA

> 具体参考：[IDE](./IDE.md)

## Git&Github

参考链接：

* https://www.cnblogs.com/syp172654682/p/7689328.html
* https://hx.dcloud.net.cn/Tutorial/SourceControl/Git/README
* https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%AE%80%E4%BB%8B
* https://zhuanlan.zhihu.com/p/648287897

### 版本控制

版本控制（Revision control）是一种在开发的过程中用于管理我们对文件、目录或工程等内容的修改历史，方便查看更改历史记录，备份以便恢复以前的版本的软件工程技术。

#### 功能

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

> **git和SVN的最主要区别**
>
> SVN是集中式版本控制系统，版本库是集中放在中央服务器的，而工作的时候，用的都是自己的电脑，所以首先要从中央服务器得到最新的版本，然后工作，完成工作后，需要把自己做完的活推送到中央服务器。集中式版本控制系统是必须联网才能工作，对网络带宽要求较高。
>
> Git是分布式版本控制系统，没有中央服务器，每个人的电脑就是一个完整的版本库，工作的时候不需要联网了，因为版本都在自己电脑上。协同的方法是这样的：比如说自己在电脑上改了文件A，其他人也在电脑上改了文件A，这时，你们两之间只需把各自的修改推送给对方，就可以互相看到对方的修改了。

#### 版本控制分类

* 本地版本控制
* 集中版本控制
* 分布式版本控制

### git安装与配置

官网：https://git-scm.com/

源码：https://github.com/git/git/

### 常用的Linux命令（bash基本操作命令）

> 1. cd 进入一个目录
> 2. cd.. 退出一个目录
> 3. pwd 显示当前所在目录
> 4. ls 列出当前目录下的所有文件
> 5. touch 新建一个文件
> 6. rm 删除一个文件    rm -r 删除一个文件夹
> 7. mkdir 创建一个目录
> 8. mv 移动文件
> 9. reset 重新初始化终端/清屏
> 10. clear 清屏
> 11. history 查看命令历史
> 12. help 帮助
> 13. exit 退出
> 14. \# 表示注释

### 配置-git config

1. 查看配置
   
   * git config -l：查看当前git环境详细配置
   
   * 查看不同级别的配置文件
     
     > * git config --system --list：查看系统配置
     > * git config ---global --list：查看当前用户配置
     > * git config --local --list：查看当前仓库配置

2. git配置文件
   
   > 在Windows系统中，Git在$HOME目录中查找.gitconfig文件（一般位于C:\Documents and Settings\$USER下）
   > 
   > **Git相关的配置文件有三个：**
   > 
   > 1）、 /etc/gitconfig：包含了适用于系统所有用户和所有项目的值。(Win：C:\Program Files\Git\mingw64\etc\gitconfig) --system 系统级
   > 
   > ![img](https://images2017.cnblogs.com/blog/63651/201709/63651-20170905155620835-541203307.png)
   > 
   > 2）、~/.gitconfig：只适用于当前登录用户的配置。(Win：C:\Users\Administrator\.gitconfig)  --global 全局
   > 
   > ![img](https://images2017.cnblogs.com/blog/63651/201709/63651-20170905112611116-974195699.png)
   > 
   > 3）、位于git项目目录中的.git/config：适用于特定git项目的配置。(Win：C:\gitProject) --local当前项目
   > 
   > 注意：对于同一配置项，三个配置文件的优先级是1<2<3
   > 
   > 这里可以直接编辑配置文件，通过命令设置后会响应到这里。

3. 配置用户名与邮箱
   
   > * 项目级别/仓库级别：仅在当前本地库范围有效
   >   
   >   * git config user.name 用户名
   >   * git config user.email 邮箱名
   > 
   > * 系统用户级别：登录当前操作系统的用户范围
   >   
   >   * git config --global user.name 用户名
   >   * git config --global user.email 邮箱名
   > 
   > * 注意：信息保存在.git/config中

4. 添加或删除配置
   
   > * 添加配置项
   >   
   >   git config [--local|--global|--system]  section.key value
   >   [--local|--global|--system]  #可选的，对应本地，全局，系统不同级别的设置
   >   section.key #区域下的键
   >   value #对应的值
   > 
   > * 删除配置项
   >   
   >   git config [--local|--global|--system] --unset section.key

5. 其他配置
   
   > git config --global color.ui true   #打开所有的默认终端着色
   > git config --global alias.ci commit   #别名 ci 是commit的别名
   > [alias]  
   > co = checkout  
   > ci = commit  
   > st = status  
   > pl = pull  
   > ps = push  
   > dt = difftool  
   > l = log --stat  
   > cp = cherry-pick  
   > ca = commit -a  
   > b = branch 
   > 
   > user.name  #用户名
   > user.email  #邮箱
   > core.editor  #文本编辑器  
   > merge.tool  #差异分析工具  
   > core.paper "less -N"  #配置显示方式  
   > color.diff true  #diff颜色配置  
   > alias.co checkout  #设置别名
   > git config user.name  #获得用户名
   > git config core.filemode false  #忽略修改权限的文件

6. 解决gitbash乱码问题
   
   > * git config --global core.quotepath false
   > 
   > * ${git_home}/etc/bash.bashrc文件最后两行加入
   >   
   >   export LANG=''zh_CN.UTF-8'
   >   
   >   export LC_ALL=''zh_CN.UTF-8'

### git结构和基本原理

![image-20211121161141743](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211121161141743.png)

git管理的文件有三种状态：已修改（modified）,已暂存（staged）,已提交(committed)

![img](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/63651-20170905201033647-1915833066.png)

![img](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/63651-20170909091456335-1787774607.jpg)

![img](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/201751509379751.png)

### 常用操作（本地）
1. 本地库初始化
   * git init：现有目录创建仓库 
   * git clone 【url】;从远程库克隆
2. 基本操作

![image-20211121163820648](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211121163820648.png)

* 查看工作区、暂存区状态：git status（可以git status -s或git status --short用于查看简化后的信息）

* 查看暂存区与工作区具体修改内容：git diff
  
  > #比较暂存区的文件与之前已经提交过的文件
  > 
  > git diff --cached
  > 
  > #比较repo与工作空间中的文件差异
  > 
  > git diff HEAD~n
  > 
  > ![img](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/63651-20170914095506203-2063795525.png)

* 将工作区的新建/修改添加到暂存区：git add 【file name】或者使用git add .

* git clean [options]：移除所有未跟踪文件，一般会加上参数-df，-d表示包含目录，-f表示强制清除

* git mv <oldName> <newName>：给文件改名

* git checkout
  
  > * 当执行 “git checkout .” 或者 “git checkout — <file>” 命令时，会用暂存区全部或指定的文件替换工作区的文件。这个操作很危险，会清除工作区中未添加到暂存区的改动。
  > * 当执行 “git checkout HEAD .” 或者 “git checkout HEAD <file>” 命令时，会用 HEAD 指向的 master 分支中的全部或者部分文件替换暂存区和以及工作区中的文件。这个命令也是极具危险性的，因为不但会清除工作区中未提交的改动，也会清除暂存区中未提交的改 动。
  > 
  > $ git checkout branch
  > #检出branch分支。要完成图中的三个步骤，更新HEAD以指向branch分支，以及用branch  指向的树更新暂存区和工作区。
  > 
  > $ git checkout
  > #汇总显示工作区、暂存区与HEAD的差异。
  > 
  > $ git checkout HEAD
  > #同上
  > 
  > $ git checkout -- filename
  > #用暂存区中filename文件来覆盖工作区中的filename文件。相当于取消自上次执行git add filename以来（如果执行过）的本地修改。
  > 
  > $ git checkout branch -- filename
  > #维持HEAD的指向不变。用branch所指向的提交中filename替换暂存区和工作区中相   应的文件。注意会将暂存区和工作区中的filename文件直接覆盖。
  > 
  > $ git checkout -- . 或写作 git checkout .
  > #注意git checkout 命令后的参数为一个点（“.”）。这条命令最危险！会取消所有本地的  #修改（相对于暂存区）。相当于用暂存区的所有文件直接覆盖本地文件，不给用户任何确认的机会！
  > 
  > $ git checkout commit_id -- file_name
  > #如果不加commit_id，那么git checkout -- file_name 表示恢复文件到本地版本库中最新的状态。

* 提交操作
  
  * 提交到本地仓库：git commit -m "commit message " 【file name】
  * 跳过git add步骤提交到本地仓库：git commit -a -m "commit message " 【file name】
  * git commit --amend：将暂存区的文件提交，若上次提交后还未做任何修改，那么快照加将保持不变

* 查看提交日志：git log [option]
  
  * options
    * --all：显示所有分支
    * --pretty=oneline：将提交信息显示为一行
    * --abbrev-commit：使得输出的comitid更简短
    * --graph：以图的形式显示
    * --stat：显示每次提交的简略统计信息

* 版本回退：git reset --hard commitID
  
  * 查看已删除的记录
    * git reflog：查看已删除的提交记录

* 忽略文件
  
  > 创建文件.gitignore，在文件中列出忽略文件的模式

* 移除文件：git rm
  
  * 从仓库移除文件：git rm --cached

* 移动文件
  
  > 对文件改名：git mv


#### 分支

1. 简介

2. 常用命令

   * 新建分支
   * 删除分支
   * 查看分支
   * 切换分支
   * 合并分支
     * merage：保持修改内容的历史记录，但是历史记录会很复杂。
     * rebase：历史记录简单，是在原有提交的基础上将差异内容反映进去。因此，可能导致原本的提交内容无法正常运行。
~~~
# 新建一个分支，但依然停留在当前分支
$ git branch [branch-name]

# 新建一个分支，并切换到该分支
$ git checkout -b [branch]

# 新建一个分支，指向指定commit
$ git branch [branch] [commit]

# 新建一个分支，与指定的远程分支建立追踪关系
$ git branch --track [branch] [remote-branch]

# 列出所有本地分支
$ git branch

# 列出所有远程分支
$ git branch -r

# 列出所有本地分支和远程分支
$ git branch -a

# 切换到指定分支，并更新工作区
$ git checkout [branch-name]

# 切换到上一个分支
$ git checkout -

# 建立追踪关系，在现有分支与指定的远程分支之间
$ git branch --set-upstream [branch] [remote-branch]

# 合并指定分支到当前分支
$ git merge [branch]

# 选择一个commit，合并进当前分支
$ git cherry-pick [commit]

# 删除分支
$ git branch -d [branch-name]

# 删除远程分支
$ git push origin --delete [branch-name]
$ git branch -dr [remote/branch]
~~~

#### 标签

1. 简介：标签是为了更方便地参考提交而给它标上易懂的名称。Git可以使用2种标签：轻标签和注解标签。打上的标签是固定的，不能像分支那样可以移动位置。

2. 类型

   * 轻标签
   * 注解标签

3. 常用操作

   ~~~
   # 添加轻标签
   git tag <tagname>
   
   # 添加注解标签
   git tag -a <tagname>
   
   # 删除标签
   git tag -d <tagname>
   ~~~

#### 合并

可以通过 `.gitattributes` 文件来指定哪些文件不参与合并。`.gitattributes` 文件允许您为特定的文件或文件类型定义合并策略。

~~~
path/to/file merge=ours // path/to/file 是要排除的文件的相对路径
~~~

#### 代码冲突处理

### 远程仓库

#### 常用的托管服务（远程仓库）

* 局域网环境下
  * GitLab
* 外网环境下
  * GitHub
  * 码云(Gitee)

#### 常用操作

1. 查看远程仓库：git remote

2. 添加远程仓库：git remote add <shortname> <url>

3. 从远程仓库抓取与拉取
   
   >  git fetch [remote-name]：这个命令会访问远程仓库，从中拉取所有你还没有的数据。 执行完成后，你将会拥有那个远程仓库中所有分支 的引用，可以随时合并或查看。 必须注意 git fetch 命令会将数据拉取到你的本地仓库——它并不会自动合并或修改你当前的工作。 当准备好时你必须手动将其合并入你的工作。
   > 
   > 运行 git pull 通常会从最初克隆的服务器上抓取数据并自动尝试合并到当前所在的分支。

4. 推送到远程仓库：git push [remote-name] [branch name]

5. 查看某个远程仓库：git remote show [remote-name]

> 注意：如果当前本地仓库不是从远程仓库克隆，而是本地创建的仓库，并且仓库中存在文件，此时再从远程仓库拉取文件的时候会报错(fatal: refusing to merge unrelated histories )解决此问题可以在git pull命令后加入参数--allow-unrelated-histories

## Postman

## Apifox

官网：https://www.apifox.cn/

# 国际化

国际化（Internationalization，通常缩写为"i18n"）是指将产品、服务或软件设计和准备得适应不同地区和国家的语言、文化和习俗的过程。它旨在使产品能够在全球范围内使用，并为用户提供本地化的体验。

国际化的主要目标是使产品具备以下特性：

* 多语言支持：产品能够适应不同的语言环境，以便用户可以使用他们所熟悉的语言进行交互。
* 文化适应性：产品能够适应不同地区和文化的习俗、偏好和视觉习惯，以便用户感到亲切并易于接受。
* 日期和时间格式：产品能够根据用户所在地区的习惯显示日期和时间格式，以确保易于理解和使用。
* 货币和单位转换：产品能够支持不同货币和度量单位的转换，以便用户能够进行正确的交易和测量。
* 地理位置相关性：产品能够根据用户所在地区提供相关的信息、功能或服务，以适应当地需求。

通过国际化，企业可以开拓全球市场，吸引更多的用户并满足其多样化的需求。对于软件开发者来说，国际化是在设计、开发和测试产品时要考虑的重要因素，以确保产品在全球范围内具有广泛的可用性和用户满意度。

> 注意：国际化仅是准备产品以适应不同地区和语言的过程，而本地化（Localization）则是指实际将产品翻译并适应特定地区的过程。国际化为本地化提供了技术和基础设施支持。

# 实用开发

## 模型转换POJO、DO、BO、DTO、VO

参考链接：https://juejin.cn/post/7053264631262871583

POJO的定义是无规则简单的对象，在日常的代码分层中pojo会被分为VO、BO、 PO、 DTO

**VO （view object/value object）表示层对象**

1、前端展示的数据，在接口数据返回给前端的时候需要转成VO

2、个人理解使用场景，接口层服务中，将DTO转成VO,返回给前台

**B0（bussines object）业务层对象**

1、主要在服务内部使用的业务对象

2、可以包含多个对象，可以用于对象的聚合操作

3、个人理解使用场景，在服务层服务中，由DTO转成BO然后进行业务处理后，转成DTO返回到接口层

**PO（persistent object）持久对象**

1、出现位置为数据库数据，用来存储数据库提取的数据

2、只存储数据，不包含数据操作

3、个人理解使用场景，在数据库层中，获取的数据库数据存储到PO中，然后转为DTO返回到服务层中

**DTO（Data Transfer Object）数据传输对象**

1、在服务间的调用中，传输的数据对象

2、个人理解，DTO是可以存在于各层服务中（接口、服务、数据库等等）服务间的交互使用DTO来解耦

**DO（domain object）领域实体对象**

DO 现在主要有两个版本：

①阿里巴巴的开发手册中的定义，DO（ Data Object）这个等同于上面的PO

②DDD（Domain-Driven Design）领域驱动设计中，DO（Domain Object）这个等同于上面的BO

模型间的转换需要使用转换器，DTO、DO的转换器：xxxConverter  ，BO的转换器：xxxAssember

> VO，DTO，DO等各个对象将的转换除了可以手动使用get，set方法外，还可以使用一些工具和框架，具体可参考下一小节[开源第三方工具包](#tools)

## <a id= 'tools'>开源第三方工具包</a>

参考：https://pdai.tech/md/develop/package/dev-package-x-overview.html

### Apache Common包

### Google Guava包

参考：

* [Guava：Java开发者的全方位工具库_guava java-CSDN博客](https://blog.csdn.net/Mrxiao_bo/article/details/134291893)
* [Google Guava官方教程（中文版） | Google Guava 中文教程 (gitbooks.io)](https://wizardforcel.gitbooks.io/guava-tutorial/content/1.html)

### Hutool包

主页：https://www.hutool.cn/

### Spring工具类

参考：

* [SpringBoot 内置工具类应有尽有，别再自己瞎造轮子了！](https://mp.weixin.qq.com/s/Is_H0eQ1paEWylE-VuuAeg)

1. Assert
2. ObjectUtils
3. StringUtils
4. CollectionUtils
5. FileCopyUtils
6. ResourceUtils
7. StreamUtils
8. ReflectionUtils
9. AopUtils
10. AopContext

### MapStruct

文档：https://mapstruct.org/documentation/stable/reference/pdf/mapstruct-reference-guide.pdf

参考：

* https://pdai.tech/md/develop/package/dev-package-x-overview.html

MapStruct是一款非常实用Java工具，主要用于解决对象之间的拷贝问题，比如PO/DTO/VO/QueryParam之间的转换问题。区别于BeanUtils这种通过反射，它通过编译器编译生成常规方法，将可以很大程度上提升效率。

1. 引入依赖

   ~~~xml
   	<properties>
   <org.mapstruct.version>1.5.5.Final</org.mapstruct.version>
       </properties>
   
       <dependencies>
           <dependency>
               <groupId>org.mapstruct</groupId>
               <artifactId>mapstruct</artifactId>
               <version>${org.mapstruct.version}</version>
           </dependency>
       </dependencies>
   
   
       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-compiler-plugin</artifactId>
                   <version>3.8.1</version>
                   <configuration>
                       <source>1.8</source>
                       <target>1.8</target>
                       <annotationProcessorPaths>
                           <path>
                               <groupId>org.mapstruct</groupId>
                               <artifactId>mapstruct-processor</artifactId>
                               <version>${org.mapstruct.version}</version>
                           </path>
                       </annotationProcessorPaths>
                   </configuration>
               </plugin>
           </plugins>
       </build>
   ~~~

2. 编写转换器（抽象类或接口均可）

3. **@Mapper，@Mappings， @Mapping**

   * 默认映射规则
     * 同类型且同名的属性，会自动映射
     * 类型不同时，mapstruct会自动进行类型转换
       * 8种基本类型和他们对应的包装类型之间
       * 8种基本类型(包括他们的包装类型)和string之间
       * 日期类型和string之间
     
   * 可以同过@Mapping指定属性的映射关系和格式化
     * 日期格式化：dateFormat = "yyyy-MM-dd HH:mm:ss"
     * 数字格式化：numberFormat = "#.00"

   * 属性是引用类型时可以按照如下操做完成映射

     ~~~java
     @Mapping(source ="driverDTo",target ="drivervo") // 并写上对应的abstract方法
     ~~~

4. **@AfterMapping，@MappingTarget**

   * `@AfterMapping` 注解用于标记一个方法，在对象映射之后执行特定的逻辑。

5. **@BeanMapping**

   * ignoreByDefault：忽略mapstruct的默认映射行为。避免不需要的赋值、避免属性覆盖

6. **@InheritConfiguration**

7. **@lnheritlnverseConfiguration**

   * 反向映射，例如将DO->DTO，使用该注解后可以不需要写对应的方法而自动实现DTO->DO

### Dozer

Dozer是Java Bean到Java Bean映射器，它以递归方式将数据从一个对象复制到另一个对象。

dozer的maven坐标：

~~~xml
<dependency>
    <groupId>com.github.dozermapper</groupId>
    <artifactId>dozer-core</artifactId>
    <version>6.5.0</version>
</dependency>
~~~

为了简化使用方式，dozer还提供了starter，其maven坐标为：

~~~xml
<dependency>
    <groupId>com.github.dozermapper</groupId>
    <artifactId>dozer-spring-boot-starter</artifactId>
    <version>6.5.0</version>
</dependency>
~~~

### Lombok

参考：

* [十分钟搞懂Lombok使用与原理 - 掘金](https://juejin.cn/post/6844903557016076302)
* [java代码简洁之道 lombok不止lombok](https://www.bilibili.com/video/BV1T64y1Z7Xm/?spm_id_from=333.999.0.0&vd_source=fabefd3fabfadb9324761989b55c26ea)

1. `@Builder`&`@SuperBuilder`：使用此注解后可以通过链式构造创建对象

   > 参考：https://blog.csdn.net/qq_61267719/article/details/131182663

   * `@Builder`： `@Builder` 注解可以用在类、构造方法或者方法上，它会自动生成一个内部静态类作为构造器，并在该构建器中提供链式调用的方式来设置属性值。通过使用 `@Builder` 注解，我们可以方便地创建一个具有多个属性的对象。`@Builder` 会为被注解的类生成 builder 模式的相关方法，如 `builder()`、`build()` 和链式的属性设置方法。
* `@SuperBuilder`： `@SuperBuilder` 注解是 `@Builder` 的增强版本，它可以用于继承关系中。当一个子类使用 `@SuperBuilder` 注解时，Lombok 会为该子类生成一个包含父类属性的构建器，并保证构建器能够正确地设置父类和子类的属性值。使用 `@SuperBuilder` 后，我们可以在构建过程中同时设置父类和子类的属性。
  
2. `@Accessors`：用于生成属性的访问器（getter 和 setter 方法）

### Fastjson

1. 简介

   * Fastjson是阿里巴巴开源的一个Java语言编写的高性能功能完善的JSON解析库，通常被用于将Java Bean和JSON 字符串之间进行转换。
   * Fastjson接口简单易用，已经被广泛使用在缓存序列化、协议交互、Web输出、Android客户端等多种应用场景。

2. 使用

   ~~~xml
   <dependency>
       <groupId>com.alibaba</groupId>
       <artifactId>fastjson</artifactId>
       <version>1.2.79</version>
   </dependency>
   ~~~

## 字符集

参考：

* [编码 隐匿在计算机软硬件背后的语言](https://www.bilibili.com/video/BV1RK41157yj/?spm_id_from=333.337.search-card.all.click&vd_source=fabefd3fabfadb9324761989b55c26ea)
* https://www.bilibili.com/video/BV1xD4y1y7yc/?spm_id_from=333.337.search-card.all.click&vd_source=fabefd3fabfadb9324761989b55c26ea

1. 字符集
   * 字符是各种文字和符号的统称，包括各个国家文字、标点符号、表情、数字等等。 
   * 字符集就是一系列字符的集合。
2. 字符编码&字符解码
   * 字符编码是一种将字符集中的字符与计算机中的二进制数据相互转换的方法。
3. 常见字符集
   * ASCII
   * GBK
   * GB2312
   * Unicode
     * UTF-32
     * UTF-8

## 链式调用

参考：

* [被问住了：如何实现链式调用？](https://mp.weixin.qq.com/s/7WeECOXuefBdB2HCeV_lCw)

## 常用cmd命令

### 网络命令

## 常见网站安全问题

### 跨站脚本攻击（SXX）

XSS：跨站脚本攻击(Cross Site Scripting)，为不和 CSS混淆，故将跨站脚本攻击缩写为XSS。XSS是指恶意攻击者往Web页面里插入恶意Script代码，当用户浏览该页时，嵌入其中Web里面的Script代码会被执行，从而达到恶意攻击用户的目的。有点类似于sql注入。

XSS攻击原理：

HTML是一种超文本标记语言，通过将一些字符特殊地对待来区别文本和标记，例如，小于符号（<）被看作是HTML标签的开始，<title>与</title>之间的字符是页面的标题等等。当动态页面中插入的内容含有这些特殊字符时，用户浏览器会将其误认为是插入了HTML标签，当这些HTML标签引入了一段JavaScript脚本时，这些脚本程序就将会在用户浏览器中执行。所以，当这些特殊字符不能被动态页面检查或检查出现失误时，就将会产生XSS漏洞。

#### AntiSamry

AntiSamy是OWASP的一个开源项目，通过对用户输入的 HTML / CSS / JavaScript 等内容进行检验和清理，确保输入符合应用规范。AntiSamy被广泛应用于Web服务对存储型和反射型XSS的防御中。

AntiSamy的maven坐标：

~~~xml
<dependency>
  <groupId>org.owasp.antisamy</groupId>
  <artifactId>antisamy</artifactId>
  <version>1.5.7</version>
</dependency>
~~~

### SQL注入攻击

### OS命令注入攻击

### HTTP首部注入攻击

### 跨站点请求伪造（CSRF）

## 浏览器安全策略

参考：https://www.bilibili.com/video/BV1pT421k7yz/?spm_id_from=333.1007.top_right_bar_window_history.content.click

### 同源策略

1. 作用：用于限制一个源的文档或者它加载的脚本如何能与另一个源的资源进行交互。

2. 定义：如果两个 URL 的协议、主机和端口都相同，我们就称这两个 URL 同源。

3. 主要表现

   - DOM 访问限制：同源策略限制了网页脚本（如 JavaScript）访问其他源的 DOM。这意味着通过脚本无法直接访问跨源页面的 DOM 元素、属性或方法。这是为了防止恶意网站从其他网站窃取敏感信息。
   - Web 数据限制：同源策略也限制了从其他源加载的 Web 数据（例如 XMLHttpRequest 或 Fetch API,Cookie、LocalStorage和IndexDB的读写）。在同源策略下，XMLHttpRequest 或 Fetch 请求只能发送到与当前网页具有相同源的目标。这有助于防止跨站点请求伪造（CSRF）等攻击。
   - 网络通信限制：同源策略还限制了跨源的网络通信。浏览器会阻止从一个源发出的请求获取来自其他源的响应。这样做是为了确保只有受信任的源能够与服务器进行通信，以避免恶意行为

4. 举例

   > 假设用户正在浏览一个银行网站，该网站的URL为`http://www.bank.com`。同时，用户在另一个标签页中打开了一个恶意网站，URL为`http://www.malicious.com`。
   >
   > 根据同源策略，由于这两个网站的协议、主机名和端口号不同，它们被认为是不同源的。因此，恶意网站无法通过JavaScript等方式直接访问或操纵银行网站的数据。

需要注意的是虽然浏览器限制从脚本内发起的跨源 HTTP 请求，XMLHttpRequest 和 Fetch API，只能从加载应用程序的同一个域请求 HTTP 资源。但同源策略并不完全禁止跨域资源共享。在一些特定的场景下，可以使用CORS（跨域资源共享）来进行控制和配置，允许某些跨域资源的访问。

### 跨域资源共享（CORS）

跨源资源共享（Cross-Origin Resource Sharing，CORS）是一种机制，允许在受控的条件下，不同源的网页能够请求和共享资源。由于浏览器的同源策略限制了跨域请求，CORS 提供了一种方式来解决在 Web 应用中进行跨域数据交换的问题。

CORS 的基本思想是，服务器在响应中提供一个标头（HTTP 头），指示哪些源被允许访问资源。浏览器在发起跨域请求时会先发送一个**预检请求**（OPTIONS 请求）到服务器，服务器通过设置适当的 CORS 标头来指定是否允许跨域请求，并指定允许的请求源、方法、标头等信息。

对于满足以下条件的请求，浏览器将认为是**简单请求**，不会CORS预检请求：

* HTTP 方法限制：只能使用 GET、HEAD、POST 这三种 HTTP 方法之一。如果请求使用了其他 HTTP 方法，就不再被视为简单请求。

* 自定义标头限制：请求的 HTTP 标头只能是以下几种常见的标头：

  * Accept
  * Accept-Language
  * Content-Language
  * Last-Event-ID
  * Content-Type（仅限于 application/x-www-form-urlencoded、multipart/form-data、text/plain）

  HTML 头部 header field 字段：DPR、Download、Save-Data、Viewport-Width、WIdth。如果请求使用了其他标头，同样不再被视为简单请求。

* 请求中没有使用 ReadableStream 对象。

* 不使用自定义请求标头：请求不能包含用户自定义的标头。

* 请求中的任意 XMLHttpRequestUpload 对象均没有注册任何事件监听器；XMLHttpRequestUpload 对象可以使用 XMLHttpRequest.upload 属性访问

## 单例模式

单例模式的常见的五种实现方式。

1. 饿汉式
   
   * 可以使用反射、反序列化、Unsafe三种方式破坏单例
   
   ```java
   public class SingletonDemo1 implements Serializable {
   
       private static final SingletonDemo1 INSTANCE = new SingletonDemo1();
   
       private SingletonDemo1(){
           //防止反射破坏单例
           if (INSTANCE!=null){
               throw new RuntimeException("对象不能重复创建");
           }
           System.out.println("构造方法。。。。。。");
       }
   
       public static SingletonDemo1 getInstance(){
           return INSTANCE;
       }
   
       public static void otherMethod(){
           System.out.println("otherMethod......");
       }
   
       /**
        * 防止反序列化破坏单例
        */
       public Object readResolve(){
           return INSTANCE;
       }
   }
   ```

2. 懒汉式
   
   ```java
   public static synchronized SingletonDemo2 getInstance(){
       if (INSTANCE==null){
           INSTANCE = new SingletonDemo2();
       }
       return INSTANCE;
   }
   ```

3. DCL懒汉式（双检索）
   
   ```java
   private static volatile SingletonDemo3 INSTANCE = null;
   
   public static SingletonDemo3 getInstance(){
       if (INSTANCE==null){
           synchronized (SingletonDemo3.class){
               if (INSTANCE == null){
                   INSTANCE = new SingletonDemo3();
               }
           };
       }
       return INSTANCE;
   }
   ```

4. 内部类懒汉式

5. 枚举

### jdk中单例模式的应用

RunTime、System中的Console对象、Collections

## 阿里巴巴Java开发手册

## <a id= "base64"> Base64&Base64URL</a>

### Base64

参考：https://c.runoob.com/front-end/693/

在线编码工具：https://c.runoob.com/front-end/693/

### Base64URL

Base64 存在以下问题：

- 使用 `+` 作为第 62 个字符，使用 `=` 作为填充字符。这两个字符在 URL 中都有特殊含义，`+` 是空格，`=` 用于通过查询字符串作为 `键=值` 发送数据；
- 使用 `/` 作为第 63 个字符，`/` 在 URL 和文件系统中都用作分隔符。

为解决能够将编码结果用作文件名或 URL 地址的问题，Base64URL 对 Base64 标准进行了修改，在以下几个方面做了稍许调整：

- 将 `+` 替换成了 `-`
- 将 `/` 替换成了 `_`
- 不再需要填充字符
- 禁止行分隔符

## 源码阅读

整体规划：

java基础（集合+泛型+注解+反射）+设计模式-->框架源码（mybatis+spring+springmvc-->springboo-->springcloud）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6D5fS3V8mLyrtXtThcpib9nGxHJ1JxW9rtcmicPs1ibWVtZaMfjjoxJv47e16xrMuiaGMmF9cdG3M6MbPOg2ymxfxA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

计算机网络+操作系统 --> BIO + 多线程 --> NIO + 线程池 + 多路复用 -->  Netty --> Tomcat Redis Zk Dubbo —> 自定义协议RPC框架

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6D5fS3V8mLyrtXtThcpib9nGxHJ1JxW9rzrMtMbgDMuJZjUlwM5UiaRfiagUKtsNv3G17h24h6EtiaDAr0arYaI1Bw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

参考：

* https://blog.csdn.net/ma_nong33/article/details/128923602
* https://mp.weixin.qq.com/s/HZt0eT2e1T4hwNGdZMfxow

## 版权（CopyRight）与开源协议（License）
具体参考：[知识产权&法律法规](./知识产权&法律法规.md)

## Api接口设计

### 统一响应对象

为了前后端协作效率的提高，后端通常会统一一个接口返回格式给前端。该返回对象格式通常如下：

常见的 HTTP 请求返回状态码：

| 状态码 | 含义                                   |
| ------ | -------------------------------------- |
| 200    | OK - 请求成功                          |
| 201    | Created - 已创建                       |
| 204    | No Content - 无内容返回                |
| 301    | Moved Permanently - 永久重定向         |
| 400    | Bad Request - 无效请求                 |
| 401    | Unauthorized - 未授权                  |
| 403    | Forbidden - 禁止访问                   |
| 404    | Not Found - 未找到资源                 |
| 405    | Method Not Allowed - 不允许的方法      |
| 500    | Internal Server Error - 服务器内部错误 |

~~~java
package com.whymechen.cloud.common.enums;

import java.util.Arrays;

/**
 * @author whymechen
 * @version 1.0
 * @date 2024/3/8 22:31
 **/
public enum ReturnCodeEnum {
    SUCCESS("200", "SUCCESS"),
    BAD_REQUEST("400", "Bad Request"),
    UNAUTHORIZED("401", "Unauthorized"),
    FORBIDDEN("403", "Forbidden"),
    NOT_FOUND("404", "URI Not Found"),
    METHOD_NOT_ALLOWED("405", "Method Not Allowed"),
    NOT_ACCEPTABLE("406", "Not Acceptable"),
    CONFLICT("409", "Resource Conflict"),
    PAYLOAD_TOO_LARGE("413", "Payload Too Large"),
    UNSUPPORTED_MEDIA_TYPE("415", "Unsupported Media Type"),
    UNAVAILABLE_FOR_LEGAL_REASONS("451", "Unavailable For Legal Reasons"),
    SERVER_ERROR("500", "Internal Server Error"),
    SERVICE_UNAVAILABLE("503", "Service Unavailable"),

    UNKNOWN_ERROR("9999", "Unknown Error");

    private final String code;

    private final String message;

    ReturnCodeEnum(String code, String message) {
        this.code = code;
        this.message = message;
    }

    public String getCode() {
        return code;
    }

    public String getMessage() {
        return message;
    }

    public static ReturnCodeEnum getReturnCodeEnum(String code) {
        if (code == null || code.isEmpty()) {
            return null;
        }
        return Arrays.stream(ReturnCodeEnum.values())
                     .filter(e -> e.getCode()
                                   .equalsIgnoreCase(code))
                     .findFirst()
                     .orElse(null);
    }

    // public static ReturnCodeEnum getReturnCodeEnum(String code) {
    //     if (code == null || code.isEmpty()) {
    //         return null;
    //     }
    //     for (ReturnCodeEnum returnCodeEnum : ReturnCodeEnum.values()) {
    //         if (returnCodeEnum.getCode()
    //                           .equals(code)) {
    //             return returnCodeEnum;
    //         }
    //     }
    //     return null;
    // }
}
~~~

~~~java
package com.whymechen.cloud.common;

import com.whymechen.cloud.common.enums.ReturnCodeEnum;
import lombok.Data;
import lombok.experimental.Accessors;

import java.time.LocalDateTime;

/**
 * @author whymechen
 * @version 1.0
 * @date 2024/3/8 22:33
 **/
@Data
@Accessors(chain = true)
public class ApiResult<T> {

    /**
     * 返回码
     */
    private String code;

    /**
     * 返回说明
     */
    private String msg;

    /**
     * 返回数据
     */
    private T data;

    private Long timestamp;

    public ApiResult(String code, String msg, T data) {
        this.code = code;
        this.msg = msg;
        this.data = data;
        this.timestamp = System.currentTimeMillis();
    }

    public ApiResult(ReturnCodeEnum returnCodeEnum, T data) {
        this(returnCodeEnum.getCode(), returnCodeEnum.getMessage(), data);
    }

    public ApiResult(ReturnCodeEnum returnCodeEnum) {
        this(returnCodeEnum, null);
    }

    public static <T> ApiResult<T> success() {
        return new ApiResult<T>(ReturnCodeEnum.SUCCESS.getCode(), ReturnCodeEnum.SUCCESS.getMessage(), null);
    }

    public static <T> ApiResult<T> success(String msg) {
        return new ApiResult<T>(ReturnCodeEnum.SUCCESS.getCode(), msg, null);
    }

    public static <T> ApiResult<T> success(T data) {
        return new ApiResult<T>(ReturnCodeEnum.SUCCESS.getCode(), ReturnCodeEnum.SUCCESS.getMessage(), data);
    }

    public static <T> ApiResult<T> success(String msg, T data) {
        return new ApiResult<T>(ReturnCodeEnum.SUCCESS.getCode(), msg, data);
    }

    public static <T> ApiResult<T> error() {
        return new ApiResult<T>(ReturnCodeEnum.UNKNOWN_ERROR.getCode(), ReturnCodeEnum.UNKNOWN_ERROR.getMessage(), null);
    }

    public static <T> ApiResult<T> error(String msg) {
        return new ApiResult<T>(ReturnCodeEnum.UNKNOWN_ERROR.getCode(), msg, null);
    }

    public static <T> ApiResult<T> error(ReturnCodeEnum returnCodeEnum) {
        return new ApiResult<T>(returnCodeEnum.getCode(), returnCodeEnum.getMessage(), null);
    }

    public static <T> ApiResult<T> error(ReturnCodeEnum returnCodeEnum, T data) {
        return new ApiResult<T>(returnCodeEnum.getCode(), returnCodeEnum.getMessage(), data);
    }
}
~~~



### 时间格式统一

对于后端返回的数据，如果涉及到时间应该尽量保持格式的统一返回给前端，例如：yyyy-MM-dd HH:mm:ss。

实现方案通常有如下几种：

1. 可以在相应的实体类的属性上使用 @JsonFormat 注解：

   ~~~xml
       /**
        * 创建时间
        */
       @Column(name = "create_time")
       @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")
       @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
       private Date createTime;
   
       /**
        * 更新时间
        */
       @Column(name = "update_time")
       @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")
       @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
       private Date updateTime;
   ~~~

2. 如果是 Spring Boot 项目，也可以在 application.yml 文件中指定：

   ~~~xml
   spring:
     jackson:
       date-format: yyyy-MM-dd HH:mm:ss
       time-zone: GMT+8
   ~~~

## 异常处理器：统一异常处理

1. 异常常见的位置
   * 框架内部抛出的异常:因使用不合规导致
   * 数据层抛出的异常:因外部服务器故障导致(例如:服务器访问超时)
     业务层抛出的异常:因业务逻辑书写错误导致(例如:遍历业务书写操作，导致索引异常等)
   * 表现层抛出的异常:因数据收集、校验等规则导致(例如:不匹配的数据类型间导致异常)
   * 工具类抛出的异常:因工具类书写不严谨不够健壮导致(例如:必要释放的连接长期未释放等)
2. 统一异常处理-aop思想
3. 项目异常分类
   * 业务异常（BusinessException）：数据不规范或规范产生的异常
   * 系统异常（SystemException）：项目运行过程中可预计无法避免的异常
   * 其他异常（Exception）：未预期的异常

## 登录校验

涉及技术：会话技术+令牌技术+过滤器/拦截器

![image-20230807230500031](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202308072305116.png)

基本思路（令牌技术）：

* 登录成功后，生成JWT令牌，并返回给前端
* 在请求到达服务器端后，对令牌进行统一拦截、校验

## 加密解密&加签验签

参考：

* [程序员必备基础：加签验签-CSDN博客](https://blog.csdn.net/woniu211111/article/details/108114402)
* [加解密、加签验签 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/383170400)
* [最详细的SpringBoot实现接口校验签名调用_springboot接口加签验签-CSDN博客](https://blog.csdn.net/qq_43290318/article/details/131516099?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-131516099-blog-108114402.235^v40^pc_relevant_rights_sort&spm=1001.2101.3001.4242.1&utm_relevant_index=3)

> 公钥加密，私钥解密；私钥加签，公钥验签

### 基本概念

1. 明文（原文）：就是被隐藏的文字
2. 密文（伪文）：指对原文按照加密法处理过后生成的可公开传递的文字
3. 加密法：指隐藏原文的法则
4. 密钥：是一种参数，它是在明文转换为密文或将密文转换为明文的算法中输入的参数。密钥分为对称密钥与非对称密钥。在加密法中起决定性的因素，可能是数字、词汇，也可能是一些字母，或者这些东西的组合。
   * 对称密钥：在对称加密算法中，同一密钥被用于加密和解密过程。这意味着发送方和接收方必须共享这个密钥，并且必须确保密钥的安全，以防泄露给第三方。常见的对称加密算法有AES（高级加密标准）、DES（数据加密标准）等。
   * 非对称密钥：非对称加密使用一对密钥，即公钥（Public Key）和私钥（Private Key）。公钥用于加密信息，可以公开分享；而私钥必须保密，用于解密信息。这种方式解决了密钥分发的安全问题，因为即使公钥被广泛传播，只要私钥安全，信息仍然是安全的。RSA、ECC（椭圆曲线密码学）是常见的非对称加密算法。
5. 加密：将明文变为密文的过程
6. 解密：将密文变为明文的过程

### 加密解密算法

1. 分类
   * 是否使用对称密钥
     * 对称加密算法
       * 常见的对称加密算法
         * AES
         * DES
         * 3DES
         * TDEA
         * Blowfish
         * RC5
         * RC6
     * 非对称加密算法
       * 常见的非对称加密算法
         * RSA
         * ELgamal
         * DSA
         * D-H
         * ECC

## 信息脱敏

## IP直连问题处理

1. 问题描述：对于数据库或者是服务使用IP直连会造成强耦合
2. 解决方案：
   * 部署内部DNS
   * 使用注册中心

## 常见性能指标

1. QPS

## cURL

cURL全称是 Client URL，是一个利用 URL 语法在命令行或脚本中工作的工具。

## API版本控制

参考：[Spring 7.0 新特性真香，API 版本控制更丝滑了！](https://mp.weixin.qq.com/s?__biz=Mzg2OTA0Njk0OA==&mid=2247548937&idx=1&sn=335ba0fbd9475a9a9ddec026ef46acbf&chksm=cfdb87bbf4fa06ce6c5b5708fd03896b36ab26b1f15312776021165ce52b3e191b347c0c1014&scene=126&sessionid=1745392640#rd)

# 开源项目

## EasyCaptcha

项目地址：https://github.com/whvcse/EasyCaptcha

Java图形验证码，支持gif、中文、算术等类型，可用于Java Web、JavaSE等项目。 

## EasyPOI

项目地址：http://easypoi.mydoc.io/ 

## EasyExcel

## SmartAdmin

项目地址：https://smartadmin.vip/

# 路线/资源

1. [2022黑马程序员Java学习路线图 - 哔哩哔哩](https://www.bilibili.com/read/cv9965357?from=articleDetail)
2. [Java全栈知识体系](https://pdai.tech/)
3. [JavaGuide](https://javaguide.cn/)
4. [TAI](http://javatai.cn/)
5. [慕课教程-编程入门快速学习手册 (imooc.com)](https://www.imooc.com/wiki/)
6. [effective-resourses](https://github.com/wususu/effective-resourses)
7. [Java各类技术栈 架构图汇总](https://mp.weixin.qq.com/s?__biz=MzAwOTE3NDY5OA==&mid=2647929690&idx=1&sn=b3f8dac73ce076e990fef898de73e214&chksm=8343389fb434b189934f58353be070d5c5e76809ad279ca05b687fd62f4149ffe83622ba9468&scene=27)
8. [Jakarta EE（JAVA EE）规范概念、规则全梳理帮你捋清 JAVA EE 技术栈](https://www.bilibili.com/video/BV1fb4y1G7Jp/?spm_id_from=333.999.0.0)

