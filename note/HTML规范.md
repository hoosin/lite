HTML规范
---

##本文来源[请这样去写你的HTML](http://sofish.de/1688)

###1. 文档声明：<!Doctype>

其实这跟 WCAG 根本上连不上什么直接关系，但为了一个兼容性更好，特别是向后兼容的页面，我推荐你这样写：

```html
<!Doctype html>
```
 



###2. 链接：```<a>```

互联网的联几乎可以说是用 ```<a>``` 来实现的，作为一个页面最常见的标签。我们应该如何对待呢？

1. 为关键链接添加 accesskey

2. 除非万不得已，不要去掉 focus 时虚线框

```html
<a href="" title="" accesskey="M" rel="" hidefocus>Link</a>
```

###3. 缩写: <abbr>
对于用 HTML Tag 的正确使用，也是非常重要的，这有利于读屏软件使用者对于页面结构的理解。特别是在 H1,H2,H3 等这些标签的使用，滥用非常容易造成结构费解。当然，使用一般的标签，再利用 CSS 来使视觉上形成对比这也是常人能辨识的。但读屏软件用户呢。当然，这里只是顺带提起需要注意页面标签的使用方法，而 abbr 最重要的应该是应该添加一个 title 属性对缩写进行描述。比如：

```html
<abbr title="Web Developer" >WD</abbr>
```
###4. 大段引用: ```<blockquote>```，一般引用: ```<cite>```

有大段引用的时候，使用 ```<blockquote>```，而行内引用则使用 ```<cite>```，让你的结构更加易读：

```html
<blockquote>
    之前就一直想写这样的一篇文章，分享一下如何去创造一个可访问性更好的页面。今天的计划里有一条把 HTML Tag 和 WCAG 标准结合起来。我推荐你这样去写你的 HTML，让某些人的生活可以更容易。
</blockquote>

<p>某A给我印象最深刻的一句话是，<cite>“做前端要有爱。不要动不动就有朩有地对各种人使用咆哮体”</cite>。</p>
```

###5. 删除：<del>

在纸上写东西不能像在计算机上写东西一样，可以用撤销键可以按，但当我们想要强调某些东西是被删除的怎么办？那就是使用 <del> 标签了。比如这样：

```html
<del>HTML上表示强调时，请使用 <b> 标签</del>
HTML上表示强调时，请使用 <strong> 标签
```

效果是这样的：

`~~HTML上表示强调时，请使用 <b> 标签~~`

*HTML上表示强调时，请使用 <strong> 标签*

###6. 定义列表：<dl>

去年带着新人做支付宝前端博客的时候，他们给我印象最深刻的是很喜欢用 <dl>。当时在想，这些同学挺不错的，对语义化的理解还不错。我们还是比较少用到定义列表的。而是使用一般的 <ul> <ol> 这两个。<dl> 也是应该慎用的，最好只使用在某些有“定义”意义的条目，如 w3school 的这个例子，对咖啡和牛奶的定义：

```html
<dl>
  <dt>Coffee</dt>
    <dd>- black hot drink</dd>
  <dt>Milk</dt>
    <dd>- white cold drink</dd>
</dl>
```

###7. 无序/有序列表 <ul>/<ol>

列表，这个对于每个前端来说，都熟悉不过了。因为结构可以非常灵活地进行应用，在导航、列表、Tab 等，都经常要要用到。这个就无须多说了。但有一点还是需要明白的，不要相信什么 <ul>/<ol> 是 <table> 的替代品。在我们常用的 HTML Tags 中，每个标签都有自己的作用，谁都不是谁的替代品。

```html
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```

###8. 表格: <table>

如果是一个表格，那就，就不要用段落来替代，更不要用列表。除非万不得已，并且他们是可以转换的。另外，表格中还有一些需要注意的点：

给 <table> 添加 summary 属性，有些表格非常大，并不需要去读完整个
添加 <tbody>，如果我没记错，如果没添加的话，浏览器会自动为你添加
必要时使用 <col> <colgroup> 来控制表示的栏

```html
<table summary="sofish's blog status">
    <thead>
        <tr>
            <th>DATE</th>
            <th>IP</th>
            <th>PV</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2011.3.11</td>
            <td>3000</td>
            <td>8000</td>
        </tr>
    </tbody>
</table>
```

###9. 格式化片段 <code>/<pre>

<code> 是指 computer code text, 而 <pre> 是指 preformatted text。<pre> 的范围更广，并且是块状元素，可能被使用来格式化各种文本，特别是代码。使用没有需要特别注意的，主要是语义上的正确使用，比如不要用 <pre> 来代替一般的 <p>。

```html
<code>text-align:center</code>
<pre>
{ ( 1 * 102 ) + ( 9 * 101 ) + ( 3 * 100 ) }
</pre>
```

###10. 换行: <br>

在现代网页中，使用 <br> 的情况是非常少的。网页中的留白，一般都是使用 CSS 的 padding 和 margin 来实现。这样更精准，并用更容易控制。现在推荐的用法是，使用到一般的段落 <p> 中做简单的换行，而不是用来控制页面留白。

