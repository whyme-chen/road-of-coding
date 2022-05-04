# 基础编程

## java发展史

## java特性

## 开发环境

1. JDK
2. JRE
3. JVM
4. 三者的关系

## JShell

java 1.9后提供。

## 注释与关键字

## 数据类型

## 运算符

## 控制逻辑

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
2. instanof关键字

保证对象向下转型的正确性

### Object类

1. Object类是所有类的父类。

2. 常用方法
   
   参考文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/Object.html#method.summary
   
   | 方法                         | 描述  |
   | -------------------------- | --- |
   | String toString()          |     |
   | boolean equals(Object obj) |     |

## 字符串

### 实质

字符串的实质是对数组的特殊包装。在JDK1.8以前使用的是字符数组，在1.9以后使用的字节数组。

### 字符串的相等比较

对于字符串的相等比较应该注意“==”比较的是字符串的对象地址，而若要比较字符串内容应该使用equals()方法进行。

### String类

#### String类两种实例化方式的区别

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
   * 暴露远程方法视图（常用语RPC分布式开发中使用 ）

3. **抽象类和接口的区别**
   
   | 区别   | 抽象类                                                               | 接口                        |
   | ---- | ----------------------------------------------------------------- | ------------------------- |
   | 定义   | abstract关键字                                                       | interface关键字              |
   | 权限   | 各种权限                                                              | 只能使用public                |
   | 子类使用 | 子类通过extends关键字只能继承一个抽象类                                           | 子类通过implements关键字可以实现多个接口 |
   | 两者关系 | 抽象类可以实现若干个接口                                                      | 接口不允许继承抽象类，但是可以继承多个接口     |
   | 使用   | 1. 抽象类或接口必须定义子类；2. 子类一定要覆写抽象类或接口中的所有抽象方法；3. 通过子类的向上转型实现抽象类或接口的实例化 |                           |

## 枚举类

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

### 普通内部类

### 静态内部类

### 方法中定义内部类

### 匿名内部类

# 常用类

### Objcet类

### Scanner类

### Math类

### String类

### StringBuilder类

### StringBuffer类

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

### 日期与时间相关类

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

### java8新增日期类

# 包的定义及使用

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

# Lambda表达式

从JDK1.8开始为简化使用者进行代码开发，专门提供有Lambda表达式的支持。对于函数式编程比较著名的语言：haskell、Scala。

Lambda表达式如果要使用，必须有一个重要的实现要求：SAM（Single Abstract Method）,只有一个抽象方法。

Lambda表达式提供有如下几种格式：

* 方法没有参数：()->{}
* 方法有参数：()->{}
* 如果只有一行语句返回：(参数，参数)->语句

利用Lambda表达式可以摆脱传统面向对象只用关于结构的限制，使得代码更加简便。

# 正则表达式

1. 作用：用于验证字符串合法性

2. 验证规则
   
   参考文档：[Pattern (Java SE 16 &amp; JDK 16)](https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/util/regex/Pattern.html)
   
   ![image-20211229104328005](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211229104328005.png)

# 异常捕获和处理

### 基本结构

在java中通过try、catch和finally关键词来实现异常的捕获和处理，常用基本结构如下：

```java
try{
    //可能出现异常的语句
}catch(//异常类型 异常对象){
    //异常处理
}finally{
    //不管是否出现异常，都执行的代码
}
```

### 处理流程

### throw和throws关键字

### 自定义异常类

### assert断言

从JDK1.4之后开始追加一个断言的功能，确定代码执行到某行之后一定是所期待的结果。在实际开发之中，断言不一定是准确的，也有可能出现偏差，但是这种偏差不应该影响程序的执行。

# 泛型

1. 泛型的引出

   泛型是JDK1.5之后开始使用的，其主要目的是为了解决ClassCastException的问题。java中向下转型始终都有可能存在安全隐患，因此希望通过泛型来慢慢解决此类问题。

2. 泛型的定义

   > * 泛型中只允许使用引用类型，若要使用基本类型则必须进行包装
   > * 从JDK1.7开始，泛型对象实例化可以简化。
   > * 泛型可以定义在类、接口和方法上

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

   ```java
   package generics;
   
   /**
    * 泛型类
    在类的名字后加上泛型标识
    */
   public class MyArrayList<E> {
       public void add(E e){
   
       }
   
       public void remove(E e){
   
       }
   
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

   ~~~ java
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

# 集合

### 1. 集合概述

1. 体系结构

   > Collection体系（单列集合）
   >
   > ![Collection](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220109124008792.png)
   >
   > Collection常用API
   >
   > ![](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220110164632701.png)
   >
   > Map体系（双列集合）

2. 使用场景

   > * 数据个数不确定，需要进行增删元素的场景

3. 迭代器

   参考文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/util/Iterator.html

   > 注意：
   >
   > 1. 增强for循环：自jdk1.5开始出现，内部原始是Iterator迭代器。
   > 2. 实现了Iterator接口的类才可以使用迭代器和增强for循环。

4. 常见数据结构

   * 栈、队列
   * 数组
   * 链表
   * 二叉树、二叉查找树
   * 平衡二叉树（任意结点的左右子树高度差不超过1）
   * 红黑树

5. 集合的并发修改异常问题

   ![image-20220402172317221](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220402172317221.png)

   使用迭代器遍历是删除操作应该用迭代器删除，而不是使用集合本身执行删除操作。使用增强for时无法解决遍历的同时执行删除元素操作。

### 2. List集合

元素有序、可重复、有索引

#### ArrayList

1. 常用方法

2. 底层实现原理

   > * 底层基于数组实现，根据所以定位元素快，但是增删元素时需要做移位操作
   > * 初始化时，默认创建长度为10的数组

#### LinkedList

1. 常用方法

2. 底层原理

   > * 底层数据结构为双链表，查询慢，但是首位操作快，故新增了许多首位操作的特有功能
   >
   >   ![image-20220402170854567](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220402170854567.png)
   >
   > * LinkedList可以完成栈和队列的操作

```java
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
```

### 3. Set集合

* 元素无序、不重复、无索引
* Set的实现类是基于Map来实现的

#### HashSet

1. 底层实现

#### LinkedHashSet

> 注意：LinkedHashSet是有序、不重复、无索引

#### TreeSet

> 注意：TreeSet按照大小默认升序排序、是不重复、无索引的

### 4. Map

参考链接：https://www.cnblogs.com/haimishasha/p/10790508.html#autoid-4-2-0

#### HashMap

#### LinkedHashMap

#### TreeMap

#### SortedMap

#### HashTable

#### WeakedHashMap

# I/O操作

## 一、 File类

1. File类：位于java.io.File包中，代表操作系统中文件对象（文件及文件夹）

2. File类的创建
   
   ![image-20211227210216574](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211227210216574.png)

3. 常用API
   
   参考文档：https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/io/File.html
   
   ![image-20211227211734081](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211227211734081.png)
   
   ![image-20211227213211148](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211227213211148.png)

4. 小案例
   
   * 搜索文件

## 二、字符集

## 三、I/O流

# 多线程

## 进程

window的时代开启了多进程设计，在一个时间段可以同时运行多个程序并进行资源的轮流抢占。但是在一个时间点只会有一个进程在执行。

## 线程

线程是在进程基础上创建并且使用的，所以线程依赖于进程的支持，但是线程的启动速度要比进程快得多。

### 1. 多线程的定义

在java中实现多线程的定义，需要有一个专门的线程主体类进行线程的定义，必须实现特定的接口或继承特定的父类。

#### 继承Thread类实现多线程

在java中提供了一个java.lang.Thread的程序类，只要一个类继承了此类就表示这个类为线程的主体类。在该主体类中覆盖重写run()方法，多线程要执行的功能都应该再run()方法内部进行定义。需要说明的是：正常情况下只需产生一个实例化对象，然后调用类中提供的方法。但是run()方法是不能被直接调用的，而是需要使用start()方法来启动多线程实现线程的调度。

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

```java
package test;

/*
    使用Runnable接口实现多线程
    1.创建一个MyRunnable类来实现Runnable接口，在这个类中重写run方法
    2.创建一个MyRunnable类的对象和Thread类的对象，将MyRunnable的对象作为参数传输Thread类的构造方法中
    3.启动线程
*/

public class MyRunnable implements Runnable {

    @Override
    public void run() {
        // TODO Auto-generated method stub
        for (int i = 0; i < 50; i++) {
            System.out.println(Thread.currentThread().getName()+":"+i);
        }
    }

}

