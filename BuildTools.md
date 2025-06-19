# 基础理论

**构建是指将源代码和资源文件转换为可执行软件的过程**。构建工具的作用在于自动化和简化这一过程，使得开发人员能够更加高效地进行软件构建、测试和部署。

构建工具通常会执行以下任务：

1. **编译**：将源代码编译成目标代码，例如将Java文件编译成class文件。
2. **依赖管理**：管理项目所需的外部依赖库，确保项目能够顺利编译和运行。
3. **单元测试**：运行项目中的单元测试，并生成测试报告以供开发人员查看。
4. **打包**：将编译后的代码和依赖打包成可执行的应用程序或者库文件。
5. **文档生成**：根据代码中的注释生成项目文档，方便团队成员理解和使用代码。
6. **静态代码分析**：对代码进行静态分析，寻找潜在的问题和优化点。
7. **发布部署**：将构建好的软件发布到指定的环境中，可以是测试环境、预生产环境或者生产环境。

Java项目的构建经历了三个时代：

* Apache Ant（2000 年左右）
* Maven（2004年）
* Gradle（2012 年左右），Gradle 相比于 Maven 配置更加简单、性能更高、用户体验更好（IDE 支持代码提示）。

![image-20240324213933631](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202403242139828.png)

+++

Gradle 和 Maven 都是流行的构建工具，用于构建、管理和部署Java项目，它们有一些区别：

1. 语法：Maven使用XML作为其构建文件的语法，而Gradle使用Groovy或Kotlin脚本。这使得Gradle的构建脚本更加简洁和易读。

2. 灵活性：Gradle提供了更大的灵活性和定制化能力，可以更轻松地定制构建过程和任务。Maven的约定优于配置的原则可能会限制一些特殊需求的实现。

3. 性能：一些基准测试显示，Gradle在构建大型项目时可能比Maven更快。这主要是因为Gradle允许并行执行任务，而Maven则是基于阶段顺序执行。

4. 社区支持：由于Maven比Gradle存在更长的历史，因此拥有更多的成熟插件和更广泛的社区支持。但Gradle也在不断发展壮大，并且吸引了越来越多的用户和贡献者。

总的来说，选择使用Maven还是Gradle取决于个人偏好，项目需求以及团队的技术栈和经验。两者都是优秀的构建工具，都能够满足大多数Java项目的构建需求。

# Make

GUN Make官网：https://www.gnu.org/software/make/

CMake官网：https://cmake.org/

参考：

