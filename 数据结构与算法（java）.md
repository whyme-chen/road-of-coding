# 数据结构与算法

## 一、概述

### 1. 数据结构

#### 1.1分类

1. 逻辑结构
   * 集合
   * 线性结构
   * 树形结构
   * 图形结构
2. 物理结构
   * 顺序结构
   * 链式结构

### 2. 算法

#### 2.1时间复杂度分析

1. 事后分析方法

2. 事前分析方法

   在计算机程序编写前，依据统计方法对算法进行估算，总结发现，高级语言编写的程序在计算机上运行的时间取决于以下几个因素：

   * 算法采用的策略和方案
   * 编译产生的代码质量
   * 问题的输入规模
   * 机器执行指令的速度
   
3. 常用的算法复杂度记法（大O记法）

   * 线性阶O(n)
   * 平方阶O(n^2)
   * 立方阶O(n^3)
   * 对数阶O(logn)
   * 常数阶O(1)

   时间复杂度比较：O(1)<O(logn)<O(n)<O(nlogn)<O(n^2) <O(n^3)


#### 2.2空间复杂度分析

## 二 、常用排序算法

### Comparable接口

### 排序的稳定性

在待排序文件中，若存在多个关键字相同的记录，经过排序后这些具有相同关键字的记录之间的相对次序保持不变，则该排序方法是稳定的，否则该排序方法是不稳定的。注意此处的稳定性是针对所有待排序的记录，即只要有一个不满足稳定规则，该排序方法就是不稳定的。

### 排序的分类

按在排序过程中是否涉及数据的内外存交换可以将排序大致分为内部排序和外部排序两类。一般情况下，内排序适宜在记录个数不多的小文件中使用，外排序则适用于记录个数太多，不能一次将其全部记录放入内存的大文件。

![img](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img849589-20190306165258970-1789860540.png)

### 1. 冒泡排序

1. 原理：比较相邻元素，如果前一个元素比后一个元素大，则交换两个元素的位置，否则不变。对每一对相邻元素做同样的比较操作，从第一对元素到最后一对元素，最终最后位置的元素就是最大值。

2. 代码实现

   ~~~java
   //排序给定数组[4,7,5,9,3,7,12,25]
   public class Test {
       public static void main(String[] args) {
           int[] arr = {4,7,5,9,3,7,12,25};
           bubbleSort(arr);
           for (int x:arr) {
               System.out.print(x+"\t");
           }
       }
   
       public static void bubbleSort(int[] array) {
           for (int i = 0; i < array.length; i++) {//记录已排好序个数
               for (int j = 0; j < array.length - i-1; j++) {//控制比较的数字
                   if (array[j]>array[j+1]) {
                       int temp=array[j];
                       array[j]=array[j+1];
                       array[j+1]=temp;
                   }
               }
           }
       }
   }
   
   ~~~

   API设计：

   ~~~java
   public class Bubble{
       /*
       	对数组元素进行排序
       */
       public static void sort(Comparable[] a){
           for(int i=a.length;i>0;i--){
               for(int j=0;j<i;j++){
                   if(greater(a[j],a[j+1])){
                       exchange(a,j,j+1);
                   }
               }
           }
       }
       
       /*
       	比较两个元素的大小	
       */
       public static boolean greater(Comparable v,Comparable w){
           return v.compareTo(w)>0;
       }
       /*
       	交换两个元素的位置
       */
       public static void exchange(Comparable[] a,int i,int j){
         Comparable temp;
           temp = a[i];
           a[i]= a[j];
           a[j]= temp;
       } 
   }
   ~~~

3. 时间复杂度分析

   最坏情况，待排序数组为逆序。此时时间复杂度为O(n^2)。

### 2. 快速排序

1. 原理（分治法）：在待排序序列中任选一个记录作为基准，以此基准将整个待排序序列划分为左右两个小区域，使得小于或等于此基准的记录位于该基准左区域中，大于该基准的记录位于该基准的有区域中。然后对划分出来的左右连个区域重复上述操作，直到整个序列排序完成。（即每一次划分都确定一个记录的最终位置）

