RuoYi官网：[RuoYi](https://www.ruoyi.vip/)

官方文档：[RuoYi-Vue](https://doc.ruoyi.vip/ruoyi-vue/)

Gitee地址：https://gitee.com/y_project/RuoYi-Vue.git

# 项目运行

## 后端

1. 环境搭建
   * JDK
   * Maven
   * MySQL
   * Redis
   * node
2. 创建数据库
3. 修改配置
   * mysql
   * redis

## 前端

# 登录

## 生成验证码

1. 思路分析

   > 后端生成一个表达，将正确答案存入redis，前端点击登录按钮是将数据验证码与redis中存入验证码进行对比

2. 前端实现

   > 反向代理，url 请求前端，进行代理，映射到后端，解决跨越问题

3. 后端实现

   > 校验验证码
   >
   > 校验用户名和密码
   >
   > 生成token

# 发生成word文件

# 主题样式修改

参考：https://blog.csdn.net/Bonjours/article/details/119640456