public class Test03 {
    public static void main(String[] args) {
        MyRunnable myRunnable=new MyRunnable();
        Thread thread=new Thread(myRunnable,"thread1");
        Thread thread2=new Thread(myRunnable,"thread2");
        thread.start();
        thread2.start();
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

### 2. 线程运行状态

![image-20210721212820134](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210721212820134.png)

### 3. 线程常用方法

1. 线程的命名与取得
   
   * 构造方法：public Thread(Runnable target,String name)
   * 设置名字：publid final void setName(String name)
   * 取得名字：public final Sttring getName()

2. 线程控制
   
   * public static void sleep(long millis)：使当前正在执行的线程停留（暂停执行）指定的毫秒数
   * void joiin()：等待这个线程死亡
   * void setDaemon(boolean on)：将此线程标记为守护线程，党运行的线程都是守护线程时，java虚拟机将退出

3. 线程中断

4. 线程调度
   
   * 常用的线程调度方式有两种：
     
     * 分时调度模型
     * 抢占式调度模型
     
     java使用的线程调度方式是抢占式调度模型。
   
   * 设置和获取线程优先级
     
     * public final int getPriority()：返回此线程的优先级
     * public final void setPriority(int newPriority)：更改线程的优先级
   
   注意：线程默认优先级为5；线程优先级的范围是：1-10；线程优先级高仅仅表示线程获取的CPU时间片的几率高，但是要在次数比较多或者多次运行的时候才能看到想要的效果。

### 4. 线程同步

# Junit单元测试

1. 测试分类
   
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

如果想要实现反射的处理操作，那么首先要采用的就是Object中所提供的的一个方法获取Class对象信息：public final Class<?> getClass();

1. 反射中所有的核心操作都是通过Class类对象展开的，获取Class对象的三种方式：
   
   * **【class类支持】**Class.forName("全类名")：将字节码文件加载进内存，返回Class对象（多用于配置文件）
   * **【JVM直接支持】**类名.class：通过类名的属性class获取（多用于参数传递）
   * **【Object类支持】**对象.getClass()：通过Object类提供的getClass（）方法获取
   
   注意：同一个字节码文件（*.class）在一次程序运行中，只会被加载一次，不论通过哪种方式获得的Class对象都是同一个对象

2. 反射获取类结构信息
   
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

# 注解（Annoation）

1. 注解：一种代码级别的说明。JDK1.5之后提出的一个新的开发技术结构，利用annoation可以有效减少程序配置的代码并且可以利用annoation进行一些结构化定义。(可以简单理解为就是给计算机看的注释)

2. 作用分类
   
   * 编写文档：通过代码里标识的元数据生成文档（生成doc文档）
   * 代码分析：通过代码里标识的元数据对代码进行分析（使用反射）
   * 编译检查：通过代码里标识的元数据让编译器能够实现基本的编译检查

3. JDK中预定义的一些注解
   
   * @Override：检测被该注解标注的方法是否继承自父类
   * @Deprecated：该注解标注的内容，表示已过时
   * @SuppressWarnings：压制警告（一般传递参数all）

4. 自定义注解
   
   * 格式：
     
     > 元注解：用于描述注解的注解
     > 
     > * @target：描述注解能够作用的位置
     >   
     >   * ElementType取值：
     >     * TYPE：可以作用于类上
     >     * METHOD：可以作用于方法上
     >     * FILED：可以作用于域上
     > 
     > * @Retention：描述注解被保留的阶段
     >   
     >   * ```
     >     @Retention(RetentionPolicy.RUNTIME)：当前被描述的注解，会保留到字节码文件中，并被JVM读取
     >     ```
     > 
     > * @Documented：描述注解是否被抽取到api文档中
     > 
     > * @Inherited：描述注解是否被子类继承
     > 
     > public @interface 注解名称{}
   
   * 本质：注解本质上就是一个接口，该接口默认继承Annoation接口
     
     > public interface MyAnnoation extends java.lang.annoation.Annoation{}
   
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

5. 在程序中解析（使用）注解：获取注解中定义的属性值
   
   * 获取注解定义位置的对象
   * 获取指定的注解（getAnnoation（CLass））
   * 调用注解中的抽象方法获取属性值
   
   ![image-20211227202726241](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211227202726241.png)

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
   
   3. U（Updata）：修改
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
   timestamp（时间错类型）
   varchar（字符串）
   
   2. 查询
   * 查询某个数据库中的所有表名称
   show tables;
   
   * 查询表结构
   desc 表名
   
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

7. 规范

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

3. 约束
   
   ```sql
   对表中数据进行限定，保证数据的正确性，有效性和完整性。
   分类：
   主键约束（primary key）
   主键：非空且唯一
   一张表中只能有一个字段为主键
   主键就是表中记录的唯一标识
   删除主键（alter table 表名 drop primary key;）
   附：自动增长
   概念：如果某一列是数值类型的，使用auto_ncreament可以完成值的自动增长
   非空约束（not null）
   在创建表时就进行约束
   创建表后添加非空约束
   唯一约束（unique）
   创建表时添加唯一约束
   创建完后添加唯一约束
   删除唯一约束（alter table 表名 drop index 列名;）
   外键约束（foregin key）
   在创建表时可以添加外键
   create table 表名（
                       外键列
                       constraint 外键名称 foreign key 外键列名称 reference 主表名称（主表列名称;
               删除外键：
   alter table 表名 drop forigen key 外键名称；
           创建表之后添加外键：
   alter table 表名 add constraint 外键名称 foreign key（外键字段名称）reference 主表名称（主表列名称）
           级联操作：
   添加级联操作：alter table add constraint 外键名称 foreign key referen 主表名称（主表列名称）on update cascade on delete cascade；
   ```

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
         * Class.forName(“com.mysql.cj.jdbc.Driver”)
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
       
       * ```
         boolean execute(String sql)
         int executeUpdate(String sql)//执行DML语句
         ResultSet executeQuery(String sql)//执行DQL语句
         ```
   
   * ResultSet：结果集对象，封装查询结果
     
     * next（）方法：游标向下移动一行
     * getxxx（参数）方法：xxx代表数据类型，参数可以代表列编号或列名称
     
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

3. C3P0实现
   
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

4. druid实现
   
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

1. 下载：官网下载即可
2. 安装：解压安装包即可
3. 卸载：删除安装文件即可
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
   * WEB—INF目录下的资源不能被浏览器直接访问

# HTTP协议

### 概念：Hyper Text Transfer Protocol（超文本传输协议）。

* 定义了客户端和服务器端通信时，发送数据的格式
* 特点：
  * 基于TCP/IP的高级协议
  * 默认端口是8080
  * 基于请求响应模型
  * 无状态的：每次请求之间是相互独立的，不能交互数据
* 历史版本

### 请求消息数据格式（四部分）

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

* **请求空行**

* **请求体（正文）**

### 响应消息数据格式(四部分)

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

# Servlet

### 一、概念

运行在服务器端的小程序。

Servlet本质上就是一个接口，定义了java类被浏览器访问到（tomcat识别）的规则。

![image-20210907170723274](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210907170723274.png)

在Servlet通常需要接收请求、处理请求、完成响应。

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

![image-20210208095117534](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210208095117534.png)

1. 当服务器接收到客户端浏览器的请求后，会解析请求URL路径，获取访问的Servlet资源路径
2. 查找web.xml文件，是否有对象的<utl-pattern>标签内容
3. 如果有，则再找到对应的<servlet-class>全类名
4. tomcat会将字节码文件加载进内存，并且创建其对象
5. 调用其方法

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

![image-20210911152738491](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210911152738491.png)

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
   
   * 分析
     
     ![image-20210920170258264](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210920170258264.png)
   
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
  > 2. 重定向i访问其他站点
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

1. ServletContext概述：服务器会为每一个应用创建一个ServletContext对象（ServletContext对象在服务器启动时创建，在服务器关闭时销毁，代表整个web应用）
   
   * ServletContext对象的作用是在整个web应用的动态资源之间共享数据。

2. 获取：
   
   * 通过request对象获取：request.getServletContext()
   * 通过HttpServlet获取：getServletContext()

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

4. 案例：**文件下载**
   
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

# 文件上传和下载

## 文件上传

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

6. 空间

## 文件下载

# 会话技术

1. 会话：一次会话中包含多次请求和响应。
2. 会话功能：在一次会话的范围内的多次请求间共享数据。
3. 方式
   * 客户端会话技术：Cookie
   * 服务器端会话技术：Session

## 1. Cookie

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

4. cookie细节
   
   * 一次可不可以发送多个cookie？可以
   * cookie在浏览器中保存多长时间？默认情况下，浏览器被关闭，cookie被清除
   * cookie能不能存中文？
   * cookie获取范围多大？

5. cookie的特点
   
   * cookie存储数据在客户端浏览器
   * 浏览器对于单个cookie的大小有限制（4KB）而且对于同一域名下的总cookie数也有限制

6. cookie的作用
   
   * cookie一般用于存储少量的不太敏感的信息
   * 在不登录的情况下，完成服务器对客户端的身份识别

## 2. Session

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
   
   ![image-20211001112805649](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211001112805649.png)

4. 细节
   
   * 当客户端关闭后，服务器不关闭，两次获取的session是否为同一个？
     * 默认情况下，不是。
   * 客户端不关闭，服务器关闭后，两次获取的session是同一个吗？
     * 不是同一个，但要确保数据不丢失
       * session的钝化：在服务器正常关闭前，将session对象序列化到硬盘上
       * session的活化：在服务器启动后，将session转化为内存中的session对象
   * session的失效时间是多久？（什么时候被销毁）
     * 服务器关闭时，或者默认失效时间30分钟，或者session对象调用invalidate（）方法

5. 特点
   
   * session用于存储一次会话的多次请求数据，存在服务器端
   * session可以存储任意类型，任意大小的数据

## 3. session和Cookie的区别

1. session存储在服务器端，Cookie存储在客户端
2. session没有数据大小限制，Cookie有
3. session数据安全，Cookie相对不安全

## 案例：验证码

1. 需求
   
   * 访问带有验证码的页面login.jsp
   * 用户输入哟红户名，密码以及验证码
     * 如果用户名和密码输入有误，跳转登录页面，提示：用户名或密码错误
     * 如果验证码输入有误，跳转登录页面，提示：验证码错误
     * 如果全部输入正确，跳转到主页succcss.jsp，显示：用户名，欢迎您

2. 分析
   
   ![image-20211001135402947](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211001135402947.png)

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

# JSP

## JSP快速入门

1. JSP：Java Server Pages，java服务器端页面

2. 原理：
   
   * jsp本质是就是一个Servlet

3. JSP的脚本：Jsp定义Java代码的方式
   
   * <%  %>
   * <%!  %>
   * <%= %>

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
       > language
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

6. 注释
   
   ```
   <%-- --%>
   ```

7. JSP的内置对象：在JSP页面中不需要获取和创建，可以直接使用的对象（共9个）
   
   > 变量名                    真实类型
   > 
   > pageContext        PageContext        当前页面共享数据（可以获取其他八个内置对象）
   > 
   > request                HttpServletRequest        一次请求访问的多次资源
   > 
   > response            HttpServletResponse        
   > 
   > session                HttpSession        一次会话的多个请求间共享数据
   > 
   > out                        JspWriter        输出对象
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

## EL表达式

1. EL表达式：Expression Language

2. 作用：替换和简化jsp页面中java代码的编写

3. 语法：${表达式}

4. 注意：
   
   * jsp默认支持EL表达式
   * 忽略EL表达式
     * 设置jsp中page指令的属性isELIgnored=“ture”
     * \${表达式}

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
     
     * el表达式只能从域对象中获取值
     
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
     
     > * el表达式中由11个隐式对象
     > * pageContext：获取其他八个内置对象

## JSTL标签

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

## javaBean在JSP中的应用

1. \<jsp:useBean\>标签：用于在JSP页面中创建一个JavaBean实例并通过属性设置将实例存放到jsp的指定范围内。
   
   ![image-20211115183439761](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211115183439761.png)

2. \<jsp:setProperty\>标签：用于对JavaBean中属性赋值，但JavaBean的属性要提供相应的set方法

3. \<jsp:getProperty\>标签：用于获取JavaBean中属性的值，但JavaBean的属性要提供相应的get方法

# MVC开发模式

1. MVC（Model-View-Controller）
   
   * 模型：完成业务操作
   * 视图：展示数据
   * 控制器：获取用户输入，调用模型，将数据交给视图进行展示
   
   ![image-20220418082619232](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418082619232.png)

# 三层架构：软件设计架构

1. 三层架构
   
   * 界面层（表示层）：用户可以通过界面上的组件和服务器进行交互
   * 业务逻辑层：处理业务逻辑
   * 数据访问层：操作数据存储文件
   
   ![image-20211002163015726](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211002163015726.png)

2. 案例：**用户信息列表展示**
   
   * 需求：用户信息的增删改查
   
   * 设计：
     
     * 技术选型：Servlet+Jsp+MySQL+JDBCTemplate+Druid+BeanUtils+tomcat
     * 数据库设计
   
   * 实现：
     
     > 1. 环境搭建

# Filter和Listener

### 1. Filter

1. 过滤器：当访问服务器的资源时，过滤器可以将请求拦截，完成一些特殊的功能

2. 过滤器的作用
   
   * 一般用于完成通用的操作，例：登录验证，统一编码处理，敏感字符处理。

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
   >    
   >    * 注解方式配置
   
   ```java
   package cn.itcast.filter;
   
   import javax.servlet.*;
   import javax.servlet.annotation.WebFilter;
   import java.io.IOException;
   
   @WebFilter("/*")
   public class FilterDemo1 implements Filter {
       @Override
       public void init(FilterConfig filterConfig) throws ServletException {
   
       }
   
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

4. 核心API
   
   > 核心接口：Filter，FilterChain，FilterConfig
   
   * Filter接口
     
     ![image-20211122194305974](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211122194305974.png)
   
   * FilterChain接口
     
     > FilterChain接口位于javax.servlet包中，由容器实现。该接口中只包含一个方法doFilter(ServletRequest request,ServletResponse response)，主要用于将过滤器处理的请求或响应传递给下一个过滤器对象。

5. 细节
   
   * web.xml配置
     
     ```xml
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
     ```
   
   * 过滤器执行流程
   
   * 过滤器生命周期
   
   * 过滤器配置详解
     
     * 拦截路径配置
       
       > * 具体资源路径，例：/index.jsp
       > * 拦截目录，例：/user/*
       > * 后缀名拦截，例：*.jsp
       > * 拦截所有路径，例：/*
     
     * 拦截方式配置（资源被访问的方式）
       
       > 注解配置
       > 
       > * 设置dispatcherType属性
       >   * REQUEST：默认值，浏览器直接请求资源
       >   * FORWARD：转发访问资源
       >   * INCLUDE：包含访问资源
       >   * ERROR：错误跳转资源
       >   * ASYNC：异步访问资源
       > 
       > web.xml配置
       > 
       > ​    设置dispatcher标签
   
   * 过滤器链
     
     * 执行顺序：先1后2
       
       > 先后顺序问题：
       > 
       > * 注解配置：按照类名的字符串比较规则比较，值小的先执行
       > * web.xml配置：谁定义在上面谁先执行

6. 案例：**登录验证**
   
   * 需求
     
     > 访问资源，验证其是否登录
     > 
     > 若果登录了，则直接放行
     > 
     > 如果没有登录，则跳转到登录页面，提示“您尚未登录，请先登录”
   
   * 分析

7. 案例：**敏感词汇过滤**

### 2. Listener

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

# JQuery

## 一、JQuery基础

### 1. 概念

1. 概念：一个JavaScript框架，用于简化JS开发。

2. JavaScript框架本质：一些js文件，封装了js的原生代码而已。

3. 基本语法：
   
   > Query 语法是为 HTML 元素的选取编制的，可以对元素执行某些操作。
   > 
   > 基础语法是：*$(selector).action()*
   > 
   > - 美元符号定义 jQuery
   > - 选择符（selector）“查询”和“查找” HTML 元素
   > - jQuery 的 action() 执行对元素的操作

### 2. 快速入门

1. 步骤
   
   > 1. 下载JQuery
   >    
   >    * 版本说明：
   >      
   >      目前jQuery有三个大版本:
   >      1.x:兼容ie678,使用最为广泛的，官方只做BUG维护，
   >      功能不再新增。因此一般项目来说，使用1.x版本就可以了，
   >      最终版本: 1.12.4 (2016年5月20日)
   >      2.x:不兼容ie678，很少有人使用，官方只做BUG维护，
   >      功能不再新增。如果不考虑兼容低版本的浏览器可以使用2.x,
   >      最终版本: 2.2.4 (2016年5月20日)
   >      3.x:不兼容ie678，只支持最新的浏览器。除非特殊要求，
   >      一般不 会使用3. x版本的，很多老的jQuery插件不支持这个版本。
   >      目前该版本是官方主要更新维护的版本。最新版本: 3.2.1 (2017年3月20日 )
   >      
   >      注意：jquery-xxx.js与jquery-xxx.min.js
   >      
   >      * jquery-xxx.js：开发版本，用于程序开发人员查阅，有良好的缩进和注释
   >      * jquery-xxx.min.js：生产版本，程序中使用，没有缩进，体积较小，便于加载
   > 
   > 2. 导入JQuery的js文件
   >    
   >    * 导入本地库文件
   >    
   >    * 导入远程库文件
   >      
   >      * 使用 Google 的 CDN
   >      
   >      ```javascript
   >      <head>
   >      <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs
   >      /jquery/1.4.0/jquery.min.js"></script>
   >      </head>
   >      ```
   >      
   >      * 使用 Microsoft 的 CDN
   >      
   >      ```javascript
   >      <head>
   >      <script type="text/javascript" src="http://ajax.microsoft.com/ajax/jquery
   >      /jquery-1.4.min.js"></script>
   >      </head>
   >      ```
   > 
   > 3. 使用
   
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>JQuery快速入门</title>
       <script src="js/jquery-3.6.0.min.js"></script>
   </head>
   <body>
       <div id="div1">div1...........</div>
       <div id="div2">div2...........</div>
   
       <script>
           var div1 = $("#div1");
           alert(div1.html());
       </script>
   </body>
   </html>
   ```

### 3. JQuery对象和JS对象区别于转换

1. JQuery对象在操作时，更加方便。
2. JQuery对象和JS对象方法不通用
3. 两者互相转换
   * jq->js：jq对象[索引]  或者  jq对象.get(索引)
   * js->jq：$(js对象)

### 4. 选择器

1. 选择器：筛选具有相似特征的元素（标签）

2. 基本语法：
   
   1. 事件绑定
   2. 入口函数
   3. 样式控制

3. 分类：
   
   > 1. 基本选择器
   >    
   >    * **标签选择器**：获得所有匹配标签名称的元素
   >      * 语法：$(“标签名”)
   >    * **id选择器**：获得与指定id匹配的元素
   >      * 语法：$(“#id的属性值”)
   >    * **类选择器**：获得与指定class属性匹配的元素
   >      * 语法：$(“.class的属性值”)
   >    * 并集选择器：获得多个选择器选中的元素
   >      * 语法：$(“选择器1，选择器2”)
   > 
   > 2. 层级选择器
   >    
   >    * **后代选择器**：选择A元素内部所有B元素
   >      * 语法：$(“A B”)
   >    * **子选择器**：选择A元素内部所有B子元素
   >      * 语法：$("A>B")
   > 
   > 3. 属性选择器
   >    
   >    * 属性名称选择器：包含指定属性的选择器
   >      * 语法：$(”A[属性名]“)
   >    * 属性选择器：包好指定属性等于指定值的选择器
   >      * 语法：$(“A[属性名='属性值']“)
   >    * 复合属性选择器：包含多个属性条件的选择器
   >      * 语法：$(”A[属性名=‘属性值’] [ ]........“)
   > 
   > 4. 过滤选择器
   >    
   >    * 首元素选择器：获得选择的元素中的第一个元素
   >      * 语法：:first
   >    * 尾元素选择器：获得选择的元素中的最后一个元素
   >      * 语法：:last
   >    * 非元素选择器：不包括指定内容的元素
   >      * 语法：:not（selector）
   >    * 偶数选择器：偶数，从0开始计数
   >      * 语法：:even 
   >    * 奇数选择器：奇数，从0开始计数
   >      * 语法：:odd 
   >    * 等于索引选择器：指定索引元素
   >      * 语法：:eq（index）
   >    * 大于索引选择器：大于指定索引的元素
   >      * 语法：:gt（index）
   >    * 标题选择器：获得标题元素，固定写法
   >      * 语法：:header
   > 
   > 5. 表单过滤选择器
   >    
   >    * 可用元素选择器：获得可用元素
   >      * 语法：:enabled
   >    * 不可用元素选择器：获得不可用元素
   >      * 语法：:disabled
   >    * 选中选择器：获得单选/复选框中的元素
   >      * 语法：:checked
   >    * 选中选择器：获得下拉框选中的元素
   >      * 语法：:selected

### 5. DOM操作

1. 内容操作
   * html()：获取/设置元素的标签体内容
   * text()：获取/设置元素标签体纯文本内容
   * val()：获取/设置元素文本内容
2. 属性操作
   * 通用属性操作
     * attr()：获取/设置元素的属性值
     * removeAttr()：删除属性
     * prop()：获取/设置元素的属性值
     * removeProp：删除属性
     * attr和prop区别：
       * 若操作固有属性，则建议使用prop
       * 若操作自定义属性，则建议使用attr
   * 对class属性的操作
     * addClass()：添加class属性值
     * removeClass()：删除class属性值
     * toggleClass()：切换class属性值
3. CRUD操作
   * append()：父元素将子元素追加到末尾（A.append(B)将B添加到A内部并且在末尾）
   * prepend()：父元素将子元素追加到开头
   * appendTo()：A.appendTo(B)将A添加到B内部并且在末尾
   * prependTo()：
   * after()：添加元素到元素后面（A.after(B)将B添加到A的后面且互为兄弟关系）
   * before()：添加元素到元素后面
   * insertAfter()：A.insertTo(B)将A添加到B后面
   * insertBefore()：
   * remove()：移除对象
   * empty()：清空元素的所有子元素

### 6. 案例

1. 案例一：隔行换色
   
   ```html
   <!DOCTYPE html>
   <html>
      <head>
         <meta charset="UTF-8">
         <title></title>
         <script  src="../js/jquery-3.6.0.min.js"></script>
   
         <script>
            //需求：将数据行的奇数行背景色设置为 pink，偶数行背景色设置为 yellow
         $(function () {
            $("tr:gt(1):odd").css("backgroundColor","pink");
            $("tr:gt(1):even").css("backgroundColor","yellow");
         });
   
         </script>
      </head>
      <body>
         <table id="tab1" border="1" width="800" align="center" >
            <tr>
               <td colspan="5"><input type="button" value="删除"></td>
            </tr>
            <tr style="background-color: #999999;">
               <th><input type="checkbox"></th>
               <th>分类ID</th>
               <th>分类名称</th>
               <th>分类描述</th>
               <th>操作</th>
            </tr>
            <tr>
               <td><input type="checkbox"></td>
               <td>1</td>
               <td>手机数码</td>
               <td>手机数码类商品</td>
               <td><a href="">修改</a>|<a href="">删除</a></td>
            </tr>
            <tr>
               <td><input type="checkbox"></td>
               <td>2</td>
               <td>电脑办公</td>
               <td>电脑办公类商品</td>
               <td><a href="">修改</a>|<a href="">删除</a></td>
            </tr>
            <tr>
               <td><input type="checkbox"></td>
               <td>3</td>
               <td>鞋靴箱包</td>
               <td>鞋靴箱包类商品</td>
               <td><a href="">修改</a>|<a href="">删除</a></td>
            </tr>
            <tr>
               <td><input type="checkbox"></td>
               <td>4</td>
               <td>家居饰品</td>
               <td>家居饰品类商品</td>
               <td><a href="">修改</a>|<a href="">删除</a></td>
            </tr>
         </table>
      </body>
   </html>
   ```

2. 案例二：全选和不全选
   
   ```html
   <!DOCTYPE html>
   <html>
      <head>
         <meta charset="UTF-8">
         <title></title>
         <script  src="../js/jquery-3.6.0.min.js"></script>
         <script>
            function selectAll(object) {
               $(".itemSelect").prop("checked",object.checked);
            };
         </script>
      </head>
      <body>
         <table id="tab1" border="1" width="800" align="center" >
            <tr>
               <td colspan="5"><input type="button" value="删除"></td>
            </tr>
            <tr>
               <th><input type="checkbox" onclick="selectAll(this)"></th>
               <th>分类ID</th>
               <th>分类名称</th>
               <th>分类描述</th>
               <th>操作</th>
            </tr>
            <tr>
               <td><input type="checkbox" class="itemSelect"></td>
               <td>1</td>
               <td>手机数码</td>
               <td>手机数码类商品</td>
               <td><a href="">修改</a>|<a href="">删除</a></td>
            </tr>
            <tr>
               <td><input type="checkbox" class="itemSelect"></td>
               <td>2</td>
               <td>电脑办公</td>
               <td>电脑办公类商品</td>
               <td><a href="">修改</a>|<a href="">删除</a></td>
            </tr>
            <tr>
               <td><input type="checkbox" class="itemSelect"></td>
               <td>3</td>
               <td>鞋靴箱包</td>
               <td>鞋靴箱包类商品</td>
               <td><a href="">修改</a>|<a href="">删除</a></td>
            </tr>
            <tr>
               <td><input type="checkbox" class="itemSelect"></td>
               <td>4</td>
               <td>家居饰品</td>
               <td>家居饰品类商品</td>
               <td><a href="">修改</a>|<a href="">删除</a></td>
            </tr>
         </table>
      </body>
   </html>
   ```

3. 案例三：qq表情
   
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="UTF-8" />
       <title>QQ表情选择</title>
       <script  src="../js/jquery-3.6.0.min.js"></script>
       <style type="text/css">
       *{margin: 0;padding: 0;list-style: none;}
   
       .emoji{margin:50px;}
       ul{overflow: hidden;}
       li{float: left;width: 48px;height: 48px;cursor: pointer;}
       .emoji img{ cursor: pointer; }
       </style>
      <script>
           //需求：点击qq表情，将其追加到发言框中
           $(function () {
               // $("ul img").click(function () {
               //     $(".word img").prop("src",this.src);
               // });
               $("ul img").click(function () {
                   $(".word").append($(this).clone());
               });
   
           });
          </script>
       </head>
      <body>
          <div class="emoji">
              <ul>
                  <li><img src="img/01.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/02.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/03.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/04.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/05.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/06.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/07.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/08.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/09.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/10.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/11.gif" height="22" width="22" alt="" /></li>
                  <li><img src="img/12.gif" height="22" width="22" alt="" /></li>
              </ul>
              <p class="word">
                  <strong>请发言：</strong>
      <!--            <img src="img/12.gif" height="22" width="22" alt="" />-->
              </p>
          </div>
      </body>
      </html>
   ```

4. 案例四：下拉列表的左右移动   

```html
   <!DOCTYPE html>
   <html>
      <head>
         <meta charset="UTF-8">
         <title></title>
         <script  src="../js/jquery-3.6.0.min.js"></script>
    <style>
        #leftName , #btn,#rightName{
           float: left;
           width: 100px;
           height: 300px;
        }
        #toRight,#toLeft{
           margin-top:100px ;
           margin-left:30px;
           width: 50px;
        }

