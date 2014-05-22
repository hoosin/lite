# cyou-framework 使用规范

- pubdate: 2013-6-18 16:01:51
- tags: standard
- status: draft

----------------

> 前端在做页面时，需要从设计师的 UI 文件中切图。为了使我们工作协作更加顺畅和高效，这里提出一些建议。
> 有些时候，设计师一个小小的改进，会给我们前端带来极大的方便。

##  工具类使用规范 ##

工具类从 Apache Commons, Google Guava, Spring 中筛选.

+ StringUtility

    有关String操作的都请使用该工具类, 该工具类继承并扩展了 Apache Commons Lang3的StringUtils.

+ TemplateUtility

    充当简易模板引擎的功能，主要处理模板和数据的结合并输出处理结果。

+ ReflectionUtility

    三家的Reflections类都不够粗暴, 不能完全无视private/protected修饰符强制访问. 因此自己实现.

+ CollectionUtility

    Guava中一些, Apache Commons的有点太老, 尽量不用吧. 所以自己封装.

+ Apache Commons Lang3 Validate, Assert防御式编程

    选用Apache Commons Lang的Validate. Spring的Assert容易和JUnit的混淆, 
    而且校验函数没有返回输入参数的能力, 出错信息也没有格式化字符串+自定义参数的能力.
    而Guava的类名叫Preconditions太长太怪，所以最后选了Apache的。

+ DateUtility 时间处理

    Joda-Time优先。

+ EncodeUtility

    Commons-Codec的 hex/base64 编码
    自制的base62 编码
    Commons-Lang的xml/html escape
    JDK提供的URLEncoder

+ IdentityUtility

    封装各种生成唯一性ID算法的工具类：uuid, uuid2...

+ PropertiesLoader

    Properties文件载入工具类. 仿造Spring编写，可载入多个properties文件, 相同的属性在最后载入的文件中的值将会覆盖之前的值，但以System的Property优先. Path可以是classpath，绝对路径file或者web-inf/

+ IOUtils(Apache Commons)

    IO工具类.

+ ThreadUtility

    只封装了两类函数： 一个是sleep函数，屏蔽了InterruptedException的异常. 一个是仿照JDK的shutdown/shutdownNow中的注释，提供了一个有超时控制，而且先尝试shutdown，超时了再尝试shutdownNow的gracefulShutdown()函数.

+ Concurrency

    JDK自带，Google补充，还有自己也写了个ThreadUtility.

+ Resource

    Spring的Resource, 可以方便加载文件路径, Classpath路径和Web App内路径的内容.

+ Dozer

    异构对象间的复制拷贝.