# HTML Email 规范

- pubdate: 2013-4-24 11:48:51
- tags: html, email, standard
- status: draft

----------------

## 邮件环境

邮件内容所在上下文或者说所在外部容器（以下简称环境）都是由邮箱服务商决定的，这就要求邮件内容需要在任何一种情况下都要正确显示。
这些环境可能是以下某几种情况：

- 可能是个iframe，你的内容是被放在body里面的；可能只是个div，你的内容就被放在这个div里面。
- 可能邮箱自身设置了些css，他可能对你产生未知的影响。
- 可能根本没有申明doctype，即使申明了，也不是你想要的doctype。

## 避免被嵌套在不正确的容器里

惑：因为容器可能是body或div，所以，我们邮件内容不应该是一个完整的html。

解：所以邮件内容应该是以div为根节点的html片段。

## 避免css冲突或被覆盖

惑：因为环境中可能已经设置了css，比如一些reset、一些.class。

解：所以我们只能使用行内style来确保我们的效果，并且在内容根节点上设置基础style，并且尽量使用div、span等无语义标签。

    <!-- 根节点 -->
    <div style="width:600px;text-align:left;color:#000;font:normal 12px/15px arial,simsun;background:#fff;">
        内容区域
    </div>
    <!-- 根节点-邮件内容居中 -->
    <div style="text-align:center;">
        <div style="width:600px;margin:0 auto;text-align:left;color:#000;font:normal 12px/15px arial,simsun;background:#fff;">
            内容区域
        </div>
    </div>
    <!-- 如果使用语义化标签，那么需要多写一些style，以避免被环境中的css覆盖 -->
    <h2 style="width:100px;height:100px;margin:0;padding:0;fong-weight:normal;font-size:12px;"></h2>
    <!-- 而使用无语义标签，就可以省下很多style -->
    <div style="width:100px;height:100px;"></div>

## 避免盒模型错误

惑：因为doctype的不确定性，我们在写style的时候，应该考虑无论doctype是什么情况，都可以正常显示，doctype影响最大的就是盒模型的解析。

解：所以我们要将盒模型拆分开来写，比如我们将原本要定义在某个div上的height和padding分别写到这个div和他的父元素或子元素上。

    <div style="height:100px;padding:20px 0;">内容</div>
    <!-- 上面的写法应该改成以下写法 -->
    <div style="padding:20px 0;"><div style="height:100px;">内容</div></div>

## 其他注意事项

- 因为只能使用行内style，所以清除浮动需要使用额外标签。
- 避免使用绝对定位，可能会被过滤。
- 避免使用js，可能会被过滤。
- 避免使用table布局，不易于修改维护。
- 背景图片或内容图片上的文字信息，必须在代码中可见。
- 如果没有特殊要求，所有a链接都要从新窗口打开，即target="_blank"，且a标签内容不能为空。
- 所有链接必须设置使用颜色、是否下划线，即style="text-decoration:;color:;"。
- 重点检查ie！！！

## 发现的问题及解决方案

问题：部分智能手机的邮件客户端可能会有只显示部分的bug（宽度被截）。

解决：在外面套一个同宽的table即可。

    <table width="600" cellpadding="0" cellspacing="0" border="0"><tr><td>
        <div style="width:600px;text-align:left;color:#000;font:normal 12px/15px simsun;background:#d9d9d9;">
            ......
        </div>
    </td></tr></table>

## 使用框架

推荐使用 [email框架](http://nec.netease.com/framework/html-email.html) 来创建邮件内容。