        .border{
           height: 500px;
           padding: 100px;
        }
     </style>

     <script>

        //需求：实现下拉列表选择条目左右选择功能
        $(function () {
           $("#toRight").click(function () {
              $("#rightName").append($("#leftName > option:selected"));
           });
           $("#toLeft").click(function () {
              $("#leftName").append($("#rightName>option:selected"));
           });
        });

     </script>

​    
​      </head>
​      <body>
​         <div class="border">
​            <select id="leftName" multiple="multiple">
​               <option>张三</option>
​               <option>李四</option>
​               <option>王五</option>
​               <option>赵六</option>
​            </select>
​            <div id="btn">
​               <input type="button" id="toRight" value="-->"><br>
​               <input type="button" id="toLeft" value="<--">
​    
​            </div>
​    
            <select id="rightName" multiple="multiple">
               <option>钱七</option>
            </select>
    ​         </div>
​      </body>

</html
```

## 二、JQuery高级

### 1. 动画

1. 三种方式显示和隐藏元素
   
   * 默认显示和隐藏方式
     
     > show([speed,[easing],[fn]]);
     > 
     > hide([speed,[easing],[fn]]);
     > 
     > toggle([speed,[easing],[fn]]);
   
   * 滑动显示和隐藏方式
     
     > slideDown([speed,[easing],[fn]]);
     > 
     > slideUp([speed,[easing],[fn]]);
     > 
     > slidetoggle([speed,[easing],[fn]]);
   
   * 淡入淡出显示和隐藏方式
     
     > fadeIn([speed,[easing],[fn]]);
     > 
     > fadeOut([speed,[easing],[fn]]);
     > 
     > fadetoggle([speed,[easing],[fn]]);
   
   说明：
   
   * 参数：
     * speed：动画的速度，三个预定义的值“slow”，“normal”，“fast”或表示动画时长的毫秒数（如：1000）
     * easing：用来指定切换效果，默认是“swing”，可用参数“linear”
       * swing：动画执行时效果是，先慢，中间快，最后又慢
       * linear：动画执行时是匀速的
     * fn：动画完成时执行的函数，每个元素执行一次

### 2. 遍历

1. js的遍历方式
   * for（初始化值；循环结束条件；步长）
2. JQuery的遍历方式
   * JQuery对象.each（callback）
   * $.each（Object，[callback]）
   * for..of（JQuery3.0之后提供的方式），for（元素对象 of 容器对象）

### 3. 事件绑定

1. JQuery标准的绑定方式：JQuery对象.事件方法（回调函数）

2. on绑定事件/off解除绑定
   
   * JQuery对象.on（“事件名称”，回调函数）
   * JQuery对象.off（“事件名称”，回调函数）

3. 事件切换：toggle
   
   * JQuery对象.toggle（事件1，事件2）（JQuery1.9以后被删除了，需要借用插件实现）
   
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="UTF-8">
       <title></title>
       <script src="../js/jquery-3.6.0.min.js" type="text/javascript" charset="utf-8"></script>
       <script src="../js/jquery-migrate-1.0.0.js"></script>
       <script type="text/javascript">
   
           $(function () {
               $("#btn").toggle(function () {
                   $("#myDiv").css("backgroundColor","green");
               },function () {
                   $("#myDiv").css("backgroundColor","pink");
               });
           })
   
       </script>
   </head>
   <body>
   
       <input id="btn" type="button" value="事件切换">
       <div id="myDiv" style="width:300px;height:300px;background:pink">
           点击按钮变成绿色，再次点击红色
       </div>
   </body>
   </html>
   ```

### 4. 案例

1. 广告的显示和隐藏
   
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="UTF-8">
       <title>广告的自动显示与隐藏</title>
       <style>
           #content{width:100%;height:500px;background:#999}
       </style>
   
