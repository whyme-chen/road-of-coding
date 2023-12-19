# JVM简介

Java虚拟机是一台执行Java字节码的虚拟计算机，它拥有独立的运行机制，其运行的Java字节码也未必由Java语言编译而成。

JVM平台的各种语言可以共享Java虛拟机带来的跨平台性、优秀的垃圾回收器，以及可靠的即时编译器。
Java技术的核心就是Java虚拟机(JVM，Java Virtual Machine)，因为所有的Java程序都运行在Java虚拟机内部。

1. jvm&jre&jdk

   ![image-20231219204824997](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202312192048550.png)

## JVM结构

JVM整体结构如下：

![image-20230903111409485](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202309031114189.png)

执行引擎有包含以下几部分：

* 解释器（Interpreter）
* 即时编译器（JIT Compiler）
* 垃圾回收（GC）

## JVM家族

1. Sun Classic/Exact VM

![image-20231219205628857](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202312192056537.png)

# 自动内存管理

## JVM内存结构

### 程序计数器

1. 程序计数器（Program  Counter Register）
2. 作用：记录程序执行过程中下一条jvm指令的地址
3. 特点
   * 线程私有的
   * 不会存在内存溢出

### 虚拟机栈

1. 栈：线程运行需要的内存空间

   > 可以通过vm参数：`-Xss`设置栈大小，比如：-Xss256k

2. 栈帧（Frame）：每个方法运行时需要的内存空间

   * 每个栈帧内部包含参数、局部变量、返回值地址。
   * 每一个线程只能有一个活动栈帧，对应着当前正在执行的那个方法。

3. 栈内存溢出

   * 栈帧过多（比如递归调用，没有出口）
   * 栈帧过大（比如创建一个非常大的数组）

#### 问题辨析

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

### 堆

### 方法区

## 类加载机制

### 字节码文件（.class）

参考：https://pdai.tech/md/java/jvm/java-jvm-class.html

1. 字节码文件：class文件本质上是一个以8位字节为基础单位的二进制流，各个数据项目严格按照顺序紧凑的排列在class文件中。jvm根据其特定的规则解析该二进制数据，从而得到相关信息。

2. 文件结构属性

   ![img](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202212012327723.png)

3. 地方

### 加载流程

### 类加载器

# 参考资料

* 文档：
  * [Oracle官方](https://docs.oracle.com/javase/specs/index.html)
* 书籍：
  * 《深入理解Java虚拟机》
  * 《Java虚拟机规范》
  * 《自己动手写Java虚拟机》
* 视频：
  * [尚硅谷JVM](https://www.bilibili.com/video/BV1PJ411n7xZ/?p=1&vd_source=fabefd3fabfadb9324761989b55c26ea)
  * [黑马程序员JVM完整教程](https://www.bilibili.com/video/BV1yE411Z7AP/?vd_source=fabefd3fabfadb9324761989b55c26ea)
  * [实战java虚拟机](https://www.bilibili.com/video/BV1r94y1b7eS/?vd_source=fabefd3fabfadb9324761989b55c26ea)

* 文章：
  * [JVM（Java虚拟机）-史上最全、最详细JVM笔记](https://blog.csdn.net/weixin_56846554/article/details/129802936)