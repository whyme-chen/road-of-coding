# Python基础

## Python简介

1. 简介：跨平台程序设计语言、解释型语言、交互式语言、面向对象语言。吉多·范罗苏姆（Guido van Rossum）在 1989 年的圣诞节期间，为了打发时间而编写的一个编程语言。

2. Python能做什么

   * 数据分析
   * 自动化
   * 网络爬虫：通过程序去获取 Web 页面上自己想要的数据，也就是自动抓取数据
   * web开发
   * 游戏开发
   * 人工智能与机器学习

3. Python之禅

   >进入到 Python 的命令行界面，输入 import this 便可以看到

4. print()函数：在控制台中输出内容

5. input函数：将内容输入到程序。但值得注意的是无论键盘输入什么类型的数据，获取到的数据永远都是字符串类型

6. 转义字符

   ![img](https://cdn.aidaxue.com/courseactive/1529/18113/0/40fc87bd95eb50b7b487d8909a5e1b97.jpg)

7. 注释：在代码中用于解释说明代码的描述性文字，注释不会被解释器执行

   * 单行注释，使用#表示
   * 多行注释：使用一对三个引号表示

   ~~~py
   # 这是当行注释
   """ 这是多行注释 """
   ~~~

## 变量及字面量

1. 变量的概念：在程序运行时，能储存计算结果或能表示值的抽象概念。变量本身是没有类型的，但是变量存储的值是有类型的。

2. 变量的创建

   > 与其他编程语言不同的是，Python 没有声明变量的命令，首次为其赋值时，才会创建变量。赋值的语法：

3. 变量命名规则

   * 变量名只能包含数字、字母和下划线

   * 变量名必须以字母或下划线字符开头

   * 变量名称区分大小写

   * 若一个变量名包含多个单词，使用下划线隔开

   * 变量名应该有意义

   * 不能使用保留字作为变量名

     ![img](https://cdn.aidaxue.com/courseactive/1447/16979/0/cfbb57d2afc8c7624533495767693459.jpg)
   
4. 字面量：代码中的固定值，包括整数、浮点数、布尔值、字符串等

## 数据类型及运算符和表达式

Python 的数据类型：数字类型、布尔型和字符串类型。

1. 数字类型

   * int（整型）

   * float（浮点型）

   * 运算符

     * 算术运算符

       ![img](https://cdn.aidaxue.com/courseactive/1449/16989/16995/e609c950fe6d4caa6501fecba1a187e9.jpg)

     * 赋值运算符

       ![img](https://cdn.aidaxue.com/courseactive/1449/16989/16995/0730171341b71002d33ae1490f7b8926.jpg)

     * 比较运算符：比较运算符返回的值是 True 或者 False。

       ![img](https://cdn.aidaxue.com/courseactive/1449/16989/16995/528494624f1f17094a4647e98f339b1c.jpg)

     * 逻辑运算符

       ![img](https://cdn.aidaxue.com/courseactive/1449/16989/16995/de3975cc9f3902da89c4a17a9488999e.jpg)

2. 布尔型

   * True
   * False

3. 字符串型

   如果字符串横跨多行，可以使用三个单引号或三个双引号将字符串括起来。

   * 索引

     > 在 Python 中，字符串中的字符可以通过索引来提取。索引语法是：`变量[下标]`，这里的下标是由数字表示，代表所要索引的字符在变量中的位置。当从前往后索引时，下标从 0 开始。当从后往前索引时，下标从 -1 开始。

   * 切片：可以通过切片来提取变量的多个字符，

     * 切片语法是：变量[头下标:尾下标]（不包括尾下标对应的元素）。
     * 当不指定头下标和尾下标时，获取的是整个字符串：star[:]。
     * 当只指定头下标时，获取的是从头下标到字符串结尾的所有字符。
     * 当只指定尾下标时，获取的是字符串的开头到尾下标的字符串（不包括尾下标对应的元素）

     ~~~python
     name = " chenwenjian  "
     
     print(name.index("wen"))
     
     print(name.replace("wenjian","WenJian"))
     
     print(name.strip(" "))
     
     print("======================")
     exercise = "itheima itcast boxuegu"
     
     print(exercise.count("it"))
     
     back = exercise.replace(" ","|")
     print(back)
     
     print(back.split("|"))
     
     print(back[0::2])
     
     print("=======================")
     
     nums = [1,2,3,4,5,6,7,8,9,10]
     print(nums[::2])
     print(nums[1::2])
     print(nums[-1::-2])
     print(nums[-2::-2])
     ~~~

   * 字符长度：Python 中 len() 可以获取字符串的长度

   * 常用字符串方法

     ![img](https://cdn.aidaxue.com/courseactive/1449/17005/17013/2032d3e6ee68e15283828b434fb68673.jpg)

     > 可以使用变量.title()方法，使每个单词的首字母大写
     >
     > 可以使用变量.rstrip()方法，删除结尾的空白字符（但这只是暂时的，再次访问时空白字符仍然存在）

   * 转义字符

     > \t：制表符
     >
     > \n：换行符
     
   * 字符串中引用变量的值

     > 在字符串前面加小写字母 'f'，然后将需要引用的变量，用花括号包起来 {name}

     ~~~ python
     name = "chen"
     age = 20
     print(f"my name is {name},age is {age}")
     ~~~
     
   * 字符串拼接与格式化

     * 可以使用加号字符串

     * 使用占位符形式

       ~~~python
       print("你好呀,%s,欢迎来到%s,%3.2f" % ("陈文健", "成都", 5.6666))
       ~~~

       | 格式符号 | 转化                             |
       | -------- | -------------------------------- |
       | %s       | 将内容转化为字符串，放入占位位置 |
       | %d       | 将内容转化为整数，放入占位位置   |
       | %f       | 将内容转化为浮点型，放入占位位置 |

     * 可以通过语法：f"内容{变量}"的格式来快速格式化

       ~~~python
       name = "张三"
       city = "成都"
       print(f"{name}来到了{city}")
       ~~~

       > 注意该种方式不校验数据类型，不做进度控制，适用于都精度没有要求的时候快速使用

4. 获得变量的数据类型

   > 使用 type()，来获取变量的数据类型

5. 数据类型转换

   ![img](https://cdn.aidaxue.com/courseactive/1449/17017/0/e76c18c076a04c5b9e8423fd8825ae17.jpg)
   
6. 表达式：一条**具有明确执行结果**的代码语句

## 流程控制

1. if语法

   ~~~python
   if 条件:
       语句块1
   语句块2
   
   
   if 条件:
       语句块1
   else:
       语句块2
   语句块3
   
   if 条件1:
       语句块1
   elif 条件2:
       语句块2
   else:
       语句块3
   语句块4
   ~~~

2. while

   * `while` 循环：只要条件满足，就会一直执行一组语句。Python 中，`while` 表示的信息是当...时候，也就是说当 `while` 循环的条件满足时，会一直执行满足条件的语句。

   * while循环语法

     ![img](https://cdn.aidaxue.com/courseactive/1455/17095/17097/b7cac9e918602fa4c218baaba88af416.jpg)

3. for

   * for 循环用于迭代序列（即列表、元组、字典、集合或字符串等）

   * for循环语法

     ![img](https://cdn.aidaxue.com/courseactive/1455/17087/17089/74ed4459263946f5b14433cd0a74760d.jpg)

4. break和continue

## 列表

列表是**有序数据的集合**。定义的语法是使用方括号 [] 括起来以逗号分隔的数据。

1. 列表的特性

   * 列表示有序的
   * 同一个列表可以包含不同类型的数据
   * 列表中的元素可以重复出现
   * 可以通过索引的方式来访问列表的元素
   * 列表可以嵌套
   * 列表元素可以修改
   * 个数上限为2**63-1、9223372036854775807个

2. 使用及常用内置方法

   * 索引：列表[下标索引]，从前向后从日开始，每次+1，从后向前从-1开始，每次-1。注意列表索引从0开始，且当索引超出范围时会报错。可以使用`index()`方法来索引对应元素

   * 使用 + 往列表中增加元素，添加的元素会自动的被添加到列表尾部

     > 列表名 += [元素1,元素2,元素3,...,元素n]

   * 改变列表的方法

     * 除了使用`+`，`append()` 也可以为列表添加元素，和`+`一样，也是在列表的结尾处添加元素，可以添加一个元素或列表。可以使用`extend()`进行批量追加

     * `insert()` 可以在指定位置插入一个元素或列表。语法是：insert(n, 需要添加的元素/列表值)，n 为需要插入元素或列表的指定位置

     * 使用 `remove(元素值)` 从列表中删除指定的元素，如果指定的元素在列表中不存在，则会报错。还可以使用 `pop(index)` 来删除指定元素，index 为元素在列表中的位置。如果不指定 index，默认删除最后一个元素。还可以使用`del 列表名[ ]`实现删除效果。同时可以使用`clear()`来清除整个列表。

       > pop()和 remove() 主要有两点不同：
       >
       > * pop()传入的参数为索引值，而不是具体的元素值。
       > * pop() 的返回值为删除的元素。

     * `count()`可以统计元素出现个数


   ![image-20230812231702527](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202308122317288.png)

![img](https://cdn.aidaxue.com/courseactive/1453/17075/0/3acb62c4c07dec491d95290af09f7e7c.jpg)

## 字典

1. 特性

   * 可以容纳多个数据且可以是不同类型的数据
   * 每一份数据是Key-Value键值对
   * 可以通过Key获取到Value, Key不可重复
   *  不支持下标索引
   * 可以修改(增加或删除更新元素等)
   * 支持for循环，环支持while循环

2. 字典创建

   字典是一系列键值对的集合。值得注意的是在创建字典时，当键值重复时，以后加入的键值对为准。

3. 访问字典

   * 访问字典中某个键值对的值：字典名[键名]
   * 还可以使用 get() 方法进行访问，语法规则是字典名.get(键名)
   * 还可以通过遍历的方式（一般通过for循环来实现遍历）来访问字典中的键值对

   * 还可以使用 values() 函数返回字典的值，语法规则是字典名.values()
   * 还可以使用 items() 函数遍历键和值，语法规则是字典名.items()

   ~~~ python
   ne_zha = {'英雄名字': '哪吒', '最大生命': 7268, '生命成长': 270.4, '初始生命': 3483, '最大法力': 1808, '法力成长': 97, '初始法力': 450, '最高物攻': 320, '物攻成长': 11.5, '初始物攻': 159, '最大物防': 408, '物防成长': 22.07, '初始物防': 99}
   
   for key, value in ne_zha.items():
       print("key = ", key, ", value = ", value)
   ~~~

4. 修改字典

   * 使用索引添加新项目
   * 使用pop() 方法删除具有指定键名的项，语法规则为字典名.pop(键名)
   * popitem() 方法删除最后插入的项目（在 3.7 之前的版本中，删除随机项目），语法规则为字典名.popitem()
   * 我们也可以使用 `del` 关键字删除具有指定键名的项目，语法规则为 `del 字典名[键名]`，
   * del 关键字也可以完全删除字典，语法规则为：del 字典名
   * clear() 函数清空字典，语法规则为：字典名.clear()

5. 复制字典

   * 使用内建的字典方法 copy()复制字典，语法规则是 字典名.copy()
   * 制作副本的另一种方法是使用内建方法 dict()，语法规则是 dict(字典名)

6. 使用dict（）创建字典

   可以使用 `dict()` 构造函数创建新的字典，语法规则为：`字典名 = dict(键名=键值, 键名=键值,..., 键名=键值)`

~~~python
grade = {
    "zhagnsan":90,
    "lisi":80,
    "wangwu":79
}

print(type(grade))
print(grade)

print(grade["lisi"])
print(grade.get("wangwu"))

grade["xiaoming"]=88

print(grade)
~~~

## 元组

1. 创建元组

   > * 元组和列表很像，区别在于**元组创建完成后便不能被修改**。创建元组很简单，只需要将用逗号分隔的元素放到 `()` 中，`(元素1,元素2,元素3,...,元素n)`
   > * 如果需要创建一个仅包含一个元素的元组，必须在该元素后面添加一个逗号，否则，Python 无法将变量识别为元组

2. 访问元组

   > * 使用索引操作符 `[]` 访问元组的元素，我们可以从左到右正索引，也可以从右到左负索引

3. 合并元组

   > 元组不能被修改，但是两个元组是可以合并成一个新的元组的，在 Python 中，使用 `+` 运算符可以连接两个或多个元组

## 集合

集合是**无序元素的集合**，集合中的元素不可重复，并且创建完成后，其中的元素不可更改。但是整个集合是可以更改的，我们可以向其增加元素，也可以从中删除元素。

1. 创建集合

   * 将以逗号分隔的元素放在花括号 {} 中，{元素1,元素2,元素3,...,元素n}
   * 集合中的元素不可重复，如果有重复元素，重复的元素将被忽略。

2. 访问集合

   * 可以通过 `for` 循环来遍历集合的元素
   * 可以使用 `in` 关键字来判断集合中是否存在某个元素

3. 修改集合

   > * add() and update()都可用于向集合结尾添加元素。语法规则为：集合名.add(元素名)、集合名.update({元素1,元素2,...,元素n})
   > * discard() 和 remove() 用于从集合中删除元素。语法规则为：`集合名.discard()`、`集合名.remove()`。这两个函数的区别在于，从集合中删除一个不存在的元素时，`discard()` 不会执行任何操作，而 `remove()` 会抛出一个异常。

4. 操作集合

   * 并集
     * Python 中，实现集合并集可以使用 union() 和 | 操作符。
     * 集合1.union(集合2)
     * 集合1|集合2
   * 交集
     * 使用 intersection() 和 & 实现不同集合间的交集。
     * 集合1.intersection(集合2)
     * 集合1 & 集合2
   * 差集
     * 可以使用 difference() 来实现差集的运算，语法规则为集合1.difference(集合2)
     * 可以使用-来实现差集的运算，语法规则为 集合1-集合2
   * 对称差集：属于集合 A，不属于集合 B 的以及属于集合 B 不属于集合 A 的元素集合
     * 可以使用 `symmetric_difference()` 来实现对称差集的运算，语法规则是：`集合1.symmetric_difference(集合2)`
     * 可以使用 ^ 来实现对称差集的运算，语法规则是：集合1^集合2

~~~python
names = {"zhagnsan","lisi","wangwu","xiaoming","xiaohong"}
print(type(names))
print(len(names))
print(names)

print("============================")
names.add("zhaoliu")
print(len(names))
print(names)

names.remove("lisi")
print(len(names))
print(names)

names2 = {"lilei","hanmeimei","zhaoliu"}
name_union = names.union(names2)
print(name_union)

name_diff = names.difference(names2)
print(name_diff)

name_inter = names.intersection(names2)
print(name_inter)
~~~

## 数据容器分类对比

数据容器可以通过以下角度进行简单的分类：

* 是否支持索引
  * 支持：列表、字符串、元组
  * 不支持：字典、集合
* 是否可以修改
  * 支持：列表、字典、集合
  * 不支持：字符串、元组
* 是否可以有重复元素
  * 支持：列表、元组、字符串
  * 不支持：集合、字典

![image-20230813102129430](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202308131021717.png)

1. 常用容器通用操作
   * `len()`
   * `max()`
   * `min()`
   * `sorted()`
2. 容器间的相互转换
   * `list()`：将容器转换成列表
   * `tuple()`：将容器转换成元组
   * `set()`：将容器转换成集合
   * `str()`：将容器转换成字符串

## 函数

1. 函数的定义：组织好的，可重复使用的，用来实现特定功能的代码段。

   ![img](https://cdn.aidaxue.com/courseactive/1463/17207/17209/689d602e3b6cd41d68c3fa77563025a2.jpg)

   注意：

   > 1. 函数也是一个对象（对象即内存中用于存储数据的一块区域）

2. 传递参数

   * 位置参数：表示参数的位置对于函数的结果是有影响的，同样的参数值，在不同的位置，会有不一样的结果表达

   * 关键字参数：在传递值的时候，还可以带上参数的名字，具体形式为 `keyword = value`，这里的 `keyword` 必须匹配上一个函数定义中的参数名，也就是说是 `参数名1=值1`，`参数名2=值2`，`参数名3=值3` 这种形式。值得注意的是函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序。

     ~~~ python
     def cal(qty, item, price):
         print(f'{qty} {item} cost ${price:.2f}')
     
     
     cal(qty=6, item='bananas', price=5.74)
     ~~~

   * 默认参数（缺省参数）：在定义函数时，可以指定参数的默认值。指定默认值之后，在调用函数时如果没有指定某个参数的值，就用参数的默认值。需要注意的是在函数定义和调用时所有位置参数必须出现在默认参数前。

   * 不定长参数（可变参数）：用于不确定调用的时候会传递多少个参数(不传参也可以)的场景。不定长参数有位置传递和关键字传递两种类型。

     * 位置传递：根据传进参数的位置合并为一个元组(tuple)
     * 关键字传递：参数是“键=值”形式的形式的情况下，所有的“键=值”都会被接受，同时会根据“ 键=值”组成字典

3. 函数返回值return

   Python 函数中的 `return` 语句有两个作用：
   
   * 立即结束本函数的执行，将程序的执行控制权交还给调用者。
   * 返回数据给调用者。
   
   Python中有一个特殊的字面量: None,其类型是: <class 'NoneType'>。无返回值的函数，实际上就是返回了: None这个字面量，也就是说函数都是有返回值的，只不过没有显示返回值时返回的是None。
   
   同时python中的支持一次返回多个值，只需在接收返回值时对应使用对个变量进行接收即可。
   
4. 全局变量和局部变量：作用范围在函数内部，在函数外部无法使用
   的变量就是局部变量。可以使用global关键字来将函数内定义的变量定义为全局变量
   
5. 匿名函数

   * 函数本声也可以作为参数传入函数中，将函数传入的作用在于传入计算逻辑，而非传入数据。

   * 使用lambda关键字定义匿名函数（无名称）

     * 语法：

       ~~~python
       lambda 传入参数: 函数体（只能写一行代码）
       ~~~

     * 有名称函数可以基于名称重复使用，但无名称函数即匿名函数只可以临时使用一次。

## 类和对象

1. 类

   * 类的创建

     ![img](https://cdn.aidaxue.com/courseactive/1465/17239/17241/bdf3a0aa4cd2f9381d06aff3ed63c809.jpg)

     ~~~ python
     #创建类Bird
     class Bird:
         #对象初始化语句
         def __init__(self, n, c, s):
             self.name = n
             self.color = c
             self.size = s
         
         #定义方法get_description，参数为self，自动传入
         def get_description(self):
             description = f'{self.name} {self.color} {self.size} '
             print(description)
     ~~~

    * 构造方法：\__init__()

      类中的函数称作方法，`__init__()` 是一个特殊的方法，每当我们实例化一个对象时，这个方法都会自动执行。方法名的开头为两个下划线，结尾同样为两个下划线，这种命名的习惯主要是为了区分 Python 默认的方法名和我们自己定义的方法名。`def __init__(self, n, c, s):` 语句中，参数 self 表示对象自身，代表实例化对象的引用。参数n, c, s则表示对象的属性，在我们创建的类 `Bird` 中就是表示，每一种鸟的具象化特征，比如鹦鹉、绿色、中等大小，因此` 方法的作用是为对象的属性赋值。

      ![](https://cdn.aidaxue.com/courseactive/1465/17239/17243/7ee477ae903cc7cb1d3588c99cf5a417.jpg)

   * 内置方法（魔术方法）：

     除了上述的`__init__()`方法外，python中还有`__str__()`,`__lt__()`,`__le__()`,`__eq__()`等几个常用的内置方法

2. 对象

   类是用来描述具有相同的属性和方法的对象的集合，它定义了该集合中每个对象所共有的属性和方法。类是抽象的，对象是对类进行具象的实例化。

   * 实例化对象

     ~~~ python
     #创建类Bird
     class Bird:
     
         #对象初始化语句
         def __init__(self, n, c, s):
             self.name = n
             self.color = c
             self.size = s
     
          #定义方法get_description，参数为self，自动传入
         def get_description(self):
             description = f'{self.name} {self.color} {self.size} '
             print(description)
     
     #实例化对象my_bird，为my_bird赋予属性'鹦鹉', '绿色', '中等大小'
     my_bird = Bird('鹦鹉', '绿色', '中等大小')
     ~~~

3. 面向对象特性

   * 封装：可以在成员变量或者成员方法名前使用两个下划线表示对其的私有化。
   * 继承
     * 在创建类时，不必每次都从零开始，假设我们想要创建的新类和已经创建过的类之间有一些共同的属性和方法，我们就可以从某个现有的类继承，新类称为子类，被继承的类称为父类。继承时，子类会获取父类的所有属性和方法，并且子类还可以定义自己的属性和方法。
     * 子类的语法规则是：`class 新类名(父类名)`，比如 `class Penguin(Bird)` 就表示一个子类，父类为 `Bird`。
     * Python的类之间也支持多继承，即一个类，可以继承多个父类。语法为：`class 新类名(父类名1,父类名2,...)`。多个父类中，如果有同名的成员,那么默认以继承顺序(从左到右)为优先级。
     * 复写：如果想要覆盖父类中的成员变量或者成员方法，只需要在子类中重新定义同名的成员变量或者成员方法即可。在子类中可以使用`父类名.成员变量或方法`，`super().成员变量或方法`的方式去使用被复写的父类成员变量和成员方法。
   * 多态：即完成某个行为时，使用不同的对象会得到不同的状态。

4. 类型注解：在代码中涉及数据交互的地方，提供数据类型的注解( 显式的说明)。

   Python在3.5版本的时候引入了类型注解，以方便静态类型检查工具，IDE等第三方工具。类型注解的主要功能是帮助第三方IDE工具(如PyCharm)对代码进行类型推断，协助做代码提示。帮助开发者自身对变量进行类型注释。

   * 变量的类型注解
     
     * 语法：`变量:类型`或在注释中，#type：类型
     
   * 函数的类型注解
   
     ~~~python
     # 形参注解
     def func_name(形参1：类型，形参2：类型):
         pass
     
     # 返回值注解
     def func_name(形参1：类型，形参2：类型)-> 返回值类型:
         pass
     ~~~
   
   * Union类型
   
     * 使用`union[类型1，类型2]`定义联合类型注解
   
     ~~~python
     from typing import Union
     my_list:list[Union[Str,int]] = ["whymechen",50]
     ~~~
   
   > 类型注解只是提示性的，并非决定性的。数据类型和注解类型无法对应也不会导致错误。

## 模块和包

### 模块

在 Python 中，一个 .py 文件称为一个模块（Module）。

1. 模块化的优点：

   * 简化问题求解
   * 提高代码可维护性
   * 提高代码可重用性
   * 减少代码冲突

2. 导入模块

   * 语法

     ~~~python
     [from模块名] import [模块|类 |变量|函数| *] [as别名]
     ~~~

     模块创建完成后，可以使用 import 关键字来导入模块。当执行 import指令时，Python 会从以下路径中搜索对应模块。

     * 在当前目录下搜索该模块。
     * 在环境变量 PYTHONPATH 指定的路径列表中依次搜索。
     * 在 Python 安装路径的 lib 库中搜索。

     上述路径可以通过变量 `sys.path` 获得，该变量位于模块 `sys` 中。`sys.path`是 Python 的一个系统变量，是 Python 搜索模块的路径列表。

     Python 中模块内的对象和方法也可以有自己的别名，实现语句为： `from 模块名 import *** as 别名` ，该命令为导入的对象起一个别名。这样就可以通过别名来使用对象。示例如下：

     ~~~python
     import模块名
     from模块名import 类、变量、方法等.
     from模块名import *
     import模块名as别名
     from模块名import 功能名as别名
     ~~~

3. 创建模块：

   ~~~python
   # import time as t
   # print(t.time())
   # 
   # print("=====================")
   
   from my_module import add
   
   add(5, 6)
   
   ~~~

   注意：当导入多个模块的时候且模块内有同名功能。在调用这不同名功能的时候，调用到的是后导入的功能

   * \__main__变量：在 Python 中，每个模块都有一个隐藏的全局变量 `__name__`，用于指示当前模块的名称。当一个脚本直接被执行时，它的 `__name__` 值被设置为 `'__main__'`，而当它被其他模块导入时，`__name__` 的值则为模块的名称。
   * \__all__变量
   
4. python常用内置模块

   * `math`：提供数学运算函数，如三角函数、对数、幂等等。
   * `random`：生成伪随机数。
   * `datetime`：处理日期和时间相关的操作。
   * `os`：提供与操作系统交互的功能，如文件和目录操作。
   * `sys`：提供对Python解释器相关的变量和函数的访问。
   * `json`：处理JSON数据的编码和解码。
   * `re`：提供正则表达式操作。
   * `csv`：处理CSV文件格式。
   * `urllib`：发送HTTP请求并处理URL。
   * `sqlite3`：操作SQLite数据库。
   * `pickle`：实现序列化和反序列化对象以便于存储和传输。
   * `gzip`：读写GZIP压缩文件。

### 包

Python 中的包实现了对模块分组管理的功能。从物理上看，包就是一个文件夹，在该文件夹下包含了一个init_ . py文件，该文件夹可用于包含多个模块文件。从逻辑上看，包的本质依然是模块。

1. 创建包和导入包

   导入包中的模块，语法规则为：import 包.模块名。可以通过 from 语句来实现模块的导入
   
   > 注意：必须在\_init_ . py文件中添加\__all__变量，控制允许导入的模块列表
   
2. 导入第三方包

   * 常用第三方包：
     * numpy：科学计算常用包
     * pandas：数据分析常用包
     * pyspark、apache-flink：大数据计算常用包
     * matplotlib、pyecharts：图形可视化常用包
     * tensorflow：人工智能常用包
     
   * pip程序
     * 阿里云 PyPI 镜像：https://mirrors.aliyun.com/pypi/simple/
     * 清华大学 PyPI 镜像：https://pypi.tuna.tsinghua.edu.cn/simple/
     * 网易云 PyPI 镜像：https://mirrors.163.com/pypi/simple/
     * wheel文件：https://www.lfd.uci.edu/~gohlke/pythonlibs/
     
     修改全局下载地址，可以通过一下命令实现：
     
     ~~~python
     # 修改全局镜像地址
     pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
     
     # 恢复默认地址
     pip config unset global.index-url
     
     # 指定临时下载包地址
     pip install 包名 -i https://mirrors.aliyun.com/pypi/simple/
     ~~~

### 闭包

1. 概念：在函数嵌套的前提下，内部函数使用了外部函数的变量,并且外部函数返回了内部函数,我们把这个使用外部函数变量的内部函数称为闭包。

   需要使用nonlocal关键字修饰外部函数的变量才可在内部函数中修改它。

2. 优缺点：

   * 优点：无需定义全局变量即可实现通过函数,持续的访问、修改某个值闭包使用的变量的所用于在函数内,难以被错误的调用修改。
   * 缺点：由于内部函数持续引用外部函数的值，所以会导致这-部分内存空间不被释放，一直占用内存。

3. 应用：

   * 装饰器

## 异常处理

1. 什么是异常

   在 Python 中，异常是在程序运行过程中发生的错误，当异常发生时，需要对异常进行处理，否则整个程序将崩溃。

2. 异常的处理

   `try` 和 `except` 语句块可以用来捕获和处理异常，`try` 后面跟的是需要捕获异常的代码，`except` 后面跟的是捕获到异常后需要做的处理。每一个 `try` 语句块后面必须跟上一个 `except` 语句块，即使 `except` 语句块什么也不做。`try` 语句块后面可以跟上多个 `except` 语句块。

   ~~~ python
   try:
       a = 5 / 0
   except ZeroDivisionError:
       print("your program is running with exception")
   else:
       print(a)
   finally:
       print("all operation have finished")
   ~~~

   `try-except` 语句块后面可以跟上 `else` 语句块，当没有异常发生时，会执行 `else` 语句块中的代码。

   `try-except-else` 语句块后面还可以跟上 `finally` 语句块，不管有没有发生异常，`finally` 语句块中的代码都会被执行。

   可以使用`expect Exception`来捕获所有异常。

3. 抛出异常

   也可以主动抛出异常。主动抛出异常使用`raise `关键字。

   ~~~python
   x = 10
   if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
   ~~~

## 读写数据

### 原生读写

1. 优点：不占内存

2. 打开文件

   `f=open(file,mode='i',encoding=None)`
   
   * file：文件路径
   * mode：文件打开模式
     * 常用参数：
       * r：以只读的方式打开文件，默认值
       * w：以写的方式打开文件
       * x：创建一个新文件并进行写入操作，若文件已存在则报错
       * a：追加
   * encoding：编码
   
3. 读写文件

   * `f.read()`：读取整个文件，字符串显示
   * `f.readLine()`：每次读取一行，指针在该行末尾
   * `f.readLines()`：读取整个文件，以列表显示
   * `strip()`：用于移除字符串头尾指定的字符
   * `write()`：直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区。当调用flush的时候，内容会真正写入文件。这样做是避免频繁的操作硬盘，导致效率下降。

   ~~~ python
   f=open("C:\\Users\\hp\\Desktop\\test.java",'r',encoding='utf-8')
   # f.read()
   f.readlines()
   
   f = open("./file/io-demo.txt", "r", encoding="UTF-8")
   print(f.name)
   print(f.read())
   
   with open("./file/io-demo.txt", "r", encoding="UTF-8") as f:
       print(f.readlines())
   
   with open("./file/word.txt", "r", encoding="utf-8") as f:
       fruits = []
       for index in fruits:
           fruits.append()
       print(fruits)
       print(f"Lemon这个单词在文件中出现了{fruits.count('Lemon')}次")
   
   names = ["zhagnsan","lisi","wangwu","zhaoliu"]
   with open("./file/io-demo.txt",'a',encoding="UTF-8") as f:
       f.write(str(names))
       f.flush()
   ~~~

4. 关闭文件

   * `close()`：关闭文件

   * `with open`语法

     ~~~python
     with open("./file/io-demo.txt", "r", encoding="UTF-8") as f:
         print(f.readlines())
     # 在with open语句块中对文件进行操作，可以在操作完成后自动关闭文件，避免遗忘关闭文件造成资源持续占用
     ~~~

### pandas文件读写

### 读取mysql数据

1. 安装pymysql库（可以使用pip命令）

2. 获取连接对象、获取cursor对象，执行slq语句

   ~~~python
   from pymysql import Connection
   
   con = Connection(
       # autocommit=True,
       host="localhost",
       port=3306,
       user="root",
       password="4112"
   )
   
   # print information of this connection
   print(con.get_server_info())
   
   # select database
   con.select_db("demo")
   
   cursor = con.cursor()
   
   # execute not query sql
   # cursor.execute("create table demo_python(id BIGINT,name VARCHAR(50),age TINYINT COMMENT '0表示女生，1表示男生')")
   
   # insert data
   cursor.execute("insert into demo_python(name,age) values('lisi',30)")
   # 对于数据更改需要手动提交，或者在获取连接对象时设置autocommit
   con.commit()
   
   # query data
   cursor.execute("select * from demo_python")
   
   result: tuple = cursor.fetchall()
   for r in result:
       print(r)
   
   # close connection
   con.close()
   ~~~

### 操作json数据

~~~python
import json

data = [
    {
        "name": "zhangsan",
        "gender": "boy",
        "age": 47
    },
    {
        "name": "lisi",
        "gender": "boy",
        "age": 36
    },
    {
        "name": "xiaohong",
        "gender": "girl",
        "age": 23
    }
]

# 将python数据转换为json数据
json_data = json.dumps(data)
print(type(json_data))
print(json_data)


# 将json数据转化为python数据
python_data = json.loads(json_data)
print(type(python_data))
print(python_data)

~~~

### 序列化与发序列化

通过文件操作，我们可以将字符串写入到一个本地文件。但是，如果是一个对象(例如列表、字典、元组等)，就无法直接写入到一个文件里，需要对这个对象进行序列化，然后才能写入到文件里。
设计一套协议， 按照某种规则，把内存中的数据转换为字节序列，保存到文件，这就是序列化，反之，从文件的字节序列恢复到内存中，就是反序列化。总结一下就是**将对象转换为字节序列就是序列化，反之将字节序列转换为对象是发序列化**。
Python中提供了JSON这个模块用来实现数据的序列化和反序列化。

## 多线程

### 基本概念

1. 进程
2. 线程
3. 并发和并行

### threading模块

```python
import threading as th


def target1():
    for i in range(0, 5000):
        print(f"第{i}次执行target1")


def target2():
    for i in range(0, 50000):
        print(f"第{i}次执行target2")


if __name__ == '__main__':
    threading_target1 = th.Thread(
        group=None,  # 暂时无用，未来功能的预留参数
        target=target1(),  # 执行目标的任务名
        args=None,  # 以元组的形式给执行任务传参
        kwargs=None,  # 以字典形式给执行任务传参
        name="target1",  # 线程名，一般不用设置
    )

    threading_target2 = th.Thread(
        group=None,  # 暂时无用，未来功能的预留参数
        target=target2(),  # 执行目标的任务名
        args=None,  # 以元组的形式给执行任务传参
        kwargs=None,  # 以字典形式给执行任务传参
        name="target2",  # 线程名，一般不用设置
    )

    # 启动线程
    threading_target1.start()
    threading_target2.start()
```

## 网络编程

网络调试助手小工具：https://github.com/nicedayzhu/netAssist

~~~python
"""
socket服务端
"""
import socket

socket_server = socket.socket()

# 绑定ip和端口号
socket_server.bind(("localhost",8081))

# 监听端口，listen中的整型参数表示接受的链接数量
socket_server.listen(1)

# 等待客户端连接,conn为连接对象，address为客户端地址信息，该方法为阻塞方法
conn,address = socket_server.accept()
print(f"address:{address}\nconn:{conn}")

while True:
    # 接受客户端消息
    # recv:接受的参数是缓冲区大小，一 般给1024即可
    # recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode 方法通过UTF- 8编码将字节数组转换为字符串
    data = conn.recv(1024).decode("utf-8")
    print(f"data:{data}")

    # 响应请求消息
    message = input("请输入响应消息：").encode("utf-8")
    if message == 'exit':
        break
    conn.send(message)

# 关闭链接
conn.close()
# socket_server.close()
~~~

```python
"""
socket客户端
"""
import socket

socket_client = socket.socket()

# 连接到服务端
socket_client.connect(("localhost", 8081))

while True:
    # 发送消息
    msg = input("请输入要发送的消息：")
    if msg == 'exit':
        break
    socket_client.send(msg.encode("utf-8"))

    # 接收消息
    data = socket_client.recv(1024)
    print(f"接收到消息：{data.decode('utf-8')}")

socket_client.close()
```

## 正则表达式

正则表达式，又称规则表达式( Regular Expression),是使用单个字符串来描述、匹配某个句法规则的字符串，常被用来检索、替换那些符合某个模式(规则)的文本。
比如通过正则规则: (^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$)即可验证一个字符串是否是符合条件的电子邮箱地址。只需要配置好正则规则,即可匹配任意邮箱。但如果不使用正则,使用if else来对字符串做判断就非常困难了。

### 基本方法

Python正则表达式,使用re模块,并基于re模块中三个基础方法来做正则匹配。

* re.match(匹配规则，被匹配字符串)：从被匹配字符串开头进行匹配，匹配成功返回匹配对象(包含匹配的信息),匹配不成功返回空。
* re.search(匹配规则，被匹配字符串)：搜索整个字符串，找出匹配的。从前向后,找到第一个后， 就停止,不会继续向后中
* re.findall(匹配规则，被匹配字符串)：匹配整个字符串,找出全部匹配项

### 元字符匹配

单字符匹配规则：

| 字符 | 功能                     | 举例                                              |
| ---- | ------------------------ | ------------------------------------------------- |
| .    | 匹配任意单个字符         | a.c 可匹配 "abc"                                  |
| []   | 字符集                   | [aeiou] 可匹配任意一个元音字母                    |
| [^]  | 排除字符集               | [^aeiou] 可匹配非元音字母                         |
| \d   | 数字字符                 | \d 可匹配 "1"                                     |
| \D   | 非数字字符               | \D 可匹配字母                                     |
| \w   | 字母、数字、下划线字符   | \w 可匹配字母、数字或下划线字符                   |
| \W   | 非字母、数字、下划线字符 | \W 可匹配空格、标点符号等非字母、数字和下划线字符 |
| \s   | 空白字符                 | \s 可匹配空格、tab键                              |
| \S   | 非空白字符               | \S 可匹配除空格外的字符                           |

数量匹配规则：

| 字符  | 功能                     | 举例                             |
| ----- | ------------------------ | -------------------------------- |
| *     | 匹配前一个字符零次或多次 | a*b 可匹配 "b"、"ab"、"aab"等    |
| +     | 匹配前一个字符一次或多次 | a+b 可匹配 "ab"、"aab" 等        |
| ?     | 匹配前一个字符零次或一次 | colou?r 可匹配 "color"、"colour" |
| {n}   | 匹配前一个字符恰好 n 次  | a{3} 可匹配 "aaa"                |
| {n,}  | 匹配前一个字符至少 n 次  | a{2,} 可匹配 "aa"、"aaa" 等      |
| {n,m} | 匹配前一个字符 n 到 m 次 | a{1,3} 可匹配 "a"、"aa"、"aaa"   |

边界匹配规则：

| 字符 | 功能             | 举例                                           |
| ---- | ---------------- | ---------------------------------------------- |
| ^    | 匹配字符串的开始 | ^Hello 可匹配 "Hello, World!"                  |
| $    | 匹配字符串的结束 | World!$ 可匹配 "Hello, World!"                 |
| \b   | 匹配单词边界     | \bcat\b 只匹配 "cat"，不匹配 "catch" 或 "scat" |
| \B   | 匹配非单词边界   | \Bcat\B 只匹配 "catch" 或 "scat"，不匹配 "cat" |

分组匹配规则：

| 字符    | 功能                       | 举例                                           |
| ------- | -------------------------- | ---------------------------------------------- |
| (...)   | 创建捕获组                 | (ab)+ 可匹配 "ab"、"abab"、"ababab" 等         |
| \|      | 分支结构，选择多个模式之一 | cat\|dog 可匹配 "cat" 或 "dog"                 |
| \N      | 反向引用前面的捕获组       | (\d{2})-\1 可匹配 "11-11"、"22-22" 等          |
| (?:...) | 创建非捕获组               | (?:ab)+ 只匹配 "abab"、"ababab" 等，不进行捕获 |

## 常用IDE

参考：https://mp.weixin.qq.com/s/W2y-1bT2dssbDX1TF7ObsA

# 第三方库

## pyecharts包

Echarts是个由百度开源的数据可视化，凭借着良好的交互性,精巧的图表设计，得到了众多开发者的认可。而Python是门富有表达力的语言，很适合用于数据处理。当数据分析遇上数据可视化时pyecharts诞生了。

官网：https://pyecharts.org/#/

pycharts 中有很多配置项，常用的有两类；

* 全局配置项：全局配置项可以通过set_global_opts方法来进行配置，

  ![image-20230813184517144](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202308131845504.png)

* 系列配置项

折线图示例：

~~~python
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
import json

with open("../file/美国.txt","r",encoding="UTF-8") as f:
    us_data = f.read()

with open("../file/日本.txt","r",encoding="UTF-8") as f:
    jp_data = f.read()

with open("../file/印度.txt","r",encoding="UTF-8") as f:
    yd_data = f.read()

us_data = us_data.replace("jsonp_1629344292311_69436(","")
us_data = us_data[:-2]

jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
jp_data = jp_data[:-2]

yd_data = yd_data.replace("jsonp_1629350745930_63180(","")
yd_data = yd_data[:-2]

us_dict = json.loads(us_data)
jp_data = json.loads(jp_data)
yd_data = json.loads(yd_data)

us_trend_data = us_dict["data"][0]["trend"]
update_date = us_trend_data["updateDate"][:314]
us_list_data = us_trend_data["list"][:314]


# create object of line chart
line = Line()
# set X-axis data
line.add_xaxis(update_date)
# set Y-axis data
for item in us_list_data:
   line.add_yaxis(item["name"], item["data"])

"""
pycharts 中有很多配置项，常用的有两类；
* 全局配置项
* 系列配置项
全局配置项可以通过set_global_opts方法来进行配置，
"""
line.set_global_opts(
    title_opts=TitleOpts(title="GDP折线图", pos_left="left"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# render chart
line.render()
~~~

地图示例：

~~~python
from pyecharts.charts import Map
from pyecharts.options import TitleOpts

map = Map()
data = [
    ("北京市", 21540000),
    ("天津市", 15600000),
    ("河北省", 75560000),
    ("山西省", 37180000),
    ("内蒙古自治区", 25346000),
    ("辽宁省", 43686000),
    ("吉林省", 27125000),
    ("黑龙江省", 37793000),
    ("上海市", 24240000),
    ("江苏省", 80529000),
    ("浙江省", 63994000),
    ("安徽省", 63252000),
    ("福建省", 40947000),
    ("江西省", 46481000),
    ("山东省", 104490000),
    ("河南省", 98238000),
    ("湖北省", 59599000),
    ("湖南省", 68987000),
    ("广东省", 126760000),
    ("广西壮族自治区", 54952000),
    ("海南省", 10066000),
    ("重庆市", 31015000),
    ("四川省", 83020000),
    ("贵州省", 39879000),
    ("云南省", 49980000),
    ("西藏自治区", 3340000),
    ("陕西省", 39443000),
    ("甘肃省", 26370000),
    ("青海省", 5922000),
    ("宁夏回族自治区", 10266000),
    ("新疆维吾尔自治区", 24232000),
    ("台湾", 23780000),
    ("香港特别行政区", 7392000),
    ("澳门特别行政区", 648000)
]

map.add("人口", data, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国各省人口数量")
)

map.render()
~~~

## pyspark包

### 简介

spark官网：https://spark.apache.org/

pyspark文档：https://spark.apache.org/docs/3.4.1/api/python/index.html

Apache Spark是用于大规模数据(large-scala data)处理的统- - (unified) 分析引擎。简单来说，Spark是一 款分布式的计算框架， 用于调度成百上千的服务器集群，计算TB、 PB乃至EB级别的海量数据。

Spark对Python语言的支持,重点体现在由Spark官方开发的Python语言第三方库PySpark之上。可以作为python库进行数据处理，同时也可以提交至spark集群进行分布式集群计算。

### 环境搭建

1. 安装：

   ~~~shell
   pip install pyspark -i https://mirrors.aliyun.com/pypi/simple
   ~~~

2. 构建执行环境入口对象

   想要使用PySpark库完成数据处理,首先需要构建一个执行环境入口对象：类SparkContex的类对象。

   ~~~python
   """
   构建pyspark的执行环境入口对象，SparkContext类对象
   """
   from pyspark import SparkConf,SparkContext
   
   # 创建SparkConf对象
   spark_conf = SparkConf()
   spark_conf.setMaster("local[*]")
   spark_conf.setAppName("demo_spark")
   
   # 创建SparkContext对象
   spark_context = SparkContext(conf=spark_conf)
   # 打印pyspark版本信息
   print(spark_context.version)
   
   # 停止pyspark程序
   spark_context.stop()
   ~~~

## pandas包

## ta-lib

TA-Lib（Technical Analysis Library）是一个用于技术分析的开源库，提供了一系列常用的技术指标和图表模式的计算方法。广泛应用于金融市场的技术分析领域，为金融分析师和交易员提供了各种常用的技术指标计算方法和图表模式识别工具，用于辅助金融市场的技术分析和交易决策。

1. TA-Lib库主要用途：
   * 技术指标计算：TA-Lib提供了多种常见的技术指标计算方法，如移动平均线（Moving Average）、相对强弱指数（Relative Strength Index）、布林带（Bollinger Bands）等。这些指标可以帮助分析市场趋势、价格波动及超买超卖情况，从而辅助投资决策和交易策略的制定。
   * 图表模式识别：TA-Lib还包含了一些图表模式识别方法，如头肩顶形态（Head and Shoulders Pattern）、双顶/双底形态（Double Top/Bottom Pattern）等。这些模式识别方法可以帮助分析市场的趋势转折点和重要的价格形态。
   * 数据可视化：TA-Lib提供了一些函数和方法，可以方便地生成绘制技术指标和图表模式的图表，以便更直观地观察和分析数据。

## Matplotlib

资料：

* https://mp.weixin.qq.com/s/oGjkiFEIk0PqbaKYrN6C4g

1. 简介：

   Matplotlib 是一个用于创建可视化图表的 Python 库。专门用于开发2d(3d)图表，提供了一种简单而灵活的方式来绘制各种类型的图表，包括线图、散点图、柱状图、饼图等等。可以用 Matplotlib 来探索数据、展示趋势、进行数据分析等。具有丰富的功能和灵活的设置选项，可以根据需要自定义图表的样式、颜色、标签等。它也可以与 NumPy、Pandas 等其他 Python 库结合使用，方便地处理和可视化数据。

2. 快速开始

   ~~~python
   import matplotlib.pyplot as plt
   
   %matplotlib inline
   
   plt.figure()
   plt.plot([0,1,2,3,4],[60,23,56,29,24])
   plt.show()
   ~~~

3. matplot图像结构

   ![image-20230827173423694](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202308271734802.png)

   * 容器层

     容器层主要由Canvas、Figure、 Axes组成。
     Canvas是位于最底层的系统层，在绘图的过程中充当画板的角色，即放置画布(Figure)的工具。Figure是Canvas上方的第一层，也是需要用户来操作的应用层的第一层，在绘图的过程中充当画布的角色。Axes是应用层的第二层，在绘图的过程中相当于画布上的绘图区的角色。

     * Figure:指整个图形(可以通过plt.figure0设置画布的大小和分辨率等)
     * Axes(坐 标系):数据的绘图区域
     * Axis(坐标轴): 坐标系中的一条轴，包含大小限制、刻度和刻度标签

     一个figure(画布)可以包含多个axes(坐标系/绘图区)， 但是一个axes只能属于一个figure。一个axes(坐标系/绘图区)可以包含多个axis(坐标轴)，包含两个即为2d坐标系，3个即为3d坐标系。

   * 辅助显示层

     辅助显示层为Axes(绘图区)内的除了根据数据绘制出的图像以外的内容，主要包括Axes外观(facecolor)、边框线(spines)、坐标轴(axis)、 坐标轴名称(axis label)、 坐标轴刻度(tick)、坐标轴刻度标签(tick label)、网格线(grid)、图例(legend)、 标题(itle)等内容 。
     该层的设置可使图像显示更加直观更加容易被用户理解，但又不会对图像产生实质的影响。

   * 图像层

     图像层指Axes内通过plot、scatter、 bar、 histogram等函数根据数据绘制出的图像。
   

## requests

1. 简介：一个用于发送 HTTP 请求的流行库。它使得发送 GET、POST、DELETE 等类型的请求变得简单，并可以处理返回的响应内容。

## beautifulsoup4

1. 简介：一个用于解析 HTML 或 XML 文档的库，可以方便地从网页中提取数据。

~~~python
from bs4 import BeautifulSoup

# 创建 BeautifulSoup 对象
soup = BeautifulSoup(html_content, 'html.parser')

# 使用选择器提取数据
links = soup.select('a')  # 提取所有 <a> 元素

for link in links:
    print(link['href'])  # 获取链接的 href 属性值

~~~

## openpyxl库

1. 简介：一个用于操作 Excel 文件的库，可以读取、修改和创建 Excel 文件。

~~~python
import openpyxl

# 创建工作簿和工作表
wb = openpyxl.Workbook()
sheet = wb.active

# 设置单元格的值
sheet['A1'] = '序号'
sheet['B1'] = 'URL地址'

# 获取单元格的值
print(sheet['A1'].value)

# 保存工作簿
wb.save('example.xlsx')

~~~

# 办公自动化

## Excel

# Anaconda

参考资料：https://zhuanlan.zhihu.com/p/32925500

# Jupyter

官网：http://jupyter.org/

## Jupyter NoteBook

文档地址：https://jupyter-notebook.readthedocs.io/en/latest/

使用参考：https://blog.csdn.net/Bocker_Will/article/details/122828050

插件推荐：

* https://blog.csdn.net/weixin_43373042/article/details/122757680?spm=1001.2101.3001.6650.18&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-18-122757680-blog-109736618.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-18-122757680-blog-109736618.pc_relevant_paycolumn_v3&utm_relevant_index=23
* https://blog.csdn.net/qq_41554005/article/details/109736988

### 简介及安装

Jupyter Notebook 是一个交互式的开发环境，可用于创建和共享代码、文档、数据可视化，并支持超过40种编程语言。总的来说，jupyter notebook是一款程序员和科学工作者的编程/文档/笔记工具。

#### 安装

pip命令

acanconda安装

#### 启动及配置

### 基本概念

1. 单元格
2. 编辑模式和命令模式

### 快捷键

命令模式下快捷键：

| 快捷键       | 描述                         |
| ------------ | ---------------------------- |
| Enter        | 进入编辑模式                 |
| Esc          | 退出编辑模式，进入命令模式   |
| A            | 在当前单元格之前插入新单元格 |
| B            | 在当前单元格之后插入新单元格 |
| X            | 剪切选中的单元格             |
| C            | 复制选中的单元格             |
| V            | 粘贴剪切/复制的单元格        |
| D,D          | 删除选中的单元格             |
| Z            | 撤销删除的单元格             |
| Shift + Up   | 选择上方的单元格             |
| Shift + Down | 选择下方的单元格             |
| Shift + M    | 合并选中的多个单元格         |
| S            | 保存 Notebook                |
| H            | 显示快捷键帮助信息           |

编辑模式下快捷键：

| 快捷键           | 描述                                 |
| ---------------- | ------------------------------------ |
| Shift + Enter    | 运行当前单元格，并移到下一个单元格   |
| Ctrl + Enter     | 运行当前单元格                       |
| Alt + Enter      | 运行当前单元格，并在下方插入新单元格 |
| Ctrl + S         | 保存 Notebook                        |
| Tab              | 代码补全                             |
| Shift + Tab      | 显示函数参数和文档字符串的帮助信息   |
| Ctrl + ]         | 缩进当前行或选中的代码块             |
| Ctrl + [         | 取消缩进当前行或选中的代码块         |
| Ctrl + /         | 注释/取消注释当前行或选中的代码块    |
| Ctrl + D         | 删除光标所在行                       |
| Ctrl + Z         | 撤销最后的操作                       |
| Ctrl + Shift + - | 分割单元格                           |
| Shift + M        | 合并选中的多个单元格                 |

### 魔法函数

参考资料：https://blog.csdn.net/qq_41554005/article/details/109736618

1. `%load`：用来加载外部脚本或文件中的代码
2. `%run`：直接执行脚本
3. `%pwd`：获取当前所在位置的**绝对路径**

### 