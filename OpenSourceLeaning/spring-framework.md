官网地址：https://spring.io/projects/spring-framework

Github地址：https://github.com/spring-projects/spring-framework

gitee镜像：https://gitee.com/mirrors/spring-framework/tree/6.0.x/

源码下载：

* [IDEA 导入 spring 源码](https://blog.csdn.net/xhmico/article/details/130612527)

# 项目结构

# 源码分析

## IOC容器

1. bean的配置：定义bean的信息，名称、创建方式、依赖bean等

   bean的配置通常有两种方式，xml文件和注解。解析这两种方式的bean配置的基本思想和流程如下：

   ![image-20231121215341506](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202311212153334.png)

2. bean的加载

BeanDefinition

PostProcessor

* BeanPostProcessor->Bean
* BeanFactoryPostProcessor->BeanFactory