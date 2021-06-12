# HTML学习总结

## 常见浏览器

* IE浏览器
* Chrome（谷歌浏览器）
* 火狐浏览器
* Edge浏览器
* Opera浏览器

## web标准

* 结构标准：对网页元素进行整理和分类，主要包括XML和HTML两个部分
* 表现标准：用于设置网页元素的版式、颜色、大小等外观样式，主要指的是CSS
* 行为标准：网页模型的定义及交互的编写，主要包括DOM和ECMAScript

## 常用标签

* 

* base标签：设置a标签整体链接状态。

  ~~~html
  <!DOCTYPE html>
  <html>
  <head>
  	<title></title>
  	<base target="_blank">
  </head>
  <body>
  	<a href="https://www.baidu.com">百度</a>
  	<a href="https://www.souhu.com">搜狐</a>
  </body>
  </html>
  ~~~

* 常用文本格式标签

  ~~~html
  <!DOCTYPE html>
  <html>
  <head>
  	<title></title>
  </head>
  <body>
  	<strong>加粗</strong>
  	<em>斜体</em>
  	<ins>下划线</ins>
  	<del>删除线</del>
  </body>
  </html>
  ~~~

* 自定义列表

  ~~~html
  <!DOCTYPE html>
  <html>
  <head>
  	<title></title>
  </head>
  <body>
  	<dl>
  		<dt>水果</dt>
  		<dd>苹果</dd>
  		<dd>香蕉</dd>
  	</dl>
  	<dl>
  		<dt>蔬菜</dt>
  		<dd>小白菜</dd>
  		<dd>大白菜</dd>
  	</dl>
  </body>
  </html>
  ~~~

* 特殊字符

  ![image-20210526120446548](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210526120446548.png)

+++



# CSS学习总结

## 语法规则

![image-20210526121911824](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20210526121911824.png)

## 书写方式

* 嵌入式
* 外链式
* 行内式

## 选择器

* 基本选择器
  * 通用选择器
  * 标签选择器
  * 类选择器
  * id选择器
* 组合选择器
  * 多元素选择器
  * 后代元素选择器（空格）
  * 子元素选择器（>）
  * 相邻兄弟选择器(+)
  * 通用兄弟选择器（~）
* 伪类选择器
  * ::link
  * ::hover
  * ::active
  * ::visited
* 伪元素选择器
* 属性选择器

## 字体属性

* font-style
* font-weight
* font-size
* font-family

## 布局

* display属性

  注意：display：none和visibility：hidden的区别

* width和max-width属性

* position属性

  position 属性规定应用于元素的定位方法的类型。

  有五个不同的位置值：

  - static
  - relative：相对于其正常位置进行定位
  - fixed：相对于视口定位
  - absolute：相对于最近的定位祖先元素进行定位
  - sticky：根据用户的滚动位置进行定位

* z-index属性：性指定元素的堆栈顺序（哪个元素应放置在其他元素的前面或后面）

