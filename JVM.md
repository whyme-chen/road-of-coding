# JVM简介

Java虚拟机是一台执行Java字节码的虚拟计算机，它拥有独立的运行机制，
其运行的Java字节码也未必由Java语言编译而成。

JVM平台的各种语言可以共享Java虛拟机带来的跨平台性、优秀的垃圾回收
器，以及可靠的即时编译器。
Java技术的核心就是Java虚拟机(JVM，Java Virtual Machine)，因为所有的Java程序都运行在Java虚拟机内部。

## JVM结构

JVM整体结构如下：

![image-20230903111409485](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202309031114189.png)

## JVM家族

1. Sun Classic/Exact VM

# 自动内存管理

## 类加载机制

### 字节码文件（.class）

参考：https://pdai.tech/md/java/jvm/java-jvm-class.html

1. 字节码文件：class文件本质上是一个以8位字节为基础单位的二进制流，各个数据项目严格按照顺序紧凑的排列在class文件中。jvm根据其特定的规则解析该二进制数据，从而得到相关信息。

2. 文件结构属性

   ![img](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202212012327723.png)

3. 地方

### 加载流程

### 类加载器

参考资料：

* 文档：
  * [Oracle官方](https://docs.oracle.com/javase/specs/index.html)
* 书籍：
  * 《深入理解Java虚拟机》
  * 《Java虚拟机规范》
  * 《自己动手写Java虚拟机》
* 视频：
  * [尚硅谷JVM](https://www.bilibili.com/video/BV1PJ411n7xZ/?p=1&vd_source=fabefd3fabfadb9324761989b55c26ea)
  * [黑马程序员JVM]([黑马程序员JVM完整教程，Java虚拟机快速入门，全程干货不拖沓_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1yE411Z7AP/?vd_source=fabefd3fabfadb9324761989b55c26ea))