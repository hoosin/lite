# CSS 规范 - 代码风格

- pubdate: 2013-4-24 12:04:58 
- tags: css, standard
- status: draft

----------------

> 除字体设置外， CSS 文件中的所有的代码都应该小写。

## 排版

- 原则上，以多行排版风格为标准，文件压缩用工具实现。
- 如果是在html中写内联的css，则必须使用单行排版风格。
- 重申：压缩工作能用工具就不要手动。

### 多行排版风格

- 空格缩进，大小为4 。
- 每个选择器占用一行。
- 每个样式声明占用一行。
- 属性名冒号之前不加空格，冒号之后加空格。
- 每条样式声明必须以分号 `;` 结束。
- `{` 前添加空格，不要另起一行。
- 两条样式规则之间用空行分隔。

代码示例：

    body,
    ul {
        margin: 0;
        padding: 0;
    }

    html {
        background: #fff;
    }

### 单行排版风格

- 每一条规则的大括号 `{` 前后加空格。
- 每一条规则结束的大括号 `}` 前加空格
- 多个selector共用一个样式集，则多个selector必须写成多行形式。
- 属性名冒号之前不加空格，冒号之后加空格。
- 每条样式声明必须以分号 `;` 结束。

代码示例：

    .test { width: 100px; height: 200px; }
    a:focus,
    a:hover { position: relative; right: 1px; }

## 选择器

### 命名风格：

- 一律由小写字母、数字和中划线组成。
- 不允许使用大写字母或下划线。

代码示例：

    .feedlist {}         // bad
    .feedList {}         // bad
    .feed_list {}        // bad
    .feed-list {}        // good

    #videoid {}          // bad
    #videoId {}          // bad
    #video_id {}         // bad
    #video-id {}         // good

### 命名原则

- 要反映元素的目的，有意义。
- 要尽可能的短，也要足够长。
- 避免表现性命名。
- 避免中文拼音。

总之，易于理解和稳定。

    .btn-yellow {}       // bad
    .btn-warning {}      // good

    #navigation {}       // bad
    #atr {}              // bad
    #nav {}              // good
    #author {}           // good

    .left {}             // bad
    .right {}            // bad
    .main {}             // good
    .aside {}            // good

### ID vs Class

- id 是唯一的并是父级的， class 是可以重复的并是子级的。
- id 原则上尽量不用，为 JavaScript 预留的钩子除外。
- 为 JavaScript 预留钩子的命名, 请以 j- 起始，比如: `#j-hide {}` ，`#j-show {}` 。

## 样式

### 尽可能使用缩写

    margin, padding, border, background, font

### 0 值不用写单位

    margin: 0;

### 0.x 可省略 0

    font-size: .8em;

### 颜色值

全小写，缩写。

    color: #FFEEDD;      // bad
    color: #ffeedd;      // bad
    color: #fed;         // good

### 使用单引号 `''`

使用单引号而非双引号。`url` 中不要使用引号。

    html {
        font-family: 'open sans', arial, sans-serif;
        background: url(../img/bg.png) repeat;
    }

注：如果必须使用 `@charset` ，则该语句使用双引号。

    @charset "utf-8";

### 顺序

- 按拼音顺序排序，便于记忆和维护。
- 如果使用CSS3的属性，如果有必要加入浏览器前缀，则按照 -webkit- / -moz- / -ms- / -o- / std 的顺序进行添加，标准属性写在最后。

代码风格：

    background: fuchsia;
    border: 1px solid;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    border-radius: 4px;
    color: black;
    text-align: center;
    text-indent: 2em;

## 注释规范

### 文件顶部注释

    /*
     * @description: XXX说明
     * @author: zhangxingkai CY2848
     * @update: zhangxingkai 2013-4-25
     */

### 模块注释

    /* module: module1 by zhangxingkai */

    /* module: module2 by liyi */

### 简单注释

    /* this is a short comment */

    /*
     * this is comment line 1.
     * this is comment line 2.
     */

### 特殊注释

    /* TODO: xxx by zhangxingkai 2012-10-18 18:32 */
    /* BUGFIX: xxx by zhifu.wang 2012-10-18 18:32 */