| 属性                                                         | 描述                         |
| :----------------------------------------------------------- | :--------------------------- |
| [bottom](https://www.w3school.com.cn/cssref/pr_pos_bottom.asp) | 设置定位框的底部外边距边缘。 |
| [clip](https://www.w3school.com.cn/cssref/pr_pos_clip.asp)   | 剪裁绝对定位的元素。         |
| [left](https://www.w3school.com.cn/cssref/pr_pos_left.asp)   | 设置定位框的左侧外边距边缘。 |
| [position](https://www.w3school.com.cn/cssref/pr_class_position.asp) | 规定元素的定位类型。         |
| [right](https://www.w3school.com.cn/cssref/pr_pos_right.asp) | 设置定位框的右侧外边距边缘。 |
| [top](https://www.w3school.com.cn/cssref/pr_pos_top.asp)     | 设置定位框的顶部外边距边缘。 |
| [z-index](https://www.w3school.com.cn/cssref/pr_pos_z-index.asp) | 设置元素的堆叠顺序。         |

* overflow属性

  

* 大健康

## 单位

### 绝对单位

| 单位 | 描述                       |
| :--- | :------------------------- |
| cm   | 厘米                       |
| mm   | 毫米                       |
| in   | 英寸 (1in = 96px = 2.54cm) |
| px * | 像素 (1px = 1/96th of 1in) |
| pt   | 点 (1pt = 1/72 of 1in)     |
| pc   | 派卡 (1pc = 12 pt)         |

### 相对单位

| 单位 | 描述                                                         |
| ---- | ------------------------------------------------------------ |
| em   | 相对于元素的字体大小（font-size）（2em 表示当前字体大小的 2 倍） |
| ex   | 相对于当前字体的 x-height(极少使用)                          |
| ch   | 相对于 "0"（零）的宽度                                       |
| rem  | 相对于根元素的字体大小（font-size）                          |
| vw   | 相对于视口*宽度的 1%                                         |
| vh   | 相对于视口*高度的 1%                                         |
| vmin | 相对于视口*较小尺寸的 1％                                    |
| vmax | 相对于视口*较大尺寸的 1％                                    |
| %    | 相对于父元素                                                 |

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

注意：undefined==null（null和undefined的值相等，但类型不等）

### 引用数据类型

* 对象（Object）
* 数组（Array）
* 函数（Function）

### 运算符

* 比较运算符

  === 全等（值和类型都进行比较）

  == 等于（只比较值）

+ 逻辑运算符号

+++

### 字符串

~~~ javascript
//常用属性和方法
1.length 字符串长度
2.indexOf() 返回字符串中指定文本首次出现的索引位置
3.lastIndexOf() 方法返回指定文本在字符串中最后一次出现的索引
4.search() 方法搜索特定值的字符串，并返回匹配的位置：
5.slice() 提取字符串的某个部分并在新字符串中返回被提取的部分。
6.substring() 类似于 slice()，不同之处在于 substring() 无法接受负的索引。
7.substr() 类似于 slice()。不同之处在于第二个参数规定被提取部分的长度。
8.replace() 方法用另一个值替换在字符串中指定的值：默认地，replace() 只替换首个匹配：
9.toUpperCase() 把字符串转换为大写：
10.toLowerCase() 把字符串转换为小写：
11.concat() 连接两个或多个字符串：
12.trim() 方法删除字符串两端的空白符：
13.charAt() 方法返回字符串中指定下标（位置）的字符串：
14.charCodeAt() 方法返回字符串中指定索引的字符 unicode 编码：
15.split() 将字符串转换为数组：
~~~

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

~~~ javascript
//函数定义
方式一：
function fun(约束列表){
    函数体
}

注意：
* javaScript无需定义返回值类型
* 参数的定义无需使用var关键字，否则报错
* 函数体中return可以写也可以不写，具体按要求使用
* javaScript中不存在方法重载

//函数表达式
var x = function (a, b) {return a * b};
var z = x(4, 3);

注意：
函数提升，但是使用表达式定义的函数不会被提升。

//箭头函数
// ES5
var x = function(x, y) {
  return x * y;
}

// ES6
const x = (x, y) => x * y;
箭头函数没有自己的 this。它们不适合定义对象方法。
箭头函数未被提升。它们必须在使用前进行定义。
使用 const 比使用 var 更安全，因为函数表达式始终是常量值。
~~~

### 自定义对象

1. 对象创建方式

~~~ javascript
//使用对象字面量
var 对象名={属性1:属性值1,属性2:属性值2}
//使用new关键字
var 对象名=new Object();
~~~

2. for ....in循环

   ```
   var person = {fname:"Bill", lname:"Gates", age:62}; 
   
   for (x in person) {
       txt += person[x];
   }
   ```

3. 删除属性

   ```
   var person = {firstName:"Bill", lastName:"Gates", age:62, eyeColor:"blue"};
   delete person.age;   // 或 delete person["age"];
   ```



### 正则对象

1. RegEXp对象

   直接量方式创建(开发中常用)

   ``` javascript
   var reg=/^表达式$/;
   ```

2. 常用方法

   test


### 正则表达式（Regular Expression）

1. 正则表达式是由一个字符序列形成的搜索模式。

2. 两个常用字符串方法：

   * search（）

   * replace（）

3. 正则表达式修饰符

   | 修饰符 | 描述                 |
   | ------ | -------------------- |
   | i      | 执行大小写不敏感匹配 |
   | g      | 执行全局匹配         |
   | m      | 执行多行匹配         |


4. 正则表达式模式

   * 方括号用于查找某个范围内的字符，例如[abc],[0-9],(x|y)查找任何以|分隔的选项
   * 元字符：拥有特殊含义的字符

   | 元字符 | 描述         |
   | ------ | ------------ |
   | \d     | 查找数字     |
   | \s     | 查找空白字符 |
   | \b     | 匹配单词边界 |
   | \uxxxx |              |


### 表单验证

1. 约束验证DOM方法

   | 属性                | 描述                                       |
   | :------------------ | :----------------------------------------- |
   | checkValidity()     | 返回 true，如果 input 元素包含有效数据     |
   | setCustomValidity() | 设置 input 元素的 validationMessage 属性。 |

```
<input id="id1" type="number" min="100" max="300" required>
<button onclick="myFunction()">OK</button>

<p id="demo"></p>

<script>
 function myFunction() {
    var inpObj = document.getElementById("id1");
    if (inpObj.checkValidity() == false) {
        document.getElementById("demo").innerHTML = inpObj.validationMessage;
    }
}
</script>
```

## 三、BOM对象

### 1. 概念：Browser Object Model（浏览器对象模型）

### 2. 组成

* **窗口对象（window）**
* **历史记录对象（history）**
* **地址栏对象（location）**
* 显示器屏幕（screen）
* 浏览器对象（navigator）

### 3. Window对象

* 特点：
  * Window对象不需要创建可以直接使用
  * Window对象可以省略
* 属性：
  * 获取其他BOM对象
    * history
    * location
    * Navigator
    * Screen
  * 获取DOM对象
    * document
* 方法：
  * 与弹出框有关的方法
    * alert（）显示带有一段消息和一个确认按钮的警告框
    * confirm（）显示带有一段消息以及确认按钮和取消按钮的对话框
    * prompt（）显示可提示用户输入的对话框
  * 与打开关闭有关的方法
    * close（）关闭浏览器窗口
    * open（）打开一个新窗口
  * 与定时器有关的方法
    * setTimeOut（）在指定的毫秒数后调用函数或计算表达式
    * clearTimeOut（）取消由setTimeOut设置的timeout
    * setInterval（）按照指定的周期（以毫秒数计）来调用函数或计算表达式
    * cleatInterval（）取消由setInterval（）设置的timeout
* 案例：轮播图

~~~ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>轮播图</title>
</head>
<body>
    <img src="../image02/QQ图片（修改后5）.jpg" width="100%" height="100%" id="image" alt="图片加载失败">
    <script>
        var i=1;
        function change() {
            i++;
            if (i>15){
                i=1;
            }
            document.getElementById("image").src = "../image02/QQ图片（修改后"+i+"）.jpg";
        }
        setInterval("change()",2000);

    </script>
</body>
</html>
~~~

### 4. location对象

* 获取：Window.location

* 方法
  * reload（）：重新加载当前文档、刷新
* 属性
  * href：设置或返回完整的URL
* 案例：自动跳转

~~~ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>自动跳转</title>
</head>
<body>
    <p id="p"></p>
    <script>
        var second=5;
        function trap() {
            document.getElementById('p').innerHTML=second+"秒后自动跳转";
            second--;
            if (second==0){
                window.location.href="https://www.baidu.com";
            }
        }
        window.setInterval("trap()",1000);
    </script>
</body>
</html>
~~~



## 四、DOM对象

DOM是将标记型文档中所有内容（标签、文本、属性）都封装成对象，通过操作对象的属性或方法，来达到操作或改变HTML展示效果的目的。

操作Element对象：

* 修改属性值
* 修改标签体内容

### DOM树

![image-20210610161008121](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20210610161008121.png)

* 每个标签会被加载成DOM树上的一个元素节点对象
* 每个标签的属性会被加载成DOM树上的一个属性节点对象
* 每个标签的内容体会被加载成DOM树上的一个文本结点对象
* 整个DOM树，是一个文档结点对象，即DOM对象
* 一个HTML文档加载到内存中就会形成一个DOM对象

### 获取元素对象的四种方式

* getElementByld（）//通过元素ID获取对应元素对象
* getElementsByName（）//通过元素的name属性获取符合要求的所有元素
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

3. **常见的JS事件**

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

+++

| 事件        | 描述                         |
| :---------- | :--------------------------- |
| onchange    | HTML 元素已被改变            |
| onclick     | 用户点击了 HTML 元素         |
| onmouseover | 用户把鼠标移动到 HTML 元素上 |
| onmouseout  | 用户把鼠标移开 HTML 元素     |
| onkeydown   | 用户按下键盘按键             |
| onload      | 浏览器已经完成页面加载       |

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



# jQuery学习笔记

## 一、简介

1. jQuery是一个轻量级的JavaScript库。
2. jQuery库的特性：
   - HTML 元素选取
   - HTML 元素操作
   - CSS 操作
   - HTML 事件函数
   - JavaScript 特效和动画
   - HTML DOM 遍历和修改
   - AJAX
   - Utilities
3. 向页面添加jQuery库

~~~ html
<head>
    <script type="text/javascript" src="jquery.js"></script>
</head>
<！--注意：<script>标签应该位于<head>部分-->
~~~

4. JQuery安装

   **下载JQuery**

   **使用 Google 的 CDN**

   ```
   <head>
   <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs
   /jquery/1.4.0/jquery.min.js"></script>
   </head>
   ```

   **使用 Microsoft 的 CDN**

   ```
   <head>
   <script type="text/javascript" src="http://ajax.microsoft.com/ajax/jquery
   /jquery-1.4.min.js"></script>
   </head>
   ```

5. 基础语法

   $(selector).action( )

   * 美元符号$定义jQuery
   * 选择器selector “查询”和“查找”HTML元素
   * jQuery的action（）执行对元素的操作

   ~~~html
   <!DOCTYPE html>
   <html>
   	<head>
   		<meta charset="utf-8" />
   		<title></title>
   		<script src="js/jquery-2.1.1.min.js" type="text/javascript" charset="utf-8"></script>
   		<style type="text/css">
   			p{
   				background-color: red;
   			}
   		</style>
   	</head>
   	<body>
   		<p>哈哈</p>
   		<p>呵呵</p>
           
     		<script>
           	$(document).ready(function(){
   				alert("文档加载完毕");
   				$("p").click(function(){
   					$(this).hide();
   				});
   			});
          	</script>
   	</body>
   </html>
   
   ~~~

## 二、选择器

### 1. 基础选择器

