# Spring

官网：https://spring.io

参考：

* https://www.bilibili.com/video/BV1WZ4y1P7Bp?p=1
* https://www.bilibili.com/video/BV1Fi4y1S7ix/?p=2&spm_id_from=pageDriver&vd_source=fabefd3fabfadb9324761989b55c26ea

## 简介

1. spring是什么

   spring是分层的的javaSE/EE应用full-stack**轻量级开源框架**，以IOC（inverse of control:反转控制）和AOP（aspect oriented programing:面向切面编程）为内核。提供了展现层SpringMVC和持久层Spring JDBCTemplate以及业务层事务管理等众多的企业级应用技术，还能整合开源世界众多著名的第三方框架和类库，逐渐成为使用最多的JavaEE企业应用开源框架。

2. 理念：使现有技术更加实用。

3. Spring发展历程

   ![image-20220117162012206](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220117162012206.png)

   ![image-20221203114939964](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202212031149763.png)

4. Spring的优势

   * 方便解耦，简化开发
   * AOP编程的支持
   * 声明式事务的支持
   * 方便程序的测试
   * 方便集成各种优秀框架
   * 减低JavaEE API的使用难度
   * java源码经典学习范例

5. Spring framework的体系结构（4.0系统结构）

   ![image-20220117162143652](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220117162143652.png)

   ![image-20221203115337228](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202212031153901.png)

## 核心概念

1. Bean及其生命周期
   * Bean：简单来说，就是由Spring IOC容器实例化、组装和管理的对象。
2. 控制反转：（IOC是一种思想）
   * 使用对象时，由主动new产生对象转换为由外部提供对象,此过程中对象创建控制权由程序转移到外部，此思想称为控制反转。
   * Spring技术对IoC思想进行了实现。Spring提供了一个容器，称为IoC容器，用来充当IoC思想中的外部。IoC容器负责对象的创建、初始化等-系列工作， 被创建或被管理的对象在IoC容器中统称为Bean。
   * 控制：指谁来控制对象的创建。传统应用程序对象是由程序本身通过new关键字来控制。而使用Spring后，由Spring通过反射机制来创建对象。
   * 反转：程序本身不去创建对象而变为被动的接收对象。
3. 依赖注入（DI）
   * 在容器中建立bean与bean之间的依赖关系的整个过程, 称为依赖注入。

![image-20230211175056032](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302111751185.png)

## 快速入门

> 想要使用spring进行开发简单来说只需要在一个普通的Maven项目中引入spring的依赖包即可使得该项目成为一个spring应用。在开发过程中就可以使用spring提供的相关api特性进行简化开发。

Spring程序开发步骤：

* **导入Spring开发的基本包坐标**

  ~~~xml
          <dependency>
              <groupId>org.springframework</groupId>
              <artifactId>spring-context</artifactId>
              <version>${spring-context.version}</version>
          </dependency>
  ~~~

* 创建service层，dao层等业务相关接口和实现类

* **配置上述相关类的元信息（BeanDefinition）**，方式如下：

  * xml配置文件
  * groovy脚本
  * java注解配置

* 使用Spring的容器相关API获得Bean实例

  * `ClassPathXmlApplicationContext`
  * `GenericApplicationContext`
  * `AnnotationConfigApplicationContext`

## IOC容器

1. 相关包：
   * `org.springframework.beans`
   * `org.springframework.context`
2. 相关常用重要类和接口
   * `BeanFactory`
   * `ApplicationContext`

### 容器

1. ApplicationContext继承体系

   ![image-20220120200453261](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220120200453261.png)

2. ApplicationContext实现类

   * ClassPathXmlApplicationContext：从类的根路径下加载配置文件（推荐使用）
   * FileSystemXmlApplicationContext：从磁盘路径上加载配置文件，配置文件可以在磁盘的任意位置
   * AnnoationConfigApplicationContext：使用注解配置容器对象时使用

3. getBean()方法

   * 传递id
   * 传递class

4. BeanFactory和FactoryBean

   * **BeanFactory**定义了IOC容器的最基本形式，并提供了IOC容器应遵守的的最基本的接口，也就是Spring IOC所遵守的最底层和最基本的编程规范。在Spring代码中，BeanFactory只是个接口，并不是IOC容器的具体实现，但是Spring容器给出了很多种实现，如 DefaultListableBeanFactory、XmlBeanFactory、ApplicationContext等，都是附加了某种功能的实现。
   * **FactoryBean** 一般情况下，Spring通过反射机制利用<bean>的class属性指定实现类实例化Bean，在某些情况下，实例化Bean过程比较复杂，如果按照传统的方式，则需要在<bean>中提供大量的配置信息。配置方式的灵活性是受限的，这时采用编码的方式可能会得到一个简单的方案。Spring为此提供了一个org.springframework.bean.factory.FactoryBean的工厂类接口，用户可以通过实现该接口定制实例化Bean的逻辑。 FactoryBean接口对于Spring框架来说占用重要的地位，Spring自身就提供了70多个FactoryBean的实现。它们隐藏了实例化一些复杂Bean的细节，给上层应用带来了便利。从Spring3.0开始，FactoryBean开始支持泛型，即接口声明改为FactoryBean<T>的形式

### Bean及其配置

1. Bean：在Spring中，由Spring IoC容器管理的对象被称为Bean。在容器本身中，Bean定义被表示为 `BeanDefinition` 对象

2. Bean标签的基本配置

   用于配置对象交由Spring来创建。默认情况下它调用的是类中的无参构造函数，如果没有无参构造函数则不能创建成功。

   基本属性：

   * id：Bean实例在Spring容器中的唯一标识
   * class：Bean的全限定名
   * name：Bena的别名

3. Bean标签的范围配置

   scope：指定对象的作用范围，取值如下：

   | 取值范围   | 说明                                                         |
   | ---------- | ------------------------------------------------------------ |
   | singleton  | 默认值，单例的                                               |
   | prototype  | 多例的                                                       |
   | request    | web项目中，spring创建一个Bean对象，将对象存入到request域中   |
   | session    | web项目中，spring创建一个Bean的对象，将对象存入到session域中 |
   | ~~global~~ | ~~web项目中，应用在protlet环境中，如果没有protlet环境，那么相当于session~~ |

   总结：

   * 当scope的取值为singleton时，Bean的实例化个数为1个，Bean的实例化时机为当Spring核心文件被加载时，实例化配置的Bean实例。Bean的生命周期：
     * 对象创建：当应用加载，创建容器时，对象就被创建了
     * 对象运行：只要容器在，对象就一直活着
     * 对象销毁：当应用卸载，销毁容器时，对象就被销毁了
   * 当scope的取值为prototype时，Bean的实例个数是多个，Bean的实例化时机是当调用getBean()方法时实例化Bean。Bean的生命周期：
     * 对象创建：当使用对象时，创建新的对象实例
     * 对象运行：只要对象在使用中，就一直活着
     * 对象销毁：当对象长时间不用时，被java的立即回收机制回收

4. Bean生命周期配置

   * 在配置文件中配置
     * init-method:指定类中的初始化方法名称
     * destroy-method：指定类中销毁方法名称
   * 在类定义时配置：实现InitalizingBean和DisposableBean两个接口

   ![image-20230211230417682](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302112304813.png)

   ![image-20230211230501166](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302112305816.png)

