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

## Linux常用命令

1. 常用命令

   * ls
   * pwd
   * cd
   * touch
   * mkdir
   * rm

   ![image-20221119125002051](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191352847.png)

2. 命令格式

   > command [-options] [parameter]

   ![image-20221119130139264](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211191352141.png)

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