       <!--引入jquery-->
       <script type="text/javascript" src="../js/jquery-3.6.0.min.js"></script>
       <script>
           /*
           * 需求：
           * 1. 当页面加载完成3秒后自动显示广告
           * 2. 广告显示5秒后自动消失
           * */
           $(function () {
               setTimeout(function () {
                   $("#ad").slideToggle("slow","linear");
                   setTimeout(function () {
                       $("#ad").slideToggle("slow","linear");
                   },5000);
               },3000);
           })
       </script>
   </head>
   <body>
   <!-- 整体的DIV -->
   <div>
       <!-- 广告DIV -->
       <div id="ad" style="display: none;">
           <img style="width:100%" src="../img/adv.jpg" />
       </div>
   
       <!-- 下方正文部分 -->
       <div id="content">
           正文部分
       </div>
   </div>
   </body>
   </html>
   ```

2. 抽奖
   
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="UTF-8">
       <title>jquery案例之抽奖</title>
       <script type="text/javascript" src="../js/jquery-3.6.0.min.js"></script>
       <script>
           var imgs = [
               "../img/man00.jpg",
               "../img/man01.jpg",
               "../img/man02.jpg",
               "../img/man03.jpg",
               "../img/man04.jpg",
               "../img/man05.jpg",
               "../img/man06.jpg"
           ];
   
           $(function () {
               var interval
               var index;
               $("#startID").click(function () {
                    interval = setInterval(function () {
                   index = Math.floor(7 * Math.random());
                   $("#img1ID").prop("src",imgs[index]);
                   },30);
               });
   
               $("#stopID").click(function () {
                   clearInterval(interval);
                   $("#img2ID").prop("src",imgs[index]);
               });
           });
       </script>
   </head>
   <body>
   
   <!-- 小像框 -->
   <div style="border-style:dotted;width:160px;height:100px">
       <img id="img1ID" src="../img/man00.jpg" style="width:160px;height:100px"/>
   </div>
   
   <!-- 大像框 -->
   <div
           style="border-style:double;width:800px;height:500px;position:absolute;left:500px;top:10px">
       <img id="img2ID" src="../img/man00.jpg" width="800px" height="500px"/>
   </div>
   
   <!-- 开始按钮 -->
   <input
           id="startID"
           type="button"
           value="点击开始"
           style="width:150px;height:150px;font-size:22px">
   
   <!-- 停止按钮 -->
   <input
           id="stopID"
           type="button"
           value="点击停止"
           style="width:150px;height:150px;font-size:22px">
       <!--<script language='javascript' type='text/javascript'>
          //准备一个一维数组，装用户的像片路径
          var imgs = [
              "../img/man00.jpg",
              "../img/man01.jpg",
              "../img/man02.jpg",
              "../img/man03.jpg",
              "../img/man04.jpg",
              "../img/man05.jpg",
              "../img/man06.jpg"
          ];
      var interval;
      var index;
      function imgStart() {
          interval = setInterval(function () {
              index = Math.floor(7*Math.random());
              $("#img1ID").prop("src",imgs[index]);
          },50);
      }
      function imgStop() {
          clearInterval(interval);
          $("#img2ID").prop("src",imgs[index]);
      }
      </script>-->
      </body>
   </html>
   ```


### 5. 插件

1. 作用：增强JQuery功能
2. 实现方式：
   * $.fn.extend(object)：增强通过JQuery获取的对象的功能     \$("#id")
   * $.extend(object)：增强JQuery对象自身的功能，\$/JQuery

# Ajax

1. 概念：Asynchronous JavaScript And XML 异步的JavaScript和XML
   
   * 异步与同步：客户端与服务器相互通信的基础
     
     ![image-20220317162519680](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220317162519680.png)
   
   * Ajax是一种在无需重新加载整个网页的情况下能够更新部分网页的技术。通过在后台与服务器进行少量数据交流，Ajax可以使网页实现异步更新。这意味着可以在不重新加载整个网页的前提下，对网页的某部分进行更新。传统的网页（不使用Ajax）如果需要更新内容，必须重新加载整个网页页面。

2. 作用
   
   * 与服务器进行数据交换
     * 使用Ajax和服务器通信，可以使用HTMl+Ajax替换jsp
   * 异步交互
   
3. 实现方式：

   * 原生的Js实现方式

     ~~~ html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <title>ajax测试</title>
     </head>
     <body>
         <script>
             //1.创建核心对象
             var xmlhttp;
             if (window.XMLHttpRequest)
             {
                 //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
                 xmlhttp=new XMLHttpRequest();
             }
             else
             {
                 // IE6, IE5 浏览器执行代码
                 xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
             }
             //2.发送请求
             xmlhttp.open("GET","http://localhost:8080/SpringIoc_war_exploded/ajaxServletDemo",true);
             xmlhttp.send();
             //3.获得响应
             xmlhttp.onreadystatechange=function()
             {
                 if (xmlhttp.readyState==4 && xmlhttp.status==200)
                 {
                     alert(xmlhttp.responseText);
                 }
             }
     
         </script>
     </body>
     </html>
   
   * JQuery实现方式
     
     * $.ajax({键值对})
       
       ```html
       <!DOCTYPE html>
       <html lang="en">
       <head>
           <meta charset="UTF-8">
           <title>JQuery实现Ajax</title>
           <script src="js/jquery-3.6.0.min.js"></script>
           <script>
               function fun() {
                   $.ajax({
                       url:"ajaxServlet",//请求路径
                       type:"POST",//请求方式
                       // date:"userName=jack&Tom";//请求参数
                       date:{"userName":"jack","gender":"man"},
                       success:function(){
                           alert("kjdf kfdj ");
                       },
                       error:function () {
                           alert("error");
                       }
       
                   });
               }
           </script>
       </head>
       <body>
           <input type="button" value="sendAsynchronousMessage" onclick="fun()">
           <input>
       </body>
       </html>
       ```
       
     * $.get(url,[data],[callback],[type])：发送get请求
     
     * $.post()
   
4. Axios框架

   官网：https://www.axios-http.cn/

   * 快速入门

     ![image-20220317171321550](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220317171321550.png)

# JSON

1. 概念：**JavaScript Object Notation**，JavaScript对象标记法
   * JSON是一种存储和交换数据的语法
   * JSON是一种轻量级的**数据交换格式**
   
2. 语法

   json的语法可以表示以下三种类型的值。

   * 简单值
   * 对象
     * 对象的属性必须加双引号
   * 数组

   > 注意：一定要清晰认识到json是一种数据格式，而非一种编程语法。json的表示和JavaScript对象的表示很相似。但是有如下区别：
   >
   > * javaScript对象结尾有分号，json没有，应为json不是语句
   > * JavaScript对象的属性可以使用分号引起，也可以不使用，但是json必须使用双引号引起

3. JSON与XML

4. 解析与序列化

   * JSON对象：在JavaScript中可以使用全局对象JSON的两个方法，分别为stringify（）和parse来达到将JavaScript对象序列化为JSON字符串和把JSON字符串解析为原生JavaScript值的效果。

5. JSON数据和java对象的转换（fastjson）

   * 请求数据：JSON字符串转为java对象
   * 响应数据：java对象转为JSON字符串

