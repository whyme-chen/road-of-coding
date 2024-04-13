# 前期准备

> 本次源码阅读spring-framework版本为v6.1.5

参考：

* [Spring Framework（6.x）源码编译与源码阅读入门](https://blog.csdn.net/qq_25409421/article/details/135991212?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-135991212-blog-127945857.235%5Ev43%5Epc_blog_bottom_relevance_base5&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-135991212-blog-127945857.235%5Ev43%5Epc_blog_bottom_relevance_base5&utm_relevant_index=5)
* [在windows10使用Gradle编译Spring源码](https://blog.csdn.net/qq_34738512/article/details/129747004)

1. Spring源码获取

   - github：https://github.com/spring-projects/spring-framework
- gitee：https://gitee.com/mirrors/Spring-Framework
  
2. 构建工具：**gradle**下载、安装及使用

   构建是指将源代码转换为可执行软件的过程。构建工具的作用在于自动化和简化这一过程，使得开发人员能够更加高效地进行软件构建、测试和部署。

   构建工具通常会执行以下任务：

   1. **编译**：将源代码编译成目标代码，例如将Java文件编译成class文件。
   2. **依赖管理**：管理项目所需的外部依赖库，确保项目能够顺利编译和运行。
   3. **单元测试**：运行项目中的单元测试，并生成测试报告以供开发人员查看。
   4. **打包**：将编译后的代码和依赖打包成可执行的应用程序或者库文件。
   5. **文档生成**：根据代码中的注释生成项目文档，方便团队成员理解和使用代码。
   6. **静态代码分析**：对代码进行静态分析，寻找潜在的问题和优化点。
   7. **发布部署**：将构建好的软件发布到指定的环境中，可以是测试环境、预生产环境或者生产环境。

   +++

   Gradle 和 Maven 都是流行的构建工具，用于构建、管理和部署Java项目，它们有一些区别：

   1. 语法：Maven使用XML作为其构建文件的语法，而Gradle使用Groovy或Kotlin脚本。这使得Gradle的构建脚本更加简洁和易读。

   2. 灵活性：Gradle提供了更大的灵活性和定制化能力，可以更轻松地定制构建过程和任务。Maven的约定优于配置的原则可能会限制一些特殊需求的实现。

   3. 性能：一些基准测试显示，Gradle在构建大型项目时可能比Maven更快。这主要是因为Gradle允许并行执行任务，而Maven则是基于阶段顺序执行。

   4. 社区支持：由于Maven比Gradle存在更长的历史，因此拥有更多的成熟插件和更广泛的社区支持。但Gradle也在不断发展壮大，并且吸引了越来越多的用户和贡献者。

   总的来说，选择使用Maven还是Gradle取决于个人偏好，项目需求以及团队的技术栈和经验。两者都是优秀的构建工具，都能够满足大多数Java项目的构建需求。

3. IDEA配置

   * [Code Style · spring-projects/spring-framework Wiki · GitHub](https://github.com/spring-projects/spring-framework/wiki/Code-Style)
   * https://github.com/spring-projects/spring-framework/wiki/IntelliJ-IDEA-Editor-Settings

# 整体架构

1. 整体架构
2. 核心模块（五大类Core Container、Web、AOP、Data Access、Test）
   * spring-core 模块：提供了 Spring 框架的核心功能，包括 IoC（控制反转）和 DI（依赖注入）功能的实现，以及对资源处理、国际化、事件传播等基本功能的支持。
   * spring-beans 模块：提供了 BeanFactory 接口的实现，负责管理应用程序中的对象（Bean），包括对象的创建、生命周期管理和依赖注入等功能。
   * spring-context 模块：构建在 spring-core 和 spring-beans 模块之上，提供了一种类似于JNDI注册器的框架式的对象访问方法，提供了更丰富的应用上下文（Application Context）功能，包括对国际化、事件传播、资源加载、应用层面的异常处理等功能的支持。ApplicationContext接口是该模块的关键。
   * spring-aop 模块：实现了面向切面编程（AOP）的功能，包括切面、连接点、通知、切点等概念的实现，可以用于实现日志记录、事务处理、性能监控等横切关注点的功能。
   * Expression Language 模块：提供了一个强大的表达式语言用于在运行时查询和操纵对象。它是JSP 2.1规范中定义的 unifed expressionlanguage 的一个扩展。该语言支持设置/获取属性的值，属性的分配，方法的调用，访问数组上下文(accessiong the contextofarrays)、容器和索引器、逻辑和算术运算符、命名变量以及从 Spring 的IoC容器中根据名称检索对象。它也支持 list投影、选择和一般的 list 聚合。
   * spring-jdbc 模块：提供了对 JDBC 的抽象和简化，包括 JdbcTemplate 等工具类，使得使用 JDBC 进行数据库操作更加便捷和安全。
   * spring-tx 模块：提供了对事务管理的支持，包括声明式事务、编程式事务等方式，可以与 JDBC、Hibernate 等持久化框架进行集成。
   * spring-web 模块：提供了对 Web 应用开发的支持，包括 Web 应用上下文、MVC 框架、远程调用、WebSocket 支持等功能。
   * spring-webmvc 模块：提供了 Spring MVC 框架，用于构建基于 Servlet 的 Web 应用程序，包括处理请求、渲染视图、处理表单提交等功能。
3. 模块间依赖关系

# 容器的基本实现

> Spring框架中支持了两种不同形式的IOC容器初始化方式：
>
> * 基于XML的容器初始化
> * 基于注解的初始化方式
>
> 初始化容器时使用的具体初始化类不同。

## 设计

1. 容器

   ![image-20240327121447812](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202403271214881.png)

2. Bean的创建

   * 通过配置文件方式

     ~~~java
     		ClassPathXmlApplicationContext context =
     				new ClassPathXmlApplicationContext("application.xml");
     		// Person person = (Person) context.getBean("person");
     		Person person = context.getBean("person", Person.class);
     ~~~

     * 过程
       * 读取配置
         * 加载及解析xml
         * 生成bean定义
       * 根据配置实例化Bean对象
         * 将bean定义注册到ioc容器中
         * 按照bean定义实例化容器中的bean
       * 使用Bean
     * 设计思路

       * 需要一个类用于验证和读取配置
       * 需要一个类用于根据配置信息进行反射实例化
       * 需要一个类用于将上述读取配置和实例化对象逻辑进行整合
     * 时序图：https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202403262017345.svg

   * 注解方式

     * 过程
     * 相关类或接口或注解
       * @Configuration
       * @Bean
       * @ComponentScan&@ComponentScans

## 核心接口和类

### DefaultListableBeanFactory

> 全类名：org.springframework.beans.factory.support.DefaultListableBeanFactory

1. 类关系

   ![image-20240326155427489](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202403261554411.png)

   > 图中蓝色表示类，绿色表示接口；实线代表extends，虚线代表implements。

   * `AliasRegistry`：定义对 alias的简单增删改等操作。
   * `SimpleAliasRegistry`：主要使用map作为 alias的缓存，并对接口 AliasRegistry 进行
     实现。
   * `SingletonBeanRegistry`：定义对单例的注册及获取
   * `BeanFactory`：定义获取bean及bean的各种属性
   * `DefaultSingletonBeanRegistry`：对接口SingletonBeanRegistry各函数的实现
   * `HierarchicalBeanFactory`：继承BeanFactory，也就是在BeanFactory定义的功能的基础上增加了对 parentFactory 的支持。
   * `BeanDefinitionRegistry`：定义对BeanDefinition的各种增删改操作。
   * `FactoryBeanRegistrySupport`：在DefaultSingletonBeanRegistry基础上增加了对 FactoryBean的特殊处理功能。
   * `ConfigurableBeanFactory`：提供配置Factory的各种方法。
   * `ListableBeanFactory`：根据各种条件获取bean的配置清单
   * `AbstractBeanFactory`：综合FactoryBeanRegistrySupport 和ConfigurableBeanFactory 的功能。
   * `AutowireCapableBeanFactory`：提供创建 bean、自动注入、初始化以及应用 bean 的后处理器。
   * `AbstractAutowireCapableBeanFactory`：综合AbstractBeanFactory 并对接口 Autowire CapableBeanFactory 进行实现。
   * `ConfigurableListableBeanFactory`：BeanFactory配置清单，指定忽略类型及接口等
   * `DefaultListableBeanFactory`：综合上面所有功能，主要是对Bean注册后的处理

### XmlBeanDefinitionReader

> 全类名：org.springframework.beans.factory.xml.XmlBeanDefinitionReader

1. 类关系

   ![image-20240326162138895](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202403261621940.png)

2. 资源文件、解析和注册相关类

   * `ResourceLoader`：定义资源加载器，主要应用于根据给定的资源文件地址返回对应的Resource.
   * `BeanDefinitionReader`：主要定义资源文件读取并转换为BeanDefinition 的各个功能
   * `EnvironmentCapable`：定义获取Environment方法。
   * `DocumentLoader`：定义从资源文件加载到转换为Document的功能。
   * `AbstractBeanDefinitionReader`：对EnvironmentCapable、BeanDefinitionReader 类定义的功能进行实现。
   * `BeanDefinitionDocumentReader`：定义读取Docuemnt 并注册BeanDefinition 功能
   * `BeanDefinitionParserDelegate`：定义解析Element的各种方法。
   * `ClassPathResource`

3. xml配置文件读取流程

   * 通过继承自AbstractBeanDefinitionReader 中的方法，来使用ResourLoader 将资源文件路径转换为对应的 Resource 文件。
   * 通过 DocumentLoader对Resource 文件进行转换，将Resource 文件转换为 Document文件。
   * 通过实现接口 BeanDefinitionDocumentReader 的DefaultBeanDefinitionDocumentReader 类对 Document 进行解析，并使用 BeanDefinitionParserDelegate对Element 进行解析。

## 配置文件封装

Spring的配置读取是通过ClassPathResource进行封装。在Java中，将不同来源的贷源抽象成 URL，通过注册不同的handler（URLStreamHandler）来处理不同来源的资源的读取逻辑，一般handler的类型使用不同前缀(协议，Protocol)来识别，如“file:”、“http:”、“iar:”等，然而 URL 没有默认定义相对 Classpath或 ServletContext等资源的 handler，虽然可以注册自己的 URLStreamHandler 来解析特定的 URL前缀(协议),比如“classpath:”，然而这需要了解URL的实现机制，而且 URL也没有提供一些基本的方法如检查当前资源是否存在、检查当前资源是否可读等方法。因而Spring对其内部使用到的资源实现了自己的抽象结构：Resource接口来封装底层资源。

对不同来源的资源文件都有相应的Resource实现：文件(FileSystemResource)、Classpath资源(ClassPathResource )、URL, 资源( UrlResource )、InputStream 资源( InputStreamResource )Byte数组(ByteArrayResource)等。

![image-20240327092031699](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202403270920205.png)

## 加载Bean

当通过 Resource相关类完成了对配置文件进行封装后配置文件的读取工作就全权交给XmlBeanDefinitionReader 来处理了。

### 获取XML的验证模式

1. xml常用验证模式

   * DTD：DTD(Document Type Defnition)即文档类型定义，是一种 XML,约束模式语言，是 XMI文件的验证机制，属于XML文件组成的一部分。DTD是一种保证 XM文档格式正确的有效方法，可以通过比较 XML 文档和 DTD 文件来看文档是否符合规范，元素和标签使用是否正确。一个 DTD 文档包含:元素的定义规则，元素间关系的定义规则，元素可使用的属性，可使用的实体或符号规则。

   * XSD：XML Schema语言就是XSD(XML, Schemas Definition)。XML Schema描述了 XML 文档的结构。可以用一个指定的 XM Schema来验证某个XML 文档，以检査该 XML 文档是否符合其要求。文档设计者可以通过XMLSchema指定一个XML文档所允许的结构和内容，并可据此检查一个XML文档是否是有效的。XMLSchema本身是一个 XML 文档，它符合 XML 语法结构。可以用通用的 XML解析器解析它。

     在使用 XML Schema 文档对 XML, 实例文档进行检验，除了要声明名称空间外(xmins-http://www.Springfamework.org/schema/beans)，还必须指定该名称空间所对应的XMLSchema 文档的存储位置。通过schemaLocation属性来指定名称空间所对应的XMLSchema文档的存储位置它包含两个部分，一部分是名称空间的 URI，另一部分就是该名称空间所标识的XMLSchema文件位置或 URL,地址(xsi:schemaocation="http://www.Springframework.org/schema/beans htp://www.Springfiamework.org/schema/beans/Spring-beans.xsd ).

     ~~~xml
     <beans xmlns="http://www.springframework.org/schema/beans"
     	   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     	   xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
     
     	<bean id="person" class="org.springframework.demo_source_test.domain.Person">
     		<property name="id" value="1"/>
     		<property name="name" value="Java"/>
     	</bean>
     
     </beans>
     ~~~

2. 相关类

   * `XmlValidationModeDetector`

Spring用来检测验证模式的办法就是判断是否包含 DOCTYPE，如果包含就是 DTD，否则就是 XSD。

### 加载XML配置文件

#### 获取Document

1. `DocumentLoader`&`DefaultDocumentLoader`

### 解析并注册BeanDefinition

#### 解析Profile

# 资料

源码地址：

* github：https://github.com/spring-projects/spring-framework
* gitee：https://gitee.com/mirrors/Spring-Framework

相关学习参考：

1. [Spring源码深度解析之通篇死磕Spring源码](https://segmentfault.com/a/1190000022372094)
2. [Java/Spring源码深度解析.pdf](https://github.com/wususu/effective-resourses/blob/master/Java/Spring%E6%BA%90%E7%A0%81%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90.pdf)
3. https://www.ddkk.com/zhuanlan/j2ee/spring/7/1.html



1. 环境准备&工具准备
   * gradle
   * groovy
   * git
   * idea
2. 类图，时序图基础知识准备
3. IDEA调试