* GNU Make Manual: https://www.gnu.org/software/make/manual/
* CMake官方文档: https://cmake.org/documentation/
* Makefile Tutorial: https://makefiletutorial.com/
* [20分钟Makefile光速入门教程](https://www.bilibili.com/video/BV1tyWWeeEpp/?spm_id_from=333.1245.0.0&vd_source=fabefd3fabfadb9324761989b55c26ea)

## 概述

Make是一个自动化构建工具，它通过读取Makefile文件中的规则来执行编译、链接等操作。Makefile是一个文本文件，包含了一系列的规则，用来告诉Make程序如何编译和链接程序。

1. 为什么需要Make

   * 自动化构建：避免手动执行编译命令
   * 只重新编译修改过的文件，节省时间
   * 管理复杂项目的依赖关系
   * 标准化构建流程

2. 安装Make

   在大多数Linux发行版中，Make已经预装。如果没有，可以通过以下命令安装：

   ```bash
   # Ubuntu/Debian
   sudo apt-get install make
   
   # CentOS/RHEL
   sudo yum install make
   
   # macOS
   brew install make
   ```

3. 工具对比

   | 工具   | 优点                         | 缺点                     | 适用场景                  |
   | ------ | ---------------------------- | ------------------------ | ------------------------- |
   | Make   | 简单直接、历史悠久、广泛支持 | 跨平台支持较弱、语法较老 | C/C++项目、Unix/Linux系统 |
   | CMake  | 跨平台、功能强大、现代语法   | 学习曲线较陡、配置复杂   | 跨平台C/C++项目           |
   | Ninja  | 构建速度快、配置简单         | 功能相对简单             | 大型项目、需要快速构建    |
   | Gradle | 功能丰富、插件生态好         | 资源消耗较大             | Java/Android项目          |
   | Maven  | 依赖管理强大、标准化         | 灵活性较差               | Java项目                  |

4. 使用建议

   * 项目规模较小或中等
   * 主要在Unix/Linux环境开发
   * 需要简单直接的构建流程
   * 团队熟悉Make语法
   * 项目依赖关系相对简单make hello



## 基础语法

### 基本规则

```makefile
target: prerequisites
    command
```

其中：

- target: 目标文件
- prerequisites: 依赖文件
- command: 要执行的命令（必须以Tab开头）

### 快速入门

最简单的Makefile

让我们从一个最简单的例子开始：

```makefile
hello:
    echo "Hello, World!"
```

~~~makefile
# 编译hello.c程序
hello: hello.c
    gcc hello.c -o hello

# 清理编译产物
clean:
    rm -f hello
~~~

运行方式：

```bash
make hello
```

### 变量使用

```makefile
# 定义变量
CC = gcc
CFLAGS = -Wall

# 使用变量
hello: hello.c
    $(CC) $(CFLAGS) -o hello hello.c
```

### 常用变量

Makefile中可以使用以下内置变量：

- `$@`: 目标文件名
- `$<`: 第一个依赖文件名
- `$^`: 所有依赖文件名
- `$?`: 比目标新的依赖文件列表

### 条件编译

```makefile
# 根据环境变量选择编译选项
ifeq ($(DEBUG),1)
    CFLAGS += -g -DDEBUG
else
    CFLAGS += -O2
endif
```

### 自动依赖生成

```makefile
# 使用gcc的-MM选项生成依赖
%.d: %.c
    @set -e; rm -f $@; \
    $(CC) -MM $(CFLAGS) $< > $@.$$$$; \
    sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
    rm -f $@.$$$$

# 包含所有依赖文件
-include $(SRC_FILES:.c=.d)
```

### 并行构建

```makefile
# 启用并行构建
MAKEFLAGS += -j$(shell nproc)

# 或者运行时指定
# make -j4
```

### 使用ccache加速编译

```makefile
# 使用ccache加速编译
CC = ccache gcc
```

## 实际示例

### 简单的C项目

```makefile
# 项目配置
CC = gcc
CFLAGS = -Wall

# 默认目标
all: hello

# 编译hello程序
hello: hello.c
    $(CC) $(CFLAGS) -o hello hello.c

# 清理编译产物
clean:
    rm -f hello

.PHONY: all clean
```

### 多文件C项目

```makefile
# 项目配置
CC = gcc
CFLAGS = -Wall -I./include
LDFLAGS = -L./lib

# 源文件和目标文件
SRCS = $(wildcard src/*.c)
OBJS = $(SRCS:.c=.o)
TARGET = myapp

# 默认目标
all: $(TARGET)

# 链接
$(TARGET): $(OBJS)
    $(CC) $(OBJS) -o $(TARGET) $(LDFLAGS)

# 编译
%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@

# 清理
clean:
    rm -f $(OBJS) $(TARGET)

.PHONY: all clean
```

### 常见问题与解决方案

缩进问题

```makefile
# 错误示例（使用空格）
target:
    command    # 错误：使用空格缩进

# 正确示例（使用Tab）
target:
    command    # 正确：使用Tab缩进
```

变量展开问题

```makefile
# 错误示例
VAR = $(shell echo "value")
TARGET = $(VAR)    # VAR可能未定义

# 正确示例
VAR := $(shell echo "value")    # 立即展开
TARGET := $(VAR)
```

### 基础C项目模板

```makefile
# 项目配置
PROJECT_NAME = myproject
VERSION = 1.0.0

# 目录结构
SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin
INC_DIR = include

# 编译选项
CC = gcc
CFLAGS = -Wall -I$(INC_DIR)
LDFLAGS = -L$(LIB_DIR)

# 源文件
SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

# 目标文件
TARGET = $(BIN_DIR)/$(PROJECT_NAME)

# 默认目标
all: directories $(TARGET)

# 创建目录
directories:
    @mkdir -p $(BIN_DIR) $(OBJ_DIR)

# 编译
$(TARGET): $(OBJS)
    $(CC) $(OBJS) -o $@ $(LDFLAGS)

# 对象文件
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
    $(CC) $(CFLAGS) -c $< -o $@

# 清理
clean:
    rm -rf $(BIN_DIR) $(OBJ_DIR)

.PHONY: all clean directories
```

# Maven

官网：https://maven.apache.org

中央仓库：[Maven Repository: Search/Browse/Explore](https://mvnrepository.com/)

其他仓库：

* https://central.sonatype.com/

参考资料：

* [Maven项目构建](https://pdai.tech/md/devops/tool/tool-maven.html)
* [Maven快速入门-慕课](http://www.imooc.com/wiki/mavenlesson/mavenintroduction.html)

## 简介

**Maven是一个用于构建和管理Java项目的强大工具**。它提供了一种标准化的项目结构、依赖管理、构建过程自动化等功能，极大地简化了Java项目的开发和维护。maven本质是一个项目管理工具，将项目开发和管理过程抽象为一个项目对象模型（POM）。

1. 重要概念：
   * 项目对象模型（POM）：在项目中通常表现为pom.xml文件
   * 坐标
   * 仓库
   * 依赖管理（Dependency）
   * 生命周期与插件
2. 作用：

   * 项目构建
     * 构建（Build）是指将源代码转换为可执行的软件应用或部署包的过程。
     * 构建过程通常包括编译源代码、运行测试、打包生成可执行文件或库，以及其他必要的步骤。
   * 统一开发结构
   * 依赖的管理
3. 同类型工具
   * Ant
   * Maven
   * Gradle

![image-20211003195950696](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211003195950696.png)

## 安装与项目创建

### 安装

#### 流程

* 安装JDK（Maven是使用java开发的工具）
* 下载Maven压缩包，并解压到目标目录
* 环境配置
  * 系统变量，变量名：MAVEN_HOME
  * 系统变量，路径：maven所在目录
  * path变量中，添加%MAVEN_HOME%\bin
* 安装确认：命令行中输入mvn -v

#### 安装包目录结构

~~~
│  LICENSE
│  NOTICE
│  README.txt
│
├─bin // 包含了 Maven 的可执行文件，例如mvn命令
├─boot // 包含了 Maven 启动时所需的库文件，例如 Maven 的启动器和类加载器
├─conf // 包含了 Maven 的配置文件，例settings.xml。
│  │  settings.xml // 用于配置 Maven 的全局设置、代理、镜像等。
│  │  toolchains.xml
│  └─logging
│          simplelogger.properties
└─lib // 包含了 Maven 运行时所需的库文件
~~~

### 项目创建

#### 项目标准目录结构

~~~
project
├── src
│   ├── main
│   │   ├── java        # 主程序代码
│   │   ├── resources   # 资源文件
│   │   └── webapp      # Web 应用程序，页面资源（js,css,图片等资源）
│   └── test
│       ├── java        # 测试代码
│       └── resources   # 测试资源文件
├── target              # 构建输出目录
├── pom.xml             # Maven 配置文件
└── README.md           # 项目说明文档

~~~

,![image-20211001224629124](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211001224629124.png)

#### 项目创建

1. 手工制作

2. 使用插件创建工程

   ![image-20211004153002024](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211004153002024.png)

3. idea工具创建

   * 不使用骨架

     * java项目

     * web项目

       * 添加tomacat插件

   * 使用骨架

     * java项目

     * web项目

       * 添加tomcat插件

## POM与配置

1. 项目对象模型（POM）：在项目中通常表现为pom.xml文件，描述了该项目的方方面面。

2. 坐标：被Maven管理的资源的唯一标识

   * groupid：组织名称，通常为组织的逆向域名

   * atifactid：模块名称，该组织下项目的唯一标识

   * version：版本号，SNAPSHOT 则是用来标记项目过程中的快照版本，该版本类型表明本项目不是稳定版本，常见的还有 RELEASE，则表示该版本为本项目的稳定版本。通常情况下，Maven 的版本号约定中包括如下几个部分：

     **<主版本号>.<次版本号>.<增量版本号>.<里程碑版本号>**

     - **主版本号**：主版本号表示该项目的重大升级。例如：Maven1 到 Maven2；
     - **次版本号**：表示在该主版本下，较大范围的升级或变化。例如：Maven-3.0 到 Maven-3.1；
     - **增量版本号**：增量版本通常是用来修复bug的版本。例如：Maven-3.1.1；
     - **里程碑版本号**：用来标记里程碑版本。例如：Maven-3.0-alpha-3。

   - package：定义该项目的打包方式（**不是maven坐标的组成**）。常见的有jar和war两种方式，一般Web项目的打包方式为war。

   ~~~xml
     <groupId>org.example</groupId>
     <artifactId>demo-maven</artifactId>
     <version>1.0.0-SNAPSHOT</version>
     <packaging>jar</packaging>
   ~~~

3. `pom.xml`

   `pom.xml`文件的常见的元素标签有：

   * `build`：用于配置项目构建相关的内容，可以设置以下内容：
     * `<sourceDirectory>`: 指定项目的源代码目录，默认为 `src/main/java`。
     * `<testSourceDirectory>`: 指定测试代码的目录，默认为 `src/test/java`。
     * `<outputDirectory>`: 指定编译后的类文件输出目录，默认为 `target/classes`。
     * `<testOutputDirectory>`: 指定测试类编译后的输出目录，默认为 `target/test-classes`。
     * `<resources>`: 配置项目资源文件的位置，如配置文件、静态资源等。
     * `<testResources>`: 配置测试资源文件的位置。
     * `<plugins>`: 配置插件，如编译插件、打包插件等。
   * `reporting`：站点生成相关

4. 超级POM

   所有使用Maven创建的项目其pox.xml都会继承一个超级POM，该POM所在路径`%Maven安装目录\lib\maven-model-builder-3.9.2.jar\org\apache\maven\model\pom-4.0.0.xml`中（可使用解压工具打开该jar包），Maven-3.9.2的superpom内容如下：

   ~~~xml
   This XML file does not appear to have any style information associated with it. The document tree is shown below.
   <!-- 
   Licensed to the Apache Software Foundation (ASF) under one
   or more contributor license agreements.  See the NOTICE file
   distributed with this work for additional information
   regarding copyright ownership.  The ASF licenses this file
   to you under the Apache License, Version 2.0 (the
   "License"); you may not use this file except in compliance
   with the License.  You may obtain a copy of the License at
   
       http://www.apache.org/licenses/LICENSE-2.0
   
   Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.
    -->
   <!--  START SNIPPET: superpom  -->
   <project>
   <modelVersion>4.0.0</modelVersion>
   <repositories>
   <repository>
   <id>central</id>
   <name>Central Repository</name>
   <url>https://repo.maven.apache.org/maven2</url>
   <layout>default</layout>
   <snapshots>
   <enabled>false</enabled>
   </snapshots>
   </repository>
   </repositories>
   <pluginRepositories>
   <pluginRepository>
   <id>central</id>
   <name>Central Repository</name>
   <url>https://repo.maven.apache.org/maven2</url>
   <layout>default</layout>
   <snapshots>
   <enabled>false</enabled>
   </snapshots>
   <releases>
   <updatePolicy>never</updatePolicy>
   </releases>
   </pluginRepository>
   </pluginRepositories>
   <build>
   <directory>${project.basedir}/target</directory>
   <outputDirectory>${project.build.directory}/classes</outputDirectory>
   <finalName>${project.artifactId}-${project.version}</finalName>
   <testOutputDirectory>${project.build.directory}/test-classes</testOutputDirectory>
   <sourceDirectory>${project.basedir}/src/main/java</sourceDirectory>
   <scriptSourceDirectory>${project.basedir}/src/main/scripts</scriptSourceDirectory>
   <testSourceDirectory>${project.basedir}/src/test/java</testSourceDirectory>
   <resources>
   <resource>
   <directory>${project.basedir}/src/main/resources</directory>
   </resource>
   </resources>
   <testResources>
   <testResource>
   <directory>${project.basedir}/src/test/resources</directory>
   </testResource>
   </testResources>
   <pluginManagement>
   <!--  NOTE: These plugins will be removed from future versions of the super POM  -->
   <!--  They are kept for the moment as they are very unlikely to conflict with lifecycle mappings (MNG-4453)  -->
   <plugins>
   <plugin>
   <artifactId>maven-antrun-plugin</artifactId>
   <version>1.3</version>
   </plugin>
   <plugin>
   <artifactId>maven-assembly-plugin</artifactId>
   <version>2.2-beta-5</version>
   </plugin>
   <plugin>
   <artifactId>maven-dependency-plugin</artifactId>
   <version>2.8</version>
   </plugin>
   <plugin>
   <artifactId>maven-release-plugin</artifactId>
   <version>2.5.3</version>
   </plugin>
   </plugins>
   </pluginManagement>
   </build>
   <reporting>
   <outputDirectory>${project.build.directory}/site</outputDirectory>
   </reporting>
   <profiles>
   <!--  NOTE: The release profile will be removed from future versions of the super POM  -->
   <profile>
   <id>release-profile</id>
   <activation>
   <property>
   <name>performRelease</name>
   <value>true</value>
   </property>
   </activation>
   <build>
   <plugins>
   <plugin>
   <inherited>true</inherited>
   <artifactId>maven-source-plugin</artifactId>
   <executions>
   <execution>
   <id>attach-sources</id>
   <goals>
   <goal>jar-no-fork</goal>
   </goals>
   </execution>
   </executions>
   </plugin>
   <plugin>
   <inherited>true</inherited>
   <artifactId>maven-javadoc-plugin</artifactId>
   <executions>
   <execution>
   <id>attach-javadocs</id>
   <goals>
   <goal>jar</goal>
   </goals>
   </execution>
   </executions>
   </plugin>
   <plugin>
   <inherited>true</inherited>
   <artifactId>maven-deploy-plugin</artifactId>
   <configuration>
   <updateReleaseInfo>true</updateReleaseInfo>
   </configuration>
   </plugin>
   </plugins>
   </build>
   </profile>
   </profiles>
   </project>
   <!--  END SNIPPET: superpom  -->
   ~~~

   通常情况下子POM（我们的项目）会覆盖父POM（superpom）中的元素，但是对于一下元素，并不会直接覆盖而是追加。

   - dependencies
   - developers 和 contributors
   - plugins
   - resources

### 依赖管理

官网参考：https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html

1. 依赖配置

   * 依赖：当前项目运行所需要的的jar，一个项目可以设置多个依赖
   * 依赖原则：
     * 路径最短优先原则
     * 声明顺序优先（最先声明的优先）
     * 覆写优先：子 POM 内声明的依赖优先于父 POM 中声明的依赖

   ~~~xml
   <!-- 所有当前项目依赖的所有jar-->
   <dependencies>
       <!-- 具体的依赖-->
       <dependency>
           <groupId><groupId/>
           <artifacted></artifacted>
           <version></version>
      <dependency/>
   </dependencies>
   ~~~

2. 依赖传递

   * 直接依赖：在当前项目中通过依赖配置建立的依赖关系
   * 间接依赖：被资源的资源如果依赖其他资源，当前项目间接依赖其他资源

   ![image-20221120192641610](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211201928160.png)

3. 可选依赖：隐藏当前工程所依赖的资源，隐藏后将不存在传递依赖关系

   > 在依赖中添加选项
   >
   > <optional>true</optional>

4. 排除依赖：排除依赖指**主动断开依赖的资源**，被排除的资源无需指定版本

   ![image-20221120193000182](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211201930581.png)

5. 依赖范围

   依赖的jar默认在所有范围内均可使用，可以通过`scope`标签来设置其作用范围，其值共有6种：

   * compile：Maven 默认的依赖范围，该范围的依赖对编译，运行，测试时均生效
   * provided：对于编译和测试的 classpath 有效，但是在运行时无效
   * runtime
   * test
   * system
   * import

   作用范围：

   * 主程序范围有效（main文件夹范围内）
   * 测试程序范围有效（test文件夹范围内）
   * 是否参与打包（package指令范围内）

   ![image-20221120193408645](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211201934150.png)

   ![image-20221120193756025](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202211201937486.png)

### 聚合

通常情况下，我们在实际开发过程中，会对项目进行模块（module）划分，来提供项目的清晰度并且能够更加方便的重用代码。但是，在这种时候，我们在构建项目的时候就需要分别构建不同的模块，Maven 的聚合特性能够将各个不同的模块聚合到一起来进行构建。

1. 聚合：将多个模块组织成一个整体，同时进行项目构建的过程称为聚合

2. 聚合工程：通常是一个不具有业务功能的“空”工程(有且仅有一-个pom文件)

   ```xml
   设置打包类型为pom
   <packaging>pom</packaging>
   ```

3. 作用：使用聚合工程可以将多个工程编组，通过对聚合工程进行构建，实现对所包含的模块进行同步构建。当工程中某个模块发生更新(变更)时，必须保障工程中与已更新模块关联的模块同步更新，此时可以使用聚合工程来解决批量模块同步构建的问题

### 继承

1. 继承：描述的是两个工程间的关系，与java中的继承相似，子工程可以继承父工程中的配置信息，常见于依赖关系的继承

2. 作用：继承的特性，则能够帮助我们抽取各个模块公用的依赖、插件等，实现配置统一。

   * 简化配置
   * 减少版本冲突

3. 配置

   ![image-20230311153610754](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202303111536873.png)

   ![image-20230311153631641](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202303111536025.png)

   > 子工程中使用父工程中的可选依赖时，仅需要提供群组id和项目id,无需提供版本，版本由父工程统一提供, 避免版本冲突;子工程中还可以定义父工程中没有定义的依赖关系

4. 聚合与继承的区别

   ![image-20230311153848002](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202303111538349.png)

### 属性

1. 定义

   ![image-20230311154148318](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202303111542602.png)

2. 使用

   ![image-20230311154254533](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202303111542002.png)

3. 属性类型

   - **内置属性：** Maven 的内置属性主要有两个，一个是`${basedir}`用来表示项目的根目录，另一个是`${version}`用来表示项目的版本号；
   - **POM属性：** 用来引用 pom.xml 文件中对应元素的值。一般来说，可以用`${project.*}`来表示，例如：`${project.groupId}`就是用来表示项目的 groupId 信息；
   - **自定义属性：** 这个比较容易理解，就像我们上面例子中的`${spring.version}`就属于自定义属性的范围；
   - **Settings属性：** 与 POM 属性类似。通常使用`${settings.*}`来表示，Settings 属性用来指向 settings.xml 文件中的属性，例如：`${settings.localrepository}`可以用来表示本地仓库的地址；
   - **Java系统属性：** 所有 Java 的系统属性都可以通过 Maven 属性来引用。我们在使用之前可以通过`mvn help:system`命令来查看对应的属性；
   - **环境变量属性：** 所有的环境变量属性都可以通过 Maven 属性来引用。通常用 `${env.*}`来表示。

   ![image-20230311155756286](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202303111557875.png)


### 多环境开发

1. 设置多环境

   ![image-20230311160336493](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202303111603573.png)

2. 使用

   ![image-20230311160406503](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202303111604145.png)

### Maven仓库

![image-20211001222603530](https://cdn.jsdelivr.net/gh/whyme-chen/Image/imgimage-20211001222603530.png)

* 本地仓库：默认情况下，本地仓库位于用户目录下的`.m2/repository`目录中。可以在maven安装目录中找到conf\settings.xml更改如下标签中的路径位置来修改本地仓库地址。

  ~~~xml
  <localRepository>xxxx</localRepository>
  ~~~

* 远程仓库

  * 中央仓库：中央仓库是 Maven 的默认远程仓库，包含了大量常用的开源依赖。默认情况下Maven 会根据依赖的坐标信息从中央仓库下载相应的依赖。

  * 镜像仓库：指与原始仓库具有相同内容的一种替代仓库。当 Maven 访问远程仓库时，它会首先检查是否配置了镜像仓库，如果有，则会直接从镜像仓库下载依赖，而不是访问原始仓库。镜像仓库的配置位于 Maven 的 `settings.xml` 文件中。国内几个常用的仓库镜像：

    ~~~xml
    <!--阿里云镜像-->
    <mirror>
        <id>alimaven</id>
        <name>aliyun maven</name>
        <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
        <mirrorOf>central</mirrorOf>
    </mirror>
    <!--阿里巴巴镜像-->
    <mirror>
        <id>ibiblio</id>
        <mirrorOf>central</mirrorOf>
        <name>Human Readable Name for this Mirror.</name>
        <url>http://mirrors.ibiblio.org/pub/mirrors/maven2/</url>
    </mirror>
    <!--repo2镜像-->
    <mirror>  
        <id>repo2</id>  
        <mirrorOf>central</mirrorOf>  
        <name>Human Readable Name for this Mirror.</name>
        <url>http://repo2.maven.org/maven2/</url>  
    </mirror>
    ~~~

  * 私服：私服是一台独立的服务器，用于解决团队内部的资源共享与资源同步问题

    学习参考视频：https://www.bilibili.com/video/BV1Fi4y1S7ix/?p=89&spm_id_from=pageDriver&vd_source=fabefd3fabfadb9324761989b55c26ea

    Nexus：

    * Sonatype公司的一款maven私服产 品

    * 地址: https://help.sonatype.com/repomanager3/download

    * 安装与启动

      ![image-20230311161230165](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202303111612698.png)

    私服仓库分类

    ![image-20230311161652945](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202303111616037.png)

#### 依赖搜索顺序

参考：https://mp.weixin.qq.com/s/pFKCBmQfzRGAZD3cDxDUjQ

### 配置

1. 环境变量
   * `MAVEN_OPTS`
   * `MAVEN_ARGS`：自maven3.9.0开始
2. 配置文件
   * `settings.xml`
     * 位于`USER_HOME`/.m2，用于配置使用maven的任何配置
3. 配置目录
   * `.mvn`
     * 位于项目根目录下，包含项目特定的maven运行配置。
     * 通常可以包含：
       * `maven.config`
       * `jvm.config`
       * `extensions.xml`
     * 该目录是项目的一部分，可以加入到git等版本控制中进行管理

## 生命周期与插件

在Maven中，构建是通过执行一系列定义在POM文件中的生命周期和阶段来完成的。每个构建过程都有其对应的生命周期，而每个生命周期又由一系列的阶段组成。

通过定义和配置POM文件中的插件，可以扩展或自定义构建过程。Maven提供了大量的插件，可以用来执行其他任务，如代码静态分析、文档生成、资源文件处理等。

### 生命周期

Maven 定义了一套标准的构建生命周期，每个生命周期由一系列固定顺序的阶段（phase）组成。主要划分为以下3个阶段：

**clean**：清理工作

![image-20230217162630995](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171626834.png)

**default**：核心工作，例如：编译，测试，打包，部署等

![image-20230217162710233](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171627097.png)

**site**：产生报告，发布站点等

![image-20230217162747671](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171627448.png)

### 插件

1. 插件（plugin）

   **生命周期只是一个抽象的模型，其本身并不会直接去做事情，真正帮我们完成事情的是 Maven 的插件。**Maven 的插件也属于构件的一种，也是可以放到 Maven 仓库当中的。通常情况下，一个插件可以做 A、B、C 等等不止一件事情，但是我们又没有必要为每一个功能都做一个单独的插件。这种时候，我们一般会给这个插件绑定不同的目标（goal），而这些目标则是对应其不同的功能。它代表了该插件可以执行的具体任务或操作。每个目标都有一个唯一的标识符，例如 `compile`、`test`、`package` 等。

   当在 Maven 中运行某个插件时，通常需要指定要执行的目标。例如，想编译项目，就会使用 Maven Compiler 插件的 `compile` 目标；想打包项目，就会使用 Maven Jar 插件的 `jar` 目标。执行命令的格式通常如下：`mvn pluginName:goalName`。例如当我们执行`dependency`插件的 list 目标的时候，我们可以执行命令：`mvn dependency:list`。

   ![image-20230217163459866](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171635337.png)

2. 插件类型

3. 自定义插件

   > 一般情况下不需要自定义插件，自定义插件可参考：[Maven编写插件](http://www.imooc.com/wiki/mavenlesson/mavenPlugin.html)

## `mvn`命令

语法格式：

```shell
mvn [options] [<goal(s)>] [<phase(s)>]
```

常用命令：

~~~shell
# 使用archetype插件创建maven项目
mvn archetype:generate
# 格式检查
mvn checkstyle:check
# 清理
mvn clean
# 验证项目是否正确、所有必要信息是否可用
mvn validate
# 编译项目的源代码
mvn compile
# 使用适当的单元测试框架测试已编译的源代码
mvn test
# 运行任何检查，以验证包是否有效并符合质量标准。
mvn verify
# 将编译后的代码打包成可分发的格式（比如 JAR、WAR）
mvn package
# 将包安装到本地仓库中，以供其他项目使用
mvn install
# 将最终的包复制到远程仓库中，以共享给其他开发者和项目
mvn deploy
~~~

命令具体执行流程：（`mvn complie`为例）

1. **读取 POM 文件**：

   - Maven 从当前目录开始，向上查找并读取 `pom.xml` 文件，这是项目的配置文件。
   - 解析 `pom.xml` 中定义的项目信息、依赖、插件和构建配置。

2. **依赖解析**：

   - Maven 根据 `pom.xml` 中定义的依赖，从本地仓库或远程仓库下载所需的依赖包。
   - 将这些依赖包添加到构建路径中，以便在接下来的编译过程中使用。

3. **执行生命周期阶段**：

   - 虽然运行的是 `compile` 阶段，Maven 会自动执行所有在 `compile` 阶段之前的阶段。这意味着会按顺序执行 `validate` 和 `compile` 阶段。

   - 在 `compile` 阶段，实际执行编译任务的是 `maven-compiler-plugin` 插件。该插件默认使用 `javac` 编译器，并根据你的 `pom.xml` 中的配置（如 Java 版本）来调整编译参数。以下是一个典型的 Maven Compiler 插件配置示例：

     ```xml
     <!-- 在这个配置中，指定了 Java 源代码和目标字节码的版本为 1.8。 -->
     <build>
       <plugins>
         <plugin>
           <groupId>org.apache.maven.plugins</groupId>
           <artifactId>maven-compiler-plugin</artifactId>
           <version>3.8.1</version>
           <configuration>
             <source>1.8</source>
             <target>1.8</target>
           </configuration>
         </plugin>
       </plugins>
     </build>
     ```

4. **编译源代码**：

   - Maven 使用 `maven-compiler-plugin` 插件的 `compile` 目标来编译 `src/main/java` 目录中的 Java 源文件。
   - 编译后的字节码文件将被输出到 `target/classes` 目录中。

## IDE集成

参考：https://www.jetbrains.com/help/idea/maven.html

## Maven Archetype原型

参考：

* https://baijiahao.baidu.com/s?id=1722242604793241553&wfr=spider&for=pc
* https://blog.csdn.net/weixin_54792520/article/details/121802898

1. 概念

   Maven官网对于Archetype的解释如下：

   > In short, Archetype is a Maven project templating toolkit. An archetype is defined as *an original pattern or model from which all other things of the same kind are made*. The name fits as we are trying to provide a system that provides a consistent means of generating Maven projects. Archetype will help authors create Maven project templates for users, and provides users with the means to generate parameterized versions of those project templates.

# Gradle

官网：https://gradle.org/

参考：

* [Gradle User Manual](https://docs.gradle.org/8.6/userguide/userguide.html)&[安装 Gradle_Gradle中文网 (github.net.cn)](https://gradle.github.net.cn/userguide/installation.html#ex-installing-manually)
* https://www.bilibili.com/video/BV1yT41137Y7/?p=1
* [gradle使用教程，小白一篇就够](https://blog.csdn.net/hai411741962/article/details/133068125)

## 简介

1. 发展

   2012 年 Google 推出的基于 Groovy 语言的全新项目构建工具，集合了 Ant 和 Maven 各自的优势。

2. 优点&缺点

   * 集 Ant 脚本的灵活性+Maven 约定大于配置的项目目录优势,支持多种远程仓库和插件,侧重于大项目构建。
   * 学习成本高、资料少、脚本灵活、版本兼容性差等。
   
3. 基本概念

   ![gradle basic 1](https://docs.gradle.org/current/userguide/img/gradle-basic-1.png)

   * `project`：可以是单项目，也可以包含多个子项目
   * `build.gradle`
   * `dependency`
   * `task`：一个基本的工作单元，例如编译代码或运行测试。
   * `plugin`：Gradle中的插件是一种扩展机制，允许您在构建过程中引入额外的功能或任务。它们通常用于将常见任务封装为可重用的组件，或者用于添加特定领域的功能，如Android应用程序开发或Java库构建。

## 安装

参考：[Gradle安装与配置教程（Windows版） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/626806226)

1. 安装jdk
2. 下载并解压gradle
3. 配置环境变量
   * `GRADLE_HOME`
   * `GRADLE_USER_HOME`
4. 检测安装
5. 配置国内maven源
   * `init.d`文件夹：可以在gradle的`init.d`目录下创建以`.gradle`结尾的文件，以实现在build开始之前进行一些预操作。
   * 启用`init.gradle`文件
     * 使用命令行指定
     * 把`init.gradle`文件放到USER_HOME/.gradle/目录下
     * 把以`.gradle`文件放到USER_HOME/.gradle/init.d目录下
     * 把以`.gradle`文件放到GRADLE_HOME/init.d目录下

## 项目目录与创建

Gradle项目默认目录结构和 Maven 项目的目录结构一致,都是基于约定大于配置。完整目录结构如下：

![image-20240324215519694](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202403242155882.png)

在项目中使用gradle主要有两种方式：

* 集成IDE
* 命令行，如[使用`gradle init`命令创建gradle项目](https://docs.gradle.org/current/userguide/part1_gradle_init.html#part1_gradle_init)

## Wrapper

1. 作用：Gradle Wrapper 实际上就是对 Gradle的一层包装,用于解决实际开发中可能会遇到的不同的项目需要不同版本的 Gradle问题。例如：把自己的代码共享给其他人使用，可能出现如下情况:

   * 对方电脑没有安装 Gradle
   * 对方电脑安装过 gradle，但是版本太旧了

   这时候，我们就可以考虑使用 Gradle Wrapper 了。这也是官方建议使用 Gradle Wrapper 的原因。实际上有了 GradleWrapper 之后，我们本地是可以不配置 Gradle的,下载 Gradle项目后，使用 gradle项目自带的 wrapper 操作也是可以的。

2. 使用 Gradle wrapper
   项目中的`gradlew`、`gradlew.cmd`脚本用的就是wrapper中规定的gradle版本。而我们上面提到的gradle指令用的是本地gradle，所以gradle指令和gradlew指令所使用的gradle版本有可能是不一样的，`gradlew`，`gradlew.cmd`的使用方式与gradle使用方式完全一致。只不过把gradle指令换成了gradlew指令。

3. gradkew 指令参数：

   指定一些参数,来控制 Wrapper 的生成，比如依赖的版本等，如下:
   
4. `gradle-wrapper.properties`：用于配置 Gradle Wrapper 的属性文件，通常位于项目中的 `gradle/wrapper/` 目录下。以下是一些常见的参数以及它们的作用：

   * `distributionBase`：指定 Gradle 发行版的基本目录，用于缓存 Gradle 发行版的位置。
   * `distributionPath`：指定从哪里下载 Gradle 发行版的相对路径。默认情况下是 `wrapper/dists`。
   * `zipStoreBase`：指定存储 Gradle 压缩文件的基本目录。
   * `zipStorePath`：指定存储 Gradle 压缩文件的相对路径。默认情况下是 `wrapper/dists`。
   * `distributionUrl`：指定要下载的 Gradle 发行版的 URL。这是 `gradle-wrapper` 脚本用来下载 Gradle 发行版的地址。

   ~~~properties
   # 解压缩后存放地址
   distributionBase=GRADLE_USER_HOME
   distributionPath=wrapper/dists
   distributionUrl=https\://services.gradle.org/distributions/gradle-8.6-bin.zip
   networkTimeout=10000
   validateDistributionUrl=true
   # 下载后压缩包存放地址
   zipStoreBase=GRADLE_USER_HOME
   zipStorePath=wrapper/dists
   ~~~

   > 若没有配置`GRADLE_USER_HOME`环境变量，则默认为`用户目录/.gradle`目录下

5. 执行流程

   下载发行版-》存储并解压发行版-》使用发行版

6. wrapper使用建议

   * 新建一个新项目时:使用gradle指令即可
   * 下载别人的项目或者使用操作以前自己写的不同版本的gxadle项目时:用Gradle wrapper,也即:gradlew

## 命令行

命令格式：

```shell
gradle [taskName...] [--option-name...]
```

1. **gradle build**：执行项目的构建过程，包括编译源代码、运行单元测试、打包生成可执行文件等。
2. **gradle clean**：清理项目构建过程中生成的临时文件和输出文件，以便重新开始新的构建。
3. **gradle tasks**：列出项目中所有可执行的任务，包括默认任务和自定义任务，以方便查看可执行的任务列表。
4. **gradle dependencies**：显示项目的依赖关系，包括外部库和模块之间的依赖关系。
5. **gradle test**：运行项目中的测试用例，检查代码的正确性和稳定性。
6. **gradle run**：运行项目的主类或指定的 Java 应用程序，用于快速启动项目并进行调试。
7. **gradle help**：获取帮助信息，显示 Gradle 命令的用法和选项说明。
8. **gradle wrapper**：生成 Gradle Wrapper 文件，用于在没有预先安装 Gradle 的环境中构建项目。
9. **gradle eclipse**：生成 Eclipse 项目文件，用于导入 Gradle 项目到 Eclipse IDE 中进行开发。
10. **gradle idea**：生成 IntelliJ IDEA 项目文件，用于导入 Gradle 项目到 IntelliJ IDEA IDE 中进行开发。

## 脚本文件

### `settings.gradle`

> `settings.gradle`是每个Gradle项目的入口点

1. 主要作用：

   * 管理子项目，对于单项目构建，设置文件是可选的。对于多项目构建，设置文件是强制性的，并声明所有子项目。
   * 管理项目的一些基本信息

2. 配置内容：支持groovy和kotlin语言进行编写

   ~~~groovy
   rootProject.name = 'root-project'   
   
   include('sub-project-a')            
   include('sub-project-b')
   include('sub-project-c')
   ~~~

### `build.gradle`

1. 作用：详细描述了构建配置、任务和插件

2. 内容：常用的包括插件的使用，依赖管理（本项目依赖的jar包，插件，库和源代码，主要分为Gradle和构建脚本依赖的库或插件，项目源(即源代码)所依赖的库两部分）

   * **repositories（仓库）**：
     - 作用：定义了项目所需的依赖项存储位置。
     - 使用：您可以指定从哪些仓库下载依赖项，例如Maven中央仓库、本地文件系统或自定义的远程仓库。
   * **dependencies（依赖项）**：
     - 作用：定义了项目所需的外部依赖项。
     - 使用：您可以指定项目所需的各种依赖项，包括库、框架和其他项目。
     - 配置项：Gradle中的依赖项是按配置分组的
       - **implementation（实现）**：
         - 作用：指定项目的主要依赖项，这些依赖项会被传递到项目的编译路径中。
         - 使用：通常用于指定项目的核心依赖，如库、框架等。
       - **api**：
         - 作用：与`implementation`类似，指定项目的主要依赖项，但这些依赖项会被传递到依赖该项目的其他模块中。
         - 使用：适用于构建库或框架时，希望将依赖项暴露给其他模块使用。
       - **compileOnly**：
         - 作用：指定在编译时需要依赖的项，但在运行时不需要。
         - 使用：通常用于编译期间需要使用但不需要打包到最终产物中的依赖，例如编译时需要的API或接口。
       - **runtimeOnly**：
         - 作用：指定只在运行时需要的依赖项，这些依赖项不会被传递到编译路径中。
         - 使用：适用于仅在运行时需要使用的依赖，例如运行时需要的数据库驱动。
       - **testImplementation**：
         - 作用：指定测试代码所需的依赖项，这些依赖项只会在测试编译和执行过程中使用。
         - 使用：用于指定测试时需要的库或框架。
       - **androidTestImplementation**（适用于Android项目）：
         - 作用：指定Android项目中的UI测试所需的依赖项。
         - 使用：用于指定在运行Android UI测试时所需的库或框架。
   * **plugins（插件）**：
     - 作用：定义了项目中使用的Gradle插件。
     - 使用：您可以在这里声明您需要使用的插件，并指定其版本和其他相关配置。
   * **sourceSets（源集）**：
     - 作用：定义了项目源代码的布局和结构。
     - 使用：您可以在这里指定不同的源代码集合，例如主源代码、测试代码等，并配置它们的路径和文件夹结构。
   * **tasks（任务）**：
     - 作用：定义了项目中可执行的任务。
     - 使用：您可以在这里声明和配置各种任务，例如编译代码、运行测试、打包应用程序等。
   * **buildScript（构建脚本）**：
     - 作用：定义了项目构建过程中使用的Gradle构建脚本。
     - 使用：您可以在这里配置构建脚本的参数和行为，例如依赖项的管理和版本控制。
   * **publishing（发布）**：
     - 作用：定义了项目的发布配置。
     - 使用：您可以在这里配置项目的发布方式和目标，例如将构建产物发布到远程仓库。
   * **buildTypes（构建类型）**（主要用于Android项目）：
     - 作用：定义了不同构建类型的配置。
     - 使用：您可以在这里指定不同构建类型的参数和行为，例如Debug构建和Release构建。

   ~~~groovy
   plugins {
       // 添加插件application
       id 'application'                
   }
   
   // 定义插件application中的约定属性
   application {
       mainClass = 'com.example.Main'  
   }
   
   dependencies {
       // Dependency on a remote binary to compile and run the code
       implementation(libs.googleMaterial)    
   
       // Dependency on a remote binary to compile and run the test code
       testImplementation(libs.mockitoCore)   
   }
   ~~~

### `libs.versions.toml`

1. 位置：`gradle\libs.versions.toml`（该文件应该被加入到版本控制中）
2. 作用：在多个子项目中共享依赖项和版本配置以及在大型项目中强制限定依赖库和插件的版本

## 任务&插件

1. 任务：表示构建执行的一些独立的工作单元，例如编译类、创建JAR、生成Javadoc或将存档发布到存储库。任务间可以相互依赖。
2. 插件：应用到Gradle构建脚本中，以添加新的任务、配置或其他与构建相关的功能:
3. 插件的三种类型（分发形式）
   * **Core plugins** - Gradle develops and maintains a set of [Core Plugins](https://docs.gradle.org/current/userguide/plugin_reference.html#plugin_reference).
     * 例如：`java`，`groovy`，`ear`
   * **Community plugins** - Gradle’s community shares plugins via the [Gradle Plugin Portal](https://plugins.gradle.org/).
     * 例如：[Spring Boot Gradle plugin](https://plugins.gradle.org/plugin/org.springframework.boot)
   * **Local plugins** - Gradle enables users to create custom plugins using [APIs](https://docs.gradle.org/current/javadoc/org/gradle/api/Plugin.html).

### 自定义插件

## 依赖管理

## 增量构建&缓存

1. 开启详细构建日志

   ~~~
   ./gradlew compileJava --console=verbose
   ~~~

   使用`--console=verbose`参数可以在以前执行过且未更改的任务时，在任务旁边打印 `UP-TO-DATE` 

## 项目部署

### 基本部署

### Gretty插件

Gretty官网：http://akhikhl.github.io/gretty-doc/index.html

1. **添加 Gretty 插件**：首先，在您的 Gradle 项目中的 `build.gradle` 文件中添加 Gretty 插件的依赖：

   ~~~groovy
   Codeplugins {
       id 'org.akhikhl.gretty' version 'X.X.X'
   }
   ~~~

   确保将 `'X.X.X'` 替换为适当的 Gretty 版本号。

2. **配置 Gretty 插件**：在 `build.gradle` 文件中添加 Gretty 插件的配置，根据需要配置端口号、上下文路径等参数。例如：

   ~~~groovy
   Codegretty {
       servletContainer = 'jetty9' // 使用 Jetty 9 作为 Servlet 容器
       port = 8080 // 指定端口号
   }
   ~~~

## DSL

Gradle DSL（Domain Specific Language）是 Gradle 构建工具使用的一种领域特定语言，**用于描述构建脚本和项目配置**。

Gradle 构建脚本通常使用 Groovy 或 Kotlin 语言编写，并且遵循特定的语法规则和约定。通过 Gradle DSL，开发者可以定义项目的依赖关系、任务和插件等信息，以及指定构建过程中的各种行为和配置。例如：

1. 定义依赖关系：使用 `dependencies { }` 块来指定项目所依赖的外部库或模块。
2. 配置任务：使用任务名称加上配置块的方式，如 `task myTask { }`，来配置任务的行为和属性。
3. 应用插件：使用 `apply plugin: 'pluginName'` 来应用 Gradle 插件，以扩展项目的构建功能。
4. 自定义函数和扩展：开发者可以编写自定义函数和扩展，以便在构建脚本中重用代码逻辑。

Gradle DSL 提供了灵活、强大的方式来管理项目的构建过程，并且允许开发者根据项目的需要进行定制和扩展。

### Kotlin

> 具体参考：[Kotlin](./Kotlin)

### Groovy

> 具体参考：[Groovy](./Groovy.md)

## 生命周期

* **插件引入:声明你所需的插件
  **
* **属性定义(可选):定义扩展属性
  **
* **局部变量(可选):定义局部变量
  **
* **属性修改(可选):指定project自带属性
  **
* **仓库定义:指明要从哪个仓库下载jar包
  **
* **依赖声明:声明项目中需要哪些依赖
  **
* **自定义任务(可选):自定义一些任务**

## IDEA集成

参考：[Gradle | IntelliJ IDEA Documentation (jetbrains.com)](https://www.jetbrains.com/help/idea/gradle.html)

# Webpack

# 常用镜像源

* 阿里云：https://maven.aliyun.com/mvn/guide
* 华为云：https://mirrors.huaweicloud.com/
* 腾讯云：https://mirrors.cloud.tencent.com/
* 清华源：https://mirrors.tuna.tsinghua.edu.cn/
* 中科大源：https://mirrors.ustc.edu.cn/
* 网易源：https://mirrors.163.com/
* 搜狐源：https://mirrors.sohu.com/