5. **Bean实例化**三种方式

   * 无参构造方法实例化

   * 工厂静态方法实例化（factory-method属性指定类中实例化方法）

     > ```java
     > public class UserDaoFactory {
     >  public static UserDao getUserDao(){
     >      return new UserDaoImpl();
     >  }
     > }
     > ===============================
     > <bean id="userDao2" class="factory.UserDaoFactory" factory-method="getUserDao"></bean>
     > ```

   * 工厂实例方法实例化（factory-bean和factory-method属性指定实例化方法）

     > ```java
     > public class UserDaoFactory {
     >  public UserDao getUserDao2(){
     >      return new UserDaoImpl();
     >  }
     > }
     > ==============================
     > <bean id="userDaoFactory" class="factory.UserDaoFactory"/>
     > <bean id="userDao2" factory-bean="userDaoFactory" factory-method="getUserDao2"/>
     > ```

   * 方式三的改进：

     > ```java
     > public class UserDaoFactoryBean implements FactoryBean<UserDao> {
     >  /**
     >      * 代替原始实例工厂中的创建实例的对象
     >      * @return
     >      * @throws Exception
     >      */
     >     @Override
     >     public UserDao getObject() throws Exception {
     >         return new UserDaoImpl();
     >     }
     > 
     >     /**
     >      *
     >      * @return
     >      */
     >     @Override
     >     public Class<?> getObjectType() {
     >         return UserDao.class;
     >     }
     > 
     >     /**
     >      * 是否单列对象
     >      * @return
     >      */
     >     @Override
     >     public boolean isSingleton() {
     >         return true;
     >     }
     > }
     > ==================================
     >     <bean id="userDao" class="factory.UserDaoFactoryBean"/>
     > ```

### 依赖注入

1. Bean的依赖注入（Dependency injection）

   * 概念：是Spring框架核心IOC的具体实现

   * 注入方式：

     * **set方法**

       * P命名空间注入本质也是set方法注入。

         ![image-20220118193841130](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220118193841130.png)

     * **有参构造**

     * 属性注入（不推荐）

     * `@Bean`方法参数或方法调用注入

   * 注入方式的选择：

     ![image-20230212110259762](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302121103544.png)

   ```
   <!--setter方法-->
   <bean id="userService" class="service.impl.UserServiceImpl">
       <property name="userDao" ref="userDao"/>
   </bean>
   
   <!--有参构造方式-->
   <bean id="userService" class="service.impl.UserServiceImpl">
       <constructor-arg name="userDao" ref="userDao"/>
   </bean>
   ```

2. 依赖注入的数据类型

   * 普通数据类型

     ```xml
     <property name="" value=""></property>
     ```

   * 引用数据类型

     ```xml
     <property name="" ref=""></property>
     ```

   * 集合数据类型

     ```xml
     <property name="">
         <list>
             <value></value>
             <value></value>
         </list>
         <map name="">
             <entry key="" value=""></entry>
         </map>
     </property>
     ```

3. 引入其他配置文件（分模块开发）

   ```xml
   <import resource="" />
   ```

4. 依赖自动装配

   * IoC容器根据bean所依赖的资源在容器中自动查找并注入到bean中的过程称为自动装配
   * 自动装配的方式
     * 按类型（常用）
     * 按名称
     * 按构造方法
     * 不启用自动装配
   * 注意：
     * 自动装配用于引用类型依赖注入, 不能对简单类型进行操作
     * 使用按类型装配时( byType )必须保障容器中相同类型的bean唯一，推荐使用
     * 使用按名称装配时( byName )必须保障容器中具有指定名称的bean , 因变量名与配置耦合, 不推荐使用
     * 自动装配优先级低于setter注入与构造器注入,同时出现时自动装配配置失效

   ```
   <bean id="userService" class="service.impl.UserServiceImpl" autowire="byType"/>
   ```

### 案例：配置数据源（连接池）

1. 数据源的作用：事先实例化数据源，初始化部分连接资源

   > 常见的数据源：DBCP，C3P0，BoneCP，Druid

2. 数据源开发步骤

   * 导入数据源和数据库驱动坐标
   * 创建数据源对象
   * 设置数据源基本连接数据
   * 使用数据源获取连接资源和归还连接资源

3. 手动配置数据源

   ```java
   package com.chen.test;
   
   import com.alibaba.druid.pool.DruidDataSource;
   import com.alibaba.druid.pool.DruidPooledConnection;
   import com.mchange.v2.c3p0.ComboPooledDataSource;
   import org.junit.Test;
   
   import java.beans.PropertyVetoException;
   import java.sql.Connection;
   import java.sql.SQLException;
   import java.util.ResourceBundle;
   
   public class DataSource {
   
       /**
        * 测试手动创建c3p0数据源
        */
       @Test
       public void test1() throws PropertyVetoException, SQLException {
           ComboPooledDataSource dataSource = new ComboPooledDataSource();
   
           //手动配置数据库信息
           /*dataSource.setDriverClass("com.mysql.cj.jdbc.Driver");
           dataSource.setJdbcUrl("jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC");
           dataSource.setUser("root");
           dataSource.setPassword("4112");*/
   
           //加载配置文件配置数据库信息
           ResourceBundle rb = ResourceBundle.getBundle("jdbc");
           String driver = rb.getString("jdbc.driver");
           String url = rb.getString("jdbc.url");
           String username = rb.getString("jdbc.username");
           String password = rb.getString("jdbc.password");
   
           dataSource.setDriverClass(driver);
           dataSource.setJdbcUrl(url);
           dataSource.setUser(username);
           dataSource.setPassword(password);
   
           Connection connection = dataSource.getConnection();
           System.out.println(connection);
           connection.close();
       }
   
       /**
        * 测试手动创建druid数据源
        */
       @Test
       public void test2() throws Exception {
           DruidDataSource druidDataSource = new DruidDataSource();
   
           druidDataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
           druidDataSource.setUrl("jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC");
           druidDataSource.setUsername("root");
           druidDataSource.setPassword("4112");
   
           DruidPooledConnection connection = druidDataSource.getConnection();
           System.out.println(connection);
           connection.close();
   
       }
   }
   
   ===========================================================
   //jdbc.properties
   jdbc.driver=com.mysql.cj.jdbc.Driver
   jdbc.url=jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC
   jdbc.username=root
   jdbc.password=4112
   ```

