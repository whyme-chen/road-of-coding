# JavaScript学习笔记



## 一、JavaScript概述

1. JavaScript是什么

   web上强大的脚本语言。

   脚本语言：无法独立执行，必须嵌入到其他语言中结合使用

   ​					浏览器解释执行

2. JavaScript能够干什么

   控制页面特效展示

3. 语言特征

   没有访问系统文件的权限

   浏览器解释执行

4. javaScript组成

   ECMAScript：规定JS语法和基本对象

   DOM（文档对象模型）：处理网页内容的方法和接口

   BOM（浏览器对象模型）：与浏览器交互的方法和接口

5. 引入方式

   内部脚本

   外部引入

   注意：<script>标签中使用了src属性，则不能在标签内部不能写代码

+++

### javaScript显示数据

~~~ 
1.使用window.alert()弹出警告框
2.使用document.write()方法将内容写到HTML文档中
3.使用innerHTML写入到HTML元素
4.使用console.log()写入到浏览器控制台
~~~

## 二、基本语法

### 字面量

​	编程语言中，一般将固定值称为字面量。包括数字（Number）字面量，字符串（String）字面量，表达式字面量，数组（Array）字面量，对象（Object）字面量，函数（Function）字面量。

+++

### 变量

1. 变量的声明

   var 变量名;
   
   注意：变量是名称，字面量是值。

+++

### 基本数据类型

* string
* boolean
* number
* null
* undefined

注意：undefined==null

### 引用数据类型

### 运算符

* 比较运算符

  === 全等（值和类型都进行比较）

  == 等于（只比较值）

+ 逻辑运算符号

### 正则对象

1. RegEXp对象

   直接量方式创建(开发中常用)

   ``` javascript
   var reg=/^表达式$/;
   ```

2. 常用方法

   test

### 数组对象

1. JS数组特性
   * 数组中每一个成员没有类型限制，
   * 数组的长度可以自动修改

2. JS数组的四种创建方式

~~~ javascript
//方式一
var arr=[1,2,3];
//方式二
var arr=new Array();//数组长度默认为0
//方式三
var arr=new Array(4);//指定数组长度
//方式四
var arr=new Array(1,2);//数组元素是1,2
~~~

3. JS数组的常用属性/方法
   * length 数组长度
   * join() 将所有数组元素以指定分隔符进行连接
   * pop() 删除并返回数组的最后一个元素
   * push() 向数组的末尾添加一个或更多元素，并返回新长度
   * reverse() 颠倒数组中元素的顺序

### 全局函数

1. eval()函数：可以把传入的字符串，作为JavaScript的脚本代码进行执行，以此达到扩展程序功能的效果。

   注意：只能传递基本数据类型的字符串

2. encodeURI():把字符串编码为URL

   decodeURI():解码

   URI：统一资源标识符

   URL：统一资源定位器

### 自定义函数

1. 函数格式

   ~~~ javascript
   function 方法名(线束列表){
       函数体
   }
   ~~~

   注意：

   	* javaScript无需定义返回值类型
   	* 参数的定义无需使用var关键字，否则报错
   	* 函数体中return可以写也可以不写，具体按要求使用
   	* javaScript中不存在方法重载

### 自定义对象

1. 格式

~~~ javascript
//function构造函数
function 对象名(){
    
}
~~~

2. 对象直接量

   ~~~ javascript
   var 对象名={属性1:属性值1,属性2:属性值2}
   ~~~

   

## 三、BOM对象

## 四、DOM对象

DOM是将标记型文档中所有内容（标签、文本、属性）都封装成对象，通过操作对象的属性或方法，来达到操作或改变HTML展示效果的目的。

### DOM树

* 每个标签会被加载成DOM树上的一个元素节点对象
* 每个标签的属性会被加载成DOM树上的一个属性节点对象
* 每个标签的内容体会被加载成DOM树上的一个文本结点对象
* 整个DOM树，是一个文档结点对象，即DOM对象
* 一个HTML文档加载到内存中就会形成一个DOM对象

DOM树的特点：

### 获取元素对象的四种方式

* getElementByld（）//通过元素ID获取对应元素对象
* getElementsByName（）//通过元素的那么属性获取符合要求的所有元素
* getElementsByTagName（）//通过元素的元素名属性获取符合要求的所有元素
* getElementsByClassName（）//通过元素的class属性获取符合要求的所有元素

### 元素对象常见属性

* value
* className
* checked
* innerHTML

## 五、JS事件

1. JS事件是什么

   通常鼠标或热键的动作我们称之为事件（Event）

2. JS事件驱动机制

* 事件源：专门产生事件的组件
* 事件：由事件源产生的动作或事件
* 监听器：专门处理事件源所产生的事件
* 注册/绑定监听器

3. 常见的JS事件

* 点击事件（onclick）

* 焦点事件

  焦点：即整个页面的注意力

  默认一个正常页面最多仅有一个焦点

  * 获取焦点事件（onfocus）
  * 失去焦点事件（onblur）

* 域内容改变事件（onchange）

* 加载完毕事件（onload）

* 表单提交事件（onsubmit）

  注意：onsubmit用于表单的校验

  ​			true 允许表单提交

  ​			false 阻止表单提交

* 键位弹起事件（onkeyup）

* 常用鼠标事件

  * 鼠标移入事件（onmouseover）
  * 鼠标移出事件（onmouseout）

4. 元素事件句柄绑定
5. DOM绑定方式





## 六、BootStrap

### bootstrap概述

bootstrap是基于HTML、CSS、javaScript的前端框架。

该框架已经预定好了一套CSS样式和样式对应的JS代码。

作用：

* 使得web开发更加便捷、高校
* 支持响应式开发，解决了移动互联网前端开发问题

### 什么是响应式布局

响应式布局：一个网站的展示能够兼容多个终端

### 环境搭建

### 布局容器

任意元素是用来布局容器样式，都会成为一个布局容器，建议使用div作为布局容器。

| .container       | 类用于固定宽度并支持响应式布局的容器 |
| ---------------- | ------------------------------------ |
| .container-fluid | 类用于100%宽度，占据全部视口的容器   |

