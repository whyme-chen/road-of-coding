# Linux学习

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

## Linux常用命令

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

1. 软件安装方式

   ![image-20221118231233904](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182312501.png)
   
   * rpm
   
     > - 语法：`rpm [选项] [软件包]`
     > - 查询是否已经安装了某软件包：`rpm -qa|grep [软件包关键词]`
     > - 卸载已经安装的软件包：`rpm -e 软件包全名`
     > - 安装软件包并查看进度：`rpm -ivh 软件包路径`
     >
     > ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAb1icG3HB87Ox6bAq3uKNn2icc6G4gRE70L861YzphEyT8rSfmIph2jHg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
     
   * yum
   
     > 常用指令：
     >
     > yum list
     >
     > yum install
     >
     > yum remove
     >
     > yum源配置
   
2. jdk安装（解压方式）

   ![image-20221119115218075](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353986.png)

3. 安装tomcat（解压方式）

   ![image-20221119122116054](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353978.png)

   ![image-20221119122225352](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353642.png)

4. 安装MySQL（rpm方式）

   * 安装

     ![image-20221119123637520](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353081.png)

   * 卸载

     ![image-20221119123756530](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353764.png)

5. 安装lrzsz（yum方式）

   ![image-20221119124107682](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353324.png)

### 防火墙相关命令

![image-20221119122455628](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353373.png)

### 用户操作命令{#userOperation}

1. su

   * 作用：切换用户
   * 常用操作：`su[用户名]`和 `su -[用户名]`都可以切换用户，前者类似于临时切换用户，当使用该命令进行切换新用户时，用户配置仍然沿用原来的用户配置，如环境变量、系统变量等。而后者进行切换用户时，环境变量、系统设置全部切换成新用户的用户配置。

2. whoami

   * 作用：常看当前登录用户

3. groups

   * 作用：查看当前登录yoghurt所属分组

4. id

   * 作用：查看当前用户UID和GID

5. useradd

   * 作用：添加新用户

   * 语法：

     ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAAljfmvoqz0GlTTgRV6qopysxnicFibVrnxFr2pN2gproxnYiadaRicuSjQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

6. password

   * 作用：修改用户密码

   * 语法：

     ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRATetM0PqJcdSFUnf5ibhgKt4jxGcnnibQkl3qBfqYL4EIHHWfqgItibIUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

7. userdel

   * 作用：删除用户

   * 语法：

     ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAm4Ik1Wic2XtARX9MpxZJtJX8nACCyEfGSNo2clgCT9qFRxMMkj21VoA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

8. usermod

   * 作用：修改用户信息

   * 语法：

     ![图片](https://mmbiz.qpic.cn/mmbiz_png/eQPyBffYbufEQTRibHEQJMC2IfHT3YmRAenicHeVwwKqSPO88vHnAhfZT7x9V7GINN5L8RgE6pf23RaOZ4Z76uLg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

   * 常用操作：

     - 修改用户登录名：`usermod -l 新用户名 旧用户名`
     - 修改用户所属分组：`usermod -g 新组名称 用户名`

9. groupadd

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

### 其他

1. clear：清屏命令
2. man：查询命令详细参数

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

## Linux文件系统

1. 基本目录结构

   > - `/var`：包含在正常操作中被改变的文件、假脱机文件、记录文件、加锁文件、临时文件和页格式化文件等。
   > - `/home`：包含用户的文件：参数设置文件、个性化文件、文档、数据、EMALL、缓存数据等，每增加一个用户，系统就会根据其用户名在 home 目录下新建和其他用户同名的文件夹，用于保存其用户配置。
   > - `/proc`：包含虚幻的文件，他们实际上并不存在于磁盘上，也不占用任何空间（用 ls-l 可以显示它们的大小）当查看这些文件时，实际上是在访问存在内存中的信息，这些信息用于访问系统。
   > - `/bin`：包含系统启动时需要的执行文件（二进制），这些文件可以被普通用户使用。
   > - `/etc`：为操作系统的配置文件目录（防火墙、启动项）
   > - `/root`：为系统管理员（也叫超级用户或根用户）的 Home 目录。
   > - `/dev`：为设备目录，Linux 下设备被当成文件，这样一来硬件被抽象化、便于读写、网络共享以及需要临时装载到文件系统中，正常情况下，设备会有一个独立的子目录，这些设备的内容会出现在独立的子目录下。

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

# Shell

1. 脚本

   从开发者的角度理解，“脚本”是一种**用于自动化任务或批处理操作的计算机程序**。它通常采用文本形式编写，可以被解释器或解释型语言直接执行，而无需编译成可执行文件。下面是对脚本概念的更详细解释：

   1. 自动化任务：脚本被用于执行需要重复性操作或批量处理的任务。通过编写脚本，开发者可以指定一系列操作、逻辑和流程，以便在不需要人工干预的情况下自动完成任务。例如，自动备份文件、定时清理临时数据等。

   2. 解释型语言：脚本通常使用解释型语言编写，如Python、JavaScript、Shell等。相比于编译型语言（例如C++、Java），解释型语言的脚本不需要事先编译成二进制文件，而是通过解释器逐行解析和执行脚本代码。

   3. 灵活性和简洁性：由于脚本语言具有简洁和高级的语法特性，开发者可以更轻松地编写复杂的脚本程序。脚本语言通常提供了丰富的内置函数和库，这有助于简化脚本编写过程，并提供各种功能来处理文本、文件、网络、操作系统等方面的任务。

   4. 可移植性：脚本程序在不同操作系统和平台上具有良好的可移植性。由于脚本语言通常是解释执行的，只要相应的解释器存在于目标系统上，脚本就可以在各种环境中运行，而无需对源代码进行修改。

   5. 快速开发和调试：脚本语言提供了快速开发和调试程序的能力。开发者可以通过交互式解释器或集成开发环境（IDE）逐行执行脚本代码，并立即查看结果。这种实时反馈可以加快开发迭代周期和问题排查过程。

   总而言之，从开发者的角度来看，脚本是一种用于自动化任务的高级编程工具，它简化了任务处理的复杂度，提高了开发效率，并在各种计算机环境中具有广泛的适应性。