2. 代码实现

   ~~~java
   
   ~~~

   API设计：

   ~~~java
   public class Quick {
       public static void QuickSort(Comparable[] a){
           sort(a,0,a.length-1);
       }
   
       /**
        * 比较元素v是否小于或等于元素w
        * @param v
        * @param w
        * @return
        */
       public static boolean less(Comparable v,Comparable w){
           return v.compareTo(w)<0;
       }
   
       /**
        * 交换数组元素的位置
        * @param a
        * @param i
        * @param j
        */
       public static void exchange(Comparable[] a,int i,int j){
           Comparable temp=a[i];
           a[i]=a[j];
           a[j]=temp;
       }
   
       /**
        * 对数组元素从low到high进行排序
        * @param a
        * @param low
        * @param high
        */
       public static void sort(Comparable[] a,int low,int high){
           //安全性校验
           if (high<=low){
               return;
           }
           //分组
           int partition=partition(a,low,high);//该返回索引为位置变换后的索引
           //使左子组有序
           sort(a,low,partition-1);
           //使右子组有序
           sort(a,partition+1,high);
       }
   
       /**
        * 对数组进行划分，从low到high并返回分组界限对应的索引
        * @param a
        * @param low
        * @param high
        */
       public static int partition(Comparable[] a,int low,int high){
           Comparable key=a[low];
           int left=low;
           int right=high+1;
           while(true){
               while(less(key,a[--right])){
                   if (right==low){
                       break;
                   }
               }
               while (less(a[++left],key)){
                   if (left==high){
                       break;
                   }
               }
               if (left>=right){
                   break;
               }else {
                   exchange(a,left,right);
               }
           }
           exchange(a,low,high);
           return right;
       }
   }
   
   ~~~

3. 时间复杂度分析

   最好情况，时间复杂度为O(nlogn)；

   最坏情况，时间复杂度为O(n^2)；

   平均情况，时间复杂度为O(nlogn)。

### 3. 选择排序

1. 原理：每一次遍历都从未排序的序列中选择出最小值作为已排序序列的最后一个元素，直到整个数组都变成已排序序列。

2. 代码实现

   ~~~java
   public class Test {
       public static void main(String[] args) {
           int[] arr={23,45,12,45,67,12,89,23};
           selectSort(arr);
           for (int x :arr) {
               System.out.print(x+"\t");
           }
   
       }
       
   	//选择排序，每次默认未排序序列的第一个为最小值
       public static void selectSort(int[] arr){
           int temp;
           for (int i = 0; i < arr.length; i++) {
               for (int j = i; j < arr.length; j++) {
                   if (arr[j]<arr[i]){
                       temp=arr[j];
                       arr[j]=arr[i];
                       arr[i]=temp;
                   }
               }
           }
       }
   }
   
   ~~~

   API设计：

   ~~~java
   public class Selection{
       /*
       	对数组元素进行排序
       */
       public static void selectSort(Comparable[] a){
           for(int i=0;i<a.length;i++){
               int minIndex=i;//记录最小值的索引下标,默认为未排序序列的第一个值的小标
               for(int j=i+1;j<a.length;j++){
                   if(greater(a[minIndex],a[j])){
                       minIndex=j;
                   }
               }
               if(i!=minIndex){
                   exchange(a,i,minIndex);//交换最小值
               }
           }
       }
   
       /*
       	判断元素v是否比元素w大
       */
       public static boolean greater(Comparable v,Comparable w){
           return v.compareTo(w)>0;
       }
   
       /*
       	交换两个元素的位置
       */
       public static void exchange(Comparable[] a,int i,int j){
           Comparable temp=a[i];
           a[i]=a[j];
           a[j]=temp;
       }
   }

3. 时间复杂度分析

   选择排序的时间复杂度为O($n^2$)。

### 4. 插入排序

1. 原理：将待排序序列分为已排序和未排序两组，找到未排序组中的第一个元素向已排序组中插入，倒序遍历已排序组，直到找到一个元素小于等于待插入元素，就把这个元素放入该位置并将其他元素后移一位。