   > ![image-20220317155620854](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220317155620854.png)
   >
   > ~~~ java
   > import com.alibaba.fastjson.JSON;
   > 
   > public class FastJsonDemo {
   >     public static void main(String[] args) {
   >         User user = new User();
   >         user.setId(1);
   >         user.setName("chen");
   >         user.setAge(20);
   >         user.setAddr("cduestc");
   > 
   >         String s = JSON.toJSONString(user);
   >         System.out.println(s);
   > 
   >         User user1 = JSON.parseObject(s,User.class);
   >         System.out.println(user1);
   > 
   >     }
   > }

# Layui

官网：https://www.layui.site/index.htm

## 快速上手

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <title>开始使用 layui</title>
  <link rel="stylesheet" href="./layui/css/layui.css">
</head>
<body>

<!-- 你的 HTML 代码 -->

<script src="./layui/layui.js"></script>
<script>
layui.use(['layer', 'form'], function(){
  var layer = layui.layer
  ,form = layui.form;

  layer.msg('Hello World');
});
</script> 
</body>
</html>
```

## 页面元素

### 1. 布局

#### 布局容器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>布局容器</title>
    <link href="../layui/css/layui.css" rel="stylesheet" type="text/css">
</head>
<body>
    <!--
        布局容器
            1. 固定宽度（两侧有留白）
            2. 完成宽度（占据屏幕的完整宽度）
     -->

    <!--固定宽度-->
    <div class="layui-container" style="background: #00F7DE;height: 500px">

    </div>
    <!--完整宽度-->
    <div class="layui-fluid" style="background: #00F7DE;height: 500px">

    </div>

</body>
</html>
```

#### 栅格系统

1. 列组合
2. 列边距
3. 列偏移
4. 列嵌套

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>布局容器</title>
    <link href="../layui/css/layui.css" rel="stylesheet" type="text/css">
</head>
<body>
    <div class="layui-container">
        <div class="layui-row">
            <div class="layui-col-md5" style="background: #00F7DE">内容的5/12</div>
            <div class="layui-col-md7" style="background: #1E9FFF">内容的7/12</div>
        </div>
        <div class="layui-row">
            <div class="layui-col-md3" style="background: #00F7DE">内容的3/12</div>
            <div class="layui-col-md9" style="background: #1E9FFF">内容的9/12</div>
        </div>
    </div>
</body>
</html>
```

# Bootstrap

# Redis

# Maven

## 一、Maven基础

### 1.什么是Maven

maven本质是一个项目管理工具，将项目开发和管理过程抽象为一个项目对象模型（POM）

![image-20211003195950696](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211003195950696.png)

### 2. Maven能解决什么问题（作用）

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

* src\main\java目录：核心代码
* src\main\resources：配置文件部分
* src\main\webapp：页面资源（js,css,图片等资源）
* src\test\java：测试代码部分
* src\test\resources：测试配置文件
* pom.xml：项目的核心配置文件

![image-20211001224629124](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211001224629124.png)

### 4. Maven仓库

* 本地仓库
* 远程仓库（私服）
* 中央仓库

![image-20211001222603530](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211001222603530.png)

### 5. Maven坐标

1. 坐标：被Maven管理的资源的唯一标识
   
   > groupid：组织名称
   > 
   > atifactid：模块名称
   > 
   > version：版本号
   > 
   > package：定义该项目的打包方式（不是maven坐标的组成）

### 6. 仓库配置

1. 本地仓库配置
   
   在maven安装目录中找到conf\settings.xml更改如下标签中的路径位置
   
   ```xml
   <localRepository>/path/to/local/repo</localRepository>
   ```

2. 远程仓库配置

### 7. Maven常用命令

> * compile：编译
> * clean：清理
> * pakage：打包
> * test：测试
> * install：安装到本地仓库

### 8. Maven的生命周期与插件

1. Maven对项目构建的生命周期划分为3套
   
   > clean：清理工作
   > 
   > default：核心工作，例如：编译，测试，打包，部署等
   > 
   > site：产生报告，发布站点等

### 9.创建Maven项目

1. 手工制作

2. 使用插件创建工程
   
   ![image-20211004153002024](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211004153002024.png)

3. idea创建
   
   * 不使用骨架
     
     * java项目
     
     * web项目
       
       * 添加tomacat插件
         
         ![image-20211004161944412](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211004161944412.png)
   
   * 使用骨架
     
     * java项目
     
     * web项目
       
       * 添加tomcat插件
         
         ![image-20211004161939251](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20211004161939251.png)

### 10. 依赖管理

1. 依赖配置
   
   > 依赖：当前项目运行所需要的的jar，一个项目可以设置多个依赖
   > 
   > 格式：
   > 
   > <!-- 所有当前项目依赖的所有jar-->
   > 
   > <dependencies>
   > 
   > ​    <!-- 具体的依赖-->
   > 
   > ​    <dependency>
   > 
   > ​        <groupId><groupId/>
   > 
   > ​        <artifacted></artifacted>
   > 
   > ​        <version></version>
   > 
   > ​    <dependency/>
   > 
   > </dependencies>

2. 依赖传递

3. 可选依赖
   
   > 在依赖中添加选项
   > 
   > <optional>true</optional>

4. 排除依赖

5. 依赖范围
   
   > 依赖的jar默认在所有范围内均可使用，可以通过scope标签来设置其作用范围
   > 
   > 作用范围：
   > 
   > * 主程序范围有效（main文件夹范围内）
   > * 测试程序范围有效（test文件夹范围内）
   > * 是否参与打包（package指令范围内）

## 二、Maven高级

# Spring

学习参考视频：https://www.bilibili.com/video/BV1WZ4y1P7Bp?p=1

## 一、Spring简介

1. spring是什么
   
   spring是分层的的javaSE/EE应用full-stack**轻量级开源框架**，以IOC（inverse of control:反转控制）和AOP（aspect oriented programing:面向切面编程）为内核。提供了展现层SpringMVC和持久层Spring JDBCTemplate以及业务层事务管理等众多的企业级应用技术，还能整合开源世界众多著名的第三方框架和类库，逐渐成为使用最多的JavaEE企业应用开源框架。
   
   * 控制反转：（IOC是一种思想）
     * 控制：指谁来控制对象的创建。传统应用程序对象是由程序本身通过new关键字来控制。而使用Spring后，由Spring通过反射机制来创建对象。
     * 反转：程序本身不去创建对象而变为被动的接收对象。

2. 理念：使现有技术更加实用。

3. Spring发展历程
   
   ![image-20220117162012206](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220117162012206.png)

4. Spring的优势
   
   * 方便解耦，简化开发
   * AOP编程的支持
   * 声明式事务的支持
   * 方便程序的测试
   * 方便集成各种优秀框架
   * 减低JavaEE API的使用难度
   * java源码经典学习范例

5. SPring的体系结构
   
   ![image-20220117162143652](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220117162143652.png)

## 二、Spring快速入门

1. Spring程序开发步骤
   * 导入Spring开发的基本包坐标
   * 编写Dao接口和实现类
   * 创建Spring核心配置文件
   * 在Spring配置文件中配置UserDapImpl
   * 使用Spring的API获得Bean实例

## 三、Spring配置文件

### bean的配置

1. Bean标签的基本配置
   
   用于配置对象交由Spring来创建。默认情况下它调用的是类中的无参构造函数，如果没有无参构造函数则不能创建成功。
   
   基本属性：
   
   * id：Bean实例在Spring容器中的唯一标识
   * class：Bean的全限定名

2. Bean标签的范围配置
   
   scope：指定对象的作用范围，取值如下：
   
   | 取值范围      | 说明                                              |
   | --------- | ----------------------------------------------- |
   | singleton | 默认值，单例的                                         |
   | prototype | 多例的                                             |
   | request   | web项目中，spring创建一个Bean对象，将对象存入到request域中         |
   | session   | web项目中，spring创建一个Bean的对象，将对象存入到session域中        |
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
   * 工厂静态方法实例化（factory-method属性指定类中实例化方法）
   * 工厂实例方法实例化（factory-bean和factory-method属性指定实例化方法）

5. Bean的依赖注入（Dependency injection）
   
   * 概念：是Spring框架核心IOC的具体实现
   
   * 注入方式：
     
     * set方法
       
       * P命名空间注入本质也是set方法注入。
         
         ![image-20220118193841130](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220118193841130.png)
     
     * 有参构造
   
6. 依赖注入的数据类型

   * 普通数据类型

     ~~~xml
     <property name="" value=""></property>

   * 引用数据类型

     ~~~xml
     <property name="" ref=""></property>

   * 集合数据类型

     ~~~xml
     <property name="">
         <list>
             <value></value>
             <value></value>
         </list>
         <map name="">
             <entry key="" value=""></entry>
         </map>
     </property>

7. 引入其他配置文件（分模块开发）
   
   ```xml
   <import resource"" />
   ```

### 配置数据源（连接池）

1. 数据源的作用：事先实例化数据源，初始化部分连接资源

   > 常见的数据源：DBCP，C3P0，BoneCP，Druid

2. 数据源开发步骤

   * 导入数据源和数据库驱动坐标
   * 创建数据源对象
   * 设置数据源基本连接数据
   * 使用数据源获取连接资源和归还连接资源

3. 手动配置数据源

   ~~~java
   package com.chen.test;
   
   import com.alibaba.druid.pool.DruidDataSource;
   import com.alibaba.druid.pool.DruidPooledConnection;
   import com.mchange.v2.c3p0.ComboPooledDataSource;
   import org.junit.Test;
   
   import java.beans.PropertyVetoException;
   import java.sql.Connection;
   import java.sql.SQLException;
   import java.util.ResourceBundle;
   
   public class DataSource {
   
       /**
        * 测试手动创建c3p0数据源
        */
       @Test
       public void test1() throws PropertyVetoException, SQLException {
           ComboPooledDataSource dataSource = new ComboPooledDataSource();
   
           //手动配置数据库信息
           /*dataSource.setDriverClass("com.mysql.cj.jdbc.Driver");
           dataSource.setJdbcUrl("jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC");
           dataSource.setUser("root");
           dataSource.setPassword("4112");*/
   
           //加载配置文件配置数据库信息
           ResourceBundle rb = ResourceBundle.getBundle("jdbc");
           String driver = rb.getString("jdbc.driver");
           String url = rb.getString("jdbc.url");
           String username = rb.getString("jdbc.username");
           String password = rb.getString("jdbc.password");
   
           dataSource.setDriverClass(driver);
           dataSource.setJdbcUrl(url);
           dataSource.setUser(username);
           dataSource.setPassword(password);
   
           Connection connection = dataSource.getConnection();
           System.out.println(connection);
           connection.close();
       }
   
       /**
        * 测试手动创建druid数据源
        */
       @Test
       public void test2() throws Exception {
           DruidDataSource druidDataSource = new DruidDataSource();
   
           druidDataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
           druidDataSource.setUrl("jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC");
           druidDataSource.setUsername("root");
           druidDataSource.setPassword("4112");
   
           DruidPooledConnection connection = druidDataSource.getConnection();
           System.out.println(connection);
           connection.close();
   
       }
   }
   
   ===========================================================
   //jdbc.properties
   jdbc.driver=com.mysql.cj.jdbc.Driver
   jdbc.url=jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC
   jdbc.username=root
   jdbc.password=4112
   ~~~

4. Spring配置数据源

   ```java
   package com.chen.testdatasource;
   
   import org.junit.Test;
   import org.springframework.context.support.ClassPathXmlApplicationContext;
   
   import javax.sql.DataSource;
   import java.sql.Connection;
   import java.sql.SQLException;
   
   public class DataSource2 {
   
       /**
        * 测试使用Spring容器产生数据源(c3p0)
        */
       @Test
       public void test() throws SQLException {
           ClassPathXmlApplicationContext ioc = new ClassPathXmlApplicationContext("applicationContext3.xml");
           DataSource dataSource = (DataSource)ioc.getBean("dataSource");
           Connection connection = dataSource.getConnection();
           System.out.println(connection);
           connection.close();
       }
   
       /**
        * 测试使用Spring容器产生数据源(druid)
        */
       @Test
       public void test2() throws SQLException {
           ClassPathXmlApplicationContext ioc = new ClassPathXmlApplicationContext("applicationContext3.xml");
           DataSource dataSource = (DataSource)ioc.getBean("dataSource2");
           Connection connection = dataSource.getConnection();
           System.out.println(connection);
           connection.close();
       }
   }
   ```

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
   
       <bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
           <property name="driverClass" value="com.mysql.cj.jdbc.Driver"></property>
           <property name="jdbcUrl" value="jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC"></property>
           <property name="user" value="root"></property>
           <property name="password" value="4112"></property>
       </bean>
   
       <bean id="dataSource2" class="com.alibaba.druid.pool.DruidDataSource">
           <property name="driverClassName" value="com.mysql.cj.jdbc.Driver"></property>
           <property name="url" value="jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC"></property>
           <property name="username" value="root"></property>
           <property name="password" value="4112"></property>
       </bean>
   
   </beans>
   ```

5. 抽取jdbc配置文件

   ![image-20220317195738972](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220317195738972.png)

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:context="http://www.springframework.org/schema/context"
          xsi:schemaLocation="
          http://www.springframework.org/schema/beans
          http://www.springframework.org/schema/beans/spring-beans.xsd
          http://www.springframework.org/schema/context
          http://www.springframework.org/schema/context/spring-context.xsd">
   
       <!--加载外部配置文件-->
       <context:property-placeholder location="classpath:jdbc.properties"/>
   
       <bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
           <property name="driverClass" value="${jdbc.driver}"></property>
           <property name="jdbcUrl" value="${jdbc.url}"></property>
           <property name="user" value="${jdbc.username}"></property>
           <property name="password" value="${jdbc.password}"></property>
       </bean>
   
       <bean id="dataSource2" class="com.alibaba.druid.pool.DruidDataSource">
           <property name="driverClassName" value="${jdbc.driver}"></property>
           <property name="url" value="${jdbc.url}"></property>
           <property name="username" value="${jdbc.username}"></property>
           <property name="password" value="${jdbc.password}"></property>
       </bean>
   
