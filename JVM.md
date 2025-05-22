# JVM简介

## 简介

Java是目前应用最为广泛的软件开发平台之一。随着Java以及Java社区的不断壮大，Java也早已不再是简简单单的一门计算机语言，它更是一个平台、一种文化、一个社区。

Java虚拟机是一台**执行Java字节码**的虚拟计算机，它拥有独立的运行机制，其运行的Java字节码也未必由Java语言编译而成。

JVM平台的各种语言可以共享Java虛拟机带来的跨平台性、优秀的垃圾回收器，以及可靠的即时编译器。
Java技术的核心就是Java虚拟机(JVM，Java Virtual Machine)，因为所有的Java程序都运行在Java虚拟机内部。

1. 虚拟机

   * 系统虚拟机：对物理计算机进行仿真，典型代表有：Visual Box，VMWare
   * 程序虚拟机：专门为执行单个计算机程序而设计，典型代表有：JVM
   
2. jvm&jre&jdk

   ![image-20231219204824997](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202312192048550.png)

3. JVM规范

   > JavaSE：https://docs.oracle.com/javase/8/docs/

4. JVM架构模型

   JVM内存整体结构如下：

   ![image-20230903111409485](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202309031114189.png)

   执行引擎有包含以下几部分：

   * 解释器（Interpreter）
   * 即时编译器（JIT Compiler）
   * 垃圾回收（GC）

   Java编译器输入的指令流基本上是一种**基于栈的指令集架构**，另外一种指令集架构则是**基于寄存器的指令集架构**。由于跨平台性设计，Java的指令都是根据栈来设计的。

5. JVM的生命周期

## JVM家族

1. Sun Classic
2. Exact VM
3. **HotSpot VM**
4. **JRockit VM**
5. **IBM J9/Eclipse OpenJ9**
6. **Graal VM**

![image-20231219205628857](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202312192056537.png)

## 编译JDK

参考：

