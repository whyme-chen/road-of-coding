# Linux

## Linux简介

1. 不同应用领域的主流操作系统
   * 桌面操作系统
   * 服务器操作系统
     * UNIX
     * Linux
     * Windows Server
   * 移动设备操作系统
     * Android
     * IOS
   * 嵌入式操作系统
     * Linux
   
2. 发展历史

   Unix 操作系统是由贝尔实验室于1969年开发的一个操作系统，最初由汇编语言实现，在1973年的时候用 C 语言重写，更加方便移植到不同的平台上去。

   开始 Unix 是以免费许可证授权给学术机构的，因此百花齐放，形成了很多 Unix 变种操作系统。但是后来贝尔实验室意识到商业价值不再授权给学术机构，这催生了Minix。

   由于贝尔实验室授权撤回，阿姆斯特丹自由大学的“Andy”教授为了教学，在完全不使用 Unix 的代码的情况下开发出了 Minix。

   Linux 则是由 Linus Torvalds 在1991年于赫尔辛基大学上学时，出于对操作系统的好奇，而开发的。起初他在他新购买的计算机上安装 Minix,但是后来他逐渐为自己的计算机写了很多驱动程序，也认识到 Minix 作为一个教学用的操作系统有许多不足，然后逐步形成了 Linux 操作系统。

3. Linux版本
   * 内核版
     * 由Linus Torvalds及其团队开发、维护
     * 免费、 开源
     * 负责控制硬件
   * 发行版
     * 基于Linux内核版进行扩展
     * 由各个Linux厂商开发、维护
     * 有收费版本和免费版本
     * 常见发行版
       * Ubuntu: 以桌面应用为主
       * RedHat: 应用最广泛、收费
       * CentOS: RedHat的社区版、免费
       * openSUSE: 对个人完全免费、图形界面华丽
       * Fedora: 功能完备、快速更新、免费
       * 红旗Linux: 北京中科红旗软件技术有限公司开发

4. Linux安装

   * 虚拟机方式：（https://blog.csdn.net/huaijiu123/article/details/82083452）

     ![image-20221118224115904](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182241660.png)

   * SSH连接工具

     ![image-20221118224300935](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182252792.png)

5. Linux目录结构简介

   ![image-20221118225310965](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182253030.png)

6. 服务

   * 概念：服务的英文为 service ，服务顾名思义是就是能为系统或者用户提供某种特殊的服务的程序，只不过**一般这种程序是常驻后台，不是直接运行的**，这种程序一般叫做守护进程daemon。

   * 常见的服务

     * SSH 用于能随时连接到服务器，提供这个服务的程序是 sshd
     * cron 提供定时任务的服务，提供这个服务的程序是 crond

   * 常见的服务管理方式

     * systemd是一种init程序，用于初始化系统，提供了对服务的管理方式。

     | 命令                    | 说明                 |
     | ----------------------- | -------------------- |
     | systemctl status crond  | 查看某个服务的状态   |
     | systemctl start crond   | 启动某个服务         |
     | systemctl stop crond    | 停止某个服务         |
     | systemctl enable crond  | 设置某个服务开机启动 |
     | systemctl disable crond | 移除某个服务开机启动 |
     | systemctl restart crond | 重启某个服务         |

7. 日志

   日志由程序在运行过程中打印出来的一些执行流程或者记录信息的文本。Systemd 同样也提供了对日志访问的方式。

   | 命令           | 说明             |
   | -------------- | ---------------- |
   | journalctl -x  | 查看日志         |
   | journalctl -xe | 跳到尾部查看日志 |

   通过直接查看文本的方式查询。

   | 日志路径          | 说明                                                         |
   | ----------------- | ------------------------------------------------------------ |
   | /var/log/message  | 全局系统日志，包括登录，对服务启停认证等                     |
   | /var/log/lastlog  | 不是一个文本文件，需要 lastlog 命令读，保存了最近的用户登录信息 |
   | /var/log/yum.log  | 最近通过yum 安装的程序的日志                                 |
   | /var/log/cron     | 定时任务日志                                                 |
   | /var/log/boot.log | 启动日志                                                     |
   | /var/log/kern     | 内核日志，也可以通过 dmesg 查看                              |

## <a id='instruct'>Linux常用命令</a>

1. 常用命令

   | 命令  | 作用                     |
   | ----- | ------------------------ |
   | ls    | list列出目录内容         |
   | cat   | 输出文件内容到标准输出   |
   | less  | 查看文件内容             |
   | more  | 查看文件内容             |
   | head  | 查看文件头部             |
   | tail  | 查看文件尾部             |
   | nano  | 编辑文件的工具           |
   | grep  | 查找文本中指定关键词的行 |
   | rm    | 删除命令                 |
   | touch | 创建一个文件             |
   | pwd   | 查看当前所在目录         |

   ![image-20221119125002051](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191352847.png)

2. 命令格式

   > command [-options] [parameter]

   ![image-20221119130139264](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191352141.png)

### 磁盘管理相关命令

1. df命令

   * 作用：该命令检查文件系统的磁盘空间占用情况。可以利用该命令来获取硬盘被占用了多少空间，目前还剩下多少空间等信息。

   * 命令语法:

     >df [参数] [目录或文件名]

   * 参数说明：

     | 参数 | 说明                                                 |
     | ---- | ---------------------------------------------------- |
     | -a   | 列出所有的文件系统，包括系统特有的/proc等文件系统。  |
     | -k   | 以KBytes为单位，返回各文件系统容量。                 |
     | -m   | 以MBytes为单位，返回各文件系统容量。                 |
     | -h   | 以GBytes、MBytes、KBytes为单位，返回各文件系统容量。 |
     | -H   | 以M=1000K取代M=1024K的进位方式显示各文件系统容量。   |
     | -T   | 显示文件系统类型。                                   |
     | -i   | 显示inode信息。                                      |

2. du命令

   * 作用：查看磁盘使用空间。du与df命令不同点在于，du命令用于查看文件和目录磁盘的使用空间。

   * 语法格式：

     > du [参数] [文件或目录名称]

   * 参数说明：

     | -a   | 列出所有的文件与目录容量。  |
     | ---- | --------------------------- |
     | -h   | 以G、M、K为单位，返回容量。 |
     | -s   | 列出总量。                  |
     | -S   | 列出不包括子目录下的总量。  |
     | -k   | 以KBytes为单位，返回容量。  |
     | -m   | 以MBytes为单位，返回容量。  |

3. fdisk命令

   * 作用：用于磁盘分区

   * 语法格式：

     > fdisk [-l] 装置名称

   * 参数说明：

     | 参数 | 说明                                                         |
     | ---- | ------------------------------------------------------------ |
     | -l   | 输出后面装置名称的所有的分区内容。若仅有 fdisk -l时， 则系统将会把整个系统内能够搜寻到的装置的分区均列出来。 |

   * 

### 文件目录操作命令

1. pwd

   * 作用：查看当前所在目录

2. ls命令

   ![image-20221119130854252](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191352461.png)

3. cd命令

   ![image-20221119131441984](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191352647.png)

4. cat命令

   ![image-20221119131517425](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191352523.png)

   > 创建并打开一个新的文件：`cat > 文件名称`

5. more命令

   ![image-20221119131749688](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353211.png)

6. head

   * 作用：查看文件开头的内容
   * 常用操作：`head -n 文件名称`显示某个文件的开始的n行数据，默认显示10行。

7. tail

   ![image-20221119132442044](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353220.png)

8. mkdir命令

   ![image-20221119132652551](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353925.png)

9. rmdir命令

   ![image-20221119132818838](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353381.png)

10. rm命令

    ![image-20221119132945812](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353834.png)

    注意：`rm -ri 目录或文件`用于在删除前询问是否删除。一般不建议使用 `rm -rf` 进行文件删除。rm 命令中不跟 r 参数，无法删除目录，只能删除文件

11. touch

    * 作用：创建文件

### 拷贝移动命令

1. cp命令

   ![image-20221119133232770](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353725.png)

2. mv命令

   ![image-20221119134054269](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353290.png)

### 打包压缩命令

1. tar命令 

   ![image-20221119134305526](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353171.png)
   
   ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRA2Eibiak8oCrCXafbcjDzWhbUINefxh8Duib8b9ib71TDhmFN9mrpoJRdrA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
   
   > cvf打包，xvf解包，zcvf打压缩包，zxvf解压包

### 文本编辑命令

