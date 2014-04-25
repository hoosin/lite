# General 规范

- pubdate: 2013-4-24 12:04:58 
- tags: standard
- status: draft

----------------

## 协议

省略图片、视频、style、script 等资源的 URL 的协议部分，除非该协议不是 `http:` 或 `https:` 。

- 省略协议可以使得 URL 变成相对地址。

    把一个链接写成： `//example.org/index.html` ，那么，如果是在一个 `http://` 页面上点击这个链接，用户就会来到 `http://example.org/index.html` ，而如果是在一个 `https://` 页面上点击这个链接，用户就会来到 `https://example.org/index.html` 。这样完全省去了各种判断协议的代码，也大量节省了服务器资源。

- 可以避免 **“混合内容”** 问题。

    通过 `https://` 协议访问，但是有问题：页面中的图片、CSS、JavaScript 的 URI 都是 `http://` 的，所以会有“混合内容”的问题，在 Chromium/Chrome 里是一个难看的红叉叉（高危内容，如 JavaScript）或灰色的锁上有个黄三角（低危内容，如图片），在 Internet Explorer 里则是显示为“混合内容”，弹出大量烦人的警告窗口。

- 节省文件大小。

不推荐：

    <script src="http://www.google.com/js/gweb/analytics/autotrack.js"></script>

    .example {
        background: url(http://www.google.com/images/example);
    }

推荐：

    <script src="//www.google.com/js/gweb/analytics/autotrack.js"></script>

    .example {
        background: url(//www.google.com/images/example);
    }

## 使用 UTF-8 (no BOM)

[Handling character encodings in HTML and CSS](http://www.w3.org/International/tutorials/tutorial-char-enc/)

## 善用 TODO

编程过程中善用 TODO 可以大大提高工作效率

    <!-- TODO: remove optional tags -->
    <ul>
        <li>Apples</li>
        <li>Oranges</li>
    </ul>