2. 代码实现

   ~~~java
   public class Test01 {
       public static void main(String[] args) {
           int[] arr = {12,5,7,9,3,18,18,3,4,2,1,34,45,232,90};
           InsertSort(arr);
           for (int x :arr) {
               System.out.print(x+"\t");
           }
       }
   
       public static void InsertSort(int[] arr){
           for (int i = 1; i < arr.length; i++) {//i为未排序组的起始位置
               if (arr[i]<arr[i-1]) {
                   int temp = arr[i];
                   arr[i] = arr[i-1];
                   arr[i-1] = temp;
               }else {
                   continue;
               }
               //倒序遍历比较
               for (int j = i-1; j > 0; j--) {
                   if (arr[j]<arr[j-1]){
                       int temp = arr[j];
                       arr[j] = arr[j-1];
                       arr[j-1] = temp;                    
                   }else {
                       break;
                   }
               }
           }
       }
   }
   
   ~~~

   API设计：

   ~~~java
   public class Insert {
       public static void insertSort(Comparable[] a) {
           for (int i = 1; i < a.length; i++) {
               for (int j = i; j > 0 ; j--) {
                   if (greater(a[j-1],a[j])){
                       exchange(a,j-1,j);
                   }else {
                       break;
                   }
               }
           }
       }
   
       /**
        * 比较元素v和w的大侠
        * @param v
        * @param w
        * @return
        */
       public static boolean greater(Comparable v,Comparable w) {
           return v.compareTo(w)>0;
       }
   
       /**
        * 交换连个元素的位置
        * @param a
        * @param i
        * @param j
        */
       public static void exchange(Comparable[] a,int i,int j) {
           Comparable temp = a[i];
           a[i] = a[j];
           a[j] = temp;
       }
   }
   

3. 时间复杂度分析

   最坏情况下时间复杂度为O(n^2)；

### 5. 归并排序

1. 原理：先将n个数据看成n个长度为1的表，将相邻的表成对合并，得到长度为2 的n/2个有序表，再次重复上述步骤，直到所有数据均合并成一个长度为n的有序表为止。

2. 代码实现

   API设计：

   ~~~java
   public class Merge {
       //辅助数组
       private static Comparable[] assists;
   
       private static boolean less(Comparable v,Comparable w) {
           return v.compareTo(w)<0;
       }
   
       private static void exchange(Comparable[] a,int i,int j) {
           Comparable temp = a[i];
           a[i] = a[j];
           a[j] = temp;
       }
   
       /**
        * 对数组a中元素进行排序
        * @param a
        */
       public static void sort(Comparable[] a) {
           assists =new Comparable[a.length];
           int low=0,high=a.length-1;
           sort(a,low,high);
       }
   
       /**
        * 对数组a中从low到high中的元素进行排序
        * @param a
        * @param low
        * @param high
        */
       private static void sort(Comparable[] a,int low,int high) {
           if (low<0){//安全性校验
               return;
           }
           int mid = low+(high-low)/2;
           sort(a,low,mid);
           sort(a,mid,high);
           merge(a,low,mid,high);
       }
   
       private static void merge(Comparable[] a,int low,int mid,int high) {
           int i=low,p1=low,p2=mid+1;
           while (p1<=mid && p2<=high) {
               if (less(a[p1],a[p2])) {
                   assists[i++]=a[p1++];
               }else {
                   assists[i++]=a[p2++];
               }
           }
   
           while (p1<=mid) {
               assists[i++]=a[p2++];
           }
   
           while (p2<=high) {
               assists[i++]=a[p2++];
           }
           for (int j = low; j < high; j++) {
               a[j]=assists[j];
           }
       }
   }
   
   ~~~

3. 时间复杂度分析

   归并排序的时间复杂度为O(nlogn)。

### 6. 希尔排序

1. 原理：选定一个增长量h，按照增长量h作为数据分组依据对数据进行分组；对分好组的每一组数据进行插入排序；减小增长量，最小减为1，重复第二步。

   ![image-20220221155022462](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220221155022462.png)

   > 增长量h选取规则：
   >
   > ~~~ java
   > int h = 1;
   > while(h<array.length/2){
   >     h = 2h+1;
   > }
   > //循环结束后确定h最大值，h的减小规则为：
   > h=h/2

2. 代码实现

   API设计：

   ~~~java
   public class Shell {
       public static void shellSort(Comparable[] a) {
           //根据数组长度确定增长量h的值
           int h=1;
           while (h<a.length/2) {
               h=2*h+1;
           }
           while (h>=1) {
               //排序
               for (int i = h; i < a.length; i++) {
                   for (int j = i; j >= h ; j-=h) {
                       if (greater(a[j-h],a[j])) {
                           exchange(a,j-h,j);
                       }else {
                           break;
                       }
                   }
               }
               //减小h的值
               h=h/2;
           }
       }
   
       public static boolean greater(Comparable v,Comparable w) {
           return v.compareTo(w)>0;
       }
   
       public static void exchange(Comparable[] a,int i ,int j) {
           Comparable temp = a[i];
           a[i] = a[j];
           a[j] = temp;
       }
   }
   