   </beans>
   ```

### 配置知识点总结：

> <bean>标签：
> 
> * id属性：容器中Bean实例的唯一标识，不允许重复
> * class属性：要实例化的Bean的全限定名
> * scope属性：Bean的作用范围
> * <property>标签：属性注入
>   * name属性：属性名称
>   * value属性：注入的普通属性名称
>   * ref属性：注入的对象引用值
>   * <list>标签
>   * \<map>标签
>   * <properties>标签
> * <constructor-arg>标签
> 
> <import>标签：导入其他的spring的分文件

## 四、Spring相关API

1. ApplicationContext继承体系

   ![image-20220120200453261](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220120200453261.png)

2. ApplicationContext实现类
   * ClassPathXmlApplicationContext：从类的根路径下加载配置文件（推荐使用）
   * FileSystemXmlApplicationContext：从磁盘路径上加载配置文件，配置文件可以在磁盘的任意位置
   * AnnoationConfigApplicationContext：使用注解配置容器对象时使用

3. getBean()方法
   * 传递id
   * 传递class

## 五、Spring注解开发

1. Spring原始注解（主要代替<bean>标签的配置）
   
   Spring是轻代码中配置的框架，配置比较繁重，影响开发效率，所以注解开发是一种趋势。

   ![image-20220317200213868](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220317200213868.png)
   
   > 注意：
   >
   > * 使用注解时需要进行组件扫描配置
   >
   >   ![image-20220317225758957](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220317225758957.png)
   >
   > * Qualifier
   >
   >   ~~~java
   >       @Autowired//按照类型从Spring容器中进行匹配
   >       @Qualifier("userDao")//按照id值从容器中进行匹配，但是需要结合@Autowired使用
   >       private UserDao userDao;
   
2. Spring新注解

   * 使用场景：
     
     * 非自定义的Bean（即当使用第三方包时无法使用原始注解）
     * 加载properties配置文件时
     * 组件扫描配置
     * 引入其他文件

   * 新注解
     
     ![image-20220318093850296](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318093850296.png)

   ~~~ java
   //核心配置类
   import com.alibaba.druid.pool.DruidDataSource;
   import org.springframework.beans.factory.annotation.Value;
   import org.springframework.context.annotation.Bean;
   import org.springframework.context.annotation.ComponentScan;
   import org.springframework.context.annotation.Configuration;
   import org.springframework.context.annotation.PropertySource;
   
   import javax.sql.DataSource;
   
   @Configuration//表明为Spring核心配置类
   @ComponentScan("com.chen")//包扫描
   @PropertySource("classpath:jdbc.properties")//加载jdbc配置文件
   public class SpringConfiguration {
   
       @Value("${jdbc.driver}")
       private String driverClassName;
   
       @Value("${jdbc.url}")
       private String url;
   
       @Value("${jdbc.username}")
       private String userName;
   
       @Value("${jdbc.password}")
       private String password;
   
       @Bean("dataSource")//将返回值添加到Spring容器中
       public DataSource getDataSource(){
           DruidDataSource dataSource = new DruidDataSource();
           dataSource.setDriverClassName(driverClassName);
           dataSource.setUrl(url);
           dataSource.setUsername(userName);
           dataSource.setPassword(password);
           return dataSource;
       }
   }
   =====================================================
       //测试
       @Test
       public void testDruidDataSource() throws SQLException {
   //        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
           AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfiguration.class);
           DataSource dataSource = (DataSource) context.getBean("dataSource");
           Connection connection = dataSource.getConnection();
           System.out.println(connection);
           connection.close();
       }

## 七、Spring集成Junit

1. 原始Junit测试Spring时存在的问题
   
   ![image-20220318100349528](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318100349528.png)

2. Spring集成Junit步骤
   
   > 1. 导入Spring集成Junit的坐标（spring-test）
   > 2. 使用@Runwith注解替换原来的运行期
   > 3. 使用@ContextConfiguration指定配置文件或配置类
   > 4. 使用@Autowired注入需要测试的对象
   > 5. 创建测试方法测试
   
   ~~~java
   package com.chen.test;
   
   import org.junit.Test;
   import org.junit.runner.RunWith;
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.test.context.ContextConfiguration;
   import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
   
   import javax.sql.DataSource;
   import java.sql.Connection;
   import java.sql.SQLException;
   
   @RunWith(SpringJUnit4ClassRunner.class)
   @ContextConfiguration("classpath:applicationContext.xml")
   public class SpringJunitTestDemo {
   
       @Autowired
       private DataSource dataSource;
   
       @Test
       public void test() throws SQLException {
           Connection connection = dataSource.getConnection();
           System.out.println(connection);
           connection.close();
       }
   }

## 八、Spring与Web集成

1. ApplicationContext的获取：被获取多次

2. 将ApplicationContext存储到ServletContext域中

   ![image-20220331204221605](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220331204221605.png)

3. Spring提供获取应用上下文的工具

   ![image-20220318103032314](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318103032314.png)

## 九、Spring JDBC Template

1. 简介

2. 开发步骤
   
   > 1. 导入spring-jdbc和spring-tx坐标
   > 2. 创建数据库表和实体
   > 3. 创建JdbcTemplate对象
   > 4. 执行数据库操作

3. 常用操作

# SPring MVC

参考文档：https://pdai.tech/files/kaitao-springMVC.pdf

## 1.  概述

SpringMVC是一种基于Java的实现MVC设计模型的请求驱动类型的轻量级Web框架，属于SpringFrameWork的后续产品，已经融合在Spring Web Flow中。SpringMVC已经成为目前最主流的MVC框架之一，并且随着Spring3.0 的发布,全面超越Struts2,成为最优秀的MVC框架。它通过一套注解， 让-个简单的Java类成为处理请求的控制器，而无须实现任何接口。同时它还支持RESTful编程风格的请求。

![image-20220318144526046](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318144526046.png)

1. SpringMVC开发步骤
   
   > 1. 导入SpringMVC相关坐标
   > 2. 配置SpringMVC核心控制器DispathcerServlet（web.xml中）
   > 3. 创建Controller类和视 图页面
   > 4. 使用注解配置Controller类中业务方法的映射地址
   > 5. 配置SpringMVC核心文件spring-mvc.xml
   > 6. 客户端发起请求测试
   
   ![image-20220318144920983](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318144920983.png)

2. SpringMvc组件解析
   
   ![](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318152049532.png)
   
   相关组件解析：
   
   > 1、前端控制器DispatcherServlet（不需要程序员开发）由框架提供，在web.xml中配置。
   > 作用：接收请求，响应结果，相当于转发器，中央处理器。
   > 
   > 2、处理器映射器HandlerMapping（不需要程序员开发）由框架提供。
   > 作用：根据请求的url查找Handler（处理器/Controller），可以通过XML和注解方式来映射。
   > 
   > 3、处理器适配器HandlerAdapter（不需要程序员开发）由框架提供。
   > 作用：按照特定规则（HandlerAdapter要求的规则）去执行Handler中的方法。
   > 
   > 4、处理器Handler（也称之为Controller，需要程序员开发）
   > 注意：编写Handler时按照HandlerAdapter的要求去做，这样适配器才可以去正确执行Handler。
   > 作用：接受用户请求信息，调用业务方法处理请求，也称之为后端控制器。
   > 
   > 5、视图解析器ViewResolver（不需要程序员开发）由框架提供。
   > 作用：进行视图解析，把逻辑视图解析成真正的物理视图。 
   > SpringMVC框架支持多种View视图技术，包括：jstlView、freemarkerView、ThymeleafView等。
   > 
   > 6、视图View（需要工程师开发）
   > 作用：把数据展现给用户的页面
   > View是一个接口，实现类支持不同的View技术（jsp、freemarker、pdf等）

3. SpringMVC注解解析
   
   ![image-20220318152957666](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318152957666.png)

4. SpringMVC配置文件解析

   ![image-20220331215507482](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220331215507482.png)

5. 接口了

## 2. SpringMVC的数据响应

1. 响应方式
   
   * 页面跳转
     
     * 直接返回字符串：该方式会将返回的字符串与视图解析器的前后缀拼接后跳转
     
       ![image-20220331220520124](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220331220520124.png)
     
     * 返回ModelAndView对象
     
   * 回写数据
     
     * 直接返回字符串
     
       * 方式一：给相应控制器方法传入HttpResponse对象
       * 方式二：使用@ResponseBody标注
     
     * 返回对象或集合（进行相应配置将对象自动转换为json数据格式）
       
       > * > 方式一：
       >   >
       >   > ```xml
       >   > <!--配置处理器映射器-->
       >   > <bean class="org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter">
       >   >     <property name="messageConverters">
       >   >         <list>
       >   >             <bean class="org.springframework.http.converter.json.MappingJackson2HttpMessageConverter"></bean>
       >   >         </list>
       >   >     </property>
       >   > </bean>
       >   > ```
       >
       > * 方式二：使用mvc的注解驱动来代替格式转换器的配置<mvc:annotion-driven/>
   
2. 代码示例及配置

   ```java
   package com.chen.controller;
   
   import com.chen.pojo.User;
   import com.fasterxml.jackson.core.JsonProcessingException;
   import com.fasterxml.jackson.databind.ObjectMapper;
   import org.springframework.stereotype.Controller;
   import org.springframework.web.bind.annotation.RequestMapping;
   import org.springframework.web.bind.annotation.ResponseBody;
   import org.springframework.web.servlet.ModelAndView;
   
   import javax.servlet.http.HttpServletRequest;
   
   @Controller
   @RequestMapping("/test")
   public class TestController {
   
       @RequestMapping("/save")
       public String save(){
           System.out.println("controller save1 running");
           return "success";//默认为转发
       }
   
       @RequestMapping("save2")
       public ModelAndView save2(){
           System.out.println("controller save2 running");
           //model 模型 作用是返回封装数据
           //view 视图 作用是封装数据
           ModelAndView modelAndView = new ModelAndView();
           modelAndView.addObject("userName","chen");
           modelAndView.setViewName("success");
           return modelAndView;
       }
   
       @RequestMapping("/save3")
       public ModelAndView save3(ModelAndView modelAndView){
           System.out.println("controller save3 running");
           modelAndView.addObject("password","123456");
           modelAndView.setViewName("success");
           return modelAndView;
       }
   
       @RequestMapping("/save4")
       public String save4(HttpServletRequest request){
           System.out.println("controller save4 running");
           return "success";
       }
   
       @RequestMapping("/save5")
       @ResponseBody//不进行视图跳转，直接进行数据回写
       public String save5(){
           System.out.println("controller save5 running");
           return "success";//通常返回json数据
       }
   
       @RequestMapping("/save6")
       @ResponseBody//不进行视图跳转，直接进行数据回写
       public String save6() throws JsonProcessingException {
           User user = new User("chen", (short) 20, "男");
   
           /*使用json转换工具将对象转换为json格式的字符串*/
           ObjectMapper objectMapper=new ObjectMapper();
           String s = objectMapper.writeValueAsString(user);
           return s;//通常返回json数据
       }
   
       @RequestMapping("/save7")
       @ResponseBody//不进行视图跳转，直接进行数据回写
       public User save7() {
           User user = new User("chen", (short) 20, "男");
           /*进行配置使SpringMVC自动将对象转换为json格式的字符串*/
           return user;//通常返回json数据
       }
   }
   ```

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:context="http://www.springframework.org/schema/context"
          xmlns:mvc="http://www.springframework.org/schema/mvc"
          xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                               http://www.springframework.org/schema/context  http://www.springframework.org/schema/context/spring-context.xsd http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd">
   
       <!--组件扫描-->
       <context:component-scan base-package="com.chen.controller">
       </context:component-scan>
   
       <!--配置内部资源视图解析器-->
       <bean id="viewResovler" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
           <property name="prefix" value="/WEB-INF/jsp/"/>
           <property name="suffix" value=".jsp"/>
       </bean>
   
       <!--配置处理器映射器-->
   <!--    <bean class="org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter">-->
   <!--        <property name="messageConverters">-->
   <!--            <list>-->
   <!--                <bean class="org.springframework.http.converter.json.MappingJackson2HttpMessageConverter"></bean>-->
   <!--            </list>-->
   <!--        </property>-->
   <!--    </bean>-->
   
       <!--替换处理器映射器的配置-->
       <mvc:annotation-driven/>
   </beans>
   ```

## 3. SpringMVC获得请求数据

1. 获得请求参数
   
   * SpringMVC可以接收的类型参数
     
     > 1. 基本数据类型参数
     >    * 要求Controller中业务方法的参数名称要与请求参数的name一致，参数值会自动映射匹配
     >    
     >      ![image-20220405144902149](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405144902149.png)
     > 2. POJO类型参数
     >    * 要求Controller中业务方法的POJO参数属性名要与请求参数的name一致，参数值会自动映射匹配
     >    
     >      ![image-20220405145947871](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405145947871.png)
     > 3. 数组类型参数
     >    * 要求Controller中业务方法数组名称n要与请求参数的name一致，参数值会自动映射匹配
     > 4. 集合类型参数
     >    * 场景一：获得集合参数时，要将集合参数包装到一个POJO中
     >    * 场景二：使用ajax提交时，可以指定contentType为json形式，那么方法参数位置使用@RequestBody可以直接接收集合数据而无需使用pojo进行封装
   
2. 请求数据乱码问题 
   
   ![image-20220405152715147](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405152715147.png)

3. 参数绑定注解@requestParam
   
   > 当请求的参数名称与Controller的业务方法参数名称不一致时，需要通过@requestParam显式绑定
   
   ![image-20220405153031913](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405153031913.png)
   
   ![image-20220405153138966](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405153138966.png)

4. 获得Restful风格的参数
   
   ![image-20220405153525637](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405153525637.png)
   
   ![image-20220405153710199](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405153710199.png)

5. 自定义类型转换器
   
   ![image-20220405154129353](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405154129353.png)

6. 获得Servlet相关API

   ![image-20220418102302878](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418102302878.png)

7. 获得请求头

   ![image-20220418102429751](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418102429751.png)

   ![image-20220418102854916](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418102854916.png)

8. 文件上传

   > 文件上传客户端三要素
   >
   > * 表单项type="file"
   > * 表单提交方式是post
   > * 表单的enetype属性是部分表单形式，及enctype="multipart/form-data"
   >
   > 文件上传原理
   >
   > 单文件上传步骤
   >
   > * 导入fileupload和io坐标
   >
   >   ![image-20220418104321191](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418104321191.png)
   >
   > * 配置文件上传解析器
   >
   >   ![image-20220418104358325](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418104358325.png)
   >
   > * 编写文件上传代码
   >
   >   ![image-20220418104531418](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418104531418.png)

知识点总结：

> 1. MVC实现数据请求方式
> 2. 中文乱码问题
> 3. @RequestParam和@PathVariable
> 4. 自定义类型转换器
> 5. 获得Servlet相关API
> 6. @RequestHeader和@CookieValue
> 7. 文件上传

## 4. SpringMVC拦截器

### 拦截器概念

1. 拦截器（Interceptor）：一种动态拦截方法调用的机制，在SpringMVC中动态拦截控制器方法的执行
2. 作用：
   * 在指定的方法调用前后执行预先设定的代码
   * 组织原始方法的执行
3. 拦截器和过滤器的区别
   * 归属不同：Filter属于Servlet技术，Interceptor属于SpringMVC技术
   * 拦截内容不同：Filter对所有访问进行增强，Interceptor仅针对SpringMVC的访问进行增强

![image-20220427191029801](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220427191029801.png)

### 快速上手

> 自定义拦截器步骤：
>
> 1. 创建拦截器
> 2. 配置拦截器

1. 创建拦截器（实现HandlerInterceptor）

   ~~~java
   package com.chen.controller.interceptor;
   
   import org.springframework.stereotype.Component;
   import org.springframework.web.servlet.HandlerInterceptor;
   import org.springframework.web.servlet.ModelAndView;
   
   import javax.servlet.http.HttpServletRequest;
   import javax.servlet.http.HttpServletResponse;
   
   /**
    * @author whyme-chen
    * @date 2022/4/27 19:27
    */
   @Component
   public class InterceptorDemo implements HandlerInterceptor {
       @Override
       public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
           System.out.println("preHandle........");
           return true;
       }
   
       @Override
       public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
           System.out.println("postHandle........");
       }
   
       @Override
       public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
           System.out.println("afterHandle........");
   
       }
   }
   

2. 配置拦截器

   ```xml
   <!--在SpringMVC配置文件中进行配置-->
   <mvc:interceptors>
       <mvc:interceptor>
           <mvc:mapping path="/**"/>
           <bean class="com.chen.controller.interceptor.InterceptorDemo"/>
       </mvc:interceptor>
   </mvc:interceptors>
   ```

   ~~~java
   //使用注解配置
   package com.chen.interceptor;
   
   import org.springframework.context.annotation.Configuration;
   import org.springframework.web.servlet.config.annotation.InterceptorRegistration;
   import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
   import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
   
   @Configuration
   public class LoginConfig implements WebMvcConfigurer {
       @Override
       public void addInterceptors(InterceptorRegistry registry) {
           InterceptorRegistration registration=
                   registry.addInterceptor(new LoginInterceptor());
           //拦截信息
           registration.addPathPatterns("/**");
           //不拦截信息
           registration.excludePathPatterns(
                   "/loginIn",
                   "/**/login.html",
                   "/**/*.js",
                   "/**/*.css",
                   "/**/images/*.*"
           );
   
       }
   }
   
   ~~~