4. Spring配置数据源

   ```java
   package com.chen.testdatasource;
   
   import org.junit.Test;
   import org.springframework.context.support.ClassPathXmlApplicationContext;
   
   import javax.sql.DataSource;
   import java.sql.Connection;
   import java.sql.SQLException;
   
   public class DataSource2 {
   
       /**
        * 测试使用Spring容器产生数据源(c3p0)
        */
       @Test
       public void test() throws SQLException {
           ClassPathXmlApplicationContext ioc = new ClassPathXmlApplicationContext("applicationContext3.xml");
           DataSource dataSource = (DataSource)ioc.getBean("dataSource");
           Connection connection = dataSource.getConnection();
           System.out.println(connection);
           connection.close();
       }
   
       /**
        * 测试使用Spring容器产生数据源(druid)
        */
       @Test
       public void test2() throws SQLException {
           ClassPathXmlApplicationContext ioc = new ClassPathXmlApplicationContext("applicationContext3.xml");
           DataSource dataSource = (DataSource)ioc.getBean("dataSource2");
           Connection connection = dataSource.getConnection();
           System.out.println(connection);
           connection.close();
       }
   }
   ```

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
   
       <bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
           <property name="driverClass" value="com.mysql.cj.jdbc.Driver"></property>
           <property name="jdbcUrl" value="jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC"></property>
           <property name="user" value="root"></property>
           <property name="password" value="4112"></property>
       </bean>
   
       <bean id="dataSource2" class="com.alibaba.druid.pool.DruidDataSource">
           <property name="driverClassName" value="com.mysql.cj.jdbc.Driver"></property>
           <property name="url" value="jdbc:mysql://localhost:3306/user_login?serverTimezone=UTC"></property>
           <property name="username" value="root"></property>
           <property name="password" value="4112"></property>
       </bean>
   
   </beans>
   ```

5. 抽取jdbc配置文件

   * 开启context命名空间

   * 使用context命名空间，加载指定的properties文件

     ![image-20230212142741153](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302121427993.png)

   * 使用el表达式读取加载的属性值

   ![image-20220317195738972](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220317195738972.png)

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:context="http://www.springframework.org/schema/context"
          xsi:schemaLocation="
          http://www.springframework.org/schema/beans
          http://www.springframework.org/schema/beans/spring-beans.xsd
          http://www.springframework.org/schema/context
          http://www.springframework.org/schema/context/spring-context.xsd">
   
       <!--加载外部配置文件-->
       <context:property-placeholder location="classpath:jdbc.properties"/>
   
       <bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
           <property name="driverClass" value="${jdbc.driver}"></property>
           <property name="jdbcUrl" value="${jdbc.url}"></property>
           <property name="user" value="${jdbc.username}"></property>
           <property name="password" value="${jdbc.password}"></property>
       </bean>
   
       <bean id="dataSource2" class="com.alibaba.druid.pool.DruidDataSource">
           <property name="driverClassName" value="${jdbc.driver}"></property>
           <property name="url" value="${jdbc.url}"></property>
           <property name="username" value="${jdbc.username}"></property>
           <property name="password" value="${jdbc.password}"></property>
       </bean>
   
   </beans>
   ```

### 配置知识点总结

* <bean>标签：

  * id属性：容器中Bean实例的唯一标识，不允许重复
  * class属性：要实例化的Bean的全限定名
  * scope属性：Bean的作用范围
  * <property>标签：属性注入
    * name属性：属性名称
    * value属性：注入的普通属性名称
    * ref属性：注入的对象引用值
    * <list>标签
    * \<map>标签
    * <properties>标签
  * <constructor-arg>标签 

* <import>标签：导入其他的spring的分文件

## 注解开发

1. Spring是轻代码重配置的框架，配置比较繁重，影响开发效率，所以注解开发是一种趋势

   > 注意：使用注解时需要进行组件扫描配置（使用全注解开发时可以使用@ComponentScan注解代替该操作）

   ![image-20220317225758957](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220317225758957.png)

2. 常用注解

   ![image-20220317200213868](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220317200213868.png)

   ![image-20220318093850296](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318093850296.png)

   * @Component：定义Bean

     * 衍生注解
       * @Controller：用于表现层Bean定义
       * @Servcie：用于业务层Bean定义
       * @Repository：用于数据层Bean定义

   * @Scope+@PostConstruct+@PreDestory：设置Bean的作用范围与生命周期

     ```java
     @Repository("userDao")
     @Scope("singleton")
     public class UserDaoImpl implements UserDao {
         @PostConstruct
         public void init(){
             System.out.println("init...........");
         }
         @PreDestroy
         public void destroy(){
             System.out.println("destroy........");
         }
     }
     ```

   * @Configuration+@ComponentScan

     ![image-20230212152955095](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302121529302.png)

   * @Value：实现简单类型的注入

   * @Qualifier：按照id值从容器中进行匹配，但是需要结合@Autowired使用

     ![image-20230212161055301](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302121610894.png)

   * @Resource： `@Resource`是Java EE提供的注解，也可以在Java SE中使用。它可以通过名称或类型进行依赖注入。

     * 当使用`@Resource`注解时，可以通过`name`属性指定要注入的依赖项的名称，或者通过`type`属性指定要注入的依赖项的类型。
     * 如果指定了`name`属性，则会按照名称进行注入，如果没有找到与该名称匹配的依赖项，则会抛出异常。
       * 如果指定了`type`属性，则会按照类型进行注入，如果找到多个与该类型匹配的依赖项，则会选择其中一个进行注入。
       * 如果既没有指定`name`属性，也没有指定`type`属性，则会按照名称进行注入，即默认使用被注解字段或方法的名称作为依赖项的名称。

   * @Autowired： `@Autowired`是Spring框架提供的注解，用于实现自动装配。该注解可以使用在成员变量、set方法和构造器上。

     * 当使用`@Autowired`注解时，Spring会尝试根据被注解字段或方法的类型来寻找匹配的依赖项进行注入。
       * 如果找到多个与该类型匹配的依赖项，则会根据一定的规则（如优先级、限定符等）选择其中一个进行注入。
       * 如果没有找到与该类型匹配的依赖项，则会抛出异常。

     ![image-20230212161016594](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302121610133.png)

   * @PropertySource：加载properties文件

     ![image-20230212161527968](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302121615596.png)

   * @Bean：将方法返回值添加到Spring容器中

     ![image-20230212163828252](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302121638962.png)

   * `@Import`

    * `@conditional`

      * `Condition`接口用于实现条件控制Bean是否放入Spring容器中，`@Conditional`注解用于指定`Condition`接口的实现类，该注解是SpringBoot框架实现自动装配的核心原理。

   ~~~java
   //核心配置类
      import com.alibaba.druid.pool.DruidDataSource;
      import org.springframework.beans.factory.annotation.Value;
      import org.springframework.context.annotation.Bean;
      import org.springframework.context.annotation.ComponentScan;
      import org.springframework.context.annotation.Configuration;
      import org.springframework.context.annotation.PropertySource;
      
      import javax.sql.DataSource;
      
      @Configuration//表明为Spring核心配置类
      @ComponentScan("com.chen")//包扫描
      @PropertySource("classpath:jdbc.properties")//加载jdbc配置文件
      public class SpringConfiguration {
      
          @Value("${jdbc.driver}")
          private String driverClassName;
      
          @Value("${jdbc.url}")
          private String url;
      
          @Value("${jdbc.username}")
          private String userName;
      
          @Value("${jdbc.password}")
          private String password;
      
          @Bean("dataSource")//将返回值添加到Spring容器中
          public DataSource getDataSource(){
              DruidDataSource dataSource = new DruidDataSource();
              dataSource.setDriverClassName(driverClassName);
              dataSource.setUrl(url);
              dataSource.setUsername(userName);
              dataSource.setPassword(password);
              return dataSource;
          }
      }
      =====================================================
          //测试
          @Test
          public void testDruidDataSource() throws SQLException {
      //        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
              AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfiguration.class);
              DataSource dataSource = (DataSource) context.getBean("dataSource");
              Connection connection = dataSource.getConnection();
              System.out.println(connection);
              connection.close();
          }
   ~~~

