# HTML 规范

- pubdate: 2013-4-23 16:56:53
- tags: html, standard
- status: draft

----------------

## for W3C

- 标签名全小写。
- 属性名由小写字母、数字和下划线组成。
- 标签是否应当关闭？
    - <del>所有标签必须关闭，比如 `<br />` 或 `<hr />`。</del> 
    - 可选关闭标签应当关闭。
    - 自动关闭标签不必要关闭。推荐 `<br>` ，不推荐 `<br />` 。
- 属性值必须用双引号包括，比如 `<img src="example.png" width="30" />`。
- 没有值的属性必须使用自己的名称做为值，如 `checked` 、 `disabled` 、 `readonly` 、 `selected` 等。
- 避免使用 `<center>` 、 `<font>` 、 `<u>` 、 `<s>` 、 `<strike>` 、 `<menu>` 、 `<dir>` 、 `<applet>` 等标签。
- 需要添加自定义属性时，使用 `data-` 作为前缀，比如 `<img src="blank.gif" data-src="pic01.jpg" />`。
- 内联元素中不可嵌套块级元素。
- `script` 标签上不必写 `type` 和 `language` 。
- `style` 标签 和 `link` 标签上不必写 `type` 。
- 避免链接重定向，如 `<a href="http://www.baidu.com/">baidu</a>` ，即需要在 URL 地址后面加上 `/` 。

## 整体结构

### 文档模板

- 文件以 `<!DOCTYPE html>` 首行顶格开始。
- 必须申明文档编码 `charset` ，且与文件本身编码一致，推荐使用 `<meta charset="utf-8"/>` ，并置于 `<head>` 的第一行。
- `title` 极为重要，紧跟在 `charset` 之后。
- 编写恰当的 `keywords` 和 `description` 。
- css 置于 head 中，文件数要尽可能少。
- js 置于 body 底部，文件数要尽可能少。

### 结构顺序和视觉顺序基本保持一致

- 按照从上至下、从左到右的视觉顺序书写HTML结构。
- But ，有时候为了便于搜索引擎抓取，我们也会将重要内容在 HTML 结构顺序上提前。
- 用div代替table布局，可以使HTML更具灵活性，也方便利用CSS控制。
- table不建议用于布局，但表现具有明显表格形式的数据，table还是首选。

### 保持良好的简洁的树形结构

- 使用空格缩进，避免使用 Tab 缩进，空格大小为 4 。
- `<html>` 、`<body>` 、`<script>` 、`<style>` 标签不缩进，其他所有标签缩进
- 每一个块级元素都另起一行，每一行都缩进对齐。
- 删除冗余的行尾的空格。
- 对于内容较为简单的表格，建议将tr写成单行。
- 可以在大的模块之间用空行隔开，使模块更清晰。

### 注释规范

- `<!-- 注释内容 -->` 。
- “注释内容” 区域不可包含 `-` 。
- 只允许使用单行HTML注释。
- HTML 注释最好不要使用在代码上，可以使用模板语言本身的注释。
- 给代码块及重要功能（如 loop）加上注释，方便后台套接页面。
- 两个浮动元素之间不允许编写 HTML 注释 （*for IE6 Bug*） 。

代码示例：

    <!-- 头部 begin -->
    <div class="container">
        <!-- LOGO begin -->
        <h1><a href="#">Chang You</a></h1>
        <!-- LOGO end -->
        <!-- 导航 begin -->
        <ul class="nav">
            <li><a href="#">About US</a></li>
            <li><a href="#">News</a></li>
            <!-- 更多导航项 -->
        </ul>
        <!-- 导航 end -->
    </div>
    <!-- 头部 end -->

### 其他

- 尽可能减少 div 嵌套，多考虑平级而非嵌套结构。如果可以写成 `<div></div><div></div>` 那么就不要写成 `<div><div></div></div>` 。
- 如果结构已经可以满足视觉和语义的要求，那么就不要有额外的冗余的结构。比如 `<div><h2></h2></div>` 已经能满足要求，那么就不要再写成 `<div><div><h2></h2></div></div>` 。
- 一个标签上引用的className不要过多，越少越好。比如不要出现这种情况： `<div class="class1 class2 class3 class4"></div>` 。
- 对于一个语义化的内部标签，应尽量避免使用className。比如在这样一个列表中，li标签中的itm应去除： `<ul class="m-help"><li class="itm"></li><li class="itm"></li></ul>` 。

