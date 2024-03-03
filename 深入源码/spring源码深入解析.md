# 前期准备

1. 构建工具：**gradle**下载、安装及使用

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

2. idea

# 资料

源码地址：

* github：https://github.com/spring-projects/spring-framework
* gitee：https://gitee.com/mirrors/Spring-Framework

相关学习参考：

1. [Spring源码深度解析之通篇死磕Spring源码](https://segmentfault.com/a/1190000022372094)
2. [Java/Spring源码深度解析.pdf](https://github.com/wususu/effective-resourses/blob/master/Java/Spring%E6%BA%90%E7%A0%81%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90.pdf)
3. https://www.ddkk.com/zhuanlan/j2ee/spring/7/1.html