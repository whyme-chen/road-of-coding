# IntelliJ IDEA

官方文档：[Getting started | IntelliJ IDEA Documentation (jetbrains.com.cn)](https://www.jetbrains.com/help/idea/getting-started.html)

参考：

* https://www.bilibili.com/video/BV1PW411X75p?from=search&seid=1533766256313085594&spm_id_from=333.337.0.0
* [主页 | IDEA 高效使用指南 (javaguide.cn)](https://idea.javaguide.cn/)

## 常用配置

1. 目录结构

   ![image-20211227103126984](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20211227103126984.png)

## Debug

参考：https://blog.csdn.net/huangjinjin520/article/details/100035427

1. 设置断点（Breakpoint Ctrl + F8）：在代码行上单击鼠标左键，在该行上设置或取消断点。断点是调试的关键，可以使程序在执行到断点时停下来，方便观察程序状态。
   * View Breakpoints (Ctrl + Shift + F8)：查看所有断点
   * Mute Breakpoints：选择这个后，所有断点变为灰色，断点失效。再次点击，断点变为红色，有效。如果只想使某一个断点失效，可以在断点上右键取消Enabled
   * 条件断点
     * 在断点上右键直接设置当前断点的条件
     * 在View Breakpoints (Ctrl + Shift + F8)窗口中设置
   * 异常断点
2. 启动调试：使用快捷键Shift + F9启动调试，或者通过点击工具栏上的调试按钮来启动调试会话。
3. 变量查看和表达式
   - 变量值查看
     * 编辑区参数所在行后面会显示当前变量的值
     * 光标悬停到参数上，显示当前变量信息
     * 在Variables里查看，这里显示当前方法里的所有变量
     * Watches窗口：用于监视和跟踪特定变量的值。在Watches里，点击New Watch，输入需要查看的变量
   - Evaluate窗口（Alt + F8）：用于动态评估和执行表达式。
     - 这个表达式不仅可以是一般变量或参数，也可以是方法，当你的一行代码中调用了几个方法时，就可以通过这种方式查看查看某个方法的返回值。
     - 设置变量，在计算表达式的框里，可以改变变量的值
4. 单步执行：
   - Step Over（F8）：逐行执行当前行，并且不进入方法内部。
   - Step Into（F7）：进入当前行所调用方法的内部。
   - Step Out（Shift + F8）：从当前方法返回到调用它的方法。
   - Smart Step Into (Shift + F7)：动定位到当前断点行，并列出需要进入的方法
   - reset frame：断点回退，其实就是回退到上一个方法调用的开始处，在[IDEA](http://mp.weixin.qq.com/s?__biz=MzI4Njc5NjM1NQ%3D%3D&chksm=ebd62d2adca1a43cb136b5740621e25854537054b9b3cac7451fd21ea55c0fc247e07a49d8cd&idx=1&mid=2247488006&scene=21&sn=d5c66d84724b1deebac6604749d04bf5#wechat_redirect)里测试无法一行一行地回退或回到到上一个断点处，而是回到上一个方法。需要注意，断点回退只能重新走一下流程，之前的某些参数/数据的状态已经改变了的是无法回退到之前的状态的，如对象、集合、更新了数据库数据等等。
5. 调试控制：
   - Resume（F9）：继续执行程序，直到遇到下一个断点或程序结束。
   - Pause（Ctrl + F2）：暂停当前正在执行的程序。
   - Stop（Ctrl + F2）：停止调试会话。
6. 监视表达式（Conditional Expression）：你可以设置条件表达式来监视变量，并在满足条件时暂停程序的执行。
7. 异常断点：除了普通断点，你还可以设置特定异常断点，在抛出或捕获该异常时暂停程序的执行。

## Version Control

官方文档：[Version control | IntelliJ IDEA Documentation (jetbrains.com)](https://www.jetbrains.com/help/idea/2023.1/version-control-integration.html)

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

| Win 快捷键                             | Mac 快捷键                                | 介绍                                                         |
| :------------------------------------- | :---------------------------------------- | :----------------------------------------------------------- |
| <kbd>Ctrl</kbd> + <kbd>F</kbd>         | <kbd>Command</kbd> + <kbd>F</kbd>         | 在当前文件进行文本查找                                       |
| <kbd>Ctrl</kbd> + <kbd>R</kbd>         | <kbd>Command</kbd> + <kbd>R</kbd>         | 在当前文件进行文本替换                                       |
| <kbd>Ctrl</kbd> + <kbd>Z</kbd>         | <kbd>Command</kbd> + <kbd>Z</kbd>         | 撤销                                                         |
| <kbd>Ctrl</kbd> + <kbd>Y</kbd>         | <kbd>Command</kbd> + <kbd>Delete</kbd>    | 删除光标所在行 或 删除选中的行                               |
| <kbd>Ctrl</kbd> + <kbd>D</kbd>         | <kbd>Command</kbd> + <kbd>D</kbd>         | 复制光标所在行 或 复制选择内容，并把复制内容插入光标位置下面 |
| <kbd>Ctrl</kbd> + <kbd>W</kbd>         | <kbd>Option</kbd> + <kbd>方向键上</kbd>   | 递进式选择代码块。可选中光标所在的单词或段落，连续按会在原有选中的基础上再扩展选中范围 |
| <kbd>Ctrl</kbd> + <kbd>E</kbd>         | <kbd>Command</kbd> + <kbd>E</kbd>         | 显示最近打开的文件记录列表                                   |
| <kbd>Ctrl</kbd> + <kbd>N</kbd>         | <kbd>Command</kbd> + <kbd>O</kbd>         | 根据输入的 **类名** 查找类文件                               |
| <kbd>Ctrl</kbd> + <kbd>J</kbd>         | <kbd>Command</kbd> + <kbd>J</kbd>         | 插入自定义动态代码模板                                       |
| <kbd>Ctrl</kbd> + <kbd>P</kbd>         | <kbd>Command</kbd> + <kbd>P</kbd>         | 方法参数提示显示                                             |
| <kbd>Ctrl</kbd> + <kbd>U</kbd>         | <kbd>Command</kbd> + <kbd>U</kbd>         | 前往当前光标所在的方法的父类的方法 / 接口定义                |
| <kbd>Ctrl</kbd> + <kbd>B</kbd>         | <kbd>Command</kbd> + <kbd>B</kbd>         | 进入光标所在的方法/变量的接口或是定义处，等效于 `Ctrl + 左键单击` |
| <kbd>Ctrl</kbd> + <kbd>/</kbd>         | <kbd>Command</kbd> + <kbd>/</kbd>         | 注释光标所在行代码，会根据当前不同文件类型使用不同的注释符号 |
| <kbd>Ctrl</kbd> + <kbd>F1</kbd>        | <kbd>Command</kbd> + <kbd>F1</kbd>        | 在光标所在的错误代码处显示错误信息                           |
| <kbd>Ctrl</kbd> + <kbd>F11</kbd>       | <kbd>Option</kbd> + <kbd>F3</kbd>         | 选中文件 / 文件夹，使用助记符设定 / 取消书签                 |
| <kbd>Ctrl</kbd> + <kbd>F12</kbd>       | <kbd>Command</kbd> + <kbd>F12</kbd>       | 弹出当前文件结构层，可以在弹出的层上直接输入，进行筛选       |
| <kbd>Ctrl</kbd> + <kbd>Space</kbd>     | <kbd>Control</kbd> + <kbd>Space</kbd>     | 基础代码补全，默认在 Windows 系统上被输入法占用，需要进行修改，建议修改为 `Ctrl + 逗号` |
| <kbd>Ctrl</kbd> + <kbd>Delete</kbd>    | <kbd>Option</kbd> + <kbd>Fn</kbd>+ Delete | 删除光标后面的单词或是中文句                                 |
| <kbd>Ctrl</kbd> + <kbd>BackSpace</kbd> | <kbd>Option</kbd> + <kbd>Delete</kbd>     | 删除光标前面的单词或是中文句                                 |
| <kbd>Ctrl</kbd> + <kbd>1,2,3...9</kbd> | <kbd>Control</kbd> + <kbd>1,2,3...9</kbd> | 定位到对应数值的书签位置                                     |
| <kbd>Ctrl</kbd> + <kbd>加号</kbd>      | <kbd>Command</kbd> + <kbd>加号</kbd>      | 展开代码                                                     |
| <kbd>Ctrl</kbd> + <kbd>减号</kbd>      | <kbd>Command</kbd> + <kbd>减号</kbd>      | 折叠代码                                                     |
| <kbd>Ctrl</kbd> + <kbd>左键单击</kbd>  | <kbd>Control</kbd> + <kbd>左键单击</kbd>  | 在打开的文件标题上，弹出该文件路径                           |
| <kbd>Ctrl</kbd> + <kbd>左方向键</kbd>  | <kbd>Option</kbd> + <kbd>左方向键</kbd>   | 光标跳转到当前单词 / 中文句的左侧开头位置                    |
| <kbd>Ctrl</kbd> + <kbd>右方向键</kbd>  | <kbd>Option</kbd> + <kbd>右方向键</kbd>   | 光标跳转到当前单词 / 中文句的右侧开头位置                    |
| <kbd>Ctrl</kbd> + <kbd>前方向键</kbd>  | 预设中没有该快捷键                        | 等效于鼠标滚轮向前效果                                       |
| <kbd>Ctrl</kbd> + <kbd>后方向键</kbd>  | 预设中没有该快捷键                        | 等效于鼠标滚轮向后效果                                       |

### Alt

| Win 快捷键                            | Mac 快捷键                                | 介绍                                                         |
| :------------------------------------ | :---------------------------------------- | :----------------------------------------------------------- |
| <kbd>Alt</kbd> + <kbd>\`</kbd>        | <kbd>Control</kbd> + <kbd>V</kbd>         | 显示版本控制常用操作菜单弹出层                               |
| <kbd>Alt</kbd> + <kbd>F1</kbd>        | <kbd>Option</kbd> + <kbd>F1</kbd>         | 显示当前文件选择目标弹出层，弹出层中有很多目标可以进行选择   |
| <kbd>Alt</kbd> + <kbd>F7</kbd>        | <kbd>Option</kbd> + <kbd>F7</kbd>         | 查询所选对象/变量被引用                                      |
| <kbd>Alt</kbd> + <kbd>Enter</kbd>     | <kbd>Option</kbd> + <kbd>Enter</kbd>      | IntelliJ IDEA 根据光标所在问题，提供快速修复选择，光标放在的位置不同提示的结果也不同 |
| <kbd>Alt</kbd> + <kbd>Insert</kbd>    | <kbd>Command</kbd> + <kbd>N</kbd>         | 代码自动生成，如生成对象的 set / get 方法，构造函数，toString() 等 |
| <kbd>Alt</kbd> + <kbd>左方向键</kbd>  | <kbd>Control</kbd> + <kbd>左方向键</kbd>  | 切换当前已打开的窗口中的子视图，比如Debug窗口中有Output、Debugger等子视图，用此快捷键就可以在子视图中切换 |
| <kbd>Alt</kbd> + <kbd>右方向键</kbd>  | <kbd>Control</kbd> + <kbd>右方向键</kbd>  | 切换当前已打开的窗口中的子视图，比如Debug窗口中有Output、Debugger等子视图，用此快捷键就可以在子视图中切换 |
| <kbd>Alt</kbd> + <kbd>前方向键</kbd>  | <kbd>Control</kbd> + <kbd>前方向键</kbd>  | 当前光标跳转到当前文件的前一个方法名位置                     |
| <kbd>Alt</kbd> + <kbd>后方向键</kbd>  | <kbd>Control</kbd> + <kbd>后方向键</kbd>  | 当前光标跳转到当前文件的后一个方法名位置                     |
| <kbd>Alt</kbd> + <kbd>1,2,3...9</kbd> | <kbd>Command</kbd> + <kbd>1,2,3...9</kbd> | 显示对应数值的选项卡，其中 1 是 Project 用得最多             |

### Shift

| Win 快捷键                             | Mac 快捷键                  | 介绍                                                 |
| :------------------------------------- | :-------------------------- | :--------------------------------------------------- |
| <kbd>Shift</kbd> + <kbd>F11</kbd>      | <kbd>Command + F3</kbd>     | 弹出书签显示层                                       |
| <kbd>Shift</kbd> + <kbd>Tab</kbd>      | <kbd>Shift + Tab</kbd>      | 取消缩进                                             |
| <kbd>Shift</kbd> + <kbd>Enter</kbd>    | <kbd>Shift + Enter</kbd>    | 开始新一行。光标所在行下空出一行，光标定位到新行位置 |
| <kbd>Shift</kbd> + <kbd>左键单击</kbd> | <kbd>Shift + 左键单击</kbd> | 在打开的文件名上按此快捷键，可以关闭当前打开文件     |

### Ctrl + Alt

| Win 快捷键                                             | Mac 快捷键                                                   | 介绍                                         |
| :----------------------------------------------------- | :----------------------------------------------------------- | :------------------------------------------- |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>L</kbd>        | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>L</kbd>        | 格式化代码，可以对当前文件和整个包目录使用   |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>O</kbd>        | <kbd>Control</kbd> + <kbd>Option</kbd> + <kbd>O</kbd>        | 优化导入的类，可以对当前文件和整个包目录使用 |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd>        | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>T</kbd>        | 对选中的代码弹出环绕选项弹出层               |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>S</kbd>        | <kbd>Command</kbd> + <kbd>逗号</kbd>                         | 打开 IntelliJ IDEA 系统设置                  |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Enter</kbd>    | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>Enter</kbd>    | 光标所在行上空出一行，光标定位到新行         |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>左方向键</kbd> | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>左方向键</kbd> | 退回到上一个操作的地方                       |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>右方向键</kbd> | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>右方向键</kbd> | 前进到上一个操作的地方                       |

### Ctrl + Shift

| Win 快捷键                                                | Mac 快捷键                                                   | 介绍                                                         |
| :-------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>         | 根据输入内容查找整个项目 或 指定目录内文件                   |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd>         | 根据输入内容替换对应内容，范围为整个项目 或 指定目录内文件   |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>         | <kbd>Control</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>         | 自动将下一行合并到当前行末尾                                 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Z</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>Z</kbd>         | 取消撤销                                                     |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>W</kbd>         | <kbd>Option</kbd> + <kbd>方向键下</kbd>                      | 递进式取消选择代码块。可选中光标所在的单词或段落，连续按会在原有选中的基础上再扩展取消选中范围 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd>         | 通过文件名定位 / 打开文件 / 目录，打开目录需要在输入的内容后面多加一个正斜杠 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>U</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>U</kbd>         | 对选中的代码进行大 / 小写轮流转换                            |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>         | 对当前类生成单元测试类，如果已经存在的单元测试类则可以进行选择 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd>         | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd>         | 复制当前文件磁盘路径到剪贴板                                 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd>         | <kbd>Control</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd>         | 跳转到类型声明处                                             |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>/</kbd>         | <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>/</kbd>        | 代码块注释                                                   |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>\[</kbd>        | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>\[</kbd>        | 选中从光标所在位置到它的顶部中括号位置                       |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>\]</kbd>        | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>\]</kbd>        | 选中从光标所在位置到它的底部中括号位置                       |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>加号</kbd>      | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>加号</kbd>      | 展开所有代码                                                 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>减号</kbd>      | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>减号</kbd>      | 折叠所有代码                                                 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F7</kbd>        | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>F7</kbd>        | 高亮显示所有该选中文本，按Esc高亮消失                        |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F12</kbd>       | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>F12</kbd>       | 编辑器最大化                                                 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd>     | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd>     | 自动结束代码，行末自动添加分号                               |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Backspace</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Backspace</kbd>    | 退回到上次修改的地方                                         |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>1,2,3...9</kbd> | <kbd>Control</kbd> + <kbd>Shift</kbd> + <kbd>1,2,3...9</kbd> | 快速添加指定数值的书签                                       |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>左键单击</kbd>  | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>左键单击</kbd>  | 把光标放在某个类变量上，按此快捷键可以直接定位到该类中       |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>左方向键</kbd>  | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>左方向键</kbd>   | 在代码文件上，光标跳转到当前单词 / 中文句的左侧开头位置，同时选中该单词 / 中文句 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>右方向键</kbd>  | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>右方向键</kbd>   | 在代码文件上，光标跳转到当前单词 / 中文句的右侧开头位置，同时选中该单词 / 中文句 |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>前方向键</kbd>  | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>前方向键</kbd>  | 光标放在方法名上，将方法移动到上一个方法前面，调整方法排序   |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>后方向键</kbd>  | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>后方向键</kbd>  | 光标放在方法名上，将方法移动到下一个方法前面，调整方法排序   |

### Alt + Shift

| Win 快捷键                                              | Mac 快捷键                                                 | 介绍                                                         |
| :------------------------------------------------------ | :--------------------------------------------------------- | :----------------------------------------------------------- |
| <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd>        | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd>        | 选择 / 添加 task                                             |
| <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>左键双击</kbd> | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>左键双击</kbd> | 选择被双击的单词 / 中文句，按住不放，可以同时选择其他单词 / 中文句 |
| <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>前方向键</kbd> | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>前方向键</kbd> | 移动光标所在行向上移动                                       |
| <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>后方向键</kbd> | <kbd>Option</kbd> + <kbd>Shift</kbd> + <kbd>后方向键</kbd> | 移动光标所在行向下移动                                       |

### Ctrl + Shift + Alt

| Win 快捷键                                                   | Mac 快捷键                                                   | 介绍             |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :--------------- |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>V</kbd> | <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>Option</kbd> + <kbd>V</kbd> | 无格式黏贴       |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>S</kbd> | <kbd>Command</kbd> + <kbd>;</kbd>                            | 打开当前项目设置 |

### 其他

| Win 快捷键     | Mac 快捷键     | 介绍                             |
| :------------- | :------------- | :------------------------------- |
| <kbd>F2</kbd>  | <kbd>F2</kbd>  | 跳转到下一个高亮错误 或 警告位置 |
| <kbd>F4</kbd>  | <kbd>F4</kbd>  | 编辑源                           |
| <kbd>F11</kbd> | <kbd>F3</kbd>  | 添加书签                         |
| <kbd>F12</kbd> | <kbd>F12</kbd> | 回到前一个工具窗口               |
| <kbd>Tab</kbd> | <kbd>Tab</kbd> | 缩进                             |
| <kbd>ESC</kbd> | <kbd>ESC</kbd> | 从工具窗口进入代码文件窗口       |

## 常用插件

### Simple Object Copy

优雅转换DTO，VO，BO，PO，DO

参考链接：https://juejin.cn/post/7053264631262871583

### Cool Request

使用参考：[IDEA中这么强大的接口调试插件，相见恨晚啊！ (qq.com)](https://mp.weixin.qq.com/s/v7KXV6jamHfXm8c-rlcm2Q)

## 插件开发

参考：

* [IntelliJ Platform SDK | IntelliJ Platform Plugin SDK (jetbrains.com)](https://plugins.jetbrains.com/docs/intellij/welcome.html)
* [IDEA 插件开发入门 | IDEA 高效使用指南 (javaguide.cn)](https://idea.javaguide.cn/tips/plug-in-development-intro.html)
* [首页 | idea插件开发文档 (ideaplugin.com)](https://www.ideaplugin.com/)
* [intellij-platform-plugin-template](https://github.com/JetBrains/intellij-platform-plugin-template)
* [Intelij开发idea插件从开发到发布的完整详细教程附带源码demo_idea插件开发-CSDN博客](https://blog.csdn.net/hj960511/article/details/135735940)

## 工具

### HTTP Client

参考：[HTTP Client | IntelliJ IDEA Documentation (jetbrains.com)](https://www.jetbrains.com/help/idea/2023.1/http-client-in-product-code-editor.html?Http_client_in__product__code_editor&utm_version=2023.1)

1. `.http`&`.rest`可执行文件

   * 基本语法：

   ~~~http
   // 1. 使用三个`#`来分隔多个请求
   // 2. GET/POST 请求地址（可拼接查询参数）
   GET https://dev-app.axzo.cn/pudge/webApi/oauth/cms/qrcode?_t=1718417126288
   // 3. 请求头键值对
   accept: application/json, text/plain, */*
   accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
   origin: https://dev-cms.axzo.cn
   ouid: 
   outype: 
   priority: u=1, i
   referer: https://dev-cms.axzo.cn/
   saastenantid: 
   sec-ch-ua: "Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
   sec-ch-ua-mobile: ?0
   sec-ch-ua-platform: "Windows"
   sec-fetch-dest: empty
   sec-fetch-mode: cors
   sec-fetch-site: same-site
   terminal: NT_CMS_WEB_ENT_ZB
   user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0
   workspaceid: 
   // 4. 请求体
   // 5. >{% %} 响应处理,使用 >符号 打头，和 shell 很像，然后用 {% %} 括起来的脚本内容,在脚本中可以使用 javascript 原生语法，，脚本中有几个内置对象 client 表示当前客户端，response 表示响应结果
   ~~~

# Visual Studio Code

# Pycharm

# Hbuilder