3. xml配置与注解配置的比较

   * 灵活度上：xml方式是具有一定局限性的，比如：在创建bean的时候，需要加入一些定制化的逻辑，当满足什么条件时在bean中加入什么样的属性，使用xml的方式就会比较麻烦，但是使用JavaConfig，即Annotation的方式更加灵活，可以很轻松地加入这些创建逻辑，而且代码更加清晰。
   * 安全性上：使用JavaConfig方式，属于类型安全的一种方式，通常在集成开发工具中，如果某一个类名写错，直接会编译提示错误，提早发现错误，而使用xml的方式，在某些编译器中是检测不出来的，类名写错之后，只有在启动或者运行的时候才会提示错误，存在一定的安全隐患。
   * 方便程度上：使用JavaConfig的方式如果在线上需要修改某一个配置，只能重新编译，然后替换配置类对应的class。而使用xml的方式，不需要重新编译，直接修改xml，重启即可生效。
   * 可读性：xml的可阅读性是比JavaConfig差很多的。

   ![image-20230212164250939](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302121642225.png)

   > xml配置和注解使用建议：
   >
   > * 如果对代码没什么要求，两种都可以，熟悉哪个用哪个；
   >
   > * 如果希望后期去学习一些Spring生态圈中的其他框架，建议尽早使用JavaConfig这种方式。

## 面向切面编程AOP

### 核心概念

1. AOP (Aspect Oriented Progr amming)：面向切面编程，一种编程范式。指导开发者如何组织程序结构。AOP并不是Spring框架的专属名称，它是OOP的一个延续，通过预编译的方式和运行期间动态代理实现程序功能的统一维护的一种技术。

2. 作用：在**不修改原始设计**的基础上为其进行**功能增强**

3. Spring理念；无侵入式

4. 核心概念（**在哪里对什么做怎样的功能增强**）

   * 连接点（JoinPoint）：程序执行过程中的任意位置，粒度为执行方法、抛出异常、设置变量等。在 Spring 中这些点指的是方法，可以看作正在访问的，或者等待访问的那些需要被增强功能的方法。**Spring 只支持方法类型的连接点。**
   * 切入点（PointCut）：匹配连接点的式子，实质就是**一个规则**，定义了我们要对哪些JoinPoint（哪个类的哪个方法）进行增强。

     * 在SpringAOP中，一个切入点可以只描述一个具体方法，也可以匹配多个方法
   * 通知：在切入点处执行的操作，也就是共性功能。实质就是**拦截到 Joinpoint 之后所要做的事情**，也就是对方法做的增强功能。在SpringAOP中，功能最终以方法的形式呈现。
     * 前置通知：在连接点之前运行的通知类型，它不会阻止流程进行到连接点，只是在到达连接点之前运行该通知内的行为，除非它引发异常
     * 后置通知：在连接点正常完成后要运行的通知，正常的连接点逻辑执行完，会运行该通知，前提条件是方法正常返回而没有引发异常；
     * 最终通知：无论连接点执行后的结果如何，正常还是异常，都会执行的通知
     * 异常通知：如果连接点执行因抛出异常而退出，则执行此通知
     * 环绕通知：环绕通知可以在方法调用之前和之后执行自定义行为
   * 通知类（Advice）：定义通知的类
   * 切面（Aspect）：**描述通知与切入点的对应关系**。本质是一个类，只不过是个功能类，作为整合 AOP 的切入点和通知。一般来讲，需要在 Spring 的配置文件中配置，或者通过注解来配置。
   * 目标对象( Target ) ：原始功能去掉共性功能对应的类产生的对象, 这种对象是无法直接完成最终工作的。简单点来说就是AOP 对连接点方法做增强，底层是代理模式生成连接点所在类的代理对象，那么连接点所在的类，就是被代理的类称呼为 Target。
   * 代理( Proxy ) ：目标对象无法直接完成工作,需要对其进行功能回填,通过原始对象的代理对象实现。一个类被 AOP 织入增强后，产生的结果就是代理类
   * 织入（Weaving）：织入是一种动作的描述，在程序运行时将增强的功能代码也就是通知，根据通知的类型（前缀后缀等…）放到对应的位置，生成代理对象。

   ![image-20230212205103543](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302122051537.png)

> 装饰者设计模式同样可以实现在不修改源代码的前提下进行功能增强，但是该方式侵入性较强，需要有顶层接口类设计和代码结构要求。

### 入门案例

1. 思路分析

   ![image-20230212210719558](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302122107730.png)

   > 使用注解方式需要额外引入AspectJ依赖，xml方式Spring本身支持无需额外依赖

   ~~~xml
   <dependency>
     <groupId>org.springframework</groupId>
     <artifactId>spring-aspects</artifactId>
     <version>${spring.version}</version>
   </dependency>
   
   <dependency>
     <groupId>org.springframework</groupId>
     <artifactId>spring-aop</artifactId>
     <version>6.1.0</version>
     <scope>compile</scope>
   </dependency>
   ~~~

2. 代码实现

   ```java
   //在配置类中使用@EnableAspectJAutoProxy()注解表示开启AOP自动配置注解功能
   @Component
   @Aspect
   public class BookDaoAdvice {
   
       /**
        * 切入点
        */
       @Pointcut("execution(void org.dao.impl.BookDaoImpl.save())")
       private void pt(){}
   
       /**
        * 通知（共性方法）
        */
       @Before(value = "pt()")
       public void printCurrentTime(){
           System.out.println(System.currentTimeMillis());
       }
   }
   ```

### 工作流程

1. Spring容器启动
2. 读取所有切面配置中的切入点
3. 初始化bean ,判定bean对应的类中的方法是否匹配到任意切入点
   * 匹配失败 ,创建对象
   * 匹配成功 ,创建原始对象(目标对象)的代理对象
4. 获取bean执行方法
   * 获取bean ,调用方法并执行,完成操作
   * 获取的bean是代理对象时 , 根据代理对象的运行模式运行原始方法与增强的内容,完成操作

### 切入点表达式

![image-20230216113833124](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302161138435.png)

![image-20230216113947331](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302161139730.png)

![image-20230216114218398](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302161142871.png)

![image-20230216122818670](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302161228497.png)

### 通知类型

1. 类型

   * 前置通知

     ![image-20230216172145390](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302161721211.png)

   * 后置通知

     ![image-20230216172240954](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302161722931.png)

   * 环绕通知（重点）

     ![image-20230216172226509](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302161722551.png)

     ![](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302161723388.png)

   * 返回后通知

     ![image-20230216182821208](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302161828568.png)

   * 抛出异常后通知

     ![image-20230216182842665](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302161828945.png)

