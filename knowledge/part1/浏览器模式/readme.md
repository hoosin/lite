# 浏览器模式

首先我们要知道，为什么会有这么多模式。其实这是个历史遗留问题，在浏览器大战时期，网景浏览器（Netscape Navigator）和微软的IE浏览器（Microsoft Internet Explorer）对网页分别有不同的实现方式，那个时候的网页要针对这两种浏览器分别开发不同的版本。而到了W3C制定标准之后，这些浏览器就不能继续使用这种页面了，因而会导致大部分现有站点都不能使用。基于这个原因，浏览器才引入两种模式来处理一些遗留的站点。

__现在的浏览器排版引擎支持三种模式：__

1. 怪异（Quirks）模式：在怪异模式中，排版引擎会模拟 网景4和Windows中的IE5的行为。
2. 准标准（Almost Standards）：在准标准模式中，则只包含很少的一部分怪异模式中的行为。
3. 标准（Standards）模式：在完全标准的模式中，会尽量执行HTML和CSS规范所指定的行为。

__各主流浏览器对三种模式的描诉：__

- FireFox：[Mozilla's DOCTYPE sniffing](https://developer.mozilla.org/en-US/docs/Mozilla's_DOCTYPE_sniffing)
- Opera：[DOCTYPE Switches support in Opera](http://www.opera.com/docs/specs/doctype/)
- IE：[Defining document compatibility](http://msdn.microsoft.com/en-us/library/cc288325(v=vs.85\).aspx) ([中文](http://msdn.microsoft.com/zh-cn/library/cc288325(v=vs.85\).aspx))

------

## 模式详解

### 内容类型为text/html的模式

1. 怪异模式（Quirks Mode）
    * 怪异模式中，为了避免“破坏”那些根据在20世纪90年代末流行的实践创作的页面，浏览器违反了现代的Web格式规范。<br>
不同的浏览器实现了不同的怪异行为。Internet Explorer6、7和8中，怪异模式有效地冻结在IE5.5 。其他浏览器中，怪异模式是对准标准模式的少量偏移。<br>
__如果正在创作新网页，你应该符合相关的规范（特别是CSS2.1）且使用标准模式。__

2. 标准模式（Standards Mode）
    * 标准模式中，浏览器尝试给符合标准的文档在规范上的正确处理达到在指定浏览器中的程度。<br>
不同的浏览器遵循不同的阶段，所以标准模式也不是一个单一目标。<br>
HTML5把这种模式叫“非怪异模式（no quirks mode）”

3. 准标准模式（Almost Standards Mode）
    * Firefox、Safari、Chrome、Opera(从7.5开始)和IE8也有个叫“准标准模式”的模式，它按照传统的做法来实现表格单元格的垂直尺寸而不是严格的遵照CSS2规范。<br>
Mac IE5、Windows IE6和7、Opera7.5以前版本和Konqueror无需准标准模式，因为它们至少没有在各自的标准模式下严格遵循CSS2规范来实现表格单元格垂直尺寸。实际上，它们的标准模式更接近Mozilla的准标准模式而不是Mozilla的标准模式。<br>
HTML5把这种模式叫着“受限怪异模式(limited quirks mode)”。


### 内容类型为application/xhtml+xml的模式（XML模式）

- Firefox、Safari、Chrome和Opera中，application/xhtml+xml HTTP内容类型（不是meta元素也不是doctype!）会触发XML模式。<br>
在XML模式中，浏览器尝试给XML文档在规范上的正确处理达到在制定浏览器中的程度。

- IE6、7和8不支持application/xhtml+xml，Mac IE5也如此。


### 非Web模式（Non-Web Modes）

某些引擎拥有的模式与Web内容无关。<br>
例如：Opera有个WML2.0模式。Leopard上的WebKit有个用于旧式Dashboard widgets的特定模式。


## 模式的影响

### 布局

1. text/html的模式主要是影响CSS布局。例如：
    * 怪异模式下表格不继承样式。
    * 在某些浏览器的怪异模式下，盒模型（box model）变成IE5.5的盒模型。
    * 在IE的怪异模式中，元素的width包含了padding和border，而标准模式中padding和border 并不属于宽度的一部分。
    * [最初的准标准模式](http://meyerweb.com/eric/thoughts/2008/01/24/almost-target/)只会[影响表格中的图像](https://developer.mozilla.org/en-US/docs/Images,_Tables,_and_Mysterious_Gaps)（包含图片的表格单元格的高和标准模式中不同），而后来各个浏览器又或多或少地进行了修改。
2. XML模式中，选择器有不同的区分大小写行为。此外，用于HTML body元素的特有规则不能应用在那些没有实现最新CSS2.1改变的较旧版本的浏览器。

### 解析

也有一些怪异影响HTML和CSS的解析且会导致符合标准的网页被错误解析。了解怪异模式和标准模式在CSS布局和解析（非HTML解析）上的主要异同是非常重要的。

一些人错误地把标准模式称为“严格解析模式（strict parsing mode）”，其让人误解了浏览器强制执行HTML语法规则和用浏览器评估标记的正确性。情况并非如此。即使当标准模式布局生效时，浏览器依旧会做[tag soup](http://en.wikipedia.org/wiki/Tag_soup)修正工作。（在2000年Netscape6发布前，Mozilla的确有用于强制执行HTML语法规则的解析模式。这些模式和现有的Web内容不兼容而被遗弃。）

另一个常见的误解是关于XHTML解析的。通常认为用XHTML doctype得到不同的解析。其实并非如此，内容类型是text/html的XHTML文档所用解析器和HTML文档的是同一个。目前浏览器在意的是文档类型为text/html的XHTML仅是“tag soup with croutons”（额外的斜线，闭合"/>"）。<br>
仅当使用XML文档类型的文档（例如：application/xhtml+xml或xmapplication/）会触发XML模式来解析，这时的解析器完全不同于HTML解析器。

### 脚本

虽然怪异模式主要是关于CSS的，但也有一些是关于脚本的。例如，Firefox的怪异模式中，HTML id 属性像在IE一样建立了全局脚本作用域的对象引用。IE8中关于脚本的影响比其他浏览器更值得关注。

XML模式中，某些DOM API的行为彻底不同，因为XML的DOM API行为被定义时不兼容HTML的行为。


## IE的模式

IE8有4种模式：IE5.5怪异模式、IE7标准模式、IE8准标准模式和IE8标准模式，<br>
而IE9有7种模式：IE5.5怪异模式、IE7标准模式、IE8准标准模式、IE8标准模式、IE9准标准模式、IE9标准模式、XML模式。

### IE9的浏览器模式和文档模式

如果你使用的是IE9，那么按下F12键就会出现开发者工具，上面有两个下拉菜单：浏览器模式和文档模式。那么什么是浏览器模式？什么又是文档模式？二者有何区别？

* 浏览器模式用于切换IE针对该网页的默认文档模式、对不同版本浏览器的条件注释解析、以及发送给网站服务器的用户代理（User-Agent）字符串的值。网站可以根据浏览器返回的不同用户代理字符串判断浏览器的版本和及安装的功能，这样就可以根据不同的浏览器返回不同的页面内容了。

* 文档模式用于指定IE的页面排版引擎（Trident）以哪个版本的方式来解析并渲染网页代码。切换文档模式会导致网页被刷新，但不会更改用户代理字符串中的版本号，也不会从服务器重新下载网页。切换浏览器模式的同时，浏览器也会自动切换到相应的文档模式。

一言以蔽之，浏览器模式会影响服务器端对客户端浏览器版本的判断，对条件注释也有影响；而文档模式会影响IE的排版引擎，对网页渲染会有影响，对CSS hack也会产生影响。因此，通过条件注释可以判断浏览器模式，而使用CSS hack可以判断文档模式。

### IE9兼容性视图与IE9标准视图

如果我们使用一句简单的JavaScript语句来查看用户代理（User-Agent）字符串的值，则可以看到IE9兼容性视图与IE9的区别：

    alert('UA:'+navigator.userAgent);  

输出结果如下所示，注意其中的MSIE版本号已经不同。判断浏览器模式就是判断User-Agent中的版本号，即MSIE后面的数值：

    // IE9  
    UA:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; Tablet PC 2.0)  
     
    // IE9 兼容性视图  
    UA:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; Tablet PC 2.0) 
     
    //真实IE7
    Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)

话说IE9兼容性视图是模拟IE7的行为，那么IE9兼容性视图与IE7有没有区别呢？<br>
肯定是有区别的，即使是IE9中的IE7标准模式，与原生的IE7在渲染上也是有区别的，具体我们暂不去深究。

那么既然IE9兼容性视图的版本号跟IE7相同，如何才能判断当前是IE9兼容性视图，还是纯正的IE7呢？<br>
其实很简单，只需要判断浏览器的用户代理（User-Agent）字符串中是否包含Trident即可。<br>
首先检测MSIE的版本号是否为7.0，然后再判断是否含有Trident字串，若包含则为IE9兼容性视图，否则则为纯正的IE7。

### 文档模式的检测

在JavaScript中可以通过documentMode来检测文档模式，在IE6和IE7中是使用compatMode来确定文档模式的，这个属性自IE8开始已经被documentMode所替代。
```javascript
engine = null;  
if (window.navigator.appName == "Microsoft Internet Explorer")  
{  
    // This is an IE browser. What mode is the engine in?  
    if (document.documentMode) // IE8 or later  
        engine = document.documentMode;  
    else // IE 5-7  
    {  
        engine = 5; // Assume quirks mode unless proven otherwise  
        if (document.compatMode)  
        {  
            if (document.compatMode == "CSS1Compat")  
                engine = 7; // standards mode  
        }  
        // There is no test for IE6 standards mode because that mode  
        // was replaced by IE7 standards mode; there is no emulation.  
    }  
    // the engine variable now contains the document compatibility mode.  
} 
```

## 参考资料

- [深入理解浏览器兼容性模式](http://www.csdn.net/article/2012-10-22/2811049-Understanding-the-browser-compatibility-)
- [用doctype激活浏览器模式](http://dancewithnet.com/2009/06/14/activating-browser-modes-with-doctype/)([英文原版](http://hsivonen.iki.fi/doctype/))