* https://www.cnblogs.com/jhxxb/p/12558970.html
* [Ubuntu 22.04.3 LTS 编译 OpenJDK 12 - Tienz1 - 博客园](https://www.cnblogs.com/tienz1/p/17923453.html)

# 自动内存管理

## JVM内存结构

整体结构（二大子系统，五大区）：

> 下图为JDK1.7的内存结构

![image-20230903111409485](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202309031114189.png)

![](https://pica.zhimg.com/80/v2-d3f3c6d951c82b47ec21a660ea1cc748_1440w.webp)



### 程序计数器

1. 程序计数器（Program  Counter Register）
2. 作用：记录程序执行过程中下一条jvm指令的地址
3. 特点
   * 线程私有的
   * **不会存在内存溢出**

### 虚拟机栈

#### 原理

1. 栈：线程运行需要的内存空间

   > 可以通过vm参数：`-Xss`设置栈大小，比如：-Xss256k

2. 栈帧（Frame）：每个方法运行时需要的内存空间

   * 每个栈帧内部包含参数、局部变量、返回值地址。
   * 每一个线程只能有一个活动栈帧，对应着当前正在执行的那个方法。

3. 栈内存溢出

   * 栈帧过多（比如递归调用，没有出口）
   * 栈帧过大（比如创建一个非常大的数组）

#### 常见问题分析

1. 垃圾回收是否涉及栈内存？

   > 不涉及，栈内存随着方法运行的结束将自动回收

2. 占内存分配越大越好？

   > 否，因为物理内存是固定的，栈内存越大将会导致可用线程数越少

3. 方法内的局部变量是否线程安全？

   > 如果方法内局部变量没有逃离方法的作用范围，它是线程安全的，因为每个方法对应一个栈帧，不同的线程对应着不同的虚拟机栈，即对应不同虚拟机栈内各自的栈帧，线程间无法共享，所以是线程安全的。
   >
   > 如果是局部变量引用了对象，并逃离方法的作用范围，需要考虑线程安全。

4. cpu占用过高

   > Linux中线程运行诊断：
   >
   > 定位：
   >
   > * 使用top命令定位cpu占用过高的进程
   > * 使用ps命令定位cpu占用过高的线程
   > * 使用jstack 进程id，然后根据线程id进行一步分析并找到问题代码的源码位置

5. 程序运行很长时间没有结果

### 本地方法栈

1. 本地方法栈：用来支持Java程序调用本地方法（Native Method）的一部分内存区域。
   * 本地方法是指使用其他编程语言（如C、C++）编写的方法，而非纯Java代码。
   * 本地方法栈与Java虚拟机栈（Java Stack）类似，但在功能和作用上有所不同。Java虚拟机栈用于管理Java方法的调用和执行，而本地方法栈则用于管理本地方法的调用和执行。
   * 本地方法栈的结构与Java虚拟机栈类似，由栈帧（Stack Frame）组成。每个栈帧对应一个本地方法的执行，包含了本地方法的局部变量表和操作数栈。与Java虚拟机栈不同的是，本地方法栈中的栈帧不需要进行方法调用和返回的相关操作，因为本地方法的调用是由外部语言（如C、C++）完成的。
   * 本地方法栈的大小可以在Java虚拟机启动时通过参数进行设置，而且它的大小不会受到Java堆大小的限制。如果本地方法栈的空间不足，会抛出StackOverflowError异常。
   * 本地方法栈在Java虚拟机规范中并没有做强制要求，因此不同的JVM实现可能采用不同的策略来支持本地方法的调用和执行。
2. 作用
   * 行本地方法：当Java程序调用本地方法时，虚拟机会将当前线程切换到本地方法栈，并执行相应的本地方法代码。
   * 传递参数：本地方法栈用于传递参数给本地方法，并保存本地方法的局部变量。
   * 分配和释放本地资源：本地方法栈可以用于分配和释放本地资源，比如文件句柄、数据库连接等。

### 堆

1. 堆（Heap）
   * 通过`new`关键字创建对象都会使用堆内存。
   * 可以通过参数`-Xmx`修改堆内存大小
2. 特点
   * 不同于程序计数器、虚拟机栈、本地方法栈是线程私有的，堆是线程共享的，堆中对象都需要考虑线程安全问题。
   * 堆中的内存有垃圾回收机制。
3. 堆内存诊断

### 方法区

> 特别注意：**方法区是规范，永久代（jdk1.6，占用的是堆内存）和元空间（jdk1.8，占用的是系统内存）只是实现。**

1. 方法区：

2. 组成

   ![image-20231221213046044](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202312212130435.png)

3. 方法区内存溢出

   * 1.8以前会导致永久代内存溢出
   * 1.8以后会导致元空间内存溢出

#### 永久代

#### 元空间

#### 常量池

1. 常量池：常量池是编译阶段的一部分，是保存在.class文件中的。它包含了类、接口、方法中的常量、字段符号引用等信息。常量池中的数据可以被编译器直接使用，也可以在运行期间被加载到运行时常量池中。可以理解为一张表，虚拟机指令根据这张常量表找到要执行的类名、方法名、参数类型、字面量等信息。
2. 运用时常量池：运行时常量池是在类加载过程中被创建的一块内存区域，它是方法区的一部分。运行时常量池是为了支持动态性而设计的，常量池在`*.class`文件中，当该类被加载，它的常量池信息就会放入运行时常量池，并把里面的符号地址变为真实地址。

##### StringTable

## 直接内存

## 对象管理

### 对象创建过程

### 对象的布局

对象在内存中主要包含三部分：

*  对象头
* 实例数据
* 对齐填充

### 对象存活判断

1. 引用计数算法
2. 可达性分析算法

### 引用类型

在java中对象的引用类型决定了垃圾回收器对对象的回收策略。从JDK 1.2版本开始，对象的引用被划分为4种级别，从而使程序能更加灵活地控制对象的生命周期，这4种级别由高到低依次为：强引用、软引用、弱引用和虚引用。

1. 强引用

   * 定义：最常见的引用类型，通过 new 创建的对象默认是强引用。

   * 特点： 只要强引用存在，对象就不会被GC回收。即使内存不足时，JVM会抛出OutOfMemoryError，也不会回收强引用对象。

   * 示例： 

     ```java
     Object obj = new Object(); // obj是强引用
     ```

2. 软引用

   * 定义：软引用是一种相对强引用弱化了一些的引用，需要用`java.lang.ref.SoftReference`类来实现。

   * 特点：如果一个对象只存在软引用，那么当内存不足时，GC就会回收这个对象。

   * 示例：

     ~~~jav
     SoftReference<String> softRef=new SoftReference<String>(str);     // 软引用
     ~~~

3. 弱引用

   * 定义：通过WeakReference类实现的引用。

   * 特点： 弱引用对象在下一次GC时会被回收，无论内存是否充足。适用于缓存场景，允许对象在需要时被自动回收。

   * 示例： 

     ```java
     WeakReference<Object> weakRef = new WeakReference<>(new Object());
     ```

4. 虚引用

   * 定义：通过`java.lang.ref.PhantomReference` 来实现的引用

   * 特点：一个对象仅持有虚引用，那么它就和没有任何引用一样，在任何时候都可能被垃圾回收器回收，主要用来跟踪对象被垃圾回收器回收的活动。

   * 示例：

     ~~~java
     A a = new A();
     ReferenceQueue<A> rq = new ReferenceQueue<A>();
     PhantomReference<A> prA = new PhantomReference<A>(a, rq);
     ~~~

## 垃圾回收算法

1. 标记-清除
2. 标记-整理
3. 复制
4. 分代收集

## 垃圾收集器

1. Serial 收集器
2. ParNew 收集器
3. Parallel Scavenge 收集器
4. Serial old 收集器
5. Parallel old 收集器
6. CMS 收集器
7. G1收集器

## 内存分配策略

Minor GC

Full GC

# 类加载机制

类加载子系统通过类加载器（引导类加载器、扩展类加载器、系统类加载器）负责从文件系统或网络中加载Class文件，将解析后的信息存放在称为**方法区**（类信息、运行时常量池信息等）的内存空间中。

## 字节码文件（.class）

参考：https://pdai.tech/md/java/jvm/java-jvm-class.html

1. 字节码文件：class文件本质上是一个以8位字节为基础单位的二进制流，各个数据项目严格按照顺序紧凑的排列在class文件中。jvm根据其特定的规则解析该二进制数据，从而得到相关信息。

2. 文件结构属性

   ![img](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202212012327723.png)

3. 地方

## 加载流程

主要包括三个阶段：

* 加载阶段：通过类的全限定名获取定义此类的二进制字节流，将该字节流代表的静态存储结构转化为方法区的运行时数据结构，在内存中生成一个代表这个类的`java.lang.Class`对象作为方法区这个类的各种数据访问入口。
* 链接阶段
  * 验证：确保Class文件中的字节流包含信息符合虚拟机要求，主要包括四种验证：文件格式验证、元数据验证、字节码验证、符号引用验证
  * 准备
  * 解析
* 初始化阶段

## 类加载机制

### 引导类加载器

### 扩展类加载器

### 系统类加载器

# 执行引擎

# JMM模型

1. 定义：JMM是一组规范，用于定义多线程环境下共享变量的访问规则（限制指令重排序、强制内存可见性），解决线程间的可见性、原子性、有序性问题，避免多线程操作引发数据不一致。
2. 作用：通过volatile、synchronized等关键字和happens-before原则，确保多线程程序在不同硬件平台上正确执行。

## 重排序

源码示例：

~~~java
    public void execute() throws Exception {
        String param = XxlJobHelper.getJobParam();

        if (method.getParameterCount() == 0) {
            method.invoke(bean);
        } else if (method.getParameterCount() == 1 && method.getParameterTypes()[0] == String.class) {
            Object invoke = method.invoke(bean, param);
            if (invoke instanceof ReturnT) {
                ReturnT<?> returnT = (ReturnT<?>) invoke;
                XxlJobHelper.handleResult(returnT.getCode(), returnT.getMsg());
            }else{
                XxlJobHelper.handleFail("Unsupported @XxlJob method signature: " + method);
                throw new RuntimeException("Unsupported @XxlJob method signature: " + method);
            }
        } else {
            XxlJobHelper.handleFail("Unsupported @XxlJob method signature: " + method);
            throw new RuntimeException("Unsupported @XxlJob method signature: " + method);
        }
    }
~~~

编译后字节码示例：

~~~java
    public void execute() throws Exception {
        String param = XxlJobHelper.getJobParam();
        if (this.method.getParameterCount() == 0) {
            this.method.invoke(this.bean);
        } else {
            if (this.method.getParameterCount() != 1 || this.method.getParameterTypes()[0] != String.class) {
                XxlJobHelper.handleFail("Unsupported @XxlJob method signature: " + this.method);
                throw new RuntimeException("Unsupported @XxlJob method signature: " + this.method);
            }

            Object invoke = this.method.invoke(this.bean, param);
            if (!(invoke instanceof ReturnT)) {
                XxlJobHelper.handleFail("Unsupported @XxlJob method signature: " + this.method);
                throw new RuntimeException("Unsupported @XxlJob method signature: " + this.method);
            }

            ReturnT<?> returnT = (ReturnT)invoke;
            XxlJobHelper.handleResult(returnT.getCode(), returnT.getMsg());
        }

    }
~~~

两种代码结构的主要区别：

1. 源码结构：

- 使用了 if-else if-else 的三层结构

- 逻辑判断比较直观，按照参数数量依次判断

- 代码结构更符合人类的阅读习惯

1. 编译后结构：

- 使用了 if-else 的两层结构

- 将原来的 else if 条件转换成了 if 的否定条件

- 代码结构更紧凑，减少了嵌套层级

这种变化是典型的编译器优化，主要目的是：

1. 减少代码分支的嵌套层级，提高代码执行效率

1. 优化控制流结构，使生成的字节码更简洁

1. 通过条件反转来简化逻辑判断

虽然代码结构发生了变化，但功能是完全等价的。编译器在保证语义不变的情况下，对代码结构进行了优化，这是正常的编译优化行为。这种优化不会影响代码的功能，只是改变了代码的组织方式，使其更适合机器执行。

# 调优与排错

## 分析诊断工具

常用的虚拟机内存分析诊断工具：

* `jstack`：它是JDK自带的一款命令行工具，用于生成当前Java进程的线程快照（Thread Dump），并且可以显示每个线程的堆栈信息。通过jstack可以查看线程是否处于死锁、哪些线程占用了过多的CPU资源等问题。
* `jps`：查看当前系统中的java进程
* `jmap`：查看堆内存占用情况
* `jvisualvm`：它是JDK自带的一款GUI工具，可以通过图形化界面实时监控Java应用程序的运行状态，支持线程、内存、CPU占用等方面的监控和分析。在jvisualvm中可以查看线程的状态、堆栈信息、内存使用情况等。
* `JConsole`：它也是JDK自带的一款GUI工具，类似于jvisualvm，可以通过图形化界面实时监控Java应用程序的运行状态，支持线程、内存、CPU占用等方面的监控和分析。在JConsole中可以查看线程数量、线程状态、内存使用情况等。
* `VisualVM`：它是JDK自带的一款扩展性较强的GUI工具，支持Java应用程序监控、性能分析、内存泄漏检测等功能。VisualVM整合了jvisualvm和JConsole的功能，并且支持插件式开发，可以通过安装插件实现更多的监控和分析功能。
* `Arthas`：它是阿里巴巴开源的一款Java诊断工具，支持实时查看Java应用程序的线程、堆栈、方法调用等信息，同时还提供了丰富的命令行工具，可以进行方法耗时统计、内存泄漏检测等操作。Arthas支持非侵入式诊断，无需修改代码或重启应用程序，方便快捷。
* `Jprofile`

# 参考资料

* 文档：
  * [Oracle官方](https://docs.oracle.com/javase/specs/index.html)
  * [OpenJDK](https://openjdk.org/)
* 书籍：
  * **《深入理解Java虚拟机》**
  * 《Java虚拟机规范》
  * **《自己动手写Java虚拟机》**
* 视频：
  * [尚硅谷JVM](https://www.bilibili.com/video/BV1PJ411n7xZ/?p=1&vd_source=fabefd3fabfadb9324761989b55c26ea)
  * [黑马程序员JVM完整教程](https://www.bilibili.com/video/BV1yE411Z7AP/?vd_source=fabefd3fabfadb9324761989b55c26ea)
  * [实战java虚拟机](https://www.bilibili.com/video/BV1r94y1b7eS/?vd_source=fabefd3fabfadb9324761989b55c26ea)
  * [尚硅谷JVM精讲与GC调优教程](https://www.bilibili.com/video/BV1Dz4y1A7FB/?spm_id_from=333.788.recommend_more_video.2&vd_source=fabefd3fabfadb9324761989b55c26ea)
* 文章：
  * [JVM（Java虚拟机）-史上最全、最详细JVM笔记](https://blog.csdn.net/weixin_56846554/article/details/129802936)
  * [♥JVM相关知识体系详解♥ | Java 全栈知识体系](https://pdai.tech/md/java/jvm/java-jvm-x-overview.html)

> 以下图知识点逻辑汇总，来源：[♥JVM相关知识体系详解♥ | Java 全栈知识体系](https://pdai.tech/md/java/jvm/java-jvm-x-overview.html)

![img](https://pdai.tech/images/jvm/java-jvm-overview.png)