2. 案例：测量业务层接口执行效率

   ```java
   @Component
   @Aspect
   public class UserServiceAdvice {
   
       @Pointcut("execution(* org.service.*Service.*(..))")
       public void point(){}
   
       @Around("point()")
       public void testExecution(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
           Signature signature = proceedingJoinPoint.getSignature();
           String className = signature.getDeclaringTypeName();
           String name = signature.getName();
   
           long start = System.currentTimeMillis();
           for (int i = 0; i < 100000; i++) {
               proceedingJoinPoint.proceed();
           }
           long end = System.currentTimeMillis();
           System.out.println("执行"+className+"."+name+"方法100000次，耗时为："+(end-start)+"ms");
       }
   }
   ```

### 通知获取数据

1. 获取参数

   ![image-20230216210513433](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302162105290.png)

2. 获取返回值类型

   ![image-20230216210533107](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302162105130.png)

3. 获取异常

   ![image-20230216210630874](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302162106648.png)

![image-20230216204057235](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302162040119.png)



### 代理模式

代理名词解释为：以被代理人名义，在授权范围内与第三方实施行为。而在软件行业中代理模式是一种非常常用的设计模式，跟现实生活中的逻辑一致。

在开发中代理模式的表现为：我们创建带有现有对象的代理对象，以便向外界提供功能接口。代理对象可以在客户端和目标对象之间起到中介的作用。**为被代理对象执行一些附带的，增加的额外功能。**

![image-20230901180930810](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202407302247146.png)

* 客户端
* 代理类：代理类需要拥有目标类的*能力*，该能力在代码中通过**接口**来体现。
* 目标类

开发中，代理模式的实现有两种：

* **静态代理**：若代理类在程序运行前就已经存在，那么这种代理方式被称为静态代理 ，这种情况下的代理类通常都是我们在 Java 代码中定义的， 静态代理中的代理类和委托类会实现同一接口；

  ~~~java
  /**
   * UserService的静态代理类
   *
   * @author whymechen
   * @version 1.0
   * @date 2023/10/26 15:48
   * @see UserService
   */
  @Slf4j
  @Component
  @RequiredArgsConstructor
  public class UserServiceProxy implements UserService {
  
      private final UserService userServiceImpl;
  
      @Override
      public void saveUser(User user) {
          log.info("开始保存用户信息：" + user.getName());
          userServiceImpl.saveUser(user);
          log.info("结束保存用户信息：" + user.getName());
      }
  }
  ~~~

* **动态代理**：代理类在程序运行时创建的代理方式被称为动态代理。 也就是说，这种情况下，代理类并不是在 Java 代码中定义的，而是在运行时根据我们在 Java 代码中的 “指示” 动态生成的。目的是为了**减少代理类的数量，解决代码复用的问题**。

  * JDK动态代理（只能代理接口）
  * CGLIB动态代理（支持接口，类）

> 个人认为不管是那一种方式，代理类均为动态生成，则其需要的描述信息均为目标类需要代理的方法（或者说是目标类与代理类需要共有的能力）和额外操作步骤（代理类多出来的能力），只不过JDK动态代理使用接口来抽取共有能力，代理类与目标类平级，CGLIG动态代理使用继承来实现共有能力的代码级表示，代理类为目标类的子级。

#### JDK

> 相关包：`java.lang.reflect`

1. 适用场景：只能代理接口

2. 重要类和接口

   * `InvocationHandler`
   * `Proxy`

3. 代码实现：

   ~~~java
   /**
    * @author chenwenjian
    * @version 1.0
    * @date 2023/12/26 18:37
    */
   @Slf4j
   @Service
   public class UserServiceInvocationHandler implements InvocationHandler {
   
       private UserServiceImpl userServiceImpl;
   
       @Autowired
       public UserServiceInvocationHandler(UserServiceImpl userServiceImpl) {
           this.userServiceImpl = userServiceImpl;
       }
   
       @Override
       public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
           long startTime = System.currentTimeMillis();
           log.info("开始调用=======");
           Object result = method.invoke(userServiceImpl, args);
           log.info("结束调用=======");
           log.info("耗时=======" + (System.currentTimeMillis() - startTime) + "ms");
           return result;
       }
   }
   
   public class Application {
       public static void main(String[] args) {
           AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringContextConfiguration.class);
   
           User user = User.builder()
                            .name("whymechen")
                            .gender("male")
                            .age(18)
                            .address("China")
                            .build();
   
           /* JDK动态代理客户端 */
           /*
            * 1. 创建一个实现接口InvocationHandler的对象
            * 2. 调用Proxy.newProxyInstance()方法创建一个代理对象
            * 3. 调用代理对象的方法
            */
           UserServiceImpl userService = context.getBean(UserServiceImpl.class);
           UserServiceInvocationHandler userServiceInvocationHandler = context.getBean(UserServiceInvocationHandler.class);
           UserService proxyInstance = (UserService)Proxy.newProxyInstance(userService.getClass().getClassLoader(), userService.getClass().getInterfaces(), userServiceInvocationHandler);
           proxyInstance.saveUser(user);
       }
   }
   ~~~

#### CGLIB

1. 简介：
   * CGLIB(Code Generation Library)是一个开源项目。
   * 是一个强大的，高性能，高质量的Code生成类库，它可以在运行期扩展Java类与实现Java接口。
   * 性能比JDK动态代理要好。（底层有一个小而快的字节码处理框架ASM）
2. 适用场景：**既可以代理接口，又可以代理类，底层是通过继承的方式实现的。**所以被代理的目标类不能使用final修饰。
3. 重要类和接口
   * `MethodInterceptor`
   * `Enhancer`

### Filter vs Intercepter  vs AOP