## 内容语义

- 在网页中某种类型的内容必定需要某种特定的 HTML 标签来承载，也就是我们常常提到的根据你的内容语义化 HTML 结构。
    - 合理利用 `<img />` 和 `background-image` 。
    - 标题用 `h*` ，段落用 `p` ，列表用 `ul` 。
    - 表单元素的描述性内容需要使用 `<label>` 。
    - 视项目情形来决定是否使用 HTML5 中的标签，结合 html5shiv 。
- 在资源型的内容上加入描述文案，比如给img添加alt属性，在audio内加入文案和链接等等。
    - 重要的图片必须添加 `alt` 属性。
- 加强“不可见”内容的可访问性。
    - 背景图上的文字应该同时写在 html 中，并使用css `text-indent` 使其不可见，有利于搜索引擎抓取你的内容，也可以在css失效的情况下看到内容。
- 重要的或者被截断的元素必须添加 `title` 属性。
- 以实体代替与HTML语法相同的字符，避免浏览解析错误，其他特殊符号的实体没有必要。
    - 常用HTML字符实体（建议使用实体）： `"` 、 `&` 、 `<` 、 `>` 、 `空格` 。
    - 常用特殊字符实体（不建议使用实体）： © ® · « » × ÷ ‰ ¥ 。

## 附录

### 代码示例

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"/>
        <title>Standard Demo</title>
        <meta name="keywords" content=""/>
        <meta name="description" content=""/>
        <meta name="viewport" content="width=device-width"/>
        <link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico"/>
        <link rel="apple-touch-icon" href="img/touchicon.png"/>
        <link rel="stylesheet" href="../css/core.css"/>
        <style>
        .nav {
            font-size: 14px;
        }
        </style>
    </head>
    <body>
    <!-- 头部 begin -->
    <div class="header"></div>
    <!-- 头部 end -->
    <!-- 内容区域 begin -->
    <div class="container">
        <div class="main"></div>
        <div class="aside"></div>
    </div>
    <!-- 内容区域 end -->
    <!-- 尾部 begin -->
    <div class="footer">
        <p>By XingKaiZhang.</p>
    </div>
    <!-- 尾部 end -->
    <script src="../js/light.js"></script>
    <script>
    alert('Standard Demo');
    </script>
    </body>
    </html>

### 特殊符号对照


    >            &amp;gt;
    <            &amp;lt;
    &            &amp;amp;
    "            &amp;quot;
    space        &amp;nbsp;
    
    ©            &amp;copy;
    ®            &amp;reg;
    ·            &amp;middot;
    «            &amp;laquo;
    »            &amp;raquo;
    ×            &amp;times;
    ÷            &amp;divide;
    ‰            &amp;permil;
    ¥            &amp;yen;


### 常用标签

    <html></html>
    <head></head>
    <body></body>
    <title></title>
    <link />                            // 引用样式或icon
    <meta />                            // 文档信息
    <script></script>                   // 引用脚本
    <style></style>                     // 引用样式

    <div></div>                         // 块级容器
    <span></span>                       // 内联容器

    <h1></h1>                           // 标题，h2，h3，h4，h5，h6
    <p></p>                             // 段落
    <a></a>                             // 超链接或锚
    <del></del>                         // 文本删除
    <em></em>                           // 强调文本
    <strong></strong>                   // 强调文本
    <sub></sub>                         // 下标
    <sup></sup>                         // 上标
    <br />
    <img />                             // 图像
    <iframe></iframe>                   // 内嵌一个网页

    <ul>                                // 无序列表
        <li></li>
        <li></li>
        <li></li>
    </ul>
    <ol>                                // 有序列表
        <li></li>
        <li></li>
        <li></li>
    </ol>
    <dl>                                // 定义列表
        <dt></dt>
        <dd></dd>
        <dd></dd>
        <dt></dt>
        <dd></dd>
    </dl>

    <table>
        <thead>
            <tr><th></th></tr>
        <thead>
        <tbody>
            <tr><td></td></tr>
        </tbody>
        <tfoot></tfoot>
    </table>

    <form>
        <label></label>
        <button></button>
        <input />
        <select>
            <option></option>
        <select>
        <textarea></textarea>
    </form>