#### 拦截器方法说明

![image-20220427200921912](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220427200921912.png)

### 小案例：用户登录权限控制



# Mybatis

## Mybatis简介

1. 原始jdbc操作分析
   
   ![image-20220420142447641](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420142447641.png)

2. mybatis概述
   
   ![image-20220420142638250](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420142638250.png)

## 快速入门

1. 开发步骤
   
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

## Mybatis的Dao实现

1. 传统实现方式：手动对Dao进行实现

2. 代理开发方式：由Mybatis实现Dao接口
   
   ![image-20211120112940959](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211120112940959.png)

![image-20220420155719754](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420155719754.png)

## 动态sql

1. if

   ![image-20220420162833609](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220420162833609.png)

2. foreach

3. sql片段抽取

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

   > 注意：使用注解时，则没有mapper映射文件,但此时应该在核心配置文件中配置加载映射关系。配置如下：
   >
   > ```xml
   > <!--加载映射关系-->
   > <mappers>
   >     <!--指定接口所在包-->
   >     <package name="com.chen.dao"/>
   > </mappers>
   > ```

# SSM整合

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

~~~ java
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
~~~

## 分页插件

1. 配置

   ~~~java
   @Bean
       public MybatisPlusInterceptor mybatisPlusInterceptor(){
           //配置分页插件
           MybatisPlusInterceptor mybatisPlusInterceptor = new MybatisPlusInterceptor();
           mybatisPlusInterceptor.addInnerInterceptor(new PaginationInnerInterceptor());
           return mybatisPlusInterceptor;
       }
   ~~~

   

# Spring boot

## 基础入门

### 快速上手

1. 概述：SringBoot是由Pivtal团队提供的全心框架，其设计目的是用来简化Spring的初始搭建和开发过程。

2. 优势对比

   * Spring程序
     * 依赖设置繁琐
     * 配置繁琐
   * SpringBoot程序优点
     * 起步依赖：提供依赖启动器简化构建配置，可快速构建独立的Spring应用
     * 辅助功能：直接嵌入Tomcat、Jetty和Undertow服务器（无需部署WAR文件）
     * 自动配置：简化常用工程相关配置

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

     ~~~ xml
     <!-- 引入热部署依赖 -->
     <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-devtools</artifactId>
     </dependency>

   * idea工具热部署设置

### 基础配置

#### 全局配置文件

1. 属性配置

   ![image-20220223222016095](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223222016095.png)

   注意：SpringBoot默认配置文件为application.properties，通过键值对配置

2. 配置文件分类

   * properties
   * yml(主流)
   * yaml

   ![image-20220223222330450](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223222330450.png)

   > 注意：SpringBootp配置文件的加载顺序（优先级）：properties>yml>yaml
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

### 整合第三方技术

#### 整合JUnit

* 导入测试对应的starter

* 测试类使用@SpringBootTest修饰

  ![image-20220224161459266](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220224161459266.png)

* 使用自动装配的形式添加要测试的对象

> 注意：
>
> * 测试类如果存在与引导类所在包或子包中无需指定引导类
> * 测试类如果不存在于引导类所在的包或子包中需要通过classes属性指定引导类

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

#### 整合Druid

### 常用注解

1. @import
   * springboot中@Enable***开头的注解表示开启某项功能，其底层依赖@import注解。
   * @import注解可以向容器中导入类，这些类对象会被注入到容器中
     * 直接导入
     * 导入配置类
     * 导入ImportSelector接口实现类
     * 导入ImportBeanDefinitionRegister接口的实现类
2. 就

### REST风格

1. 简介

   REST（Representational State Transfer）,表现形式转态转换。

   * 传统风格资源描述形式
     * http://localhost/user/getById?id=1
     * http://localhost/user/saveUser
   * REST风格描述形式
     * http://localhost/user/1
     * http://localhost/user
   * 优点
     * 隐藏资源的访问行为，无法通过地址得知对资源是何种操作
     * 书写简化
   * 按照REST风格访问资源时使用行为动作区分对资源的操作
     * http://localhost/users查询全部用户信息 GET（查询）
     * http://localhost/users/1查询指定用户信息 GET
     * http://localhost/users添加用户信息 POST（新增或保存）
     * http://localhost/users修改用户信息 PUT（修改或更新）
     * http://localhost/users/1删除指定用户信息 DELETE（删除）
   * 根据REST风格对资源进行访问称为RESTful

2. 入门案例

   ![image-20220223213459243](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223213459243.png)

   请求路径参数

   ![image-20220223213435601](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223213435601.png)

## 应用

### 导入导出Excel

#### 导出

1. 基于POI导出

2. 基于EasyExcel导出

3. 基于EasyPoi导出

   参考：https://zhuanlan.zhihu.com/p/426308817
   
   ~~~java
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
   
   ~~~

#### 导入

1. 基于EasyPoi导入

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

## 原理

# Swagger

官网：https://swagger.io/

参考文章：

* https://blog.csdn.net/YR_112233/article/details/122630446
* https://blog.csdn.net/weixin_46645338/article/details/123895447

### 简介

1. 简介
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
   * 以前叫做Swagger规范，是REST API的API描述格式，为REST API定义了一个与语言无关的标准接口
   * OpenAPI规范可以使用YAML或JSON格式进行编写

### SpringBoot集成Swagger

参考：https://blog.csdn.net/weixin_46645338/article/details/123895447

### Swagger配置（swagger3.0）

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

### 常用注解

