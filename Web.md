前端&后端相关技术栈概述：

|                      | 前端                      | 后端               |
| -------------------- | ------------------------- | ------------------ |
| 环境                 | ES6+...                   | JDK8,11,17...      |
| 依赖管理             | npm                       | Maven              |
| 项目构建             | Vite，Webpack             | Maven              |
| 快速开发框架         | Vue3，Angular, React      | Spirng，Springboot |
| 页面跳转（路由管理） | Vue-Router                | SpringMVC          |
| 数据共享             | Pinia                     | Redis              |
| 页面布局框架         | Ant-Design-Vue，ElementUI |                    |
| 前后端交互           | ajax（axios）,Json        | ajax（axios）,Json |

# HTML

参考资料：https://www.w3school.com.cn/html/html5_intro.asp

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

## HTML基本骨架

~~~html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
        
	</body>
</html>

~~~

## 注释

html使用<!---->表示注释

## 常用标签

* 标题标签
  
* 水平线

* 段落标签

* br标签

* a标签
  
  ```html
  <!--
  重要属性
  1. href：链接的路径
  2. target：打开链接的方式
      值：
          _blank
          _parent
          _self
          _top
          framename
  3. name：规定锚的名称
  -->
  ```

* 媒体标签

  * img标签

    * 重要属性
      * src：图像存储位置
      * alt：为图像定义一串预备的可替换的文本。替换文本属性的值是用户定义的。

  * audio标签

    ![image-20230105151210477](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051512736.png)

    * 注意：音频标签目前支持3 E种格式: MP3、Wav、 Ogg

  * video标签

    ![image-20230105151438602](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051514010.png)

    * 注意：视频标签目前支持E种格式: MP4、WebM、Ogg

* base标签：设置a标签整体链接状态。
  
  ```html
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
  ```

* 引用
  
  ```html
  <!--
      <q>用于短引用
      <blockquote>用于引用节
      <abbr>用于缩略词
      <dfn>用于定义
      <address>用于联系信息
      <cite>用于著作标题
  -->
  ```

* 文本格式标签
  
  ```html
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
  ```

* 列表
  
  ```html
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
  ```

* 表格
  
  ```html
  
  <!--使用rowspan和colspan两个属性来合并单元格，注意只有同一个结构标签中的单元格才能合并，不能跨结构标签合并（即不能跨thead，tbody，tfoot合并）-->
  <table border="1">
      <caption>表格名</caption>
      <thead>
           <tr>
              <th>Heading</th>
              <th>Another Heading</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>row 1, cell 1</td>
              <td>row 1, cell 2</td>
          </tr>
        <tr>
              <td>row 2, cell 1</td>
              <td>row 2, cell 2</td>
          </tr>
      </tbody>
      <tfoot></tfoot>
  </table>
  ```
  
* div和span标签

* 语义化标签

  * 在HTML5新版本中，推出了- -些有语义的布局标签供开发者使用
  * 常见标签
    * header
    * nav
    * footer
    * aside
    * section
    * article

* iframe标签
  
  ```html
  <!--
  iframe 可用作链接的目标（target）。
  链接的 target 属性必须引用 iframe 的 name 属性：
  实例：
  <iframe src="demo_iframe.htm" name="iframe_a"></iframe>
  <p><a href="http://www.w3school.com.cn" target="iframe_a">W3School.com.cn</a></p>
  -->
  ```

* 表单标签

  * input标签

    * 通过type属性不同，展示不同的效果

      ![image-20230105155021642](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051550647.png)

    * placholder属性用于占位符，即提示信息

    * radio属性：通过name属性进行分组，checked属性表示默认选中。

    * file属性：通过multiple属性允许上传多个文件

  * button标签

    * type属性值如下

      ![image-20230105160107117](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051601778.png)

    * 注意：谷歌浏览器中button默认是提交按钮。button是双标签，更便于包裹其他内容（文字、图标）。

  * select标签

    * option标签是下拉菜单中的每一项。
    * 常用属性：selected表示默认选中。

  * textarea标签

    * 常见属性：cols表示文本域可见宽度，rows表示文本域可见高度。

  * lable标签：常用于绑定内容与表单标签的关系

    * 使用方法：
      * 方法1：使用lable标签包裹内容，为表单标签添加id，将id填入lable标签中的for属性中。
      * 方法2：直接使用lable标签把内容和表单标签包裹。

* 字符实体

  ![image-20230105161602755](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051616864.png)

# CSS

1. CSS特性
   * 继承性
   * 层叠性
   * 优先级

## 引入方式

* 内嵌式：使用style标签。
  
  ```html
  <style>
  </style>
  ```

* 外链式：将样式单独写在css文件中，通过link标签引入。
  
  ```html
  <link rel="stylesheet" type="text/css" href="">
  ```

* 行内式

## 选择器

### 基本选择器

* 通用选择器

  ![image-20230105181249672](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051812727.png)

* 标签选择器

  ![image-20230105180936199](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051809661.png)

* 类选择器

  ![image-20230105181000007](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051810684.png)

* id选择器

  ![image-20230105181112761](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051811495.png)

### 组合选择器

1. 多元素选择器（并集）

   ![image-20230105192618904](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051926717.png)

2. 交集选择器

   ![image-20230105192948343](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051929922.png)

3. 后代元素选择器（空格）

   ![image-20230105192451518](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051924814.png)

4. 子元素选择器（>）

   ![image-20230105192546301](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051925146.png)

5. 相邻兄弟选择器(+)

6. 通用兄弟选择器（~）

### 伪类选择器

1. :link

2. :hover

   ![image-20230105193036046](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051930701.png)

3. :active

4. :visited

5. :fitst-child

6. :last-child

7. nth-child(n)

8. nth-last-child(n)

### 伪元素选择器

1. 概念：一般页面中的非主体内容可以使用伪元素，由CSS模拟出来的标签效果，并非真正的标签。
2. 常用的伪元素
   * ::before
   * ::after
3. 注意
   * 必须设置content属性才能生效
   * 伪元素默认是行内元素。

### 属性选择器

* [attribute]：选取带有指定属性的元素
* [attribute="value"]：选取带有指定属性和值的元素
* [attribute~="value"]：选取属性值包含指定词的元素
* [attrbute|="value"]：选取指定属性以指定值开头的元素（值必须是完整或单独的单词）
* [attribute^="value"]：选取指定属性以指定值开头元素（值不必是完整单词）
* [attribute$="value"]：选取指定属性以指定值结尾的元素
* [attribute*="value"]：选取属性值包含指定词的元素（值不必是完整的单词）

### 选择器的优先级

1. 优先级

   ![image-20230105201009800](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301052010129.png)

2. 权重叠加计算

   ![image-20230105201545247](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301052015372.png)

3. 注意点

   * !important写在属性值的后面，分号的前面!
   * !important不能提升继承的优先级，只要是继承优先级最低!
   * 实际开发中不建议使用!important。

## 字体和文本样式

### 字体样式

1. font-size：字体大小

   * 谷歌浏览器默认文字大小是16px，单位需要设置，否则无效

2. font-style：字体样式

   * 取值
     * 正常（默认值）：normal
     * 倾斜：italic

3. font-weight：字体粗细

   * 取值：
     * 关键字
       * 正常：normal
       * 加粗：bold
     * 纯数字：100-999的整百数
       * 正常：400
       * 加粗：700
   * 不是所有字体都提供了九种粗细，因此部分取值页面中无变化。实际开发中以正常、加粗两种取值使用最多。

4. font-family：字体类型

   ![image-20230105182327436](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051823313.png)

   ![image-20230105182553706](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051825606.png)

5. font：字体类型，font属性连写

   ![image-20230105184541371](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051845850.png)

### 文本样式

1. text-indent：文本缩进
   * 取值
     * 数字+px
     * 数字+em（1em=当前font-size大小，推荐）
2. text-align：文本对齐
   * 取值
     * left
     * center
     * right
3. text-decoration：文本修饰
   * 取值
     * underline：下划线
     * line-through：删除线
     * overline：上划线
     * none：无装饰线
4. line-height：行高

## 背景相关属性

1. 背景颜色：background-color

2. 背景图片：background-image

   * 背景图片和img标签的区别

3. 背景平铺：background-repeat

   * 属性值：

     ![image-20230105193839629](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051938980.png)

4. 背景位置：background-position

   * 属性值：

     ![image-20230105194024449](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051940417.png)

   * 方位名词取值和坐标取值可以混使用，第一个取值表示水平，第二个取值表示垂直。

5. 背景相关属性连写

## 元素显示模式

1. 块级元素

   ![image-20230105195237865](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051952766.png)

2. 行内元素

   ![image-20230105195343256](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051953558.png)

3. 行内块元素

   ![image-20230105195519877](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051955326.png)

4. 元素模式间的转换

   ![image-20230105195825725](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051958713.png)

## 布局

* display属性：用于元素模式的转换
  
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

