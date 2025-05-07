官网：https://sa-token.cc/index.html

# SpringBoot集成

1. 导入依赖

   ```xml
   <!-- Sa-Token 权限认证，在线文档：https://sa-token.cc -->
   <dependency>
       <groupId>cn.dev33</groupId>
       <artifactId>sa-token-spring-boot-starter</artifactId>
       <version>1.35.0.RC</version>
   </dependency>
   ```

2. 配置

   ~~~yml
   server:
       # 端口
       port: 8081
       
   ############## Sa-Token 配置 (文档: https://sa-token.cc) ##############
   sa-token: 
       # token 名称（同时也是 cookie 名称）
       token-name: satoken
       # token 有效期（单位：秒） 默认30天，-1 代表永久有效
       timeout: 2592000
       # token 最低活跃频率（单位：秒），如果 token 超过此时间没有访问系统就会被冻结，默认-1 代表不限制，永不冻结
       active-timeout: -1
       # 是否允许同一账号多地同时登录 （为 true 时允许一起登录, 为 false 时新登录挤掉旧登录）
       is-concurrent: true
       # 在多人登录同一账号时，是否共用一个 token （为 true 时所有登录共用一个 token, 为 false 时每次登录新建一个 token）
       is-share: true
       # token 风格（默认可取值：uuid、simple-uuid、random-32、random-64、random-128、tik）
       token-style: uuid
       # 是否输出操作日志 
       is-log: true
   
   ~~~

## 方法深入

~~~java
// 会话登录：参数填写要登录的账号id，建议的数据类型：long | int | String， 不可以传入复杂类型，如：User、Admin 等等
StpUtil.login(Object id);  

// 当前会话注销登录
StpUtil.logout();

// 获取当前会话是否已经登录，返回true=已登录，false=未登录
StpUtil.isLogin();

// 检验当前会话是否已经登录, 如果未登录，则抛出异常：`NotLoginException`
StpUtil.checkLogin();
~~~

