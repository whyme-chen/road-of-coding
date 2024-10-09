# GraphQL

参考：
* [GraphQL 官方文档](https://graphql.org/learn/)
* [GraphQL | A query language for your API](https://graphql.cn/)
* https://www.freecodecamp.org/chinese/news/a-detailed-guide-to-graphql/

## 简介
1. 简介：一个用于 API 的查询语言，是一个使用基于类型系统来执行查询的服务端运行时（类型系统由你的数据定义）。GraphQL 并没有和任何特定数据库或者存储引擎绑定，而是依靠你现有的代码和数据支撑。
2. 重要概念
   * 字段
     
   * 参数
     
   * 别名
     
   * 片段：可复用单元
     
   * 操作类型（Operation Type）：描述客户端希望进行什么样的操作，包括查询（query）、订阅（subscription）、变更（mutation）
     
     * 查询（query）：获取数据， 比如查找，CRUD 中的 R 
     * 变更（mutation）：对数据进行变更，比如增加、删除、修改，CRUD 中的 CUD
     * 订阅（subscription）：订阅数据，当数据变化时，进行消息推送
     
     ~~~graphql
     query {
       user { id }
     }
     ~~~
     
   * 变量：查询语句中的动态值
   
     * 使用
       * 使用 `$variableName` 替代查询中的静态值。
       * 声明 `$variableName` 为查询接受的变量之一。
       * 将 `variableName: value` 通过传输专用（通常是 JSON）的分离的变量字典中。
       * 可以通过在查询中的类型定义后面附带默认值的方式，将默认值赋给变量。
     * 所有声明的变量都必须是标量、枚举型或者输入对象类型。
   
     ~~~graphql
     # {
     #    "id": "66e3d32743e5283017a190cc",
     #    "example": {
     #        "tags": [
     #            "tag"
     #        ],
     #        "messageConditions": [
     #            {
     #                "key": "comments.commentId",
     #                "operator": "like",
     #                "value": "c"
     #            }
     #        ]
     #    }
     # }
     query GetLogs($id: ID! = "0", $example: LogFindReq) {
         findLogById(id: $id) {
             id
             scene
             timestamp
             tags
             message
         }
         findLogsWithExample(logFindReq: $example) {
             id
             scene
             level
             timestamp
             tags
             message
         }
     }
     ~~~
   
   * 指令：附着在字段或者片段包含的字段上，然后以任何服务端期待的方式来改变查询的执行。
     
     * 核心规范
       * `@include(if: Boolean)` 仅在参数为 `true` 时，包含此字段。
       * `@skip(if: Boolean)` 如果参数为 `true`，跳过此字段。
     
   * 模式（Schema）：定义了字段的类型、数据的结构，描述了接口数据请求的规则
     
  * Schema 使用一个简单的强类型模式语法，称为模式描述语言（Schema Definition Language, SDL） 
     ~~~graphql
     # Query 入口
     type Query {
         hello: String
         users: [User]!
         user(id: String): [User]!
     }
     
     # Mutation 入口
     type Mutation {
         createUser(id: ID!, name: String!, email: String!, age: Int,gender: Gender): User!
         updateUser(id: ID!, name: String, email: String, age: Int, gender: Gender): User!
      deleteUser(id: ID!): User
     }
     
     # Subscription 入口
     type Subscription {
         subsUser(id: ID!): User
     }
     
     type User implements UserInterface {
         id: ID!
         name: String!
         age: Int
         gender: Gender
         email: String!
     }
     
     # 枚举类型
     enum Gender {
         MAN
         WOMAN
     }
     
     # 接口类型
     interface UserInterface {
         id: ID!
         name: String!
         age: Int
         gender: Gender
     }
     ~~~
     
   * 对象类型（Object Type）：描述客户端想要获取的数据，包括字段（field）和关联（relation）
     
     * 用户在 schema 中定义的 type
     * 如果一个 GraphQL 服务接受到了一个 query，那么这个 query 将从 Root Query 开始查找，找到对象类型（Object Type）时则使用它的解析函数 Resolver 来获取内容，如果返回的是对象类型则继续使用解析函数获取内容，如果返回的是标量类型（Scalar Type）则结束获取，直到找到最后一个标量类型。
     ~~~graphql
      type User {
          id : ID
          name: String!
          age: Int
     }
     ~~~
     
   * 标量类型（Scalar Type）：描述客户端想要获取的数据的**基本类型**（查询的叶子节点）
     * GraphQL 中内置有一些标量类型，包括：
       * 字符串（String）：UTF‐8 字符序列
       * 布尔值（Boolean）：true` 或者 `false
       * 整数（Int）：有符号 32 位整数
       * 浮点数（Float）：有符号双精度浮点值
       * ID（ID）：ID 标量类型表示一个唯一标识符，通常用以重新获取对象或者作为缓存中的键。ID 类型使用和 String 一样的方式序列化；然而将其定义为 ID 意味着并不需要人类可读型。
     * 用户也可以定义自己的标量类型
     
   * 枚举类型
   
   * 接口类型
   
   * 联合类型
   
     * 联合类型的成员需要是具体对象类型，不能使用接口或者其他联合类型来创造一个联合类型。
     
   * 解析函数（resolver）：前端请求信息到达后端之后，需要由解析函数 [Resolver](https://link.juejin.im/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Fgraphql-tools%2Fresolvers.html) 来提供数据
   
     ~~~graphql
     # query
     query {
       hello
     }
     # 同名解析函数
     Query: {
       hello (parent, args, context, info) {
         return ...
       }
     }
     ~~~
   
     * `parent`：当前上一个解析函数的返回值
     * `args`：查询中传入的参数
     * `context`：提供给所有解析器的上下文信息
     * `info`：一个保存与当前查询相关的字段特定信息以及 schema 详细信息的值

## GraphQL服务