```html
<p>我是一个段落。<br />
诗歌都会用换行的。
</p>
###11. 分割线: <hr>
<hr> 具有非常好的语义作用。但他的视觉效果很难控制。之前就写过这样的文章关于<hr />在各浏览器中的问题。一般也都很少用。如果专门为读屏软件使用者提供单独页面的话，或许 <hr> 会大有用处。

<h3>标题一</h3>
<p>Lorem Ipsum is ...</p>
<hr />
<h3>标题二</h3>
<p>This is the entry of... </p>
```

###12. 无语义标签：<div>/<span>

其实 <div>/<span> 这两个标签是有语义的，都是 defines a section in a document。是的，和 HTML5 中的 <section> 其实是一样的。只是，因为搜索引擎的的原因，搜索引擎认为它们是无语义标签，因此他们成了 “无语义” 标签。推荐用法是尽量使用其他来做为页面框架的容器，比如布局、添加额外的视觉效果，而不是段落等的替代品。

```html
<div id="container">
    <div id="content">
    </div>
    <div id="sidebar">
        <ul>
            <li><span>God</span>, oh my zsh</span></li>
        </ul>
    </div>
</div>
```

###13. 段落/标题: <p>,<h1>/<h2>/<h3>…

这几个标签几乎可以说是一个页面标签等级结构中最重要的标签。我们可以用一本书的结构来说明这几个标签，而我们构建一个页面的时候，也应该有这样的一种思想在脑中：

书的名称：H1
书的每个章节标题: H2
章节内的文章标题: H3
章节的段落: P
小标题/副标题: H4/H5/H6
是的，当然还有引用 <blockquoute>，技术类书中提供的代码 <pre class="code">，一些需要注意点的列表 <ul>，一些方便比较的表格 <table> 等。

```html
<h1>LOGO</h1>
<h2>Title</h2>
<div class="entry">
    <h3>Summary:</h3>
    <p>lorem ipsum is ...<em>emphasize</em></p>
</div>
###14. 强调: <em>/<strong>
<em> emphasize 的缩写。而 <strong> 是 strong emphasize。可能很多刚入门前端的同学会对 <em>、<strong>、<cite> 、<i>、<b> 这几个标签的使用拿捏不准。<i> 和 <b> 基本上是被废置的，相当于现在的 <em> 和 <strong>，一般情况下他们对于内容重要性的排序是这样的：strong > em ≈ cite。 

<strong>注意：</strong>别使用老掉牙的标签，比如<cite>FONT、CENTER</cite>等，特别是 <em>FONT</em>。
###15. 表单项: <input>/<textarea>/<select>
表单项是 HTML 中相对比较复杂的标签，需要注意的点也比较多：

需要给每个表单项添加 <label> 对其进行描述，当不能使用 label 时，为表单项添加 title 属性
当表单项是必填项的时候，使用 “*“ 符号来标记
Flash 创建表单项一般是不会生成 <label> 的，请勾上 auto label 那个选项
<form method="post" action="http://sofish.de">
    <fieldset><legend>My Form</legend>
      <label for="firstname">* First name:</label> <input type="text" id="firstname" />
      <label for="speech">Say something:</label>
      <textarea id="speech" />
      </textare>
      <input type="submit" value="submit" title="submit button" />
    </fieldset>
</form>
```

###16. 图片: <img>

对于图片，盲人看不到。提供 alt 来表示替代文本。告诉他们这是一张什么样的图。

```html
<img src="http://sofish.de/favicon.ico" alt="幸福收藏夹的 favicon" />
```

###17. 框架: <iframe>

尽量避免 <iframe>框架的使用，但当你需要使用的时候，最好提供一个 title 属性对其进行描述。

```html
<iframe src="http://sofish.de" title="幸福收藏夹" /></iframe>
```
###18. 流媒体：<video>/<audio>/<object>/<embed>

媒体也是比较复杂的格式，处理起来比较麻烦。通常我们可以这样做：

为视听媒体提供相应的文本，包括相应的场景，比如演讲中的鼓掌等有利有阅读者感知现在气氛的，都应该体现在演讲文本中。其他的依此类推。
如果像交响乐这种不能提供具体描述的，可以进行简单的说明
如果文本较长，不能在当前页面展示，可以在媒体后提供一个链接到相应替代文本的链接
如果媒体中有可能会引起癫痫发作的，应做相应的说明

```html
<audio src="mozart.mp4">莫扎特39号交响曲</audio>
```

###19. 网页标题：<title>
网页中一定要包含标题，并且每个标签应该具有辨识性。比如支付宝中是这样体现的：

```html
<title>联系我 -- 幸福收藏夹</title>
```


###20. 总结
好吧。就先写到这里了。WCAG 并不只是这些简单的 HTML Tags 的用法，语义化的网页也不是一两篇文章能够写完的。慢慢来吧。从最常见的做起，养成好的习惯。回到文章前面的那句话，难道你忍心把页面写得这么难用吗？