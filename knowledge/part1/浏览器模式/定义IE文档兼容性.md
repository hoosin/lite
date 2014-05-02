# 定义IE文档兼容性

## IE下的模式

IE8有4种模式：IE5.5怪异模式、IE7标准模式、IE8准标准模式、IE8标准模式。<br>
IE9有7种模式：IE5.5怪异模式、IE7标准模式、IE8准标准模式、IE8标准模式、IE9准标准模式、IE9标准模式、XML模式

__模式的选择取决于来自几个方面的数据：__

1. meta标签：<meta http-equiv="X-UA-Compatible" content="...">
2. HTTP头：设置X-UA-Compatible
3. doctype：<!DOCTYPE ....>
4. 来自微软的定期下载数据：[其实是个黑名单，其中指定了一组始终使用兼容性视图显示的网站](http://msdn.microsoft.com/en-us/library/dd567845(v=VS.85\).aspx)
5. 局域网域：局域网管理员可以把该站点放置到[黑名单](http://go.microsoft.com/fwlink/?LinkId=145413)上（始终使用兼容性视图）
6. 用户所做设置：可以使用开发人员工具覆盖在该网页中指定的设置
7. 兼容视图：用户可以触发地址栏兼容视图按钮
8. 父框架的模式：（如果有）页面通过frame嵌入到其他页面中

上述除两个关于X-UA-Compatible的情况外，4-8没有设置，IE8则会进行正常流程的doctype嗅探。<br>
不幸的是，没有X-UA-Compatible的HTTP头或meta标签，即使使用了合适的doctype，IE8让用户无意间使页面从IE8的标准模式降到IE7模式，这是一种仿真的IE7标准模式。更糟糕的是，局域网管理员也可以这么做。微软也可以把你所用的所有域名到列入黑名单。<br>
为了对付这些影响，doctype是不够的，你需要X-UA-Compatible HTTP头和meta标签。


## 指定文档兼容性模式：使用X-UA-Compatible 

IE 浏览器支持多种文档兼容模式，得以因此改变页面的渲染效果。<br>
为了帮助确保网页在将来的 Internet Explorer 版本中具有一致的外观，Internet Explorer 8 引入了文档兼容性。 <br>
文档兼容性是对 Microsoft Internet Explorer 6 中引入的兼容性模式的扩展，使开发者可以选择 Internet Explorer 用于显示网页的特定呈现模式。

```html
<!-- IE9 模式支持全范围的既定行业标准，包括 HTML5（草案）, W3C CSS Level 3 规范（草案）, SVG 1.0 规范等 -->
<meta http-equiv="X-UA-Compatible" content="IE=9">

<!-- IE8 模式支持许多既定行业标准，W3C CSS Level 2.1 规范和 W3C Selectors API，有限支持 W3C CSS Level 3 规范（草案）和其他行业标准 -->
<meta http-equiv="X-UA-Compatible" content="IE=8">

<!-- IE7 模式强制浏览器按照 IE 7 标准模式渲染文档，忽略是否定义指令 -->
<meta http-equiv="X-UA-Compatible" content="IE=7">

<!-- Emulate IE9 模式告诉 IE 使用指令来决定如果渲染文档。
标准模式下以 IE9 渲染，怪异模式下以 IE5 渲染。和 IE9 模式不同的是，Emulate IE9 模式会考虑指令 -->
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9">

<!-- Emulate IE8 模式告诉 IE 使用指令来决定如果渲染文档。
标准模式下以 IE8 渲染，怪异模式下以 IE5 渲染。和 IE8 模式不同的是，Emulate IE8 模式会考虑指令 -->
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE8">

<!-- Emulate IE7 模式告诉 IE 使用指令来决定如果渲染文档。
标准模式下以 IE7 渲染，怪异模式下以 IE5 渲染。和 IE7 模式不同的是，Emulate IE7 模式会考虑指令。
对于大多数站点而言，这是首选的兼容模式 -->
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7">

<!-- IE5 模式告诉 IE7 是否以怪异模式渲染文档 -->
<meta http-equiv="X-UA-Compatible" content="IE=5">

<!-- Edge 模式告诉 IE 以最高级模式渲染文档，也就是任何 IE 版本都以当前版本所支持的最高级标准模式渲染，避免版本升级造成的影响。
简单的说，就是什么版本 IE 就用什么版本的标准模式渲染 -->
<meta http-equiv="X-UA-Compatible" content="IE=edge">

<!-- 使用以下代码强制 IE 使用 Chrome Frame 渲染 -->
<meta http-equiv="X-UA-Compatible" content="chrome=1">

<!-- 最佳的兼容模式方案，结合考虑以上两种： -->
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
```

__注：__

1. 把X-UA-Compatible写在`<link>`或`<script>`标签下面，X-UA-Compatible的设置无效。
2. 页面、服务器HTTP Header都设置了X-UA-Compatible的情况，使用页面的X-UA-Compatible设置。页面无X-UA-Compatible，才使用HTTP Header设置的值。
3. IE=xx的值，ie会尝试xx转换为最接近的值。比如：IE=7.789 -> IE=7；介于5、6之间的->IE=5。
4. IE=4、IE=3、IE=0.1、IE=-7 这些小于5的，包括类似IE=IE8、IE=IE7、IE=IE6、IE=a、IE=b、IE=bcd，和无X-UA-Compatiblesh是一样。可以理解为X-UA-Compatible设置了无效的值，所以跳过这里了。

__参考资料：__

- [定义文档兼容性](http://msdn.microsoft.com/zh-cn/library/cc288325.aspx)
- [关于ie8兼容性视图(English)](http://blogs.msdn.com/b/ie/archive/2009/02/16/just-the-facts-recap-of-compatibility-view.aspx)


### 关于Chrome Frame

Google Chrome Frame（Google Chrome內嵌框架）是专为Internet Explorer设计的一个插件。<br>
这插件可运行于Windows 7、Vista、XP SP2或更高版本操作系统中的Internet Explorer 6、7、8、9，使Internet Explorer可以基于谷歌瀏覽器中的Webkit引擎及V8引擎进行排版及运算，即能令Internet Explorer 6、7、8支持HTML5代码。<br>

开发原意是使不支持HTML5的Internet Explorer也能浏览Google Wave及其它使用了HTML5代码的Google服务。

网页设计员可以在网页中加入以下代码使网站能以Chrome Frame浏览：
```html
<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=IE8">
<!-- 若浏览者有安装Chrome Frame，且浏览者的IE浏览器版本为IE8或更低，此代码会自动引导浏览器激活插件进行排版及运算；
但若浏览者并没有安装插件或IE版本为IE9或更高，则不会进行任何动作。 -->
```

__参考资料：__

- [百度百科](http://baike.baidu.com/view/2831140.htm)<br>
- [维基百科](http://zh.wikipedia.org/wiki/Google_Chrome_Frame)<br>
- [Google Chrome Frame](https://developers.google.com/chrome/chrome-frame/)

## IE模式选择流程图：
![IE模式选择流程图](http://hsivonen.iki.fi/doctype/ie8-mode.png)