| 属性                                                                   | 描述             |
|:-------------------------------------------------------------------- |:-------------- |
| [bottom](https://www.w3school.com.cn/cssref/pr_pos_bottom.asp)       | 设置定位框的底部外边距边缘。 |
| [clip](https://www.w3school.com.cn/cssref/pr_pos_clip.asp)           | 剪裁绝对定位的元素。     |
| [left](https://www.w3school.com.cn/cssref/pr_pos_left.asp)           | 设置定位框的左侧外边距边缘。 |
| [position](https://www.w3school.com.cn/cssref/pr_class_position.asp) | 规定元素的定位类型。     |
| [right](https://www.w3school.com.cn/cssref/pr_pos_right.asp)         | 设置定位框的右侧外边距边缘。 |
| [top](https://www.w3school.com.cn/cssref/pr_pos_top.asp)             | 设置定位框的顶部外边距边缘。 |
| [z-index](https://www.w3school.com.cn/cssref/pr_pos_z-index.asp)     | 设置元素的堆叠顺序。     |

* overflow属性

### 浮动

1. 标准流

   ![image-20230107162802118](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301071628069.png)

2. 行内块元素的问题

   * 浏览器解析行内块或者行内标签的时候，如果标签换行书写则会产生一个空格的距离。

   ~~~html
   		<!-- 会产生间距 -->
   		<div class="one">one</div>
   		<div class="two">two</div>
   		<!-- 不会产生间距 -->
   		<div class="one">one</div><div class="two">two</div>
   ~~~

3. 浮动的作用

   * 早期：图文环绕
   * 现在：网页布局

4. 浮动的特点

   * 浮动元素会脱离标准流，在标准流中不占位置。
   * 浮动元素比标准流高半个级别，可以覆盖标准流中的元素
   * 浮动找浮动，下一个浮动元素会在上一个浮动元素后面左右浮动

5. css建议书写顺序

   > 1. 浮动或display
   > 2. 盒子模型
   > 3. 文字样式

6. 清除浮动

   * 含义：清除浮动带来的影响，如果子元素浮动了，此时子元素不能撑开标准流的块级父元素。
   * 原因：子元素浮动脱离标准元素后不占位置
   * 目的：父元素应该有自己的高度，从而不影响其他网页元素的布局。
   * 方法：
     * 额外标签
     * 单伪元素
     * 双伪元素
     * overflow属性

### Flex布局

参考教程：

* http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html
* https://www.ruanyifeng.com/blog/2015/07/flex-examples.html

~~~ html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Flex布局</title>
		<style type="text/css">
			
			.div1{
				
				display: flex;
				width: 500px;
				height: 700px;
				border: 3px soild #FF0000;
				background-color: #999900;
				flex-direction: row;/* 主轴方向 */
				flex-wrap: wrap;/* 是否换行 */
				justify-content: space-between;/* 主轴对齐方式 */
				align-items: center;/* 交叉轴对齐方式 */
			}
			.item{
				width: 200px;
				height: 50px;
				border: 1px solid #FF0000;
				background-color: #000000;
				flex-grow: 0;/* 放大 */
			}
		</style>
	</head>
	<body>
		<div class="div1">
			<div class="item">
				
			</div>
			<div class="item">
				
			</div>
			<!-- <div class="item">
				
			</div>
			<div class="item">
				
			</div> -->
		</div>
	</body>
</html>
~~~

## 颜色

![image-20230105192325160](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301051923036.png)

## 单位

### 绝对单位

| 单位   | 描述                       |
|:---- |:------------------------ |
| cm   | 厘米                       |
| mm   | 毫米                       |
| in   | 英寸 (1in = 96px = 2.54cm) |
| px * | 像素 (1px = 1/96th of 1in) |
| pt   | 点 (1pt = 1/72 of 1in)    |
| pc   | 派卡 (1pc = 12 pt)         |

### 相对单位

| 单位   | 描述                                       |
| ---- | ---------------------------------------- |
| em   | 相对于元素的字体大小（font-size）（2em 表示当前字体大小的 2 倍） |
| ex   | 相对于当前字体的 x-height(极少使用)                  |
| ch   | 相对于 "0"（零）的宽度                            |
| rem  | 相对于根元素的字体大小（font-size）                   |
| vw   | 相对于视口*宽度的 1%                             |
| vh   | 相对于视口*高度的 1%                             |
| vmin | 相对于视口*较小尺寸的 1％                           |
| vmax | 相对于视口*较大尺寸的 1％                           |
| %    | 相对于父元素                                   |

## 盒子模型

1. 简介

   ![image-20230105203406122](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202301052034471.png)

2. 内容的宽度和高度（width和height）

3. 边框（border）

4. 外边距（margin）

   * 外边距折叠现象：垂直布局的块级元素，上下的margin会合并，最终为两者中的最大值。可以只设置一个元素的margin解决此问题。
   * 塌陷现象：互相嵌套的块级元素，子元素的margin-top会作用在父元素上，导致父元素一起向下移动。
     * 方法1：给父元素设置border-top或者padding-top (分隔父子元素的margin-top)
     * 方法2：给父元素设置overflow: hidden
     * 方法3：转换成行内块元素
     * 方法4：设置浮动
   * 行内元素的垂直内外边距

5. 内边距（padding）

## 浏览器调试工具（google）

# JavaScript

权威网站：https://developer.mozilla.org/zh-CN/

## JavaScript概述

1. JavaScript
   
   * web上强大的脚本语言。
   
   * 脚本语言：无法独立执行，必须嵌入到其他语言中结合使用，浏览器解释执行

2. JavaScript功能/作用：
   
   * 页面特效
* 表单验证
   * 数据交互
   * 服务器端编程（nodejs）
   
3. 语言特征

   没有访问系统文件的权限

   浏览器解释执行

4. 浏览器执行JS

   * 浏览器分成两部分，一部分是渲染引擎，一部分是JS引擎
     * 渲染引擎（俗称内核）：用于解析HTML和CSS
     * JS引擎（JS解释器）：读取网页js代码

5. javaScript组成

   * ECMAScript：规定JS语法和基本对象

   * DOM（文档对象模型）：处理网页内容的方法和接口
   * BOM（浏览器对象模型）：与浏览器交互的方法和接口

6. 引入方式（书写位置）

   * 内部脚本
   * 外部引入
   * 行内

   注意：<script>标签中使用了src属性，则不能在标签内部写代码

## 基本语法

### 区分大小写

ECMAScript中一切变量区分大小写

### 标识符命名

即变量、函数、属性的名字或者函数的参数，规则如下：

* 由字母，下划线，数字或美元符组成
* 第一个字符必须是字母或下划线（_）或者美元符（$）

> 按照惯例，ECMAScript标识符采用驼峰大小写格式

### 注释

* 单行注释

  ~~~html
  //注释内容
  ~~~

* 块级注释

  ~~~html
  /*注释内容*/
  ~~~

### 输入输出

1. 输出

   > 1.使用window.alert()弹出警告框
   > 2.使用document.write()方法将内容写到HTML文档中
   > 3.使用innerHTML写入到HTML元素
   > 4.使用console.log()写入到浏览器控制台
   > 注意：在 HTML 文档完全加载后使用 document.write() 将删除所有已有的 HTML ：

2. 输出

   > prompt()：显示一一个对话框，对话框中包含一条文字信息，用来提示用户输入文字

### 严格模式

ECMAScript 5 引入严格模式概念。严格模式是为JavaScript定义了一种不同的解析和执行模型。严格模式下，ECMAScript 3中的一些不确定的行为将得到处理，而且对某些不安全的操作也会抛出错误。在整个脚本中启用严格模式，可以在顶部添加如下代码：

~~~
*use strict*
~~~

指定函数在严格模式下执行：

~~~
function doSomething(){
	*use strict*
	//函数体
}
~~~

### 关键字和保留字

![image-20220301180653244](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220301180653244.png)

### 字面量

​    编程语言中，一般将固定值称为字面量。包括数字（Number）字面量，字符串（String）字面量，表达式字面量，数组（Array）字面量，对象（Object）字面量，函数（Function）字面量。

### 变量

1. 变量的声明
   
   ```javascript
   let 变量名;
   ```
   
   > 注意：
   >
   > * 变量是名称，字面量是值。
   > * ECMAScript中变量是松散类型的，即可以用来保存任何类型的数据。
   > * 严格模式下，不能定义名为eval或argument的变量，否则会导致语法错误。
   
2. 变量命名规则（遵循标识符命名规则）
   
   * 由数字、字母、下划线和$组成
   * 不能以数字开头
   * 不能是关键字
   * 严格区分大小写
   
3. var和let的区别

   ![image-20230214130242527](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302141302073.png)

### 常量

1. 概念：一经定义，值不予许改变

2. 声明

   > const 常量名

3. 命名规范：与变量一致

### 作用域

1. 全局作用域

   > *全局*（在函数之外）声明的变量拥有*全局作用域*。

2. 函数作用域

   > 局部（函数内）声明的变量拥有函数作用域。

3. 块级作用域：

   > ES2015 引入了两个重要的 JavaScript 新关键词：`let` 和 `const`。这两个关键字在 JavaScript 中提供了块作用域（*Block Scope*）变量（和常量）。
   >
   > * 通过 `var` 关键词声明的变量没有块*作用域*。在块 *{}* 内声明的变量可以从块之外进行访问。
   > * 在 ES2015 之前，JavaScript 是没有块作用域的。可以使用 `let` 关键词声明拥有块作用域的变量。在块 *{}* 内声明的变量无法从块外访问：
   > * JavaScript const 变量必须在声明时赋值：关键字 `const` 有一定的误导性。它没有定义常量值。它定义了对值的常量引用。因此，我们不能更改常量原始值，但我们可以更改常量对象的属性。

### 运算符

* 赋值运算符

  | 运算符 | 例子   | 等同于    |
  | :----- | :----- | :-------- |
  | =      | x = y  | x = y     |
  | +=     | x += y | x = x + y |
  | -=     | x -= y | x = x - y |
  | *=     | x *= y | x = x * y |
  | /=     | x /= y | x = x / y |
  | %=     | x %= y | x = x % y |

* 算术运算符

  | 运算符 | 描述         |
  | :----- | :----------- |
  | +      | 加法         |
  | -      | 减法         |
  | *      | 乘法         |
  | /      | 除法         |
  | %      | 取模（余数） |
  | ++     | 递加         |
  | --     | 递减         |
  | **     | 幂运算       |

* 比较运算符

  | 运算符  | 描述           |
  | :------ | :------------- |
  | **==**  | 等于           |
  | **===** | 等值等型       |
  | !=      | 不相等         |
  | **!==** | 不等值或不等型 |
  | >       | 大于           |
  | <       | 小于           |
  | >=      | 大于或等于     |
  | <=      | 小于或等于     |
  | ?       | 三元运算符     |
  
  > === 全等（值和类型都进行比较）
  >
  > == 等于（只比较值）

+ 逻辑运算符

  | 运算符 | 描述   |
  | :----- | :----- |
  | &&     | 逻辑与 |
  | \|\|   | 逻辑或 |
  | !      | 逻辑非 |

+ 类型运算符

  | 运算符     | 描述                                  |
  | :--------- | :------------------------------------ |
  | typeof     | 返回变量的类型。                      |
  | instanceof | 返回 true，如果对象是对象类型的实例。 |

+ 位运算符

  位运算符处理 32 位数。该运算中的任何数值运算数都会被转换为 32 位的数。结果会被转换回 JavaScript 数。

  | 运算符 | 描述         | 例子    | 等同于       | 结果 | 十进制 |
  | :----- | :----------- | :------ | :----------- | :--- | :----- |
  | &      | 与           | 5 & 1   | 0101 & 0001  | 0001 | 1      |
  | \|     | 或           | 5 \| 1  | 0101 \| 0001 | 0101 | 5      |
  | ~      | 非           | ~ 5     | ~0101        | 1010 | 10     |
  | ^      | 异或         | 5 ^ 1   | 0101 ^ 0001  | 0100 | 4      |
  | <<     | 零填充左位移 | 5 << 1  | 0101 << 1    | 1010 | 10     |
  | >>     | 有符号右位移 | 5 >> 1  | 0101 >> 1    | 0010 | 2      |
  | >>>    | 零填充右位移 | 5 >>> 1 | 0101 >>> 1   | 0010 | 2      |

### 表达式和语句

> 表达式可被求值
>
> ECMAScript中语句以一个分号结尾，若省略分号，则由解析器确定语句的结尾。以分号结束语句不是必需的，但我们仍然强烈建议您这么做。

### 流程控制

1. 顺序结构

2. 判断结构
   * if
   
     > 小括号内的结果若不是布尔类型时，会发生隐式转换转为布尔类型
   
   * switch
   
     > 找到跟小括号里数据全等的case值，并执行里面对应的代码。若没有全等===的则执行default里的代码
   
   * 三元运算符
3. 循环结构
   * do-while
   * while
   * for
     * for-in：常用语循环对象的属性
4. label语句
5. break和continue语句
6. with语句

### 数据类型

ECMAScript中有5中简单数据类(Number,String,Boolean,Null,Undefine)和1种复杂数据类型（Object，本质上是一组无序的名值对组成）。

#### typeof操作符

用于判断给定变量的数据类型，可以返回的值为string，number，boolean，undefined，object，function

#### 基本数据类型（5种）

* String

  > * 模板字符串
  >
  >   * ~~~js
  >     let name = 'chen'
  >     let age = 20
  >     document.write(`i am ${name},now is ${age} years old`)
  >     //必须使用反引号包裹字符串
  >     ~~~

* Boolean

* Number

  > NaN（Not a Number）：表示不是一个数字

* Null

* Undefined

注意：undefined==null（null和undefined的值相等，但类型不等）

#### 数据类型的转换

* 隐式转换

  > +号作为正号解析可以转换成数字型，任何数据和字符串相加结果都是字符串

* 显示转换

  * 转为数字：Number()

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>数据类型的转换</title>
    </head>
    <body>
        <script>
            /*
             * 其他类型数据转换为字符串
             * 1.toString()方法
             * 2.使用+运算符
             * 3.String()创建对象
             */
            var s1=123;
            console.log(s1.toString());
            console.log(""+s1);
            console.log(typeof(String(s1)));

            /*
             * 其他数据类型转换为数值型
             * 1.Number()
             * 2.parseInt()：只保留整数
             * 3.parseFloat()：可以保留小数
             */
            var s2='123';
            var s3=null;
            var s4=undefined;
            var s5=true;
            console.log(typeof(Number(s2)));
            console.log(Number(s3));//0
            console.log(Number(s4));//NaN
            console.log(Number(s5));//1

            /*
             * 布尔类型转换
             * 1.Boolean()
             */
            console.log(Boolean('0'));//true
            console.log(Boolean(0));//false
            console.log(Boolean(null));//false
            console.log(Boolean(undefined));//false
        </script>
    </body>
</html>
```



### 函数

#### 自定义函数

1. 函数声明（使用function关键字）

   ~~~javascript
   function fun(arg1,...argN){
   	//函数体
   }
   ~~~

2. 参数的理解 

   * 形参:声明函数时写在函数名右边小括号里的叫形参(形式上的参数)
   * 实参:调用函数时写在函数名右边小括号里的叫实参(实际上的参数)
   * ECMAScript函数不介意传递进入函数的参数个数和类型。（原因是ECMAScript中参数在内部使用一个数组来表示）
   * 在函数体中可以通过argments对象（不是Array实例）访问参数数组

3. 没有重载

   * 由于参数是由包含零个或多个值的数组来表示的，所以ECMAScript函数不能像传统意义上那样实现重载
   * 在ECMAScript中定义了两个相同名字的函数，则该名字只属于后定义的函数 

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

//注意：函数提升，但是使用表达式定义的函数不会被提升。
~~~

#### 全局函数

1. eval()函数：可以把传入的字符串，作为JavaScript的脚本代码进行执行，以此达到扩展程序功能的效果。

   注意：只能传递基本数据类型的字符串

2. encodeURI():把字符串编码为URL

   decodeURI():解码

   URI：统一资源标识符

   URL：统一资源定位器

#### 箭头函数

~~~ javascript
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

### 对象

> ECMAScript中，引用类型时一种数据结构，用于将数据和功能组织在一起。引用类型有时也被称为对象定义，因为他们描述的是一类对象所具有的属性和方法。
>
> 对象是某个特定引用类型的实例，新对象使用new操作符后跟一个构造函数来创建。构造函数本身是一个函数，只是该函数出于创建新对象的目的而定义。

#### 自定义对象

1. 对象创建方式

```javascript
//使用对象字面量
var 对象名={属性1:属性值1,属性2:属性值2}
//使用new关键字
var 对象名=new Object();
```

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

#### this关键字

#### Object

> Object类型所具有的任何属性和方法都存在于更具体的对象中。Object的每个实例都具有下列属性和方法：
>
> * Constructor：保存着用于创建当前对象的函数
> * hasOwnProperty(propertyName)：用于检查给定的属性在当前对象实例中是否存在（不是实例的原型中）
> * _sPrototypeOf(object)：用于检查传入对象是否是另一个对象的原型
> * propertyIsEnumberable(propertyName)：用于检查给定的属性是否能够使用for~in语句来枚举
> * toLocalString()：返回对象的字符串表示
> * valueOf()：返回对象字符串、数值或布尔值表示

* 实例化方式

  ~~~javascript
  //方式一，使用new操作符
  var person = new Object();
  
  //方式二，使用对象字面量表示法
  var person = {
      name:"tom"
      age:20
  }
  ~~~

#### 字符串

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

##### 常用转义字符

| 代码 | 结果       |
| :--- | :--------- |
| \b   | 退格键     |
| \f   | 换页       |
| \n   | 新行       |
| \r   | 回车       |
| \t   | 水平制表符 |
| \v   | 垂直制表符 |

### 数组对象

1. JS数组特性
   
   * 数组中每一个成员没有类型限制，
   * 数组的长度可以自动修改

2. JS数组的四种创建方式

```javascript
//方式一
let arr=[1,2,3];
//方式二
let arr=new Array();//数组长度默认为0
//方式三
let arr=new Array(4);//指定数组长度
//方式四
let arr=new Array(1,2);//数组元素是1,2
```

3. JS数组的常用属性/方法

   > * length 数组长度
   > * toString()将所有数组元素以逗号分隔装换为字符串
   > * join() 将所有数组元素以指定分隔符进行连接
   > * pop() 删除并返回数组的最后一个元素
   > * push() 向数组的末尾添加一个或更多元素，并返回新长度
   > * shift()删除首个数组元素，并把所有其他元素“位移”到更低的索引
   > * unshift()在开头向数组添加新元素，并“反向位移”旧元素
   > * delete
   > * splice()
   > * concat()通过合并（连接）现有数组来创建一个新数组：
   > * slice()用数组的某个片段切出新数组。
   > * 排序
   >   * sort()
   > * reverse() 颠倒数组中元素的顺序
   > * 查找最值
   > * 

### 正则对象

1. RegEXp对象
   
   直接量方式创建(开发中常用)
   
   ```javascript
   var reg=/^表达式$/;
   ```

2. 常用方法
   
   * test（）
   * exec（）

### 正则表达式（Regular Expression）

1. 正则表达式是由一个字符序列形成的搜索模式。

2. 两个常用字符串方法：
   
   * search（）
   
   * replace（）

3. 正则表达式修饰符
   
   | 修饰符 | 描述         |
   | --- | ---------- |
   | i   | 执行大小写不敏感匹配 |
   | g   | 执行全局匹配     |
   | m   | 执行多行匹配     |

4. 正则表达式模式
   
   * 方括号用于查找某个范围内的字符，例如[abc],[0-9],(x|y)查找任何以|分隔的选项
   
   * 元字符：拥有特殊含义的字符
     
     | [.](https://www.w3school.com.cn/jsref/jsref_regexp_dot.asp)              | 查找单个字符，除了换行和行结束符。             |
     | ------------------------------------------------------------------------ | ----------------------------- |
     | [\w](https://www.w3school.com.cn/jsref/jsref_regexp_wordchar.asp)        | 查找单词字符。                       |
     | [\W](https://www.w3school.com.cn/jsref/jsref_regexp_wordchar_non.asp)    | 查找非单词字符。                      |
     | [\d](https://www.w3school.com.cn/jsref/jsref_regexp_digit.asp)           | 查找数字。                         |
     | [\D](https://www.w3school.com.cn/jsref/jsref_regexp_digit_non.asp)       | 查找非数字字符。                      |
     | [\s](https://www.w3school.com.cn/jsref/jsref_regexp_whitespace.asp)      | 查找空白字符。                       |
     | [\S](https://www.w3school.com.cn/jsref/jsref_regexp_whitespace_non.asp)  | 查找非空白字符。                      |
     | [\b](https://www.w3school.com.cn/jsref/jsref_regexp_begin.asp)           | 匹配单词边界。                       |
     | [\B](https://www.w3school.com.cn/jsref/jsref_regexp_begin_not.asp)       | 匹配非单词边界。                      |
     | \0                                                                       | 查找 NUL 字符。                    |
     | [\n](https://www.w3school.com.cn/jsref/jsref_regexp_newline.asp)         | 查找换行符。                        |
     | \f                                                                       | 查找换页符。                        |
     | \r                                                                       | 查找回车符。                        |
     | \t                                                                       | 查找制表符。                        |
     | \v                                                                       | 查找垂直制表符。                      |
     | [\xxx](https://www.w3school.com.cn/jsref/jsref_regexp_octal.asp)         | 查找以八进制数 xxx 规定的字符。            |
     | [\xdd](https://www.w3school.com.cn/jsref/jsref_regexp_hex.asp)           | 查找以十六进制数 dd 规定的字符。            |
     | [\uxxxx](https://www.w3school.com.cn/jsref/jsref_regexp_unicode_hex.asp) | 查找以十六进制数 xxxx 规定的 Unicode 字符。 |

### 事件

HTML 事件是发生在 HTML 元素上的“事情”。

~~~ html
<!--使用单引号-->
<element event='一些 JavaScript'>
<!--使用双引号-->
<element event="一些 JavaScript">
~~~

常用html事件

| 事件        | 描述                         |
| :---------- | :--------------------------- |
| onchange    | HTML 元素已被改变            |
| onclick     | 用户点击了 HTML 元素         |
| onmouseover | 用户把鼠标移动到 HTML 元素上 |
| onmouseout  | 用户把鼠标移开 HTML 元素     |
| onkeydown   | 用户按下键盘按键             |
| onload      | 浏览器已经完成页面加载       |

### 表单验证

1. 约束验证DOM方法
   
   | 属性                  | 描述                                 |
   |:------------------- |:---------------------------------- |
   | checkValidity()     | 返回 true，如果 input 元素包含有效数据          |
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

## 面向对象程序设计

###  理解对象

#### 1. 属性类型

ECMAScript中有两种属性：数据属性和访问器属性。

1. 数据属性

   > 数据属性包含一个数据值的位置。数据属性有4个描述其行为的特性：
   >
   > * [[Configurable]]：表示能否通过delete删除属性从而重新定义属性
   > * [[Enumberable]]：表示能否通过for-in循环返回属性
   > * [[Writable]]：表示能否修改属性的值
   > * [[Value]]：包含这个属性的数据值。
   >
   > 对于直接在对象上定义的属性，他们的[[Configurable]]，[[Enumberable]]，[[Writable]]均默认为true，[[Value]]特性设置为指定值。
   >
   > 若要修改属性默认的特性，必须使用ECMAScript 5 的Object.defineProperity（）方法。这个方法接受三个参数：属性所在对象，属性名字和一个描述对象（必须是configurable，enumerate，writable或value）

2. 访问器属性

   > 访问器属性不包含数据值，它们包含一对getter和setter函数。访问器属性有如下4个特性：
   >
   > * [[Configurable]]：表示能否通过delete删除属性从而重新定义属性
   > * [[Enumerable]]：表示是否可以通过for-in循环返回属性
   > * [[Get]]：读取属性是调用的函数，默认值为undefined
   > * [[Set]]：写入属性是调用的函数，默认值为undefined
   >
   > 访问器属性不能直接定义，必须使用Object.defineProperity（）来定义

#### 2. 读取属性的特性

使用Object.getOwnPropertyDescription()方法

#### 3. 构造函数模式

~~~ javascript
function Person(name,age,job){
    this.name=name;
    this.age=age;
    this.job=job;
    this.sayName=function(){
        alert(this.name);
    };
}

var person1 = new Person("chen",20,"student");
var person2 = new Person("wang",20,"student");
/*
	按照惯例，构造函数始终以一个大写字母开头
	使用new操作符创建新对象，调用构造函数实际经历一下4个步骤：
	1.创建一个新对象
	2.将构造函数的作用域赋给新对象（因此this指向了新对象）
	3.执行构造函数中的代码（为新对象添加属性）
	4.返回新对象
	person1和person2分别保存Person的不同势力，这两个对象都有一个constructor属性，指向Person。
	任何函数只要通过new操作符调用，那它就可以作为构造函数，二任何函数，如果不通过new操作符调用，那它和普通函数没什么区别。
	构造函数的问题：每个方法都要在每个实例上重新创建一遍（应为在ECMAScript中函数是对象）
*/
~~~

#### 4. 原型模式

我们创建的每一个函数都有一个prototype属性，这个属性是一个指针，指向一个对象，而这个对象的用途是包含可以由特定类型的所有实例共享的属性和方法。

1. 原型对象
   * 无论什么时候，只要创建一个新函数，就会根据一组特定的规则为该函数创建一个prototype属性，这个属性指向函数的原型对象。在默认情况下，所有原型对象都会自动获得一个constructor属性，这个属性包含一个指向prototype属性所在函数的指针。
   * 创建了自定义构造函数后，其原型对象默认只会获得constructor属性，而其他方法，则从Object继承而来。
2.  看

### JavaScript类



## BOM对象

### 1. 概述

1. 简介

   Browser Object Model（浏览器对象模型）

2. 组成
   * **窗口对象（window）**
   * **历史记录对象（history）**
   * **地址栏对象（location）**
   * 显示器屏幕（screen）
   * 浏览器对象（navigator）

### 2. window对象

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

```
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
```

### 3. location对象

* 获取：Window.location

* 方法
  
  * reload（）：重新加载当前文档、刷新

* 属性
  
  * href：设置或返回完整的URL

* 案例：自动跳转

```
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
```

### 4. navigator对象

### 5. screen对象

### 6. history对象

### 本地存储

1. 本地存储特性

   * 数据存储在用户浏览器中
   * 设置、读取方便、甚至页面刷新不丢失数据
   * 容量较大，sessionStorage约5M、localStorage约20M
   * 只能存储字符串，可以将对象JSON.stringify()编码后存储

2. window.sessionStorage

   * 生命周期为关闭浏览器窗口
   * 在同一个窗口（页面）下数据可以共享
   * 以键值对形式存储使用

   ~~~html
   <!DOCTYPE html>
   <html>
   	<head>
   		<meta charset="utf-8">
   		<title></title>
   	</head>
   	<input type="text" name="" id="" value="" />
   	<button type="button" class="set">存储数据</button>
   	<button type="button" class="get">获取数据</button>
   	<button type="button" class="del">删除数据</button>
   	<button type="button" class="remove">清空所有数据</button>
   	<body>
   		
   		<script type="text/javascript">
   			var input=document.querySelector('input');
   			var set=document.querySelector('.set');
   			var get=document.querySelector('.get');
   			var del=document.querySelector('.del');
   			var remove=document.querySelector('.remove');
   			
   			set.addEventListener('click',function(){
   				/* 添加 */
   				sessionStorage.setItem('username',input.value);
   			});
   			get.addEventListener('click',function(){
   				console.log(sessionStorage.getItem('username'));
   			});
   			del.addEventListener('click',function(){
   				sessionStorage.removeItem("username");
   			})
   			remove.addEventListener('click',function(){
   				sessionStorage.clear();
   			});
   			
   		</script>
   	</body>
   </html>,
   ~~~

3. window.localStorage

   * 生命周期永久生效，除非手动删除，否则关闭页面也会存在
   * 可以多窗口（页面）共享（同一浏览器可以共享）
   * 以键值对形式存储使用

   ~~~html
   <!DOCTYPE html>
   <html>
   	<head>
   		<meta charset="utf-8">
   		<title>localStorage</title>
   	</head>
   	<input type="text" name="" id="" value="" />
   	<button type="button" class="set">存储数据</button>
   	<button type="button" class="get">获取数据</button>
   	<button type="button" class="del">删除数据</button>
   	<button type="button" class="remove">清空所有数据</button>
   	<body>
   		
   		<script type="text/javascript">
   			var input=document.querySelector('input');
   			var set=document.querySelector('.set');
   			var get=document.querySelector('.get');
   			var del=document.querySelector('.del');
   			var remove=document.querySelector('.remove');
   			
   			set.addEventListener('click',function(){
   				/* 添加 */
   				localStorage.setItem('username',input.value);
   			});
   			get.addEventListener('click',function(){
   				console.log(localStorage.getItem('username'));
   			});
   			del.addEventListener('click',function(){
   				localStorage.removeItem("username");
   			})
   			remove.addEventListener('click',function(){
   				localStorage.clear();
   			});
   			
   		</script>
   	</body>
   </html>,
   ~~~

## DOM对象

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

## JS事件

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
  
  ​            true 允许表单提交
  
  ​            false 阻止表单提交

* 键位弹起事件（onkeyup）

* 常用鼠标事件
  
  * 鼠标移入事件（onmouseover）
  * 鼠标移出事件（onmouseout）

+++

| 事件          | 描述                |
|:----------- |:----------------- |
| onchange    | HTML 元素已被改变       |
| onclick     | 用户点击了 HTML 元素     |
| onmouseover | 用户把鼠标移动到 HTML 元素上 |
| onmouseout  | 用户把鼠标移开 HTML 元素   |
| onkeydown   | 用户按下键盘按键          |
| onload      | 浏览器已经完成页面加载       |

4. 元素事件句柄绑定
5. DOM绑定方式

## ECMAScript（ES6-ES11）

ES全称EcmaScript，是脚本语言的规范，JavaScript是EcmaScript的一种实现。

核心知识点：

* let，const关键字
* 解构
* 链判断
* 参数默认值
* 箭头函数
* Promise
* async关键字
* 模块化

1. ES6新特性

   * JavaScript let
   * JavaScript const
   * 幂 (**)
   * 默认参数值
   * Array.find()
   * Array.findIndex()

2. 推荐使用`let`关键字替代 `var`关键字声明变量，因为`var`关键字存在诸多问题：

   * 越域问题
   * 重复声明

3. 解构

   * 数组解构
   * 对象解构

4. 链判断

   ~~~javascript
   body?.data?.user?.name || 'default'
   ~~~

5. 参数默认值

6. 箭头函数

7. `Promise`&`async`

8. 模块化

## 知识点总结

参看资料：https://blog.csdn.net/Augenstern_QXL/article/details/119249534

## 第三方库

数据可视化库D3：https://d3js.org/

数据可视化库echarts：

# BootStrap

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

| .container       | 类用于固定宽度并支持响应式布局的容器  |
| ---------------- | ------------------- |
| .container-fluid | 类用于100%宽度，占据全部视口的容器 |

# jQuery

## 基础

### 1. 简介

1. 简介：一个轻量级的JavaScript库，用于简化JS开发。
2. JavaScript框架本质：一些js文件，封装了js的原生代码而已。
3. jQuery库的特性：
   - HTML 元素选取
   - HTML 元素操作
   - CSS 操作
   - HTML 事件函数
   - JavaScript 特效和动画
   - HTML DOM 遍历和修改
   - AJAX
   - Utilities

4. JQuery安装

   > 版本说明：
   >
   > 目前jQuery有三个大版本，其中：
   > 1.x:兼容ie678,使用最为广泛的，官方只做BUG维护，
   > 功能不再新增。因此一般项目来说，使用1.x版本就可以了，
   > 最终版本: 1.12.4 (2016年5月20日)
   > 2.x:不兼容ie678，很少有人使用，官方只做BUG维护，
   > 功能不再新增。如果不考虑兼容低版本的浏览器可以使用2.x,
   > 最终版本: 2.2.4 (2016年5月20日)
   > 3.x:不兼容ie678，只支持最新的浏览器。除非特殊要求，
   > 一般不 会使用3. x版本的，很多老的jQuery插件不支持这个版本。
   > 目前该版本是官方主要更新维护的版本。最新版本: 3.2.1 (2017年3月20日 )
   >
   > 注意：jquery-xxx.js与jquery-xxx.min.js
   >
   > * jquery-xxx.js：开发版本，用于程序开发人员查阅，有良好的缩进和注释
   > * jquery-xxx.min.js：生产版本，程序中使用，没有缩进，体积较小，便于加载

   **下载JQuery**

   ~~~html
   <head>
       <script type="text/javascript" src="jquery.js"></script>
   </head>
   <！--注意：<script>标签应该位于<head>部分-->
   ~~~

   **使用 Google 的 CDN**

   ```html
   <head>
   <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs
   /jquery/1.4.0/jquery.min.js"></script>
   </head>
   ```

   **使用 Microsoft 的 CDN**

   ```html
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

   ```html
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

## 进阶

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

     ```html
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
     ```

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

参考资料：https://www.json.org/json-en.html

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
   > ```java
   > import com.alibaba.fastjson.JSON;
   > 
   > public class FastJsonDemo {
   > public static void main(String[] args) {
   >   User user = new User();
   >   user.setId(1);
   >   user.setName("chen");
   >   user.setAge(20);
   >   user.setAddr("cduestc");
   > 
   >   String s = JSON.toJSONString(user);
   >   System.out.println(s);
   > 
   >   User user1 = JSON.parseObject(s,User.class);
   >   System.out.println(user1);
   > 
   > }
   > }
   > ```

# npm

参考资料：

*  https://blog.csdn.net/qq_416814621/article/details/111042374
* https://www.runoob.com/nodejs/nodejs-npm.html
* https://www.jianshu.com/p/b1ca85169f4a
* https://www.cnblogs.com/zhuyutang/p/14863011.html
* https://www.cnblogs.com/nxmxl/p/14677596.html

1. 什么是npm

2. 常用命令

   > * 更新npm
   >
   >   ~~~  
   >   npm install npm@latest -g
   >   ~~~
   >

3. package.json文件

   * 使用npm init可以创建一个package.json文件（可以使用npm init --yes跳过问询）

   * 内容

     > package.json文件至少要有两部分(name和version)
     >
     > * “name”：全部小写，没有空格，可以使用下划线或者横线
     > * “version”： x.x.x 的格式，符合 “语义化版本规则”
     > * description：描述信息，有助于搜索
     > * main：入口文件，一般都是 index.js
     > * scripts：支持的脚本，默认是一个空的 test
     > * keywords：关键字，有助于在人们使用 npm search搜索时发现你的项目
     > * author :作者信息
     > * license ：默认是 MIT
     > * bugs：当前项目的一些错误信息，如果有的话
     >
     > ~~~ json
     > "name": "demo-package",
     > "version": "1.0.0",
     > ~~~

# Webpack

1. 工程化概念
   * 模块化
   * 组件化
   * 规范化
   * 自动化
   
2. webpack基本介绍

   * webpack 是前端项目工程化的具体解决方案。
   * 主要功能：它提供了友好的前端模块化开发支持，以及代码压缩混淆、处理浏览器端 JavaScript 的兼容性、性能优化等强大的功能。

3. 基本使用步骤

   * 项目搭建

     ![image-20220521130504580](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220521130504580.png)

   * 安装webpack相关包

     ~~~ 
     npm install webpack@5.42.1 webpack-cli@4.7.2 -D
     ~~~
* 配置webpack
  
  ![image-20220521123744928](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220521123744928.png)
  
   * 空间

# Vite

# Vue

1.vue官网：https://cn.vuejs.org/

2.vue-cli（vue脚手架,基于webpack,用于快速构建vue项目）：https://cli.vuejs.org/zh/guide/

3.vuex（vue官方提供的状态管理机制）：https://vuex.vuejs.org/zh/

　　vuex介绍（vue官网介绍）：https://vuex.vuejs.org/zh

4.vue-router（vue 路由，实现单页面应用）：https://router.vuejs.org/zh/

5.vue-loader：https://vue-loader.vuejs.org/zh/

## Vue基础

### 简介

1. 介绍

   Vue (读音 /vjuː/，类似于 view) 是一套用于构建用户界面的渐进式框架。Vue 被设计为可以自底向上逐层应用。

   Vue.js 使用了基于 HTML 的模板语法，允许开发者声明式地将 DOM 绑定至底层 Vue 实例的数据。所有 Vue.js 的模板都是合法的 HTML，所以能被遵循规范的浏览器和 HTML 解析器解析。

   在底层的实现上，Vue 将模板编译成虚拟 DOM 渲染函数。结合响应系统，Vue 能够智能地计算出最少需要重新渲染多少组件，并把 DOM 操作次数减到最少。

   Vue.js 的核心是一个允许采用简洁的模板语法来声明式地将数据渲染进 DOM 的系统，只关注视图层，易于上手。所有东西都是响应式的。

2. 主要特性

   * 数据驱动视图
   * 双向数据绑定
   
3. 优势

   * 轻量级渐进式框架
   * 视图、数据和结构的分离
   * 响应式双向数据绑定
   * 组件化
   * 虚拟DOM
   * 运行速度快，易于上手
   * 便于与第三方库或既有项目整合

### 基础

#### 模板语法

1. 插值语法：常用解析标签体内容
2. 指令：常用于解析标签（包括标签属性，标签体内容，绑定事件等）
   > 指令按照不同的用途，一般分为六类
   >
   > * 内容渲染
   >   * v-text，会覆盖原有内容
   >   * v-html更新innerHTML，可解析html标签
   > * 属性绑定
   >   * v-bind:动态绑定(简写为:)
   > * 事件绑定
   >   * v-on用于监听DOM事件（可简写为@）
   > * 双向绑定
   >   * v-model
   > * 条件渲染
   >   * v-once
   >   * v-if
   > * 列表渲染

#### 数据绑定

* 单向数据绑定（v-bind:）：数据只能从data流向页面
* 双向数据绑定（v-model:）：数据可以双向流动
  * v-model只能应用在表单类元素上
  * v-model:value可以简写为v-model，应为v-model默认收集value的值


	<!DOCTYPE html>
	<html>
		<head>
			<meta charset="utf-8">
			<title></title>
			<script src="vue.js" type="text/javascript" charset="utf-8"></script>
		</head>
	<body>
		<div id="app">
			单项数据绑定：<input type="text" v-bind:value="value1" /><br>
			双向数据绑定：<input type="text" v-model:value="value2" />
		</div>
		
		<script type="text/javascript">
			var vm = new Vue({
				el: '#app',
				data: {
					value1:12345,
					value2:'chen'
				}
			});
		</script>
	</body>
#### el与data的两种写法

data与el的2种写法：

1. el有2种写法
   * .new Vue时候配置el属性。
   * 先创建Vue实例，随后再通过vm . $mount( ' #root' )指定e1的值。

2. data有2种写法
  * 对象式
  * 函数式（如何选择:目前哪种写法都可以，以后学习到组件时，data必 须使用函数式，否则会报错。）

> 一个重要的原则:由Vue管理的函数，一定 不要写箭头函数，一但写了箭头函数，this就不再是Vue实例了。

~~~html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<script src="vue.js" type="text/javascript" charset="utf-8"></script>
	</head>

	<body>
		<div id="app">
			{{message}}
		</div>
		
		<script type="text/javascript">
		
			var vm = new Vue({
				// 写法一：
				// el: '#app',
				// data: {
				// 	message:'chen',
				// 	url: 'https://www.baidu.com/'
				// }
				
				//写法二：函数式
				data:function(){
					return{
						message:'chen'
					}
				}
                //data(){
                //return {
                //    message:'chen'
                //	}
                //}
                /*
                data 必须声明为返回一个初始数据对象的函数（注意函数内返回的数据对象不要直接引用函数外的对象）；否则页面关闭时，数据不会自动销毁，再次打开该页面时，会显示上次数据。
                */
            }
			});
			vm.$mount("#app");//挂载
			
		</script>
	</body>
</html>
~~~

#### MVVM模型

1. M：模型(Model) ：对应 data 中的数据
2.  V：视图(View) ：模板 
3. VM：视图模型(ViewModel) ： Vue 实例对象

![image-20220304094933119](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220304094933119.png)

#### 数据代理

#### 事件处理

1. 事件的基本使用:
   * 使用v-on:xxx或@xxx 绑定事件，其中xxx是 事件名;
   * 事件的回调需要配置在methods对象中，最终会在vm上;
   * methods中配置的函数，不要用箭头函数!否则this就不是vm了;
   * methods中配置的函数，都是被Vue所管理的函数，this的指向是vm 或组件实例对象;
   * @click="demo"和@click= ”demo($event)"效果一致， 但后者可以传参;
2. Vue中的事件修饰符
   * prevent:阻止默认事件(常用) ;
   * stop:阻止事件冒泡(常用)
   * once:事件只触发一次(常用) ;
   * capture:使用事件的捕获模式;
   * self:只有event。target是当前操作的元素是才触发事件;
   * passive:事件的默认行为立即执行，无需等待事件回调执行完毕;
3. 键盘事件
   * Vue中常用的按键别名:
     * 回车=>，enter
     * 删除，=>.delete，(捕获“删除”和“退格”键)
     * 退出:=>esc
     * 空格=> space
     * 换行=> : tab
     * 上.=>，up
     * 下=> dowr
     * 左=> left
     * 右=> right
   * Vue未提供别名的按键，可以使用按键原始的key值去绑定，但注意要转为kebab-case(短横线命名)
   * 系统修饰键(用法特殊) : ctrl、 alt、 shift、 meta
     * 配合keyup使用:按下修饰键的同时，再按下其他键，随后释放其他键，事件才被触发。
     * 配合keydown使用:正常触发事件。
   * 也可以使用keyCode去指定具体的按键(不推荐)
   * Vue . config. keyCodes.自定义键名=键码，可以去定制按键别名

#### 计算属性

1. 定义:要用的属性不存在，要通过已有属性计算得来。
2. 原理:底层借助了objcet . defineproperty方法提供的getter和setter.
3. get函数什么时候执行?
   * 初次读取时会执行一次。
   * 当依赖的数据发生改变时会被再次调用。
4. 优势:与methods实 现相比，内部有缓存机制(复用)，效率更高，调试方便。

> 注意：
>
> 1.计算属性最终会出现在vm上，直接读取使用即可。
> 2.如果计算属性要被修改，那必须写set函数去响应修改，且set中要引起计算时依赖的数据发4

~~~html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<script src="vue.js" type="text/javascript" charset="utf-8"></script>
	</head>

	<body>
		<div id="app">
			姓：<input type="text" id="" v-model="firstName" /><br>
			名：<input type="text" id="" v-model="lastName" /><br>
			<!-- 插值语法 -->
			全名：<span>{{firstName}}·{{lastName}}</span><br>
			<!-- 计算属性 -->
			全名：<span>{{fullName}}</span>
		</div>
		
		<script type="text/javascript">
		
			var vm = new Vue({
				el: '#app',
				data: {
					firstName:'tom',
					lastName:'smisth'
				},
				computed:{
					fullName:{
						// get的作用是读取fullName时调用，返回值作为fullName的值
						get(){
							return this.firstName+'-'+this.lastName;
						},
						//当fullName被修改时调用
						set(value){
							var str=value.split("-");
							this.firstName=str[0];
							this.lastName=str[1];
						}
					}
                    /* 简写，只有当只读取是才可以使用简写方式 */
					fullName(){
						return this.firstName+'-'+this.lastName;
					}
				}
				// methods:{
				// 	fullName(){
				// 		return this.firstName+'-'+this.lastName;
				// 	}
				// }
			});
		</script>
	</body>
</html>

~~~

#### 监视属性

监视属性watch

* 当被监视属性变化是，回调函数自动调用，进行相关操作
* 监视的属性必须存在，才能进行监视
* 监视的两种写法
  * 在创建Vue对象时传入watch配置
  * 通过调用vm对象的$watch属性进行配置
* 要监视多级结构的属性是，可开启深度监视

~~~html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<script src="vue.js" type="text/javascript" charset="utf-8"></script>
	</head>

	<body>
		<div id="app">
			<h2>今天天气{{info}}</h2>
			<button @click="changeWeather">切换天气</button>
			<h2>{{numbers.a}}</h2>
			<button @click="numbers.a++">点我使a加1</button>
			<h2>{{numbers.b}}</h2>
			<button @click="numbers.b++">点我使a加1</button>
		</div>
		
		<script type="text/javascript">
		
			var vm = new Vue({
				el: '#app',
				data: {
					isHot:true,
					numbers:{
						a:35,
						b:24
					}
				},
				methods:{
					changeWeather(){
						this.isHot=!this.isHot;
					}
				},
				computed:{
					info(){
						return this.isHot?'炎热':'凉爽';
					}
				},
				// 方式一
				watch:{
					isHot:{
						// immediate:true,//初始化时让handler调用一次
						handler(newValue,oldValue){
							console.log(newValue+','+oldValue)
							console.log("isHot被修改了");
						}
					},
					numbers:{
						deep:true,//开启深度监视，监视多级结构中数据的变化
						handler(){
							console.log("numbers 的值发生了改变")
						}
					}
				}
			});
			
			vm.$watch('isHot',{
				immidiate:true,
				handler(){
					console.log('isHot的值改变了')
				}
			})
		</script>
	</body>
</html>

~~~

知识点补充：vue数据监视原理

#### Class与Style绑定

1. 对象语法
2. 数组语法

~~~ html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<script src="vue.js" type="text/javascript" charset="utf-8"></script>
		
		<title></title>
		<style type="text/css">
			.base{
				height: 200rpx;
				width:500rpx;
			}
			
			.red{
				background-color: red;
			}
			
			.blue{
				background-color: blue;
			}
			
			.green{
				background-color: green;
			}
		</style>
	</head>
	<body>
		<div id="app" class="base" :class="color">
			{{name}}
		</div>
		
		<script type="text/javascript">
			var vm=new Vue({
				el:"#app",
				data:{
					name:'chen',
					color:'blue'
				}
			})
		</script>
	</body>
</html>

~~~

#### 条件渲染

1. v-if

2. v-else

3. v-show

   > `v-show` 是一个根据条件展示元素选项的指令 。用法大致和 `v-if` 一样。不同的是带有 v-show 的元素始终会被渲染并保留在 DOM 中。v-show 只是简单地切换元素的 `CSS` 属性的 `display` 。
   >
   > 注意：注意，v-show 不支持 template 元素，也不支持 v-else。nvue 页面不支持 v-show。


~~~ html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<script src="vue.js" type="text/javascript" charset="utf-8"></script>
		
		<title></title>
		<style type="text/css">
			.base{
				height: 200rpx;
				width:500rpx;
			}
			
			.red{
				background-color: red;
			}
			
			.blue{
				background-color: blue;
			}
			
			.green{
				background-color: green;
			}
		</style>
	</head>
	<body>
		<div id="app" class="base" :class="color">
			<div id="" v-if="seen">
				显示出来了
			</div>
			<div id="" v-else>
				直接不显示
			</div>
		</div>
		
		<script type="text/javascript">
			var vm=new Vue({
				el:"#app",
				data:{
					color:'green',
					seen:false
				}
			})
		</script>
</html>

~~~

#### 列表渲染

1. v-for指令以及key属性

   > react、Vue中可以key的作用（key的内部原理）
   >
   > 1. 虚拟DOM中key的作用：key是虚拟DOM对象的标识，当数据发生变化时，Vue会根据【新数据】生成【新的虚拟DOM】，随后Vue进行【新虚拟DOM】与【旧虚拟DOM】的差异比较，
   >
   >    比较规则如下：
   >
   >    * 旧虚拟DOM中找到了与新虚拟相同的key
   >      * 若虚拟DOM中内容没有改变，直接使用之前的真实DOM
   >      * 若虚拟DOM中内容改变了，则生成新的真实DOM，随后替换掉页面中之前的真实DOM
   >    * 旧虚拟DOM中未找到与新虚拟DOM相同的key：创建新的真实DOM，随后渲染到页面
   >
   > 2. 用index作为key可能会引发的问题：
   >
   >    * 若对数据进行逆序添加、逆序删除等破坏顺序操作会产生没有必要的真实DOM更新（界面效果没问题，但效率低）
   >    * 如果结构中还包含输入类的DOM，会产生错误DOM更新（界面出现问题）
   >
   > 3. 开发中如何选择key
   >
   >    * 最好使用与每条数据的唯一标识作为key
   >    * 如果不存在对数据的逆序添加、逆序删除等破坏顺序操作，仅用于渲染列表用于展示，使用index作为key是没有问题的

2. 列表过滤

   ~~~html
   <!DOCTYPE html>
   <html>
   	<head>
   		<meta charset="utf-8" />
   		<meta name="viewport" content="width=device-width, initial-scale=1">
   		<script src="vue.js" type="text/javascript" charset="utf-8"></script>
   		<title></title>
   	</head>
   	<body>
   		<div id="app">
   			<!-- <input type="text" placeholder="请输入姓名" v-model="keyword"/>
   			<ul v-for="(person,index) in filPersons" :key="person.id">
   				<li>{{person.name}}-{{person.age}}-{{person.sex}}</li>
   			</ul> -->
   			
   			<input type="text" placeholder="请输入姓名" v-model="keyword"/>
   			<ul v-for="(person,index) in filPersons" :key="person.id">
   				<li>{{person.name}}-{{person.age}}-{{person.sex}}</li>
   			</ul>
   		</div>
   		
   		<script type="text/javascript">
   			var vm=new Vue({
   				el:"#app",
   				data:{
   					keyword:'',
   					persons:[
   						{id:'001',name:'马冬梅',age:20,sex:'女'},
   						{id:'002',name:'周冬雨',age:20,sex:'女'},
   						{id:'003',name:'周杰伦',age:30,sex:'男'},
   						{id:'004',name:'温兆伦',age:20,sex:'男'}
   					],
   					// filPersons:[]
   				},
   				computed:{
   					filPersons(){
   						return this.filPersons=this.persons.filter((p)=>{
   							return p.name.indexOf(this.keyword) !== -1
   						})
   					}
   				}
   				//watch实现方式
   				// watch:{
   				// 	keyword:{
   				// 		immediate:true,
   				// 		handler(val){
   				// 			this.filPersons=this.persons.filter((p)=>{
   				// 				return p.name.indexOf(val) !== -1
   				// 			})
   				// 		}
   				// 	}
   				// }
   			})
   		</script>
   	</body>
   </html>
   
   ~~~

3. 列表排序

   ~~~html
   <!DOCTYPE html>
   <html>
   	<head>
   		<meta charset="utf-8" />
   		<meta name="viewport" content="width=device-width, initial-scale=1">
   		<script src="vue.js" type="text/javascript" charset="utf-8"></script>
   		<title></title>
   	</head>
   	<body>
   		<div id="app">
   			<input type="text" placeholder="请输入姓名" v-model="keyword"/>
   			<button type="button" @click="sortType=2">年龄升序</button>
   			<button type="button" @click="sortType=1">年龄降序</button>
   			<button type="button" @click="sortType=0">原顺序</button>
   			<ul v-for="(person,index) in filPersons" :key="person.id">
   				<li>{{person.name}}-{{person.age}}-{{person.sex}}</li>
   			</ul>
   		</div>
   		
   		<script type="text/javascript">
   			var vm=new Vue({
   				el:"#app",
   				data:{
   					keyword:'',
   					persons:[
   						{id:'001',name:'马冬梅',age:20,sex:'女'},
   						{id:'002',name:'周冬雨',age:20,sex:'女'},
   						{id:'003',name:'周杰伦',age:30,sex:'男'},
   						{id:'004',name:'温兆伦',age:20,sex:'男'}
   					],
   					sortType:2
   					// filPersons:[]
   				},
   				computed:{
   					filPersons(){
   						var arr=this.persons.filter((p)=>{
   							return p.name.indexOf(this.keyword) !== -1
   						});
   						if(this.sortType){
   							arr.sort((p1,p2)=>{
   								return this.sortType === 1?p2.age-p1.age:p1.age-p2.age;
   							})
   						}
   						return arr;
   					}
   				}
   			})
   		</script>
   	</body>
   </html>
   
   ~~~

#### 表单数据收集

> 1. 若input的type为text，则v-model默认收集的就是value的值
> 2. 若input的type为radio，则v-model手机端shivalue的值，且要给标签配置value值
> 3. 若input的type为checkbox
>    * 没有配置value属性，手机的是checked（布尔值）
>    * 配置了value属性，若v-model的初始值不是数组，收集的就是checked，否则手机的是value组成的数组
> 4. v-model的三个修饰符
>    * trim：过滤掉字符串首尾的空格
>    * lazy：失去焦点再收集数据
>    * number：输入字符串转为有效数字

~~~html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<script src="vue.js" type="text/javascript" charset="utf-8"></script>
		<title></title>
	</head>
	<body>
		<div id="app">
			<form action="" method="post">
				账号：<input type="text" v-model.trim="account"/><br>
				密码：<input tabindex="password" v-model="password"/><br>
				年龄：<input type="number" v-model.number="age"/>
				性别：
				<input type="radio" name="sex" v-model='sex' value="1"/>男
				<input type="radio" name="sex" v-model='sex' value="0"/>女<br>
				爱好：
				<input type="checkbox" name="hobby" id="" v-model='hobby' value="学习" />学习
				<input type="checkbox" name="hobby" id="" v-model='hobby' value="打游戏" />打游戏
				<input type="checkbox" name="hobby" id="" v-model='hobby' value="吃饭" />吃饭<br>
				其他信息：<br>
				<textarea rows="4" cols="50" v-model.lazy='other'></textarea>
				<input type="submit" value="提交"/>
			</form>
			
			
		</div>
		
		<script type="text/javascript">
			var vm=new Vue({
				el:"#app",
				data:{
					account:'',
					password:'',
					age:20,
					sex:'',
					hobby:[],
					other:''
				},
				methods:{
					
				}
			})
		</script>
	</body>
</html>

~~~

#### 生命周期

生命周期又叫生命周期回调函数、生命周期函数、生命周期钩子，主要由Vue在关键时刻调用的一些特殊名称的函数，生命周期函数的名字不可更改，生命周期函数中this指向的是Vue或组件实例对象。

![生命周期](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F.png)

### 组件

1. 组件：实现应用中局部功能代码和资源的集合，可复用的Vue实例

3. 单文件组件

4. 组件注册
   
   * 全局注册
   * 局部注册
   
5. VueComponent解析

5. Vue实例和组件实例区别：组件是可复用的Vue实例

   ![image-20230410120337874](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202304101203368.png)

6. ref属性

   * 作用：被用来给元素或子组件注册引用信息（类似id属性），引用信息将会注册在父组件的 `$refs` 对象上。如果在普通的 DOM 元素上使用，引用指向的就是 DOM 元素；如果用在子组件上，引用就指向组件实例：
   * 说明：因为 `ref` 本身是作为渲染结果被创建的，在初始渲染的时候你不能访问它们，它们还不存在！`$refs` 也不是响应式的，因此你不应该用它在模板中做数据绑定
   * 使用方式
     * 在标签上添加ref属性
     * 获取：this.$refs.xxx

7. props属性

   * 功能：让组件接受外部（父组件）传过来的数据

   * 接收方式

     * ~~~java
       props:['xxx']
       ~~~

     * ~~~javascript
         props:{
             xxx:String
         }
       ~~~

     * ~~~javascript
       props:{
           xxx:{
               type:String,
               required:true
           },
           xxx:{
               type:Number,
               default:100
           }
       }
       ~~~

     > 注意：props是只读的，Vue底层会检测对props的修改，若进行修改，则会发出警告


| 选项      | 类型                                                         | 说明                                                         |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| type      | `String` 、 `Number` 、 `Boolean` 、 `Array` 、 `Object` 、 `Date` 、 `Function` 、 `Symbol` ，任何自定义构造函数、或上述内容组成的数组 | 会检查一个 `prop` 是否是给定的类型，否则抛出警告             |
| default   | any                                                          | 为该 `prop` 指定一个默认值。如果该 `prop` 没有被传入，则换做用这个值。对象或数组的默认值必须从一个工厂函数返回。 |
| required  | Boolean                                                      | 定义该 `prop` 是否是必填项                                   |
| validator | Function                                                     | 自定义验证函数会将该 `prop` 的值作为唯一的参数代入。在非生产环境下，如果该函数返回一个 `false` 的值 (也就是验证失败)，一个控制台警告将会被抛出 |

8. mixins（混入）

   * 功能： 把多个组件共有的配置提取成一个混入对象
   * 使用方式： 
     * 第一步：定义混合
     * 使用：可以全局混入（Vue.mixin(xxx)）也可以局部混入（mixins:[]）

9. 插件

   * 功能：用于增强Vue
   * 本质：包含install方法的一个对象，install的第一个参数是Vue，第二开始为插件使用者传递的参数

10. scoped样式

    * 作用:让样式在局部生效，防止冲突。

    * 写法:

      ~~~
       <style scoped> 
      ~~~

11. 插槽：让父组件可以向子组件指定位置插入html结构， 也是一种组件间通信的方式，适用于父组件===>子组件。

    * 默认插槽
    * 具名插槽
    * 作用域插槽：数据在组件的自身，但根据数据生成的结构需要组件的使用者来决定。(games数据在Category组件中， 但使用数据所遍历出来的结构由Ap组件决定)

12. 组件化编码流程（通用）

    * 实现静态组件：抽取组件，使用组件实现静态页面效果
    * 展示动态数据
      * 数据的类型，名称
      * 数据保存在哪个组件
    * 交互： 从绑定事件监听开始

## Vue-cli

1. vue-cli：vue官方提供标准化开发工具，简化了程序员基于webpack创建工程化的Vue项目的过程。

2. 使用步骤

   * 全局安装

     > npm install -g @vue/cli

   * 切换到要创建项目的目录，执行创建命令

     > vue create xxx

   * 启动项目

     > npm run serve

   备注：

   * 若出现下载缓慢，可以配置npm淘宝镜像：

     > npm config set registry https//registry.npm.taobao.org

   * Vue脚手架隐藏了所有webpack相关的配置，若要查看具体配置，可以执行：

     > vue inspect > output.js

3. 文件结构分析

   ![image-20230410143059062](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202304101431686.png)

   ![image-20230407231806780](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202304072318799.png)

4. render函数

   > 关于不同版本的Vue
   >
   > 1. vue.js和vue.runtijme.xx.js的区别
   >    * vue.js是完整版的Vue，包含核心功能和模板解析器
   >    * vue.runtime.xx.js是运行版Vue，只包含核心功能
   > 2. 因为vue.runtime.xxx.js没有模板解析器，所以不能使用template配置项，需要使用render函数接收到的createElement函数去指定具体内容

5. 修改默认配置

   > 配置默认隐藏，可以使用vue inspect > output.js查看配置
   >
   > 使用vue. config. js可以对脚手架进行个性化定制，详情见: https://cli. vuejs .org/zh

## Vue-router

库地址：https://github.com/vuejs/vue-router

文档地址：https://router.vuejs.org/zh/installation.html

1. 路由：一组key-value对应关系。
2. 作用：实现SPA(single page web application) 应用

### 快速入门

1. 安装vue-router

   ~~~js
   npm install vue-router@4
   ~~~

2. 引入（main.js）

   ~~~js
   //main.js
   import router from './router/index.js'
   vue.use(VueRouter)
   new Vue({
     render: h => h(App),
     router:router
   }).$mount('#app')
   ~~~

3. 配置（router/index.js）

   ~~~js
   import VueRouter from "vue-router"
   import Home from '../components/Home.vue'
   import About from '../components/About.vue'
   
   const router = new VueRouter({
   	routes:[
   		{
   			path:'/home',
   			component: Home
   		},
   		{
   			path:'/about',
   			component: About
   		}
   	]
   })
   
   export default router
   ~~~

4. 使用

   ~~~vue
   <template>
   <div id="app">
   	<router-link to="/home">Home</router-link><br>
   	<router-link to="/about">About</router-link>
   	<router-view></router-view>
   </div>
   </template>
   ~~~

> 注意点：
>
> * 路由组件通常存放在pages（或view）文件夹，一般组件通常存放在components文件夹
> * 路由间切换时，“隐藏”了的路由组件，默认是被销毁掉的，需要的时候再去挂载。
> * 每个组件都有自己的$route属性，里面存储着自己的路由信息
> * 整个应用只有一个router，可以通过组件的$router 属性获取到

### 嵌套路由（多级路由）

1. 配置路由规则，使用children配置项

   ~~~js
   routes:[
   		{
   			path:'/home',
   			component: Home,
   			children:[
   				{
   					path:'news',
   					component: News,
   				},
   				{
   					path:'message',
   					component: Message,
   				}
   			]
   		},
   		{
   			path:'/about',
   			component: About
   		}
   	]
   ~~~

2. 使用完整路径进行路由跳转

   ~~~vue
   <router-link to="/home/message">Message</router-link>
   ~~~

### 命名路由

1. 作用：简化路由跳转

2. 使用

   步骤一：

   ~~~js
   {
   			path:'/home',
   			component: Home,
   			children:[
   				{
   					path:'news',
   					component: News,
   				},
   				{
   					path:'message',
   					component: Message,
   					children:[
   						{
                               //给路由命名
   							name:'detail',
   							path:'detail',
   							component:Detail
   						}
   					]
   				}
   			]
   		}
   ~~~

   步骤二：

   ~~~vue
   //简化前使用path				
   <router-link to="/home/message/detail">
       跳转
   </router-link>
   
   //简化后可以使用name			
   <router-link :to="{name='detail'}">
       跳转
   </router-link>
   ~~~

### 参数传递

#### query参数

1. 传递参数

   ~~~vue
   <!-- 跳转路由并传递query参数，to的字符串写法 -->
   <router-link :to="`/home/message/detail?id=${m.id}&title=${m.title}`">
       {{m.title}}</router-link>
   				
   <!-- 跳转路由并传递query参数，to的对象写法 -->
   <router-link :to="{
   		path:'/home/message/detail',
   		query:{
   			id:m.id,
   			title:m.title
   			}
   		}">
   		{{m.title}}
   		</router-link>
   ~~~

2. 接收参数

   ~~~vue
   <li>消息编号:{{$route.query.id}}</li>
   <li>消息标题:{{$route.query.title}}</li>
   ~~~

#### params

1. 配置路由，声明接收params参数

   ~~~js
   {
   	path:'message',
   	component: Message,
   	children:[
   		{
   			name:'detail',
   			path:'detail/:id/:title',
   			component:Detail
   		}
       ]
   }
   ~~~

2. 传递参数

   ~~~vue
   <!-- 路由跳转使用params参数 ，字符串写法-->
   <router-link :to="`/home/message/detail/${m.id}/${m.title}`">{{m.title}}</router-link>
   
   <!-- 跳转路由并传递param参数，to的对象写法 -->
   	<router-link :to="{
   		name:'detail',
   		query:{
   			id:m.id,
   			title:m.title
   		}
   	}">
   	{{m.title}}
   	</router-link>
   ~~~

   > 注意：路由携带params参数时，若使用to的对象写法，则不能使用path配置项，必须使用name配置!

#### 路由的props配置

1. 作用：让路由组件更方便的接收参数

2. 配置

   ![image-20230429115757587](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202304291158910.png)

### router-link的replace属性

1. 作用：控制路由跳转时操作浏览器历史记录的模式

2. 浏览器历史记录方式：共两种push和replace模式，push是追加历史记录，replace是替换当前记录。路由跳转时默认为push模式

3. 开启replace模式：

   ~~~vue
   <!-- 简写方式 -->
   <router-link replace></router-link>
   
   <!-- 完整方式 -->
   <router-link :replace='true'></router-link>
   ~~~

### 编程式路由导航

1. 作用：不借助router-link标签实现路由跳转，让路由跳转更灵活

2. 实现：

   ~~~js
   pushShow(m){
   				this.$router.push({
   					name:'detail',
   					params:{
   						id:m.id,
   						title:m.title
   					}
   				})
   			},
   replaceShow(m){
   				this.$router.replace({
   					name:'detail',
   					params:{
   						id:m.id,
   						title:m.title
   					}
   				})
   			}
   this.$router.forward();//前进
   this.$router.forward();//后退
   this.$router.forward();//可前进可后退
   ~~~

### 缓存路由组件

1. 作用：让不展示的路由组件保持挂载，不被销毁。

2. 具体实现

   ~~~vue
   <keep-alive include="组件名">
   	<router-view></router-view>
   </keep-alive>
   ~~~

### 生命周期钩子

1. 作用：路由组件特有的两个钩子，用于捕获路由组件的激活状态
2. 具体说明：
   * activated：路由组件被激活时触发
   * deactivate：路由组件失活时触发

### 路由守卫

1. 作用：对路由进行权限控制

2. 分类：全局守卫、独享守卫、组件内守卫

3. 全局守卫

   ![image-20230429175228447](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202304291752302.png)

4. 独享路由守卫

   ~~~js
   {
   					path:'news',
   					component: News,
   					beforeEnter: () => {
   						console.log("enter,news")
   					}
   				}
   ~~~

5. 组件内路由

   ![image-20230429180439959](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202304291804271.png)

6. 路由器的两种工作模式

   * 路由器有两种工作模式hash和history
   * hash模式的hash值（#后的内容）不会包含在http请求中，
   * hash模式地址中永远带着#号；若以后将地址通过第三方手机app分享，若app校验严格，则地址会被标记为不合法；兼容性较好
   * history地址干净，较美观；兼容性相比hash模式略差；应用部署上线时需要后端人员支持，解决刷新页面服务端404的问题

## Vuex

## Vue UI组件库

1. 移动端常见UI组件库
   * Vant：https://youzan.github.io/vant
   * Cube UI：https://didi.github.io/cube-ui
   * Mint UI：http://mint-ui.github.io
2. PC端常用UI组件库
   * Element UI：https://element.eleme.cn
   * IView UI：https://www.iviewui.com

## Vue3

# uni-app

官网地址：https://uniapp.dcloud.io/

## 简介

1. 背景
   * 多端泛滥
   * 体验不好
   * 生态不丰富
2. 产品特征
   * “一套代码、多端发行”
   * 条件编译：在一个项目中调用不同平台的特色功能

### 工程简介

一个 uni-app 工程，就是一个 Vue 项目，你可以通过 HBuilderX 或 cli 方式快速创建 uni-app 工程，详见：[快速上手](https://uniapp.dcloud.io/quickstart-hx.html)。

#### 目录结构

一个uni-app工程，默认包含如下目录及文件：

![image-20220304095916358](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220304095916358.png)

> ┌─uniCloud              云空间目录，阿里云为uniCloud-aliyun,腾讯云为uniCloud-tcb（详见uniCloud）
> │─components            符合vue组件规范的uni-app组件目录
> │  └─comp-a.vue         可复用的a组件
> ├─hybrid                App端存放本地html文件的目录，详见
> ├─platforms             存放各平台专用页面的目录，详见
> ├─pages                 业务页面文件存放的目录
> │  ├─index
> │  │  └─index.vue       index页面
> │  └─list
> │     └─list.vue        list页面
> ├─static                存放应用引用的本地静态资源（如图片、视频等）的目录，注意：静态资源只能存放于此
> ├─uni_modules           存放[uni_module](/uni_modules)规范的插件。
> ├─wxcomponents          存放小程序组件的目录，详见
> ├─main.js               Vue初始化入口文件
> ├─App.vue               应用配置，用来配置App全局样式以及监听 应用生命周期
> ├─manifest.json         配置应用名称、appid、logo、版本等打包信息，详见
> ├─pages.json            配置页面路由、导航条、选项卡等页面类信息，详见
> └─uni.scss              这里是uni-app内置的常用样式变量 

## 基础配置

### 全局和页面配置

### 页面配置

### tabbar配置

### condition启动模式

## 组件基本使用

## 生命周期

### 应用生命周期

| 函数名   | 说明                                        |
| -------- | ------------------------------------------- |
| onLaunch | 当uni-app初始化完成时触发（全局只触发一次） |
| onShow   | 当uni-app启动或从后台及进入前台显示         |
| onHide   | 当uni-app从前台进入后台                     |
| onError  | 当uni-app报错时触发                         |

### 页面生命周期

## 网络请求

官网API地址：https://uniapp.dcloud.io/api/request/request.html

~~~ vue
<template>
	<view>
		<button type="default" @click="getData">发送请求</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			getData(){
				uni.request({
					url:'http://localhost:8081/user/findAll',
					method:'GET',
					data:{
						page:5,
						limit:6
					},
					success(res) {
						console.log(res);
					}
				})
			}
		}
	}
</script>

<style>

</style>

~~~

## 数据缓存

官网API地址：https://uniapp.dcloud.io/api/storage/storage.html#setstorage

~~~ javascript
uni.setStorage({
							key:"uses",
							data:res.data.data
						})
~~~

## 导航跳转

1. navigator进行跳转
2. l用编程式导航进行跳转

# NodeJS

官网：https://nodejs.org/en/

## 简介

1. node：Node.js是一个基于Chrome V8引擎的JavaScript 运行环境。

   ![image-20230214092653066](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302140926106.png)

2. node的作用：

   ![image-20230214092723293](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302140927016.png)

3. node安装

4. 使用node执行JavaScript代码

   > * 打开命令行终端
   > * 使用node 待运行js代码路径

## 内置模块

### fs文件系统模块

1. fs模块：fs模块是Node.js官方提供的、用来操作文件的模块。它提供了一 系列的方法和属性,用来满足用户对文件的操作需求。

2. 常用API接口

   > * fs.readFile():用来读取指定文件中的内容
   >
   >   ![image-20230214094504034](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302140945328.png)
   >
   > * fs.writeFile0方法，用来向指定的文件中写入内容
   >
   >   ![image-20230214101437708](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302141014694.png)
   >
   > 注意：
   >
   > ![image-20230214111002041](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302141110906.png)

3. 

# Hbuilder

官网文档：https://hx.dcloud.net.cn/Tutorial/StartedTutorial

# 低代码or组件复用

## 开源项目&组件

### Element-UI

## Layui

官网：https://www.layui.site/index.htm

### 快速上手

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

### 页面元素

#### 布局

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

## wti-form

Vue.js 低代码表单组件，基于 Element UI 二次开发而成。

文档地址：http://lovelovewall.com/wti_form_demo/home.html#/Install

# 资源&路线

* [Fe-Docs (axzo.cn)](http://fe-doc.axzo.cn/)
* [MDN Web Docs (mozilla.org)](https://developer.mozilla.org/en-US/)