1. vi/vim

   ![image-20221120202048921](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211202020494.png)

   vi 的三种模式如下：

   * 命令模式

   当用户使用 vi 命令打开文件后，则进入命令模式，用户可以输入命令来执行各种功能。

   ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAhuicP6icN2Z3pOgn9vOQ9FhiaSYG6SfJTEpvjjS7cFyTpHr6pQzshPOwg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

   * 输入模式

   如果用户要对文件做修改，则可以使用下面几种命令，进入输入模式，用户进入输入模式之后，可以任意修改文件，除了 Esc 键外，用户输入的任何字符都会被作为内容写入文件中，用户输入 Esc 可以对文件进行相关操作。

   ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRA3IcL5vreJibBhZMJJk3dR43SKaiaC8LnCmIhCnCNeNgMXDDSNU2DfYmA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

   * 末行模式

   如果用户完成编辑命令，则可以按照 esc + “:” 进入末行模式，用户可以对文件内容继续进行搜索，也可以输入 “:wq!” 进行文件保存并退出，或者输入 “:q!” 强制退出文件编辑。

   ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRA1pv5MGYicSUfMnZkaTdTqvHAsuMZlSE25RkwqBGD9wH2KaPjm4h46Lg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

### 查找命令

1. find命令

   ![image-20221120203432544](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211202034929.png)

2. grep命令

   ![image-20221120203545011](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211202035320.png)

### 进程操作命令

1. ps
   * 作用：查看 Linux 操作系统中正在运行的过程，并可以获得进程的 PID（进程的唯一标识），通过 PID 可以对进程进行相应的管理。
   * 常用操作：
     * `ps -ef | grep [进程关键字]`
2. kill：当系统中有进程进入死循环，或者需要被关闭时，我们可以使用 kill 命令对其关闭

### 软件安装命令

