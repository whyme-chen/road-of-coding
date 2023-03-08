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

   * 虚拟机方式：

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

1. ls命令

   ![image-20221119130854252](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191352461.png)

2. cd命令

   ![image-20221119131441984](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191352647.png)

3. cat命令

   ![image-20221119131517425](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191352523.png)

4. more命令

   ![image-20221119131749688](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353211.png)

5. tail

   ![image-20221119132442044](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353220.png)

6. mkdir命令

   ![image-20221119132652551](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353925.png)

7. rmdir命令

   ![image-20221119132818838](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353381.png)

8. rm命令

   ![image-20221119132945812](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353834.png)

### 拷贝移动命令

1. cp命令

   ![image-20221119133232770](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353725.png)

2. mv命令

   ![image-20221119134054269](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353290.png)

### 打包压缩命令

1. tar命令 

   ![image-20221119134305526](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191353171.png)
   
   > cvf打包，xvf解包，zcvf打压缩包，zxvf解压包

### 文本编辑命令

1. vi/vim

   ![image-20221120202048921](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211202020494.png)

### 查找命令

1. find命令

   ![image-20221120203432544](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211202034929.png)

2. grep命令

   ![image-20221120203545011](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211202035320.png)

### 软件安装命令

1. 软件安装方式

   ![image-20221118231233904](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211182312501.png)
   
   * yum
   
     > 常用指令：
     >
     > yum list
     >
     > yum install
     >
     > yum remove
     >
     > 
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

### 项目部署

1. 手动部署

2. shell脚本部署

   ![image-20221120204540453](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211202045621.png)

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