![img](https://img2020.cnblogs.com/blog/2088791/202112/2088791-20211229104433596-25349310.png)

# Thymeleaf

1. 简介

2. 使用流程（在springboot项目中）

   * 引入依赖

     > ```xml
     > <dependency>
     >    <groupId>org.springframework.boot</groupId>
     >    <artifactId>spring-boot-starter-thymeleaf</artifactId>
     > </dependency>
     > ```

   * 配置相关项

     > ```yaml
     > # thymeleaf
     > spring:
     >   thymeleaf:
     >     prefix: classpath:/templates/ # 渲染的模板文件所在根目录
     >     check-template: true # 是否强制性检查templates目录下是否有待渲染模板文件
     >     suffix: .html # 设定thymeleaf文件后缀名
     >     encoding: UTF-8
     >     servlet:
     >       content-type: text/html # thymeleaf文件的内容类型
     >     cache: false # 禁止使用缓存
     > ```

   * 编写控制器

     ~~~java
     @Controller
     @RequestMapping("/test")
     public class IndexController {
     
         @GetMapping("/index")
         public String index(Model model){
             model.addAttribute("str","hello thymeleaf!");
             return "index";
         }
     }
     ~~~

   * 编写页面

     ~~~html
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

3. 常用语法标签

   * 

# Idea

参考资料：https://www.bilibili.com/video/BV1PW411X75p?from=search&seid=1533766256313085594&spm_id_from=333.337.0.0

## 常用配置

1. 目录结构
   
   ![image-20211227103126984](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211227103126984.png)

## 集成Tomcat

## 版本控制

## 配置Maven

## 常用快捷键

### Mac 键盘符号说明

- `⌘` == `Command`
- `⇧` == `Shift`
- `⇪` == `Caps Lock`
- `⌥` == `Option`
- `⌃` == `Control`
- `↩` == `Return/Enter`
- `⌫` == `Delete`
- `⌦` == `向前删除键（Fn+Delete）`
- `↑` == `上箭头`
- `↓` == `下箭头`
- `←` == `左箭头`
- `→` == `右箭头`
- `⇞` == `Page Up（Fn+↑）`
- `⇟` == `Page Down（Fn+↓）`
- `Home` == `Fn + ←`
- `End` == `Fn + →`
- `⇥` == `右制表符（Tab键）`
- `⇤` == `左制表符（Shift+Tab）`
- `⎋` == `Escape (Esc)`
- `⏏` == `电源开关键`

### Ctrl

| Win 快捷键                                | Mac 快捷键                                   | 介绍                                                    |
|:-------------------------------------- |:----------------------------------------- |:----------------------------------------------------- |
| <kbd>Ctrl</kbd> + <kbd>F</kbd>         | <kbd>Command</kbd> + <kbd>F</kbd>         | 在当前文件进行文本查找                                           |
| <kbd>Ctrl</kbd> + <kbd>R</kbd>         | <kbd>Command</kbd> + <kbd>R</kbd>         | 在当前文件进行文本替换                                           |
| <kbd>Ctrl</kbd> + <kbd>Z</kbd>         | <kbd>Command</kbd> + <kbd>Z</kbd>         | 撤销                                                    |
| <kbd>Ctrl</kbd> + <kbd>Y</kbd>         | <kbd>Command</kbd> + <kbd>Delete</kbd>    | 删除光标所在行 或 删除选中的行                                      |
| <kbd>Ctrl</kbd> + <kbd>D</kbd>         | <kbd>Command</kbd> + <kbd>D</kbd>         | 复制光标所在行 或 复制选择内容，并把复制内容插入光标位置下面                       |
| <kbd>Ctrl</kbd> + <kbd>W</kbd>         | <kbd>Option</kbd> + <kbd>方向键上</kbd>       | 递进式选择代码块。可选中光标所在的单词或段落，连续按会在原有选中的基础上再扩展选中范围           |
| <kbd>Ctrl</kbd> + <kbd>E</kbd>         | <kbd>Command</kbd> + <kbd>E</kbd>         | 显示最近打开的文件记录列表                                         |
| <kbd>Ctrl</kbd> + <kbd>N</kbd>         | <kbd>Command</kbd> + <kbd>O</kbd>         | 根据输入的 **类名** 查找类文件                                    |
| <kbd>Ctrl</kbd> + <kbd>J</kbd>         | <kbd>Command</kbd> + <kbd>J</kbd>         | 插入自定义动态代码模板                                           |
| <kbd>Ctrl</kbd> + <kbd>P</kbd>         | <kbd>Command</kbd> + <kbd>P</kbd>         | 方法参数提示显示                                              |
| <kbd>Ctrl</kbd> + <kbd>U</kbd>         | <kbd>Command</kbd> + <kbd>U</kbd>         | 前往当前光标所在的方法的父类的方法 / 接口定义                              |
| <kbd>Ctrl</kbd> + <kbd>B</kbd>         | <kbd>Command</kbd> + <kbd>B</kbd>         | 进入光标所在的方法/变量的接口或是定义处，等效于 `Ctrl + 左键单击`                |
| <kbd>Ctrl</kbd> + <kbd>/</kbd>         | <kbd>Command</kbd> + <kbd>/</kbd>         | 注释光标所在行代码，会根据当前不同文件类型使用不同的注释符号                        |
| <kbd>Ctrl</kbd> + <kbd>F1</kbd>        | <kbd>Command</kbd> + <kbd>F1</kbd>        | 在光标所在的错误代码处显示错误信息                                     |
| <kbd>Ctrl</kbd> + <kbd>F11</kbd>       | <kbd>Option</kbd> + <kbd>F3</kbd>         | 选中文件 / 文件夹，使用助记符设定 / 取消书签                             |
| <kbd>Ctrl</kbd> + <kbd>F12</kbd>       | <kbd>Command</kbd> + <kbd>F12</kbd>       | 弹出当前文件结构层，可以在弹出的层上直接输入，进行筛选                           |
| <kbd>Ctrl</kbd> + <kbd>Space</kbd>     | <kbd>Control</kbd> + <kbd>Space</kbd>     | 基础代码补全，默认在 Windows 系统上被输入法占用，需要进行修改，建议修改为 `Ctrl + 逗号` |
| <kbd>Ctrl</kbd> + <kbd>Delete</kbd>    | <kbd>Option</kbd> + <kbd>Fn</kbd>+ Delete | 删除光标后面的单词或是中文句                                        |
| <kbd>Ctrl</kbd> + <kbd>BackSpace</kbd> | <kbd>Option</kbd> + <kbd>Delete</kbd>     | 删除光标前面的单词或是中文句                                        |
| <kbd>Ctrl</kbd> + <kbd>1,2,3...9</kbd> | <kbd>Control</kbd> + <kbd>1,2,3...9</kbd> | 定位到对应数值的书签位置                                          |
| <kbd>Ctrl</kbd> + <kbd>加号</kbd>        | <kbd>Command</kbd> + <kbd>加号</kbd>        | 展开代码                                                  |
| <kbd>Ctrl</kbd> + <kbd>减号</kbd>        | <kbd>Command</kbd> + <kbd>减号</kbd>        | 折叠代码                                                  |
| <kbd>Ctrl</kbd> + <kbd>左键单击</kbd>      | <kbd>Control</kbd> + <kbd>左键单击</kbd>      | 在打开的文件标题上，弹出该文件路径                                     |
| <kbd>Ctrl</kbd> + <kbd>左方向键</kbd>      | <kbd>Option</kbd> + <kbd>左方向键</kbd>       | 光标跳转到当前单词 / 中文句的左侧开头位置                                |
| <kbd>Ctrl</kbd> + <kbd>右方向键</kbd>      | <kbd>Option</kbd> + <kbd>右方向键</kbd>       | 光标跳转到当前单词 / 中文句的右侧开头位置                                |
| <kbd>Ctrl</kbd> + <kbd>前方向键</kbd>      | 预设中没有该快捷键                                 | 等效于鼠标滚轮向前效果                                           |
| <kbd>Ctrl</kbd> + <kbd>后方向键</kbd>      | 预设中没有该快捷键                                 | 等效于鼠标滚轮向后效果                                           |

### Alt

| Win 快捷键                               | Mac 快捷键                                   | 介绍                                                             |
|:------------------------------------- |:----------------------------------------- |:-------------------------------------------------------------- |
| <kbd>Alt</kbd> + <kbd>\`</kbd>        | <kbd>Control</kbd> + <kbd>V</kbd>         | 显示版本控制常用操作菜单弹出层                                                |
| <kbd>Alt</kbd> + <kbd>F1</kbd>        | <kbd>Option</kbd> + <kbd>F1</kbd>         | 显示当前文件选择目标弹出层，弹出层中有很多目标可以进行选择                                  |
| <kbd>Alt</kbd> + <kbd>F7</kbd>        | <kbd>Option</kbd> + <kbd>F7</kbd>         | 查询所选对象/变量被引用                                                   |
| <kbd>Alt</kbd> + <kbd>Enter</kbd>     | <kbd>Option</kbd> + <kbd>Enter</kbd>      | IntelliJ IDEA 根据光标所在问题，提供快速修复选择，光标放在的位置不同提示的结果也不同              |
| <kbd>Alt</kbd> + <kbd>Insert</kbd>    | <kbd>Command</kbd> + <kbd>N</kbd>         | 代码自动生成，如生成对象的 set / get 方法，构造函数，toString() 等                   |
| <kbd>Alt</kbd> + <kbd>左方向键</kbd>      | <kbd>Control</kbd> + <kbd>左方向键</kbd>      | 切换当前已打开的窗口中的子视图，比如Debug窗口中有Output、Debugger等子视图，用此快捷键就可以在子视图中切换 |
| <kbd>Alt</kbd> + <kbd>右方向键</kbd>      | <kbd>Control</kbd> + <kbd>右方向键</kbd>      | 切换当前已打开的窗口中的子视图，比如Debug窗口中有Output、Debugger等子视图，用此快捷键就可以在子视图中切换 |
| <kbd>Alt</kbd> + <kbd>前方向键</kbd>      | <kbd>Control</kbd> + <kbd>前方向键</kbd>      | 当前光标跳转到当前文件的前一个方法名位置                                           |
| <kbd>Alt</kbd> + <kbd>后方向键</kbd>      | <kbd>Control</kbd> + <kbd>后方向键</kbd>      | 当前光标跳转到当前文件的后一个方法名位置                                           |
| <kbd>Alt</kbd> + <kbd>1,2,3...9</kbd> | <kbd>Command</kbd> + <kbd>1,2,3...9</kbd> | 显示对应数值的选项卡，其中 1 是 Project 用得最多                                 |

### Shift

| Win 快捷键                             | Mac 快捷键                  | 介绍                         |
|:----------------------------------- |:------------------------ |:-------------------------- |
| <kbd>Shift</kbd> + <kbd>F11</kbd>   | <kbd>Command + F3</kbd>  | 弹出书签显示层                    |
| <kbd>Shift</kbd> + <kbd>Tab</kbd>   | <kbd>Shift + Tab</kbd>   | 取消缩进                       |
| <kbd>Shift</kbd> + <kbd>Enter</kbd> | <kbd>Shift + Enter</kbd> | 开始新一行。光标所在行下空出一行，光标定位到新行位置 |
| <kbd>Shift</kbd> + <kbd>左键单击</kbd>  | <kbd>Shift + 左键单击</kbd>  | 在打开的文件名上按此快捷键，可以关闭当前打开文件   |

### Ctrl + Alt

| Win 快捷键                                             | Mac 快捷键                                                   | 介绍                     |
|:--------------------------------------------------- |:--------------------------------------------------------- |:---------------------- |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>L</kbd>     | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>L</kbd>     | 格式化代码，可以对当前文件和整个包目录使用  |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>O</kbd>     | <kbd>Control</kbd> + <kbd>Option</kbd> + <kbd>O</kbd>     | 优化导入的类，可以对当前文件和整个包目录使用 |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd>     | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>T</kbd>     | 对选中的代码弹出环绕选项弹出层        |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>S</kbd>     | <kbd>Command</kbd> + <kbd>逗号</kbd>                        | 打开 IntelliJ IDEA 系统设置  |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Enter</kbd> | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>Enter</kbd> | 光标所在行上空出一行，光标定位到新行     |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>左方向键</kbd>  | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>左方向键</kbd>  | 退回到上一个操作的地方            |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>右方向键</kbd>  | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>右方向键</kbd>  | 前进到上一个操作的地方            |

### Ctrl + Shift

| Win 快捷键                                                   | Mac 快捷键                                                      | 介绍                                              |
|:--------------------------------------------------------- |:------------------------------------------------------------ |:----------------------------------------------- |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>         | 根据输入内容查找整个项目 或 指定目录内文件                          |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd>         | 根据输入内容替换对应内容，范围为整个项目 或 指定目录内文件                  |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>         | <kbd>Control</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>         | 自动将下一行合并到当前行末尾                                  |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Z</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>Z</kbd>         | 取消撤销                                            |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>W</kbd>         | <kbd>Option</kbd> + <kbd>方向键下</kbd>                          | 递进式取消选择代码块。可选中光标所在的单词或段落，连续按会在原有选中的基础上再扩展取消选中范围 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd>         | 通过文件名定位 / 打开文件 / 目录，打开目录需要在输入的内容后面多加一个正斜杠       |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>U</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>U</kbd>         | 对选中的代码进行大 / 小写轮流转换                              |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>         | 对当前类生成单元测试类，如果已经存在的单元测试类则可以进行选择                 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd>         | 复制当前文件磁盘路径到剪贴板                                  |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd>         | <kbd>Control</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd>         | 跳转到类型声明处                                        |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>/</kbd>         | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>/</kbd>        | 代码块注释                                           |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>\[</kbd>        | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>\[</kbd>        | 选中从光标所在位置到它的顶部中括号位置                             |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>\]</kbd>        | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>\]</kbd>        | 选中从光标所在位置到它的底部中括号位置                             |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>加号</kbd>        | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>加号</kbd>        | 展开所有代码                                          |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>减号</kbd>        | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>减号</kbd>        | 折叠所有代码                                          |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F7</kbd>        | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>F7</kbd>        | 高亮显示所有该选中文本，按Esc高亮消失                            |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F12</kbd>       | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>F12</kbd>       | 编辑器最大化                                          |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd>     | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd>     | 自动结束代码，行末自动添加分号                                 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Backspace</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Backspace</kbd>    | 退回到上次修改的地方                                      |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>1,2,3...9</kbd> | <kbd>Control</kbd> + <kbd>Shift</kbd> + <kbd>1,2,3...9</kbd> | 快速添加指定数值的书签                                     |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>左键单击</kbd>      | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>左键单击</kbd>      | 把光标放在某个类变量上，按此快捷键可以直接定位到该类中                     |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>左方向键</kbd>      | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>左方向键</kbd>       | 在代码文件上，光标跳转到当前单词 / 中文句的左侧开头位置，同时选中该单词 / 中文句     |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>右方向键</kbd>      | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>右方向键</kbd>       | 在代码文件上，光标跳转到当前单词 / 中文句的右侧开头位置，同时选中该单词 / 中文句     |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>前方向键</kbd>      | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>前方向键</kbd>      | 光标放在方法名上，将方法移动到上一个方法前面，调整方法排序                   |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>后方向键</kbd>      | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>后方向键</kbd>      | 光标放在方法名上，将方法移动到下一个方法前面，调整方法排序                   |

### Alt + Shift

| Win 快捷键                                             | Mac 快捷键                                                | 介绍                                   |
|:--------------------------------------------------- |:------------------------------------------------------ |:------------------------------------ |
| <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd>    | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd>    | 选择 / 添加 task                         |
| <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>左键双击</kbd> | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>左键双击</kbd> | 选择被双击的单词 / 中文句，按住不放，可以同时选择其他单词 / 中文句 |
| <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>前方向键</kbd> | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>前方向键</kbd> | 移动光标所在行向上移动                          |
| <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>后方向键</kbd> | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>后方向键</kbd> | 移动光标所在行向下移动                          |

### Ctrl + Shift + Alt

| Win 快捷键                                                            | Mac 快捷键                                                                  | 介绍       |
|:------------------------------------------------------------------ |:------------------------------------------------------------------------ |:-------- |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>V</kbd> | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>Option</kbd> + <kbd>V</kbd> | 无格式黏贴    |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>S</kbd> | <kbd>Command</kbd> + <kbd>;</kbd>                                        | 打开当前项目设置 |

### 其他

| Win 快捷键        | Mac 快捷键        | 介绍                |
|:-------------- |:-------------- |:----------------- |
| <kbd>F2</kbd>  | <kbd>F2</kbd>  | 跳转到下一个高亮错误 或 警告位置 |
| <kbd>F4</kbd>  | <kbd>F4</kbd>  | 编辑源               |
| <kbd>F11</kbd> | <kbd>F3</kbd>  | 添加书签              |
| <kbd>F12</kbd> | <kbd>F12</kbd> | 回到前一个工具窗口         |
| <kbd>Tab</kbd> | <kbd>Tab</kbd> | 缩进                |
| <kbd>ESC</kbd> | <kbd>ESC</kbd> | 从工具窗口进入代码文件窗口     |

## 常用插件

### Simple Object Copy

参考链接：https://juejin.cn/post/7053264631262871583

# git和GitHub

使用参考链接：https://www.cnblogs.com/syp172654682/p/7689328.html

### 1. 版本控制

版本控制（Revision control）是一种在开发的过程中用于管理我们对文件、目录或工程等内容的修改历史，方便查看更改历史记录，备份以便恢复以前的版本的软件工程技术。

### 2. 版本控制工具

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

#### 版本控制分类

* 本地版本控制
* 集中版本控制
* 分布式版本控制

### 3. git和SVN的最主要区别

SVN是集中式版本控制系统，版本库是集中放在中央服务器的，而工作的时候，用的都是自己的电脑，所以首先要从中央服务器得到最新的版本，然后工作，完成工作后，需要把自己做完的活推送到中央服务器。集中式版本控制系统是必须联网才能工作，对网络带宽要求较高。

Git是分布式版本控制系统，没有中央服务器，每个人的电脑就是一个完整的版本库，工作的时候不需要联网了，因为版本都在自己电脑上。协同的方法是这样的：比如说自己在电脑上改了文件A，其他人也在电脑上改了文件A，这时，你们两之间只需把各自的修改推送给对方，就可以互相看到对方的修改了。

### 4. git安装与配置

官网：https://git-scm.com/

源码：https://github.com/git/git/

#### 常用的Linux命令（bash基本操作命令）

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

#### 配置-git config

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

### 5. git结构和基本原理

![image-20211121161141743](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211121161141743.png)

git管理的文件有三种状态：已修改（modified）,已暂存（staged）,已提交(committed)

![img](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/63651-20170905201033647-1915833066.png)

![img](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/63651-20170909091456335-1787774607.jpg)

![img](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/201751509379751.png)

### 6. git和代码托管中心

* 局域网环境下
  * GitLab
* 外网环境下
  * GitHub
  * 码云

### 7.常用操作

* 本地库初始化
  
  * git init：现有目录创建仓库
  * git clone 【url】;从远程库克隆

* 基本操作
  
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
  
* 分支
  
  * 总结分支中常用命令
    
    ```
    # 列出所有本地分支
    $ git branch
    
    # 列出所有远程分支
    $ git branch -r
    
    # 列出所有本地分支和远程分支
    $ git branch -a
    
    # 新建一个分支，但依然停留在当前分支
    $ git branch [branch-name]
    
    # 新建一个分支，并切换到该分支
    $ git checkout -b [branch]
    
    # 新建一个分支，指向指定commit
    $ git branch [branch] [commit]
    
    # 新建一个分支，与指定的远程分支建立追踪关系
    $ git branch --track [branch] [remote-branch]
    
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
    ```

### 8.远程仓库

#### 常用的托管服务（远程仓库）

* github
* gitee
* gitLab

#### 常用操作

1. 查看远程仓库：git remote

2. 添加远程仓库：git remote add <shortname> <url>

3. 从远程仓库抓取与拉取
   
   >  git fetch [remote-name]：这个命令会访问远程仓库，从中拉取所有你还没有的数据。 执行完成后，你将会拥有那个远程仓库中所有分支 的引用，可以随时合并或查看。 必须注意 git fetch 命令会将数据拉取到你的本地仓库——它并不会自动合并或修改你当前的工作。 当准备好时你必须手动将其合并入你的工作。
   > 
   > 运行 git pull 通常会从最初克隆的服务器上抓取数据并自动尝试合并到当前所在的分支。

4. 推送到远程仓库：git push [remote-name] [branch name]

5. 查看某个远程仓库：git remote show [remote-name]



# 开发经验

## 跨域问题（CROS）