3. 时间复杂度分析

   希尔排序是直接插入排序的优化，时间复杂度优于直接插入排序。另外希尔排序是一种不稳定的排序方法。

### 7. 堆排序

1. 原理
2. 代码实现
3. 时间复杂度分析

### 总结

![img](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img849589-20180402133438219-1946132192.png)

## 三、线性表



### 顺序表



### 链表

## 堆栈

## 队列

### 1. 队列的定义及基本概念

1.  队列定义：队的操作是在两端进行，其中一端只能进行插入，该端称为队列的队尾。而另一端只能进行删除，称为该队列的队首。

2. 特征：先进先出（FIFO）

3. 存储方式：顺序存储和链式存储。

   > 注意： 队列在顺序存储时常出现“假溢出”的现象。解决该问题的方法有许多种。例如，保持队首指针始终不动，但是该方法会造成大量的数据移动。因此解决该问题的常用方法是使用循环队列。

4. 基本运算：

   * 置空队：构造一个空队列
   * 判空队：判断队列是否为空，空则返回真，否则返回假
   * 判队满：队列满则返回真，否则返回假
   * 入队：队列非满时，从队尾插入元素
   * 出队：队列非空时，从队首删除元素
   * 取队首元素

### 2. 顺序队列

队列的顺序存储结构成为顺序队列，实际上是运算受限的顺序表。为解决“假溢出”问题，通常使用循环队列，其表示如下：

## 树

树形结构反映了数据元素之间的层次关系和分支关系。

### 1. 树的概念

1. 树的定义：树是一种数据结构，表示为TREE=（D,R）。其中，D是具有相同特性的数据元素的集合，R是元素集合D上的关系集合。

   > 树的递归定义：树是由根阶段和若干科子树构成的。
   >
   > 注意：树中结点一般没有次序之分，其次序可以任意颠倒。

2. 树的表示方法

   * 树型表示法
   * 文氏图表示法
   * 凹入图表示法
   * 广义表表示法

3. 基本术语

   * 结点的度：一个结点的子树个数
   * 树的度：一棵树中结点度最大值
   * 叶子（终端结点）：度为零的结点
   * 分支结点（非终端结点）：度不为零的结点
   * 内部结点：除根节点外的分枝结点
   * 祖先：一个结点的祖先是从根节点到该结点路径上所经过的所有结点
   * 子孙：一个结点的子孙是以该结点为根的子树中的所有的结点
   * 结点的层数：从根节点开始算起，设根节点层数为1
   * 树的高度（深度）：树中结点的最大层数
   * 有序树：若把树中每个结点的各子树看成从左到右有次序，则该树为有序树
   * 无序树：若把树中每个结点的各子树看成可以互换次序，则该树为序树
   * 森林：m（m>=0）棵互不相交树的集合。

### 2. 二叉树

#### 定义

#### 性质

* 二叉树第i（i>=1）层上的结点数最多为2^(i-1)
* 高度为k的二叉树最多有2^k-1个结点

#### 抽象数据类型

#### 存储结构

##### 顺序存储

原则：不管该二叉树是否为完全二叉树，都将其看成完全二叉树进行存储

##### 链式存储

#### 遍历

##### 前序遍历

若二叉树非空，依次进行如下操作：

* 遍历根结点
* 遍历左子树
* 遍历右子树

##### 中序遍历

若二叉树非空，依次进行如下操作：

* 遍历左子树
* 遍历根结点
* 遍历右子树

##### 后序遍历

若二叉树非空，依次进行如下操作：

* 遍历左子树
* 遍历右子树
* 遍历根结点

##### 层次遍历

## 图

### 1. 图的定义及相关术语

1. 图的定义
2. 基本术语
   * 有向图
   * 无向图
   * 度
   * 子图
   * 路径
   * 连通图
   * 连通分量

### 2. 图的存储

### 邻接矩阵

### 邻接表

### 十字链表

### 邻接多重表



