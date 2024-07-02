# 前期准备

参考：

* [Spring Framework（6.x）源码编译与源码阅读入门](https://blog.csdn.net/qq_25409421/article/details/135991212?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-135991212-blog-127945857.235%5Ev43%5Epc_blog_bottom_relevance_base5&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-135991212-blog-127945857.235%5Ev43%5Epc_blog_bottom_relevance_base5&utm_relevant_index=5)
* [在windows10使用Gradle编译Spring源码](https://blog.csdn.net/qq_34738512/article/details/129747004)

1. JDK

   > 需要注意JDK版本与spring框架版本的关系，比如Spring6需要JDK17
   
2. Git

3. Gradle

4. Spring源码获取&构建

   - github：https://github.com/spring-projects/spring-framework
   - gitee：https://gitee.com/mirrors/Spring-Framework

   获取源码到本地后，先修改仓库相关配置（例如：国内的阿里镜像仓库）和gradle warpper获取地址以加快构建速度，然后可以按照[官方文档](https://github.com/spring-projects/spring-framework/wiki/Build-from-Source)使用命令行进行构建，第一次构建成功后，后期可以利用gradle的增量构建特性，针对需要重新构建的模块进行构建。例如：

   ~~~shell
   ./gradlew -a :spring-webmvc:test
   ~~~

5. 导入IDE

   按照官方文档[Code Style · spring-projects/spring-framework Wiki · GitHub](https://github.com/spring-projects/spring-framework/wiki/Code-Style)和[Import-into-idea](https://github.com/spring-projects/spring-framework/wiki/IntelliJ-IDEA-Editor-Settings)将源码项目导入到IDEA中。

# 整体架构

> 本次源码阅读spring-framework版本为v6.1.5
>
> 源码阅读原则：
>
> * 先学使用，再究原理
> * 带着问题分析，抓住重点，逐个击破

1. 设计理念
2. 整体架构
3. 核心模块（五大类Core Container、Web、AOP、Data Access、Test）
   * spring-core 模块：提供了 Spring 框架的核心功能，包括 IoC（控制反转）和 DI（依赖注入）功能的实现，以及对资源处理、国际化、事件传播等基本功能的支持。
   * spring-beans 模块：提供了 BeanFactory 接口的实现，负责管理应用程序中的对象（Bean），包括对象的创建、生命周期管理和依赖注入等功能。
   * spring-context 模块：构建在 spring-core 和 spring-beans 模块之上，提供了一种类似于JNDI注册器的框架式的对象访问方法，提供了更丰富的应用上下文（Application Context）功能，包括对国际化、事件传播、资源加载、应用层面的异常处理等功能的支持。ApplicationContext接口是该模块的关键。
   * spring-aop 模块：实现了面向切面编程（AOP）的功能，包括切面、连接点、通知、切点等概念的实现，可以用于实现日志记录、事务处理、性能监控等横切关注点的功能。
   * Expression Language 模块：提供了一个强大的表达式语言用于在运行时查询和操纵对象。它是JSP 2.1规范中定义的 unifed expressionlanguage 的一个扩展。该语言支持设置/获取属性的值，属性的分配，方法的调用，访问数组上下文(accessiong the contextofarrays)、容器和索引器、逻辑和算术运算符、命名变量以及从 Spring 的IoC容器中根据名称检索对象。它也支持 list投影、选择和一般的 list 聚合。
   * spring-jdbc 模块：提供了对 JDBC 的抽象和简化，包括 JdbcTemplate 等工具类，使得使用 JDBC 进行数据库操作更加便捷和安全。
   * spring-tx 模块：提供了对事务管理的支持，包括声明式事务、编程式事务等方式，可以与 JDBC、Hibernate 等持久化框架进行集成。
   * spring-web 模块：提供了对 Web 应用开发的支持，包括 Web 应用上下文、MVC 框架、远程调用、WebSocket 支持等功能。
   * spring-webmvc 模块：提供了 Spring MVC 框架，用于构建基于 Servlet 的 Web 应用程序，包括处理请求、渲染视图、处理表单提交等功能。
4. 模块间依赖关系

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
       * @Import

## 核心接口和类

### BeanFactory

> 全类名：org.springframework.beans.factory.BeanFactory

### ApplicationContext

> 全类名：org.springframework.context.ApplicationContext

`ApplicationContext`接口组合并扩展了`BeanFactory`的功能，主要包扩：

* `EnvirmentCaple`：环境变量相关
* ``ApplicationEventPublisher`：发送事件对象
* `ResourcePatternResolve`：资源通配符解析相关
* `MessageSource`：国际化相关

### DefaultListableBeanFactory

> 全类名：org.springframework.beans.factory.support.DefaultListableBeanFactory
>
> 该类是`BeanFactory`接口的重要实现类

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

## Bean的元数据

> 元数据：描述数据的数据

### BeanDefinition

1. 作用：使用统一“描述语言”来描述一个Bean，使得容器可以根据这些描述的元数据进行Bean的创建和管理

2. 类图

   ![image-20240630163624687](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202406301636650.png)

   > 接口用于顶层设计，是核心能力的抽象。抽象类用于核心能力的共享。

   * `BeanDefinition`：
   * `AbstractBeanDefinition`

### BeanDefinitionRegistry

1. 作用：定义了注册和管理Bean定义的核心接口。它定义了一系列方法，如注册Bean定义、移除Bean定义、检查Bean定义是否存在等。

2. 类图

   ![image-20240630173728901](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202406301737614.png)

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

相关参考：

1. [Spring源码深度解析之通篇死磕Spring源码](https://segmentfault.com/a/1190000022372094)
2. [Java/Spring源码深度解析.pdf](https://github.com/wususu/effective-resourses/blob/master/Java/Spring%E6%BA%90%E7%A0%81%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90.pdf)
3. https://www.ddkk.com/zhuanlan/j2ee/spring/7/1.html
4. https://github.com/doocs/source-code-hunter