具体参考：[软件安装](#install)

软件安装方式（centOS为例）

![image-20221118231233904](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182312501.png)

#### 常用软件安装示例

1. jdk安装（解压方式）

   ![image-20221119115218075](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353986.png)

2. 安装tomcat（解压方式）

   ![image-20221119122116054](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353978.png)

   ![image-20221119122225352](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353642.png)

3. 安装MySQL（rpm方式）

   * 安装

     ![image-20221119123637520](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353081.png)

   * 卸载

     ![image-20221119123756530](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353764.png)

4. 安装lrzsz（yum方式）

   ![image-20221119124107682](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353324.png)

5. 安装docker

   * 参考：[【精选】Docker安装(Alibaba Cloud Linux 3)_alibaba cloud linux docker-CSDN博客](https://blog.csdn.net/weixin_40750633/article/details/122412224)

### 防火墙相关命令

![image-20221119122455628](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353373.png)

### <a id='userOperation'>用户操作命令</a>

1. `su`

   * 作用：切换用户
   * 常用操作：`su[用户名]`和 `su -[用户名]`都可以切换用户，前者类似于临时切换用户，当使用该命令进行切换新用户时，用户配置仍然沿用原来的用户配置，如环境变量、系统变量等。而后者进行切换用户时，环境变量、系统设置全部切换成新用户的用户配置。

2. `whoami`

   * 作用：查看当前登录用户

3. `groups`

   * 作用：查看当前登录yoghurt所属分组

4. `id`

   * 作用：查看当前用户UID和GID

5. `useradd`

   * 作用：添加新用户

   * 语法：

     ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAAljfmvoqz0GlTTgRV6qopysxnicFibVrnxFr2pN2gproxnYiadaRicuSjQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

6. `password`

   * 作用：修改用户密码

   * 语法：

     ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRATetM0PqJcdSFUnf5ibhgKt4jxGcnnibQkl3qBfqYL4EIHHWfqgItibIUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

7. `userdel`

   * 作用：删除用户

   * 语法：

     ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAm4Ik1Wic2XtARX9MpxZJtJX8nACCyEfGSNo2clgCT9qFRxMMkj21VoA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

8. `usermod`

   * 作用：修改用户信息

   * 语法：

     ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAenicHeVwwKqSPO88vHnAhfZT7x9V7GINN5L8RgE6pf23RaOZ4Z76uLg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

   * 常用操作：

     - 修改用户登录名：`usermod -l 新用户名 旧用户名`
     - 修改用户所属分组：`usermod -g 新组名称 用户名`

9. `groupadd`

   * 作用：添加用户组

   * 语法：

     ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAzRQWzicFTXjiayCTxsic2r3s9gjZr8BnibvwSODBicySnGCODwZJZ2pXV5w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

   * 常用命令：

     * 修改用户登陆名：`groupadd 组名`
     * 修改用户所属分组：`groupadd -g 组 GID 组名`

### 项目部署

1. 手动部署

   * 在后台运行java项目：`nohup java -jar jar-0.0.1-SNAPSHOT.jar &`

2. shell脚本部署

   ![image-20221120204540453](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211202045621.png)

### <a id="caculater">计算命令</a>

1. `expr`：expr是 evaluate expressions 的缩写，译为“求值表达式”。Shell expr 是一个功能强大，并且比较复杂的命令它除了可以实现整数计算，还可以结合一些选项对字符串进行处理，例如计算字符串长度、字符串比较、字符串匹配、字符串提取等。

   * 语法

     ~~~shell
     # 计算
     expr 算术运算符表达式
     # 将计算结果赋值给变量,注意: 运算符表达式中每个数字与符号之间要有空格
     res = `expr 算术运算符表达式`
     
     # 字符串长度：使用length参数获取字符串的长度。
     expr length "hello"  # 输出：5
     
     # 子字符串提取：使用substr参数提取字符串的子串。
     expr substr "hello world" 7 5  # 输出："world"
     
     # 字符串连接：使用冒号（:）将两个字符串连接起来。
     expr "hello" : "he" : "llo"  # 输出："hello"
     
     # 字符串匹配：使用match参数检查字符串是否与指定模式匹配。
     expr "hello world" : 'h.*d'  # 输出：1 (表示匹配成功)
     
     # 字符串替换：使用sub参数替换字符串中的模式。
     expr "hello world" : 'h' : 'H'  # 输出："Hello world"
     
     # 字符串索引位置：使用index参数确定字符串中某个子串的位置。
     expr index "hello" "e"  # 输出：2 (表示字母'e'在字符串中的位置)
     ~~~
   
   > 在较新的Shell版本中，推荐使用更强大的字符串处理工具，如`bash`内置的字符串操作功能或`awk`命令来代替`expr`命令。
   
2. `let`：let 命令和双小括号(())在数字计算方面功能一样，但是没有(0)功能强大，let只能用于赋值计算，不能直接输出，不可以条件判断

3. `bc`：Bash shel内置了对整数运算的支持，但是并不支持浮点运算，而 linux bc(basic calculator)命令可以很方便的进行浮点运算.bc命令是Linux简单的计算器,能进行进制转换与计算。能转换的进制包括十六进制、十进制、八进制、二进制等。可以使用的运算符号包括(+)加法、()减法、()乘法、(/除法、()指数、(%)余数等

   以下是`bc`命令的一些常见用法：

   1. 基本运算：`bc`可以执行基本的数学运算，包括加法、减法、乘法和除法。
      ```shell
      echo "2 + 3" | bc  # 输出：5
      echo "5 - 2" | bc  # 输出：3
      echo "2 * 3" | bc  # 输出：6
      echo "10 / 3" | bc  # 输出：3 (整数除法)
      echo "scale=2; 10 / 3" | bc  # 输出：3.33 (浮点数除法，设置小数位数为2)
      ```

   2. 变量赋值：`bc`允许使用变量进行计算，并可以在计算中使用这些变量。
      ```shell
      echo "a = 2; b = 3; a + b" | bc  # 输出：5
      ```

   3. 数学函数：`bc`提供了一些常见的数学函数，如平方根、指数函数、三角函数等。
      ```shell
      echo "sqrt(16)" | bc  # 输出：4 (平方根)
      echo "e(1)" | bc  # 输出：2.718281828459045 (自然对数的底数)
      echo "s(0)" | bc  # 输出：0 (正弦函数)
      ```

   4. 控制输出格式：`bc`可以通过设置输出格式来控制结果的显示方式。
      ```shell
      echo "scale=2; 10 / 3" | bc  # 输出：3.33 (设置小数位数为2)
      ```

   5. 文件操作：`bc`还可以从文件中读取计算表达式，并将结果输出到文件中。
      ```shell
      echo "2 + 3" > input.txt
      bc < input.txt > output.txt
      cat output.txt  # 输出：5
      ```



### 其他

1. clear：清屏命令

2. man：查询命令详细参数

3. `echo`：在终端上显示文本或变量的内容

   * 语法：

     ~~~shell
     echo [选项] [字符串]
     ~~~

   * 常见选项：
     * `-n`：不输出结尾的换行符。
     * `-e`：启用转义字符解析。

   * 示例用法：

     1. 显示文本：

        ```shell
        echo "Hello, World!"
        ```

        输出：`Hello, World!`

     2. 显示变量的值：

        ```shell
        name="Alice"
        echo "My name is $name"
        ```

        输出：`My name is Alice`

     3. 不输出换行符：

        ```shell
        echo -n "Hello, "
        echo "World!"
        ```

        输出：`Hello, World!`（不换行）

     4. 使用转义字符：

        ```shell
        echo -e "Hello\tWorld\nGoodbye"
        ```

        输出：

        ```
        Hello    World
        Goodbye
        ```

4. `read`：用于从终端读取用户输入的内置命令。它可以读取用户输入的文本，并将其存储到一个或多个变量中。

   * 语法：

     ~~~shell
     read [选项] [变量]
     ~~~

   - 常见选项：

     - `-p prompt`：显示提示信息并等待用户输入。
     - `-t timeout`：设置超时时间，如果在指定时间内未输入，则终止读取。
     - `-s`：静默模式，用户输入不会显示在终端上。
     - `-n count`：读取固定数量的字符后立即返回。

   - 示例用法：

     1. 读取用户输入的文本：

        ```
        read name
        echo "Hello, $name!"
        ```

        用户输入：`Alice`
        输出：`Hello, Alice!`

     2. 显示自定义提示信息并读取用户输入：

        ```
        read -p "请输入您的年龄：" age
        echo "您的年龄是 $age 岁"
        ```

        用户输入：`25`
        输出：`您的年龄是 25 岁`

     3. 设置超时时间：

        ```
        if read -t 5 -p "请输入用户名：" username; then
            echo "欢迎，$username!"
        else
            echo "超时，未输入用户名"
        fi
        ```

        如果在 5 秒内未输入用户名，将输出：`超时，未输入用户名`

     4. 静默模式读取密码：

        ```
        read -s -p "请输入密码：" password
        echo
        echo "您输入的密码是：$password"
        ```

        用户输入：`abc123`
        输出：`您输入的密码是：abc123`


## 常用发行版

### Debian系

1. Debian

| 特点       | 完全由自由软件组成的Linux发行版，以稳定著称                  |
| ---------- | ------------------------------------------------------------ |
| 包管理前端 | APT高级打包工具                                              |
| 包管理系统 | dgkp,对应deb包                                               |
| 最新版本   | 目前是Debian10.9                                             |
| Init程序   | debian 8以后使用systemd                                      |
| 默认桌面   | Gnome                                                        |
| 平台       | 多CPU架构支持                                                |
| 生命周期   | 每2年发布一个稳定版本，每个版本获得三年的正式支持，以及额外的两年安全更新，共计5年安全更新支持 |

2. Ubuntu

| 特点       | 基于Debian，接受私有软件，旨在提供一个更加友好的通用的桌面环境，是目前桌面用户最多的一个发行版 |
| ---------- | ------------------------------------------------------------ |
| 包管理前端 | APT高级打包工具; software updater; ubuntu软件中心            |
| 包管理系统 | dpkg，对应deb包; snappy                                      |
| 最新版本   | 目前是ubuntu 21.04                                           |
| Init程序   | Ubuntu 15.04以后使用systemd                                  |
| 默认桌面   | Gnome                                                        |
| 平台       | X86-64，Arm                                                  |
| 生命周期   | 每半年发布一个新版本（4月和10月)，长期支持版本LTS每2年发布一次，普通版本只提供9个月支持，LTS版本提供5年支持 |

### RHEL系

1. RHEL（Red Hat Enterprise Linux）

| 特点       | 是Red Hat公司推出的带有商业支持的Linux 发行版，目前是基于fedora，可以使用fedora epel的软件包 |
| ---------- | ------------------------------------------------------------ |
| 包管理前端 | yum or dnf                                                   |
| 包管理系统 | RPM                                                          |
| 最新版本   | 目前是RHEL 8.3                                               |
| Init程序   | RHEL 7以后使用systemd                                        |
| 默认桌面   | Gnome                                                        |
| 平台       | 多CPU架构支持                                                |
| 生命周期   | 大约每三年发布一个版本，每个版本提供十年支持                 |

2. Fedora

| 特点       | 由Fedora社区开发，但是由Redhat 公司赞助，是 RHEL的上游源码，经过Fedora测试验证充分的技术会被加入到RHEL |
| ---------- | ------------------------------------------------------------ |
| 包管理前端 | dnf                                                          |
| 包管理系统 | RPM                                                          |
| 最新版本   | 目前是Fedora 33                                              |
| Init程序   | Fedora 15以后使用systemd                                     |
| 默认桌面   | Gnome                                                        |
| 平台       | 多CPU架构支持                                                |
| 生命周期   | 大约每三年发布一个版本，每个版本提供十年支持                 |

3. Centos

| 特点       | 基于RHEL依照开放源代码规定发布的源代码所编译而成。由于出自同样的源代码，因此有些要求高度稳定性的服务器以CentOs替代商业版的Red Hat Enterprise Linux使用。两者的不同，在于CentOS并不包含封闭源代码软件。可以使用fedora epel |
| ---------- | ------------------------------------------------------------ |
| 包管理前端 | yum or dnf                                                   |
| 包管理系统 | RPM                                                          |
| 最新版本   | 目前是centos 8                                               |
| Init程序   | Centos 7以后使用systemd                                      |
| 默认桌面   | Gnome or KDE                                                 |
| 平台       | 多CPU架构支持社区长期支持                                    |
| 生命周期   | Centos 8已经被centos团队宣布停止维护更新了，以后centos8-stream将作为一个RHEL的上游，而不是下游，来反哺给RHEL了 |

4. Anolis OS

| 特点       | OpenAnolis社区发行的开源Linux发行版，与CentOS 8 100%兼容 |
| ---------- | -------------------------------------------------------- |
| 包管理前端 | yum                                                      |
| 包管理系统 | RPM                                                      |
| 最新版本   | RC2                                                      |
| Init程序   | systemd                                                  |
| 默认桌面   | Gnome or KDE                                             |
| 平台       | X86,arm                                                  |
| 生命周期   | --                                                       |
| 备注       | 作为Centos8停止维护以后，社区推出的发行版之一            |

### LFS以及其他发行版

1. Arch Linux

| 特点       | 滚动更新发行版，以 KISS为原则，优雅以及极简主义，希望用户去理解系统，wiki资料齐全，安装无GUI 界面，有AUR仓库作为软件包补充，国内用户非常活跃 |
| ---------- | ------------------------------------------------------------ |
| 包管理前端 | pacman                                                       |
| 包管理系统 | pacman                                                       |
| 最新版本   | 滚动更新                                                     |
| Init程序   | 2012年就采用了systemd                                        |
| 默认桌面   | 默认命令行，用户可选桌面安装                                 |
| 平台       | 多CPU架构支持                                                |
| 生命周期   | 滚动更新，一直升级就可以保持系统最新                         |

2. Gentoo Linux

| 特点       | 元发行版，从源码构建系统，根据自己系统的硬件定制软件包，优化软件包的特性等，wiki齐全 |
| ---------- | ------------------------------------------------------------ |
| 包管理前端 | emerge                                                       |
| 包管理系统 | portage                                                      |
| 最新版本   | 滚动更新                                                     |
| Init程序   | 可选openrc或 systemd                                         |
| 默认桌面   | 默认命令行，用户可选桌面安装                                 |
| 平台       | 多CPU架构支持                                                |
| 生命周期   | 源码构建，只要构建成功就可以升级，基本不会把系统弄挂，只有编译不通过 |

3. Linux Form Search

| 特点       | 本质上是一本教科书，描述了从源码构建Linux系统的方法          |
| ---------- | ------------------------------------------------------------ |
| 包管理前端 | 无，基于源代码                                               |
| 包管理系统 | 无，基于源代码                                               |
| 最新版本   | 10.1                                                         |
| Init程序   | 可选openrc或 systemd                                         |
| 默认桌面   | 无，看编译哪个init程序默认命令行，用户自由决定               |
| 平台       | x86-64，Arm，IA-32                                           |
| 生命周期   | 从源码构建，教你理解Linux系统运行到底需要什么，可以制作自己的发行版 |

### Alibaba Cloud Linux

官方文档：[Alibaba Cloud Linux_免费操作系统_云服务器_弹性计算-阿里云 (aliyun.com)](https://www.aliyun.com/product/ecs/alinux?spm=5176.28508143.J_XmGx2FZCDAeIy2ZCWL7sW.21.214b154aWWMFtB&scm=20140722.S_product@@云产品@@634016._.ID_product@@云产品@@634016-RL_Aliyun Linux-LOC_topbar~UND~product-OR_ser-V_3-P0_0)

Alibaba Cloud Linux 2(原Aliyun Linux 2)是阿里云官方操作系统，为云上应用程序提供安全、稳定、高性能的定制化运行环境，并针对云基础设施进行了深度优化，为您打造更好的运行时体验。您可以免费使用Alibaba Cloud Linux 2公共镜像，并免费获得阿里云针对该操作系统的长期支持。

| 特点       | 为阿里云基础设施进行深度优化，在阿里云上部署性能优异 |
| ---------- | ---------------------------------------------------- |
| 包管理前端 | yum                                                  |
| 包管理系统 | RPM                                                  |
| 最新版本   | 2                                                    |
| Init程序   | systemd，额外支持cloud-init为云实例做初始化          |
| 默认桌面   | 默认命令行                                           |
| 平台       | x86-64                                               |
| 生命周期   | 阿里云通过支持                                       |

## 进程管理

## 文件系统

1. 基本目录结构

   > - `/var`：包含在正常操作中被改变的文件、假脱机文件、记录文件、加锁文件、临时文件和页格式化文件等。
   > - `/home`：包含用户的文件：参数设置文件、个性化文件、文档、数据、EMALL、缓存数据等，每增加一个用户，系统就会根据其用户名在 home 目录下新建和其他用户同名的文件夹，用于保存其用户配置。
   > - `/proc`：包含虚幻的文件，他们实际上并不存在于磁盘上，也不占用任何空间（用 ls-l 可以显示它们的大小）当查看这些文件时，实际上是在访问存在内存中的信息，这些信息用于访问系统。
   > - `/bin`：包含系统启动时需要的执行文件（二进制），这些文件可以被普通用户使用。
   > - `/etc`：为操作系统的配置文件目录（防火墙、启动项）
   > - `/root`：为系统管理员（也叫超级用户或根用户）的 Home 目录。
   > - `/dev`：为设备目录，Linux 下设备被当成文件，这样一来硬件被抽象化、便于读写、网络共享以及需要临时装载到文件系统中，正常情况下，设备会有一个独立的子目录，这些设备的内容会出现在独立的子目录下。

### FHS

参考：

* [Filesystem Hierarchy Standard（FHS）官方网站](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
* [Linux Filesystem Hierarchy指南](https://www.pathname.com/fhs/)
* 《鸟哥的Linux私房菜》第四版：陈嵩（鸟哥）著，详细介绍了Linux文件系统结构和基本命令等内容。
* 《Understanding the Linux Kernel, 3rd Edition》：Daniel P. Bovet, Marco Cesati 著，这本书对Linux内核和文件系统有非常深入的讲解。

## 权限管理

### 用户和用户组

1. 用户：

   用户是指在一个操作系统中，一系列权限的集合体，操作人员通过用户名和口令可以在系统中执行某一些被允许的操作。不同的用户可以具有不同的权限。Linux 操作系统中每个用户都具有唯一标识 UID，当使用命令创建用户时，如果不指定用户的 UID，则系统将自动为其分配 UID。

2. 用户组：

   用户组就是具有相同特征的用户的集合体，在 Linux 系统中，每一个用户都属于至少一个用户组。Linux 操作系统中每个用户分组都具有唯一标识 GID，当使用命令创建用户组时，如果不指定用户组的 GID，则系统将自动为其分配 GID。当使用 -u 指定用户 id 时，用户 id 尽量大于500，以免冲突。因为 Linux 操作系统安装后，会默认建立一些用户，所以可能会占用 500 之内的 id 号。

3. root用户：

   - 系统有一个权限最大的用户，其名称为 root ，root 用户属于 root 用户组。
   - 系统默认只有 root 权限可以添加和删除用户。
   - 添加用户之后，如果没有给用户指定用户组，则系统会为用户添加一个同名的用户组，用户属于该组。
   - root 切换到普通用户无需登录，普通用户切换到 root 用户需要登陆。
   - root 可以给用户赋予和回收某一个文件的读、写、执行的权限。

4. 常用操作命令：

   [常用用户操作](#userOperation)
   
5. 创建用户

   > 1. **使用 root 或具有 sudo 权限的用户登录**：
   >
   >    - 以 root 用户身份登录，或者使用具有 sudo 权限的用户账号登录到系统。
   >
   > 2. **打开终端**：
   >
   >    - 打开终端应用程序，以便能够输入命令。
   >
   > 3. **使用 useradd 命令创建用户**：
   >
   >    - 在终端中输入以下命令来创建新用户：
   >
   >      ```
   >      Copy Codesudo useradd -m newusername
   >      ```
   >
   >    - 这里的 `newusername` 是你希望创建的新用户的用户名。`-m` 选项会自动为新用户创建一个与用户名相同的家目录。
   >
   > 4. **设置新用户的密码**：
   >
   >    - 输入以下命令来为新用户设置密码：
   >
   >      ```
   >      Copy Codesudo passwd newusername
   >      ```
   >
   >    - 系统会提示你输入新用户的密码两次以完成设置。
   >
   > 5. **（可选）分配附加组**：
   >
   >    - 如果需要将新用户加入其他附加组，可以使用以下命令：
   >
   >      ```
   >      Copy Codesudo usermod -aG groupname newusername
   >      ```
   >
   >    - 这里的 `groupname` 是你希望将新用户加入的附加组的名称。
   >
   > 6. **（可选）为新用户设置个性化配置**：
   >
   >    - 如果需要为新用户设置特定的环境配置或个性化设置，可以编辑新用户的 bash 配置文件 `~/.bashrc` 或其他相关配置文件。

### 权限操作

Linux 操作系统为文件定义了读、写、执行三种权限，不同的用户或者用户组可以具有不同的权限，系统采用 “r”、“w”、“x” 来分别表示文件的读、写、执行权限。使用 ls -l 命令可以查看到用户在当前目录或者文件的操作权限。举例如下：

~~~shell
drwxr-xr-x 4 root root  4096 5月  18 23:44 project_management
# d：代表 bin 数目目录而不是文件
#rwx：代表拥有者具有读、写、执行的权限
#r-x：代表同组用户具有读、执行的权限，但是没有写权限
#r-x：代表其他组用户具有读、执行权限，没有写权限
~~~

1. 常用命令：

   * chmod：变更权限。

   * 语法：

     * 选项

       ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAlGK1zvGzibmnP92LLEibGhcZyjBGInDANKsQeKhMxicOUrvqB0uIS9iaIw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

     * 参数：chmod 的参数可以分为两种，分别是权限模式和数字模式。**权限模式**使用 u、g、o 分别代表拥有者、同组用户、其他组用户，使用 + 和一代表赋予和收回权限，使用 r、w、x 代表读、写、执行权限。为了简化授权步骤，用户也可以采用**数字模式**进行授权，使用二进制的形式代表 r、w、x 三种权限，如 `101 (5) =r -x`，`111 (7) =rwx`，`100 (3) =r- -`。

       ~~~shell
       chmod -r U+X,G+W F01
       # 将文件01的执行权限给当前用户，写权限赋给用户所在的用户组和其他用户。
       chmod -r u=rwx,g=rw,o=rw f01
       # 将文件 f01 的读、写、执行的权限赋给当前用户，将读、写权限赋给用户所在的用户组和其他用户。
       chmod 753 -r f01
       # 将文件 f01 的读、写、执行的权限赋给当前用户，将读和执行权限赋给用户组、将写和执行权限赋给其他用户。
       ~~~

## <a id="install">软件安装</a>

在Linux系统上安装软件时，通常有以下几种方式：

* 使用软件包管理器（如yum、apt、dnf）：不同的发行版可能会使用不同的软件包管理器，例如，基于Debian的发行版（如Ubuntu）通常使用apt作为软件包管理器，而基于Red Hat的发行版（如CentOS、Fedora）则使用yum或dnf。
* 手动编译源代码安装程序
* 使用容器技术（如Docker）

1. 软件包管理器

   * rpm
   * yum：主要用于Red Hat、CentOS 等发行版，它允许你从预配置的软件仓库中安装、更新和删除软件包。
   * apt：在Debian、Ubuntu 等基于Debian 的发行版中使用，它也从预配置的软件仓库中管理软件包。
   * dnf：是yum的下一代版本，在最新的Fedora以及Red Hat Enterprise Linux 8中出现

2. 软件安装位置

   通常来说，Linux系统中的软件安装位置遵循FHS（Filesystem Hierarchy Standard）标准。常见的安装位置包括：

   - `/bin`：存放系统启动时需要的最基本的命令。
   - `/sbin`：存放系统管理员使用的系统管理命令。
   - `/usr/bin`：存放用户使用的标准命令。
   - `/usr/local`：存放本地安装的软件，默认安装位置为 `/usr/local/bin`、`/usr/local/sbin` 等。

3. 本地软件管理

   使用软件包管理器的查询功能可以列出已安装的软件包。
   
   * 对于yum、dnf 可以使用 `yum list installed` 或 `dnf list installed`；
   * 对于apt，可以使用 `dpkg --list`。

### RPM

参考：

* [**Linux系统-RPM包详解**](https://www.cnblogs.com/luodenglin/p/11888751.html)

> RPM主要用于基于RPM的Linux发行版（如Red Hat Enterprise Linux、Fedora、CentOS等），而Debian系列的发行版（如Ubuntu）使用的是不同的包管理系统（APT）。

1. rpm（Red Hat Package Manager）：一种常见的包管理系统，用于在基于RPM的Linux发行版中安装、升级、管理和删除软件包。

   * **RPM包**是一种预编译的软件包，它包含了要在Linux系统上安装的软件及其相关文件。RPM包的文件扩展名通常为`.rpm`。RPM包由软件的开发者或发行版的维护者创建。
   * **RPM命令**执行安装rpm包和源码包，rpm包以`.rpm`结尾，而源码包以`.src.rpm`结尾
   * **RPM数据库**是一个记录已安装的软件包及其信息的系统数据库。它包含了软件包的名称、版本、文件列表等信息。RPM使用数据库来追踪系统上已安装的软件包，并进行依赖性管理和软件包冲突解决。

2. 依赖性管理（RPM优点）：RPM可以管理软件包之间的依赖关系。当安装或升级软件包时，RPM会自动检查并解决依赖关系，以确保所需的库和组件也被正确安装

3. RPM包

   * 命令规则：

     ~~~
     name-version-arch.rpm
     name-version-arch.src.rpm
     ~~~

   * 示例：`bind-9.8.2-0.47.rc1.el6.x86_64.rpm`

     * name，如：bind，是软件的名称
     * version，如：9.8.2-0，是软件的版本号，版本号格式通常为“主版本号.次版本号.修正号”。47，是发布版本号，表示这个rpm软件包是第几次编译生成的
     * arch，如i386，是表示包适用的硬件平台，目前rpm支持的平台有：i386，i586，i686，sparc和alpha
     * .rpm和.src.rpm，是rpm包类型后缀，rpm是编译好的二进制包，.src.rpm是源码包
     * 特殊名称：
       * el*：表示发行商的版本，el6表示这个软件包是在rhel6.x/centos6.x下使用；
       * devel：表示这个rpm包是软件的开发包
       * noarch：说明这样的软件包可以在任何平台安装和运行，不需要特定的硬件平台

4. RPM命令行工具：RPM提供了一组命令行工具，用于管理软件包。

   * 语法：`rpm [选项] [软件包]`

   * 常用命令

     * `rpm -i package.rpm`：安装一个RPM包，也可以使用`rpm -ivh 软件包路径`安装软件包并查看进度。
     * `rpm -e package`：卸载一个已安装的软件包。
     * `rpm -q package`：查询已安装的软件包信息，也可使用`rpm -qa|grep [软件包关键词]`查询具体包。
     * `rpm -U package.rpm`：升级一个已安装的软件包。
     * `rpm -F package.rpm`：仅在软件包已安装的情况下升级。
     * `rpm -Va`：验证已安装的软件包的完整性。

   * 常用选项组合

     * --force 忽略软件包及文件的冲突，即强制安装（长格式命令）
     * --nodeps 忽略软件包的依赖关系（长格式命令）
     * --test 安装测试，并不实际安装（长格式命令）

     ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAb1icG3HB87Ox6bAq3uKNn2icc6G4gRE70L861YzphEyT8rSfmIph2jHg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

5. RPM包默认安装路径

   * `/etc/`配置文件安装目录 
   * `/usr/bin/`可执行的命令安装目录
   * ` /usr/lib/`程序所使用的函数库保存位置 
   * `/usr/share/doc/`基本的软件使用手册保存位置
   * `/usr/share/man/`帮助文件保存位置

6. RPM构建

   RPM提供了一种打包和构建软件包的机制，使开发者能够将自己的软件打包为RPM包，并与其他人共享或发布。构建RPM包需要创建一个`.spec`文件，其中包含软件包的描述和构建逻辑。

### yum&dnf

#### yum

1. yum
2. 常用指令：
   * yum list
   * yum install
   * yum remove
   * yum源配置

#### dnf

1. dnf：新一代的rpm软件包管理器。
   * DNF包管理器克服了YUM包管理器的一些瓶颈，提升了包括用户体验，内存占用，依赖分析，运行速度等多方面的内容。
   * DNF使用 RPM, libsolv 和 hawkey 库进行包管理操作。
2. dnf常用命令

### apt

### wegt

# Shell

* [花费90分钟一口气学完！带你掌握shell脚本所有核心知识点](https://www.bilibili.com/video/BV14L4y157Bv/?spm_id_from=333.337.search-card.all.click&vd_source=fabefd3fabfadb9324761989b55c26ea)
* [java高级程序员拓展课，玩转Shell编程](https://www.bilibili.com/video/BV1z54y1C7Cw/?spm_id_from=333.337.search-card.all.click&vd_source=fabefd3fabfadb9324761989b55c26ea)
* [Linux Shell脚本攻略（第2版） (aliyuncs.com)](https://axzo-static.oss-cn-chengdu.aliyuncs.com/fe-doc/febooks/Linux Shell脚本攻略（第2版）.pdf?e=1585903766&token=sCDBnLNlkabH959_G0_P38gBc7LZN2XHXcdIwPv4:BTJwJzSwiJkITCuKV4TCPEshlMQ=)

## 简介

1. 脚本

   从开发者的角度理解，“脚本”是一种**用于自动化任务或批处理操作的计算机程序**。它通常采用文本形式编写，可以被解释器或解释型语言直接执行，而无需编译成可执行文件。下面是对脚本概念的更详细解释：

   1. 自动化任务：脚本被用于执行需要重复性操作或批量处理的任务。通过编写脚本，开发者可以指定一系列操作、逻辑和流程，以便在不需要人工干预的情况下自动完成任务。例如，自动备份文件、定时清理临时数据等。

   2. 解释型语言：脚本通常使用解释型语言编写，如Python、JavaScript、Shell等。相比于编译型语言（例如C++、Java），解释型语言的脚本不需要事先编译成二进制文件，而是通过解释器逐行解析和执行脚本代码。

   3. 灵活性和简洁性：由于脚本语言具有简洁和高级的语法特性，开发者可以更轻松地编写复杂的脚本程序。脚本语言通常提供了丰富的内置函数和库，这有助于简化脚本编写过程，并提供各种功能来处理文本、文件、网络、操作系统等方面的任务。

   4. 可移植性：脚本程序在不同操作系统和平台上具有良好的可移植性。由于脚本语言通常是解释执行的，只要相应的解释器存在于目标系统上，脚本就可以在各种环境中运行，而无需对源代码进行修改。

   5. 快速开发和调试：脚本语言提供了快速开发和调试程序的能力。开发者可以通过交互式解释器或集成开发环境（IDE）逐行执行脚本代码，并立即查看结果。这种实时反馈可以加快开发迭代周期和问题排查过程。

   总而言之，从开发者的角度来看，脚本是一种用于自动化任务的高级编程工具，它简化了任务处理的复杂度，提高了开发效率，并在各种计算机环境中具有广泛的适应性。
   
   > 从脚本的定义出发，通常在Windows中是`.bat`文件，在Linux中是`.sh`文件。
   
2. Shell：Shell 是一种**命令行解释器**，它是用户与操作系统内核进行交互的界面。在计算机领域，Shell 通常是指用于执行操作系统命令和脚本的用户界面。

3. Shell的特点和功能：

   * **命令解释**：用户可以通过 Shell 输入命令，Shell 会将这些命令解释并传递给操作系统内核执行。

   * **脚本编写**：Shell 提供了一种编写脚本的方式，用户可以将一系列命令以脚本的形式存储起来，并通过 Shell 执行这些脚本，实现自动化操作。
   * **环境控制**：Shell 允许用户对操作系统环境进行控制和定制，比如设置环境变量、修改文件权限等。
   * **通配符扩展**：Shell 支持通配符，比如 `*` 和 `?` 等，用于快速匹配文件名或其他字符串。
   * **管道和重定向**：Shell 支持管道操作和重定向，允许用户将多个命令连接起来，以及将命令的输入输出重定向到文件或其他命令。

   总之，Shell 在计算机系统中扮演着至关重要的角色，它**为用户提供了一个灵活而强大的接口，使得用户能够通过命令行完成各种操作**，从简单的文件操作到复杂的系统管理任务。

4. Shell运行过程

   当用户下达指令给该操作系统的时候，实际上是把指令告诉shell，经过shell解释，处理后让内核做出相应的动作。系统的回应和输出的信息也由shell处理，然后显示在用户的屏幕上。

   ![image-20231111215724838](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202311112157597.png)

5. Shell解释器

   在 Linux 和 Unix 系统中，有多种不同的 Shell解释器，其中最常见的包括 ：

   | Shell 解析器 | 描述                                                         |
   | ------------ | ------------------------------------------------------------ |
   | **Bash**     | Bourne Again Shell，是最常用的 Shell，也是许多 Linux 系统默认的 Shell。它继承自 Bourne Shell，并添加了许多新特性。 |
   | **Sh**       | Bourne Shell，是 Unix 系统的早期 Shell，为后来的 Shell 提供了基础。 |
   | **Csh**      | C Shell，具有 C 语言风格的语法，支持命令历史和作业控制等特性。 |
   | **Ksh**      | Korn Shell，结合了 Csh 和 Bourne Shell 的优点，是 Unix 系统中的另一种流行的 Shell。 |
   | **Zsh**      | Z Shell，拥有强大的自动补全功能和丰富的插件支持，被认为是 Bash 的升级版。 |
   | **Fish**     | Friendly Interactive Shell，注重易用性和交互性，提供了更加人性化的命令行体验。 |
   | **Dash**     | dash (Debian Almquist Shell) ，也是一种 Unix shell。它比 Bash 小，只需要较少的磁盘空间，但是它的对话性功能也较少，交互性较差。 |

   这些 Shell 提供了一种方式，让用户可以通过输入文本命令来与操作系统进行交互，并且能够执行诸如文件操作、进程管理、系统配置等任务。

   通过以下命令可以查看，当前Linux系统支持的Shell解释器和默认使用的Shell解释器，以及切换默认Shell：

   ~~~shell
   # 查看所有Shell解释器
   cat /etc/shells
   # 查看当前系统环境默认使用解释器
   echo $SHELL
   # 切换默认Shell
   chsh -s $(which zsh)
   ~~~

## Shell脚本

### 脚本编写

1. 后缀名：使用`.sh`

2. 首行格式（Shebang）

   首行需要设置Shell解析器的类型，语法如下：

   ~~~shell
   #!/bin/bash 
   ~~~

   > 含义：
   >
   > * #!/bin/bash设置当前shell脚本文件采用bash解析器运行脚本代码
   > * #!/usr/bin/python 开头的文件，代表指定python解释器去执行
   > * #!/usr/bin/env 解释器名称 ，是一种在不同平台上都能正确找到解释器的办法
   >
   > 注意事项：
   >
   > * 如果脚本未指定 shebang ，脚本执行的时候，默认用当前shell去解释脚本，即 $SHELL
   > * 如果 shebang 指定了可执行的解释器，如 /bin/bash /usr/bin/python ，脚本在执行时，文件名会作为参数传递给解释器
   > * 如果#!指定的解释程序没有可执行权限，则会报错“bad interpreter: Permission denied”。
   > * 如果#!指定的解释程序不是一个可执行文件，那么指定的解释程序会被忽略，转而交给当前的SHELL去执行这个脚本。
   > * 如果#!指定的解释程席不存在，那么会报错“badinterpreter: No such file or directory”
   > * #!之后的解释程序，需要写其绝对路径 (如: #!/bin/bash)，它是不会自动到SPATH中寻找解释器的
   > * 如果你使用"bash test.sh“这样的命令来执行脚本，那么#!这一行将会被忽略掉，解释器当然是用命令行中显式指定的bash。

3. 注释

   ~~~shell
   # 这是单行注释
   
   :<<!
   # 这是多行注释
   # 这是多行注释
   !
   ~~~

### 脚本执行

1. 常用执行方式

   * sh解释器执行方式：使用sh命令执行脚本文件，本质就是使用Shell解析器运行脚本文件

     语法：

     ~~~shell
     sh 脚本文件
     ~~~

   * bash解释器执行方式：使用bash命令执行脚本文件，本质就是使用Shell解析器运行脚本文件

     语法：

     ~~~shell
     bash 脚本文件
     ~~~

   * 仅路径执行方式：执行当前目录下的脚本文件，脚本文件自己执行需要具有可执行权限，否则无法执行

     语法：

     ~~~shell
     ./脚本文件
     ~~~

### Shell变量

1. 变量作用：用于存储管理临时的数据这些数据都是在运行内存中的。
2. 变量类型
   * 系统环境变量：系统提供的共享变量.是linux系统加载Shell的配置文件中定义的变量共享给所有的Shell程序使用。
   * 自定义变量
   * 特殊符号变量

#### 系统环境变量

1. Shell的配置文件分类

   * 全局配置文件

     > /etc/profile
     >
     > /etc/profile.d/*.sh
     >
     > /etc/bashrc

   * 个人用户配置文件

     > 当前用户/.bash_profile
     >
     > 当前用户/.bashrc

   一般情况下，通常直接针对全局配置文件进行操作。

2. 系统环境变量

   在Linux系统中，环境变量按照其作用范围不同大致可以分为系统级环境变量和用户级环境变量。

   * 系统级环境变量: Shell环境加载全局配置文件中的变量共享给所有用户所有Shell程序使用，全局共享
   * 用户级环境变量: Shell环境加载个人配置文件中的变量共享给当前用户的Shell程序使用,登录用户使用

   ~~~shell
   # 查看系统环境变量
   env
   # 查看Shell变量(系统环境变量+自定义变量+函数)
   set
   ~~~

   以下是一些常用的系统环境变量：

   | 变量      | 作用                                                    | 值                                                           |
   | --------- | ------------------------------------------------------- | ------------------------------------------------------------ |
   | PATH      | 指定可执行程序的搜索路径，以冒号分隔                    | /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin |
   | HOME      | 当前用户的主目录路径                                    | /home/username                                               |
   | SHELL     | 用户默认的 Shell 程序路径                               | /bin/bash                                                    |
   | USER      | 当前用户的用户名                                        | username                                                     |
   | LOGNAME   | 用户的登录名                                            | username                                                     |
   | PS1       | 主提示符（Primary Prompt）的格式字符串                  | \u@\h:\w$                                                    |
   | PS2       | 次级提示符（Secondary Prompt）的格式字符串              | >                                                            |
   | HISTIFILE | 显示当前用户执行命令的历史列表文件: /root/.bash_history |                                                              |

3. 环境变量初始化流程

   * 交互式Shell和非交互式Shell
   * 登录Shell环境和非登录Shell环境

   ![image-20231112134159744](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202311121342689.png)

#### 自定义变量

1. 自定义变量

   * 类型：

     * 自定义局部变量：定义在一个脚本文件中的变量,只能在这个脚本文件中使用的变量,就是局部变量
     * 自定义全局变量
     * 自定义常量：变量设置值以后不可以修改的变量，也叫只读变量

   * 定义与使用

     ~~~shell
     # 定义局部标量
     var_name=value
     #!<< 
     # 注意事项:
     # 变量名称可以有字母,数字和下划线组成，但是不能以数字开头
     # 等号两侧不能有空格
     # 在bash环境中,变量的默认类型都是字符串类型,无法直接进行数值运算
     # 变量的值如果有空格,必须使用双引号括起来
     # 不能使用Shell的关键字作为变量名称
     !
     
     # 查询变量值
     # 语法一：直接使用变量名
     $var_name
     # 语法二：使用花括号
     ${var_name}
     #区别： 花括号适用拼接字符串
     
     # 变量删除
     unset var_name
     
     # 定义常量
     readonly var_name
     
     # 定义全局变量
     export var_name1 var_name2
     ~~~

2. 自定义系统级环境变量

   当前用户进入Shel环境初始化的时候会加载全局配置文件/etc/profile里面的环境变量,供给所有Shell程序使用以后只要是所有Shell程序或命令使用的变量,就可以定义在这个文件中。步骤如下：

   1. 打开 `/etc/profile` 文件进行编辑：

      ```shell
      sudo nano /etc/profile
      ```

   2. 在文件末尾添加你需要设置的环境变量，例如：

      ```shell
      export CUSTOM_VAR="custom value"
      ```

      > 对于vim编辑器，可以使用`G`快速定位到文件末尾，使用`gg`快速定位到文件首行

#### 特殊变量

1. 特殊变量

   常用的特殊变量如下：

   | 变量  | 作用                                                         |
   | ----- | ------------------------------------------------------------ |
   | $0    | 当前脚本的文件名                                             |
   | $1-$9 | 用于接收脚本或函数的参数，$1 是第一个参数，依次类推，第十个起使用花括号包裹 |
   | $*    | 所有的位置参数，作为单个字符串显示                           |
   | $@    | 所有的位置参数，作为独立的字符串显示                         |
   | $#    | 传递给脚本或函数的参数个数                                   |
   | $?    | 用于获取上一个shell命令的退出状态码,或者是函数的返回值每个shell命令的执行都有一个返回值,这个返回值用于说明命令执行是否成功般来说,返回0代表命令执行成功,非0代表执行失败 |
   | $$    | 当前 Shell 进程的进程 ID                                     |
   | $!    | 后台运行的最后一个进程的进程 ID                              |

#### 字符串变量

1. 3种格式：

   * 单引号：任何字符都会原样输出，在拼接字符串中使用变量是无效的。
   * 双引号：其中包含了变量，那么该变量会被解析得到值，而不是原样输出。字符串中还可以出现双引号的子字符串，但是需要转义
   * 无引号：不被引号包围的字符串中出现变量时也会被解析，这一点和双引号包围的字符串一样。字符串中不能出现空格，否则空格后边的字符串会作为其他命令解析

2. 获取字符串长度

   ~~~shell
   ${#var_name}
   ~~~

3. 字符串拼接

   * 无符号拼接
   * 双引号拼接
   * 混合拼接

4. 字符串截取

   | 语法                        | 描述                              |
   | --------------------------- | --------------------------------- |
   | `${variable}`               | 变量本身的值                      |
   | `${variable-}`              | 如果变量未被设置，则为空          |
   | `${variable:-default}`      | 如果变量未被设置，则使用默认值    |
   | `${variable#pattern}`       | 从开头删除最短匹配 pattern 的子串 |
   | `${variable##pattern}`      | 从开头删除最长匹配 pattern 的子串 |
   | `${variable%pattern}`       | 从末尾删除最短匹配 pattern 的子串 |
   | `${variable%%pattern}`      | 从末尾删除最长匹配 pattern 的子串 |
   | `${variable:offset}`        | 从指定偏移量开始的子串            |
   | `${variable:offset:length}` | 从指定偏移量开始指定长度的子串    |

#### 索引数组

Shell 支持数组 (Array)，组是若干数据的集合，其中的每一份数据都称为数组的元素。

> 注意Bash shell 只支持一维数组，不支持多维数组。 

1. 定义

   在 Shell 中，用括号(来表示数组，数组元素之间用空格来分隔。语法为：

   ~~~shell
   # 方式一
   arr=(value1 value2 ...)
   # 方式二
   arr=([index1]=value1 [index2]=value2,...)
   ~~~

   > 注意等号两边不能有空格

2. 数组元素获取和使用

   ~~~shell
   # 通过下标获取元素，索引从0开始
   ${arr[index]}
   # 使用@或*获取数组中所有元素
   ${arr[@]}
   ${arr[*]}
   # 获取数组长度
   ${#arr[@]}
   ${#arr[*]}
   # 获取数组指定元素的字符长度
   ${#arr[索引]}
   # 拼接数组
   arr3 = (${arr1[*]} ${arr2[*]})
   ~~~

3. 删除数组

   ~~~shell
   # 删除整个数组
   unset arr
   # 删除指定元素
   unset arr[index]
   ~~~

### Shell内置命令

1. 概念：shell 内置命令，就是由 Bash Shell 自身提供的命令，而不是文件系统中的可执行脚本文件

2. 判断：可以通过使用type命令查看一个命令是否是内置命令

   ~~~shell
   type 命令
   ~~~

   通常来说，内置命令会比外部命令执行得更快，执行外部命令时不但会触发磁盘 /0，还需要 fork 出一个单独的井程来执行，执行完成后再退出。而执行内置命令相当于调用当前 Shell 进程的一个函数,还是在当前Shell环境进程内,减少了上下文切换。

3. 常用内置命令

   具体使用可参考[Linux常用命令](#instruct)

   | 命令      | 描述                                                         |
   | --------- | ------------------------------------------------------------ |
   | `echo`    | 显示文本或变量的内容                                         |
   | `cd`      | 切换当前工作目录                                             |
   | `pwd`     | 显示当前工作目录的路径                                       |
   | `ls`      | 列出目录内容                                                 |
   | `mkdir`   | 创建新目录                                                   |
   | `rm`      | 删除文件或目录                                               |
   | `cp`      | 复制文件或目录                                               |
   | `mv`      | 移动文件或目录，或重命名文件                                 |
   | `cat`     | 显示文件内容                                                 |
   | `grep`    | 在文件中搜索指定模式                                         |
   | `chmod`   | 修改文件或目录的权限                                         |
   | `chown`   | 修改文件或目录的所有者                                       |
   | `ps`      | 显示当前运行的进程                                           |
   | `kill`    | 终止正在运行的进程                                           |
   | `bg`      | 将作业放到后台运行                                           |
   | `fg`      | 将作业调至前台运行                                           |
   | `jobs`    | 列出当前作业列表                                             |
   | `source`  | 执行指定脚本文件                                             |
   | `alias`   | 创建命令别名或显示当前别名列表                               |
   | `unalias` | 删除指定别名（临时删除，长久删除需要去配置文件中删除）       |
   | `export`  | 设置环境变量                                                 |
   | `history` | 显示最近执行的命令列表                                       |
   | `exit`    | 退出当前 shell                                               |
   | `help`    | 显示内置命令的帮助信息                                       |
   | `test`    | 用于检查某个条件是否成立，可以进行数值、字符和文件三个方面的测试 |

### Shell运算符

#### 计算命令

具体使用，参考[计算命令](#caculater)

#### 算术运算符

1. 常用算术运算符

   | 运算符 | 描述               | 示例                             |
   | ------ | ------------------ | -------------------------------- |
   | +      | 加法               | `result=$((num1 + num2))`        |
   | -      | 减法               | `result=$((num1 - num2))`        |
   | *      | 乘法               | `result=$((num1 * num2))`        |
   | /      | 除法               | `result=$((num1 / num2))`        |
   | %      | 求模（取余）       | `result=$((num1 % num2))`        |
   | **     | 幂运算             | `result=$((num1 ** num2))`       |
   | ++     | 自增运算           | `num++` 或 `((num++))`           |
   | --     | 自减运算           | `num--` 或 `((num--))`           |
   | +=     | 加法赋值           | `num1+=num2` 或 `((num1+=num2))` |
   | -=     | 减法赋值           | `num1-=num2` 或 `((num1-=num2))` |
   | *=     | 乘法赋值           | `num1*=num2` 或 `((num1*=num2))` |
   | /=     | 除法赋值           | `num1/=num2` 或 `((num1/=num2))` |
   | %=     | 模赋值（取余赋值） | `num1%=num2` 或 `((num1%=num2))` |
   | ==     | 相等比较           | `if [ $num1 == $num2 ]`          |
   | !=     | 不相等比较         | `if [ $num1 != $num2 ]`          |
   | >      | 大于比较           | `if [ $num1 > $num2 ]`           |
   | <      | 小于比较           | `if [ $num1 < $num2 ]`           |
   | >=     | 大于等于比较       | `if [ $num1 >= $num2 ]`          |
   | <=     | 小于等于比较       | `if [ $num1 <= $num2 ]`          |

   > 注意事项：
   >
   > - Shell 算术运算符一般用于在脚本中进行数值计算。
   > - 在双括号 `(( ))` 中使用算术运算符时，可以省略 `$` 符号。
   > - 在条件判断语句中使用比较运算符时，需要在运算符前后添加空格。

#### 比较运算符

1. 整数比较运算符

   | 运算符 | 描述                 | 示例                     |
   | ------ | -------------------- | ------------------------ |
   | -eq    | 等于                 | `if [ $num1 -eq $num2 ]` |
   | -ne    | 不等于               | `if [ $num1 -ne $num2 ]` |
   | -gt    | 大于                 | `if [ $num1 -gt $num2 ]` |
   | -lt    | 小于                 | `if [ $num1 -lt $num2 ]` |
   | -ge    | 大于等于             | `if [ $num1 -ge $num2 ]` |
   | -le    | 小于等于             | `if [ $num1 -le $num2 ]` |
   | ==     | 等于（双括号内）     | `if (( num1 == num2 ))`  |
   | !=     | 不等于（双括号内）   | `if (( num1 != num2 ))`  |
   | >      | 大于（双括号内）     | `if (( num1 > num2 ))`   |
   | <      | 小于（双括号内）     | `if (( num1 < num2 ))`   |
   | >=     | 大于等于（双括号内） | `if (( num1 >= num2 ))`  |
   | <=     | 小于等于（双括号内） | `if (( num1 <= num2 ))`  |

   >注意事项：
   >
   >- 这些整数比较运算符用于在条件判断语句中比较整数值。
   >- 在方括号 `[ ]` 中使用整数比较运算符时，需要添加空格。

2. 字符串比较运算符：变量的类型可以为数字'(整数，小数)与字符串，字符串比较可以使用`[[]]`和`[]`两种方式。 

   | 运算符 | 描述             | 示例                         |
   | ------ | ---------------- | ---------------------------- |
   | =      | 相等             | `if [ "$str1" = "$str2" ]`   |
   | ==     | 相等（同 `=`）   | `if [ "$str1" == "$str2" ]`  |
   | !=     | 不相等           | `if [ "$str1" != "$str2" ]`  |
   | -z     | 空字符串         | `if [ -z "$str" ]`           |
   | -n     | 非空字符串       | `if [ -n "$str" ]`           |
   | $      | 是否不为空       | `if [ ? "$str"]`             |
   | <      | 小于（按字典序） | `if [[ "$str1" < "$str2" ]]` |
   | >      | 大于（按字典序） | `if [[ "$str1" > "$str2" ]]` |

   > 注意事项：
   >
   > - 这些字符串比较运算符用于在条件判断语句中比较字符串。
   > - 在方括号 `[ ]` 或双方括号 `[[ ]]` 中使用字符串比较运算符时，需要添加空格。
   > - 使用双方括号 `[[ ]]` 进行字符串比较时，可以使用 `<` 和 `>` 进行按字典序的大小比较。

#### 逻辑运算符

#### 布尔运算符

1. 布尔运算符

   | 运算符 | 描述              | 示例                                                         |
   | ------ | ----------------- | ------------------------------------------------------------ |
   | !      | 逻辑非（取反）    | `if [ ! condition ]`                                         |
   | -a     | 逻辑与（and）     | `if [ condition1 -a condition2 ]` 或 `if [ condition1 && condition2 ]` |
   | -o     | 逻辑或（or）      | `if [ condition1 -o condition2 ]` 或 `if [ condition1 || condition2 ]` |
   | &&     | 短路逻辑与（and） | `if [ condition1 && condition2 ]`                            |
   | \|\|   | 短路逻辑或（or）  | `if [ condition1 || condition2 ]`                            |

   > 注意事项：
   >
   > - 在方括号 `[ ]` 中使用布尔运算符时，需要添加空格。
   > - 布尔运算符放在[或与test命令配合使用才有效
   > - `&&` 和 `||` 是短路逻辑运算符，如果第一个条件能够确定整个表达式的值，就不会再计算第二个条件。
   > - `&&` 和 `||` 必须放在`[[]]`或`(())`中执行，否则报错

#### 文件测试运算符

1. Linux系统文件类型

   * `-`：普通文件
   * `d`：目录文件
   * `l`：链接文件
   * `b`： 块设备文件
   * `c`：字符设备文件
   * `p`：管道文件

2. 文件测试运算符：用于检测文件的各种属性

   属性检测描述：

   | 运算符 | 描述                                             | 示例                           |
   | ------ | ------------------------------------------------ | ------------------------------ |
   | -e     | 检测文件是否存在，包括普通文件、目录、符号链接等 | `-e file.txt`                  |
   | -f     | 检测文件是否为普通文件                           | `-f script.sh`                 |
   | -d     | 检测文件是否为目录                               | `-d /path/to/directory`        |
   | -s     | 检测文件是否非空（大小不为0）                    | `-s data.txt`                  |
   | -r     | 检测文件是否可读                                 | `-r file.txt`                  |
   | -w     | 检测文件是否可写                                 | `-w file.txt`                  |
   | -x     | 检测文件是否可执行                               | `-x script.sh`                 |
   | -L/-h  | 检测文件是否为符号链接                           | `-L link.txt` 或 `-h link.txt` |
   | -O     | 检测文件是否属于当前用户                         | `-O file.txt`                  |
   | -G     | 检测文件是否属于当前用户组                       | `-G file.txt`                  |
   | -nt    | 检测文件1是否比文件2新（修改时间较晚）           | `file1.txt -nt file2.txt`      |
   | -ot    | 检测文件1是否比文件2旧（修改时间较早）           | `file1.txt -ot file2.txt`      |
   | -ef    | 检测文件1和文件2是否为同一个文件（硬链接）       | `file1.txt -ef file2.txt`      |

#### `[[]]`&`[]`

1. word splitting：会将含有空格字符串进行分拆分割后比较
2. 区别：
   * `[[]]`不会有word splitting发生，`[]`会有word splitting发生
   * `[[]]`对`<`不需要转义，`[]`需要对`<`，`>`转义

### Shell流程控制

主要包括以下几种类型的流程控制语句：

* 条件判断语句（if-then-else）
* 循环语句（for、while、until）
* case语句（switch语句）

1. 条件判断语句（if-then-else）：

   - `if-then-else`语句根据条件的真假执行不同的代码块。

   ```shell
   if [ condition ]; then
       # 如果条件为真，则执行这里的代码
   else
       # 如果条件为假，则执行这里的代码
   fi
   ```

   示例：

   ```shell
   num=10
   if [ $num -gt 0 ]; then
       echo "Number is positive"
   else
       echo "Number is non-positive"
   fi
   ```

2. 循环语句：

   - `for`循环：用于遍历列表中的元素执行特定的代码块。

   ```sh
   for var in list; do
       # 执行针对每个元素的操作
   done
   ```

   示例：

   ```shell
   for fruit in apple banana orange; do
       echo "I like $fruit"
   done
   ```

   - `while`循环：当指定条件为真时，重复执行代码块。

   ```shell
   while [ condition ]; do
       # 只要条件为真，就会一直执行这里的代码
   done
   ```

   示例：

   ```shell
   count=0
   while [ $count -lt 5 ]; do
       echo "Count: $count"
       ((count++))
   done
   ```

   - `until`循环：当指定条件为假时，重复执行代码块。

   ```shell
   until [ condition ]; do
       # 只要条件为假，就会一直执行这里的代码
   done
   ```

   示例：

   ```shell
   input=""
   until [ "$input" = "yes" ]; do
       read -p "Enter 'yes' to continue: " input
   done
   ```

3. case语句（switch语句）：

   - `case`语句根据变量的不同取值执行不同的代码块。

   ```shell
   case value in
       pattern1)
           # 匹配模式1时执行的代码
           ;;
       pattern2)
           # 匹配模式2时执行的代码
           ;;
       *)
           # 默认情况下执行的代码
           ;;
   esac
   ```

   示例：

   ```shell
   fruit="apple"
   case $fruit in
       "apple")
           echo "It's an apple"
           ;;
       "banana")
           echo "It's a banana"
           ;;
       *)
           echo "It's neither an apple nor a banana"
           ;;
   esac
   ```

4. select语句

   * `select`语句用于创建一个简单的菜单，允许用户从一组选项中进行选择。用户可以根据显示的菜单编号来选择相应的选项，然后脚本将根据用户的选择执行相应的代码块。`select`语句通常与`case`语句结合使用，以处理用户的选择。

   `select`语句的基本语法如下：

   ```
   select var in list
   do
       # 执行针对每个选项的操作
   done
   ```

   - `var` 是一个变量，用于存储用户选择的选项。
   - `list` 是一个由空格分隔的选项列表，供用户选择。

   接下来我们通过一个示例来说明`select`语句的使用：

   ```shell
   #!/bin/bash
   
   PS3="Enter the number of your choice: "  # 设置提示符
   
   echo "Which is your favorite programming language?"
   select language in "Python" "Java" "JavaScript" "C++" "Go" "Exit"
   do
       case $language in
           "Python")
               echo "Python is a great choice!"
               ;;
           "Java")
               echo "Java is a powerful language."
               ;;
           "JavaScript")
               echo "JavaScript is widely used for web development."
               ;;
           "C++")
               echo "C++ is a high-performance language."
               ;;
           "Go")
               echo "Go is a modern language developed by Google."
               ;;
           "Exit")
               echo "Exiting the menu..."
               break
               ;;
           *)
               echo "Invalid option, please try again."
               ;;
       esac
   done
   ```

   > 注意: select 是无限循环(死循环)，输入空值，或者输入的值无效，都不会结束循环，只有遇到 break 语句，或者按下Itrl+D 组合键才能结束循环。
   > 执行命令过程中: 终端会输出 ? 代表可以输入选择的菜单编号

### Shell重定向

### Shell函数

### 学习案例

* [shell脚本一天一练](https://www.bilibili.com/video/BV1ih4y1Y7nh/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=fabefd3fabfadb9324761989b55c26ea)

1. 已知目录/root/demo-shell目录，编写shell脚本，实现在/root/demo-shell/目录下创建一个one.txt，在one.txt文件中增加内容“Hello shell”。
2. 循环打印脚本文件的所有输入参数

# 资源&路线&工具

## 远程连接工具

参考：

* [14个优秀的SSH连接客户端软件工具推荐 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/609376551#:~:text=14个优秀的SSH连接客户端软件工具推荐 1 PUTTY 2 Hyper 3 Terminus 4,OpenSSH 6 MobaXterm 7 MremoteNG 8 WinSCP 更多项目)

1. XShell

2. MobaXterm

   官网：https://mobaxterm.mobatek.net/

   使用参考：

   * https://www.bilibili.com/video/BV1ze41157SP/?spm_id_from=333.337.search-card.all.click&vd_source=fabefd3fabfadb9324761989b55c26ea

3. FinalShell

   使用参考：

   * http://www.tuohang.net/article/273804.html

4. WindTerm

5. Putty

## 宝塔面板

官网：[宝塔面板 - 简单好用的Linux/Windows服务器运维管理面板 (bt.cn)](https://www.bt.cn/new/index.html)

## 1Panel

GitHub地址：https://link.zhihu.com/?target=https%3A//github.com/1Panel-dev/1Panel

## Linux资源网站

* [Linux 用户必备的 8 大网站 | Linux 中国 (qq.com)](https://mp.weixin.qq.com/s/5HyldkHH7snATWzIkpgYuQ)
* [Arch Linux](https://archlinux.org/)
* [DistroWatch.com: Put the fun back into computing. Use Linux, BSD.](https://distrowatch.com/)