参考：[SpringBoot实战：深度剖析 Filter、Interceptor、AOP请求三剑客 | 高并发系统设计必修课](https://mp.weixin.qq.com/s?__biz=MzU1MjAwODAzOA==&mid=2247484339&idx=1&sn=e17c9b29fcbadf49611444030135286a&chksm=fb89e3baccfe6aac4be935acca682d7b378245b99df17231ab2c4ad9b1fbd2ec39b02acbe044&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_pcfeeds&ranksessionid=1745393159_1#rd)

## Spring事务

参考：https://www.bilibili.com/video/BV1WZ4y1P7Bp?p=138&spm_id_from=pageDriver&vd_source=fabefd3fabfadb9324761989b55c26ea

1. 事务的作用：在数据层保障一系列的数据库操作同成功同失败。

2. Spring事务的作用：在数据层或业务层保障一系列的数据库操作同成功同失败。

3. 实现(编程式的注解方式)

   > 编程式
   >
   > 声明式：xml配置和注解配置

   * 在业务层添加事务管理器

     ![image-20230217111241449](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171112335.png)

   * 设置事务管理器

     ![image-20230217111340020](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171113400.png)

   * 开启注解式事务驱动

     ![image-20230217111439817](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171114547.png)

4. 编程式事务的相关对象

   ![image-20230218113305962](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181133052.png)

   ![image-20230218113330404](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181133185.png)

5. spring事务角色

   * 事务管理员：发起事务方,在Spring中通常指代业务层开启事务的方法。
   * 事务协调员：加入事务方,在Spring中通常指代数据层方法,也可以是业务层方法。

6. 事务相关配置

   ![image-20230217112303737](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171123496.png)

   * 事务的隔离级别

     ![image-20230218113506460](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302181135598.png)

   * 事务的传播行为：事务协调员对事务管理员所携带事务的处理态度

     ![image-20230217115236161](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171152993.png)

     ![image-20230217115402849](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171154816.png)

## Spring JDBC Template

1. 简介

2. 开发步骤

   > 1. 导入spring-jdbc和spring-tx坐标
   > 2. 创建数据库表和实体
   > 3. 创建JdbcTemplate对象
   > 4. 执行数据库操作

3. 常用操作

## Spring Event

Spring Event是Spring的事件通知机制，可以将相互耦合的代码解耦，从而方便功能的修改与添加。Spring Event是监听者模式的一个具体实现。

监听者模式包含了监听者Listener、事件Event、事件发布者EventPublish，过程就是EventPublish发布一个事件，被监听者捕获到，然后执行事件相应的方法。

## 定时任务

> 使用spring的定时任务需要使用@EnableScheduling注解开启该功能

## Junit集成

1. 原始Junit测试Spring时存在的问题

   ![image-20220318100349528](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318100349528.png)

2. Spring集成Junit步骤

   > 1. 导入Spring集成Junit的坐标（spring-test）
   > 2. 使用@Runwith注解替换原来的运行期
   > 3. 使用@ContextConfiguration指定配置文件或配置类
   > 4. 使用@Autowired注入需要测试的对象
   > 5. 创建测试方法测试

   ```java
   package com.chen.test;
   
   import org.junit.Test;
   import org.junit.runner.RunWith;
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.test.context.ContextConfiguration;
   import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
   
   import javax.sql.DataSource;
   import java.sql.Connection;
   import java.sql.SQLException;
   
   @RunWith(SpringJUnit4ClassRunner.class)
   @ContextConfiguration("classpath:applicationContext.xml")
   public class SpringJunitTestDemo {
   
       @Autowired
       private DataSource dataSource;
   
       @Test
       public void test() throws SQLException {
           Connection connection = dataSource.getConnection();
           System.out.println(connection);
           connection.close();
       }
   }
   ```

## Web集成

1. ApplicationContext的获取：被获取多次

2. 将ApplicationContext存储到ServletContext域中

   ![image-20220331204221605](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220331204221605.png)

3. Spring提供获取应用上下文的工具

   ![image-20220318103032314](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318103032314.png)

## Mybatis的集成

参考：http://www.mybatis.cn/archives/769.html

1. 步骤

   > 导入相关包mybatis-spring、spring-jdbc（spring操作数据库必须要导的包）

2. mybatis的单独配置类

   ```java
   package org.config;
   
   import org.mybatis.spring.SqlSessionFactoryBean;
   import org.mybatis.spring.mapper.MapperScannerConfigurer;
   import org.springframework.context.annotation.Bean;
   
   import javax.sql.DataSource;
   
   /**
    * @author WenJianChen
    * @version 1.0
    * @date 2023/2/12 19:23
    */
   public class MybatisConfiguration {
   
       @Bean
       public SqlSessionFactoryBean sqlSessionFactory(DataSource dataSource){
           SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
           sqlSessionFactoryBean.setTypeAliasesPackage("org.domain");
           sqlSessionFactoryBean.setDataSource(dataSource);
           return sqlSessionFactoryBean;
       }
   
       @Bean
       public MapperScannerConfigurer mapperScannerConfigurer(){
           MapperScannerConfigurer mapperScannerConfigurer = new MapperScannerConfigurer();
           mapperScannerConfigurer.setBasePackage("org.dao");
           return mapperScannerConfigurer;
       }
   }
   ```

>>>>>>> 52071a02add265787740552d6708b67902e86887

# Spring MVC

参考文档：https://pdai.tech/files/kaitao-springMVC.pdf

## 概述

SpringMVC是一种基于Java的实现MVC设计模型的请求驱动类型的轻量级**Web框架**，属于SpringFrameWork的后续产品，已经融合在Spring Web Flow中。SpringMVC已经成为目前最主流的MVC框架之一，并且随着Spring3.0 的发布,全面超越Struts2,成为最优秀的MVC框架。它通过一套注解， 让一个简单的Java类成为处理请求的控制器，而无须实现任何接口。同时它还支持RESTful编程风格的请求。

![image-20220318144526046](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318144526046.png)

### SpringMVC开发步骤

1. 导入SpringMVC相关坐标（spring-webmvc和javax.servlet-api）

   ![image-20230217150326040](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171503843.png)

2. 配置SpringMVC核心控制器DispathcerServlet（即将SpringMVC容器配置到Servlet容器中）

   * web.xml中配置

     ```xml
     <?xml version="1.0" encoding="UTF-8"?>
     <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
              version="4.0">
     <!--配置SpringMVC的前端控制器-->
     <servlet>
         <servlet-name>DispatcherServlet</servlet-name>
         <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
         <init-param>
             <param-name>contextConfigLocation</param-name>
             <param-value>classpath:spring-mvc.xml</param-value>
         </init-param>
         <load-on-startup>1</load-on-startup>
     </servlet>
     <servlet-mapping>
         <servlet-name>DispatcherServlet</servlet-name>
         <url-pattern>/</url-pattern>
     </servlet-mapping>
     
     <!--全局初始化参数-->
     <context-param>
         <param-name>contextConfiguration</param-name>
         <param-value>classpath:applicationContext.xml</param-value>
     </context-param>
     
     <!--配置监听器-->
     <listener>
         <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
     </listener>
     
     <servlet>
         <servlet-name>UserServlet</servlet-name>
         <servlet-class></servlet-class>
     </servlet>
     <servlet-mapping>
         <servlet-name>UserServlet</servlet-name>
         <url-pattern>/userServlet</url-pattern>
     </servlet-mapping>
     </web-app>
     ```

   * 注解配置

     * 方式一：继承类

       ![image-20230217150514749](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171505624.png)

     * 方式二：继承AbstractAnnotationConfigDispatcherServletInitializer类

3. 创建Controller类和视图页面，并使用注解配置Controller类中业务方法的映射地址

![image-20230217150357914](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171503983.png)

![image-20230217165530465](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171655397.png)

4. 配置SpringMVC核心文件（spring-mvc.xml或者注解形式）
   ![image-20230217150429514](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171504191.png)

5. 客户端发起请求测试

   ![image-20220318144920983](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318144920983.png)

### SpringMvc组件解析（执行流程分析）

参考视频：https://www.bilibili.com/video/BV1WZ4y1P7Bp?p=46&vd_source=fabefd3fabfadb9324761989b55c26ea

![image-20230217164118218](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171641527.png)

![](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318152049532.png)

![image-20230218093259342](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302180933186.png)

1. 用户发送请求至前端控制器DispatcherServlet.

2. DispatcherServlet收到请求调用HandlerMapping处理器映射器。

3. 处理器映射器找到具体的处理器(可以根据xm|配置、注解进行查找), 生成处理器对象及处理器拦截器(如果有则生成)一并返回给DispatcherServlet.

4. DispatcherServlet调用HandlerAdapter处理器适配器。

5. HandlerAdapter经过适配调用具体的处理器(Controller,咖叫后端控制器)。

6. Controller执行完成返回ModelAndView。

7. HandlerAdapter将controller执行结果ModelAndView返回给

   DispatcherServlet.

8. DispatcherServlet将ModelAndView传给ViewReslover视图解析器。
   ViewReslover解析后返回具体View。

9. DispatcherServlet根据View进行渲染视图(即将模型数据填充至视图中)。

10. DispatcherServlet响应用户。

相关组件解析：

> 1、前端控制器DispatcherServlet（不需要程序员开发）由框架提供，在web.xml中配置。
> 作用：接收请求，响应结果，相当于转发器，中央处理器。
>
> 2、处理器映射器HandlerMapping（不需要程序员开发）由框架提供。
> 作用：根据请求的url查找Handler（处理器/Controller），可以通过XML和注解方式来映射。
>
> 3、处理器适配器HandlerAdapter（不需要程序员开发）由框架提供。
> 作用：按照特定规则（HandlerAdapter要求的规则）去执行Handler中的方法。
>
> 4、处理器Handler（也称之为Controller，需要程序员开发）
> 注意：编写Handler时按照HandlerAdapter的要求去做，这样适配器才可以去正确执行Handler。
> 作用：接受用户请求信息，调用业务方法处理请求，也称之为后端控制器。
>
> 5、视图解析器ViewResolver（不需要程序员开发）由框架提供。
> 作用：进行视图解析，把逻辑视图解析成真正的物理视图。 
> SpringMVC框架支持多种View视图技术，包括：jstlView、freemarkerView、ThymeleafView等。
>
> 6、视图View（需要工程师开发）
> 作用：把数据展现给用户的页面
> View是一个接口，实现类支持不同的View技术（jsp、freemarker、pdf等）

### SpringMVC注解解析

![image-20220318152957666](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220318152957666.png)

### SpringMVC配置文件解析

![image-20220331215507482](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220331215507482.png)

## SpringMVC的数据响应

1. 响应方式

   * 响应页面

     * 直接返回字符串：该方式会将返回的字符串与视图解析器的前后缀拼接后跳转

       ![image-20220331220520124](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220331220520124.png)

     * 返回ModelAndView对象

   * 回写数据

     * 直接返回字符串

       * 方式一：给相应控制器方法传入HttpResponse对象
       * 方式二：使用@ResponseBody标注

     * 返回对象或集合（进行相应配置将对象自动转换为json数据格式）

       > * > 方式一：
       >   >
       >   > ```xml
       >   > <!--配置处理器映射器-->
       >   > <bean class="org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter">
       >   >  <property name="messageConverters">
       >   >      <list>
       >   >          <bean class="org.springframework.http.converter.json.MappingJackson2HttpMessageConverter"></bean>
       >   >      </list>
       >   >  </property>
       >   > </bean>
       >   > ```
       >
       > * 方式二：使用mvc的注解驱动来代替格式转换器的配置<mvc:annotion-driven/>

2. 代码示例及配置

   ```java
   package com.chen.controller;
   
   import com.chen.pojo.User;
   import com.fasterxml.jackson.core.JsonProcessingException;
   import com.fasterxml.jackson.databind.ObjectMapper;
   import org.springframework.stereotype.Controller;
   import org.springframework.web.bind.annotation.RequestMapping;
   import org.springframework.web.bind.annotation.ResponseBody;
   import org.springframework.web.servlet.ModelAndView;
   
   import javax.servlet.http.HttpServletRequest;
   
   @Controller
   @RequestMapping("/test")
   public class TestController {
   
       @RequestMapping("/save")
       public String save(){
           System.out.println("controller save1 running");
           return "success";//默认为转发
       }
   
       @RequestMapping("save2")
       public ModelAndView save2(){
           System.out.println("controller save2 running");
           //model 模型 作用是返回封装数据
           //view 视图 作用是封装数据
           ModelAndView modelAndView = new ModelAndView();
           modelAndView.addObject("userName","chen");
           modelAndView.setViewName("success");
           return modelAndView;
       }
   
       @RequestMapping("/save3")
       public ModelAndView save3(ModelAndView modelAndView){
           System.out.println("controller save3 running");
           modelAndView.addObject("password","123456");
           modelAndView.setViewName("success");
           return modelAndView;
       }
   
       @RequestMapping("/save4")
       public String save4(HttpServletRequest request){
           System.out.println("controller save4 running");
           return "success";
       }
   
       @RequestMapping("/save5")
       @ResponseBody//不进行视图跳转，直接进行数据回写
       public String save5(){
           System.out.println("controller save5 running");
           return "success";//通常返回json数据
       }
   
       @RequestMapping("/save6")
       @ResponseBody//不进行视图跳转，直接进行数据回写
       public String save6() throws JsonProcessingException {
           User user = new User("chen", (short) 20, "男");
   
           /*使用json转换工具将对象转换为json格式的字符串*/
           ObjectMapper objectMapper=new ObjectMapper();
           String s = objectMapper.writeValueAsString(user);
           return s;//通常返回json数据
       }
   
       @RequestMapping("/save7")
       @ResponseBody//不进行视图跳转，直接进行数据回写
       public User save7() {
           User user = new User("chen", (short) 20, "男");
           /*进行配置使SpringMVC自动将对象转换为json格式的字符串*/
           return user;//通常返回json数据
       }
   }
   ```

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:context="http://www.springframework.org/schema/context"
          xmlns:mvc="http://www.springframework.org/schema/mvc"
          xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                               http://www.springframework.org/schema/context  http://www.springframework.org/schema/context/spring-context.xsd http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd">
   
       <!--组件扫描-->
       <context:component-scan base-package="com.chen.controller">
       </context:component-scan>
   
       <!--配置内部资源视图解析器-->
       <bean id="viewResovler" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
           <property name="prefix" value="/WEB-INF/jsp/"/>
           <property name="suffix" value=".jsp"/>
       </bean>
   
       <!--配置处理器映射器-->
   <!--    <bean class="org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter">-->
   <!--        <property name="messageConverters">-->
   <!--            <list>-->
   <!--                <bean class="org.springframework.http.converter.json.MappingJackson2HttpMessageConverter"></bean>-->
   <!--            </list>-->
   <!--        </property>-->
   <!--    </bean>-->
   
       <!--替换处理器映射器的配置-->
       <mvc:annotation-driven/>
   </beans>
   ```

## SpringMVC获得请求数据

1. 获得请求参数

   * SpringMVC可以接收的类型参数

     > 1. 基本数据类型参数
     >
     >    * 要求Controller中业务方法的参数名称要与请求参数的name一致，参数值会自动映射匹配
     >
     >      ![image-20220405144902149](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405144902149.png)
     >
     > 2. POJO类型参数
     >
     >    * 要求Controller中业务方法的POJO参数属性名要与请求参数的name一致，参数值会自动映射匹配
     >
     >      ![image-20220405145947871](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405145947871.png)
     >
     > 3. 数组类型参数
     >
     >    * 要求Controller中业务方法数组名称要与请求参数的name一致，参数值会自动映射匹配
     >
     > 4. 集合类型参数
     >
     >    * 场景一：获得集合参数时，要将集合参数包装到一个POJO中
     >    * 场景二：使用ajax提交时，可以指定contentType为json形式，那么方法参数位置使用@RequestBody可以直接接收集合数据而无需使用pojo进行封装

2. json数据的传递

   * json数组
   * json对象（pojo对象）
   * json数组（pojo对象）

   > 导入json数据转换相关坐标；
   >
   > 在Springmvc核心配置类中使用@EnableWebMvc注解开启自动转换json数据支持；
   >
   > 在方法参数列表中使用@RequestBody；

3. 日期型参数传递

   ![image-20230217210033145](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302172100213.png)

   ![image-20230217210306168](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302172103665.png)

4. 请求数据乱码问题 

   ![image-20220405152715147](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405152715147.png)

5. 参数绑定注解@requestParam

   > 当请求的参数名称与Controller的业务方法参数名称不一致时，需要通过@requestParam显式绑定

   ![image-20220405153031913](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405153031913.png)

   ![image-20220405153138966](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405153138966.png)

6. 获得Restful风格的参数

   ![image-20220405153525637](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405153525637.png)

   ![image-20220405153710199](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405153710199.png)

7. 自定义类型转换器

   ![image-20220405154129353](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220405154129353.png)

8. 获得Servlet相关API

   ![image-20220418102302878](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418102302878.png)

9. 获得请求头

   ![image-20220418102429751](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418102429751.png)

   ![image-20220418102854916](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418102854916.png)

10. 文件上传

    > 文件上传客户端三要素
    >
    > * 表单项type="file"
    > * 表单提交方式是post
    > * 表单的enetype属性是部分表单形式，及enctype="multipart/form-data"
    >
    > 文件上传原理
    >
    > 单文件上传步骤
    >
    > * 导入fileupload和io坐标
    >
    >   ![image-20220418104321191](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418104321191.png)
    >
    > * 配置文件上传解析器
    >
    >   ![image-20220418104358325](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418104358325.png)
    >
    > * 编写文件上传代码
    >
    >   ![image-20220418104531418](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220418104531418.png)

知识点总结：

> 1. MVC实现数据请求方式
> 2. 中文乱码问题
> 3. @RequestParam和@PathVariable
> 4. 自定义类型转换器
> 5. 获得Servlet相关API
> 6. @RequestHeader和@CookieValue
> 7. 文件上传

## 常用注解

1. @Controller

   ![image-20230217163613096](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171636503.png)

2. @RequestMapping

   ![image-20230217163647192](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171636056.png)

   ![image-20230217195614852](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171956520.png)

3. @ResponseBody

   ![image-20230217163724874](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171637324.png)

   ![image-20230217211033227](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302172110991.png)

4. @ComponentScan

   ![image-20230217165647448](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302171656095.png)

5. @RequestParam

   ![image-20230217202336638](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302172023846.png)

6. @EnableWebMvc

7. @RequestBody

   ![image-20230217203851685](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302172038466.png)

8. @DateTimeFormat

9. @PathValuable

   ![image-20230217212235074](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302172122963.png)

   ![image-20230217212314561](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302172123084.png)

10. @RestController

    ![image-20230217212728180](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302172127944.png)

11. @GetMapping

    ![image-20230217212804306](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302172128512.png)

## SpringMVC拦截器

### 拦截器概念

1. 拦截器（Interceptor）：一种动态拦截方法调用的机制，在SpringMVC中动态拦截控制器方法的执行

   ![image-20230218222658940](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302182227537.png)

2. 作用：

   * 在指定的方法调用前后执行预先设定的代码
   * 组织原始方法的执行

3. 拦截器和过滤器的区别

   * 归属不同：Filter属于Servlet技术，Interceptor属于SpringMVC技术
   * 拦截内容不同：Filter对所有访问进行增强，Interceptor仅针对SpringMVC的访问进行增强

### 快速上手

1. 创建拦截器（实现HandlerInterceptor）

   ![image-20230219103050487](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191030255.png)

   ```java
   package com.chen.controller.interceptor;
   
   import org.springframework.stereotype.Component;
   import org.springframework.web.servlet.HandlerInterceptor;
   import org.springframework.web.servlet.ModelAndView;
   
   import javax.servlet.http.HttpServletRequest;
   import javax.servlet.http.HttpServletResponse;
   
   /**
    * @author whyme-chen
    * @date 2022/4/27 19:27
    */
   @Component
   public class InterceptorDemo implements HandlerInterceptor {
       @Override
       public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
           System.out.println("preHandle........");
           return true;
       }
   
       @Override
       public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
           System.out.println("postHandle........");
       }
   
       @Override
       public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
           System.out.println("afterHandle........");
   
       }
   }
   ```

2. 配置拦截器

   ![image-20230219103131384](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191031403.png)

   ![image-20230219103308637](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191033662.png)

   ```xml
   <!--在SpringMVC配置文件中进行配置-->
   <mvc:interceptors>
       <mvc:interceptor>
           <mvc:mapping path="/**"/>
           <bean class="com.chen.controller.interceptor.InterceptorDemo"/>
       </mvc:interceptor>
   </mvc:interceptors>
   ```

   ```java
   //使用注解配置
   package com.chen.interceptor;
   
   import org.springframework.context.annotation.Configuration;
   import org.springframework.web.servlet.config.annotation.InterceptorRegistration;
   import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
   import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
   
   @Configuration
   public class LoginConfig implements WebMvcConfigurer {
       @Override
       public void addInterceptors(InterceptorRegistry registry) {
           InterceptorRegistration registration=
                   registry.addInterceptor(new LoginInterceptor());
           //拦截信息
           registration.addPathPatterns("/**");
           //不拦截信息
           registration.excludePathPatterns(
                   "/loginIn",
                   "/**/login.html",
                   "/**/*.js",
                   "/**/*.css",
                   "/**/images/*.*"
           );
   
       }
   }
   ```

#### 拦截器参数

![image-20220427200921912](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220427200921912.png)

![image-20230219103621141](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191036427.png)

![image-20230219103605664](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191036320.png)

![image-20230219103646624](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191036475.png)

#### 拦截器链

![image-20230219104044255](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202302191040323.png)

## REST风格

1. 简介

   REST（Representational State Transfer）,表现形式转态转换。

   * 传统风格资源描述形式
     * http://localhost/user/getById?id=1
     * http://localhost/user/saveUser
   * REST风格描述形式
     * http://localhost/user/1
     * http://localhost/user
   * 优点
     * 隐藏资源的访问行为，无法通过地址得知对资源是何种操作
     * 书写简化
   * 按照REST风格访问资源时使用**行为动作**区分对资源的操作
     * http://localhost/users查询全部用户信息 GET（查询）
     * http://localhost/users/1查询指定用户信息 GET
     * http://localhost/users添加用户信息 POST（新增或保存）
     * http://localhost/users修改用户信息 PUT（修改或更新）
     * http://localhost/users/1删除指定用户信息 DELETE（删除）
   * 根据REST风格对资源进行访问称为RESTful

2. 入门案例

   ![image-20220223213459243](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223213459243.png)

   请求路径参数

   ![image-20220223213435601](https://cdn.jsdelivr.net/gh/whyme-chen/Image/img/image-20220223213435601.png)