#CSS命名规范
---

##1 前端开发命名规范

###1.1 为什么要制定CSS命名规范

统一的命名规范，便于多人开发维护时代码统一，减少项目沟通和交接的成本，增加代码的语义化。

###1.2 CSS命名规则

1. 样式类名全部用小写，首字符必须是字母，禁止数字或其他特殊字符。由以字母开头的小写字母```（a-z）```、数字```（0-9）```、中划线 ```（-）```组成。

2. 可以是单个单词，也可以是组合单词，要求能够描述清楚模块和元素的含义，使其具有语义化。避免使用 ```123456…,red,blue,left,right```之类的（如颜色、字号大小等）矢量命名，如```class="left-news"、class="2"``` ，以避免当状态改变时名称失去意义。尽量用单个单词简单描述class名称。

3. 双单词或多单词组合方式：形容词-名词、命名空间-名次、命名空间-形容词-名词。例如：```news-list、mod-feeds、mod-my-feeds、cell-title```

###1.3 Class 和 id的使用方法
把id留给后台开发和JS使用，除此之外页面的page id(如首页的外层需要一个ID ```id="pageIndex"```)，页面结构（header main footer）允许用id命名(ID命名建议使用驼峰命名)。其他禁止id使用在样式表CSS命名中，一律使用class命名。

###1.4 命名空间

在编码思想上，我们可以将页面拆分成不同的层级（布局、模块、元件）。

什么是CSS命名空间？

通过统一的命名规范定义命名的范围，成为CSS  class & id命名空间。

布局: 以语义化的单词layout作为命名空间，例如主栏布局命名 layout-main，只改变layout-命名空间后面的命名，layout始终保留。布局的命名空间为layout-xxx。

模块：页面是由一个或多个模块组成，模块的英文单词是module，规范简写成mod，如新闻模块```mod-news```，照片展示模块```mod-photo-show```。模块的命名空间为```mod-xxx``` 。

元件：元件是属于模块内部的，也可以说模块是由元件和它内部的自有元素组成。如用户照片信息元件```cell-user-photo```。元件的命名空间为```cell-xxx``` 。


###1.5 通用命名

####(1)页面框架命名，一般具有唯一性，推荐用ID命名

ID名称|命名|ID名称	|命名
:---------------|:---------------|:---------------|:---------------
头部|header|主体|	main
脚部|footer|容器|wrapper
侧栏|sideBar|栏目|column
布局|layout|||

####(2)模块结构命名

Class名称|命名|Class名称|命名
:---------------|:---------------|:---------------|:---------------
模块(如：新闻模块)	|mod (mod-news)	|标题栏	|title
内容	|content	|次级内容	|sub-content


####(3)导航结构命名

Class名称|命名|Class名称|命名
:---------------|:---------------|:---------------|:---------------
导航	|nav	|主导航	|main-nav
子导航|	sub-nav	|顶部导航	|top-nav
菜单	|menu	|子菜单	|sub-menu

 
####(4)一般元素命名
Class名称|命名|Class名称|命名
:---------------|:---------------|:---------------|:---------------
二级|	sub	|面包屑|	breadcrumb
标志	|logo	|广告	|bner(禁用banner或ad)
登陆	|login	|注册	|register/reg
搜索	|search	|加入	|join
状态	|status	|按钮	|btn
滚动	|scroll	|标签页	|tab
文章列表	|list|	短消息|	msg/message
当前的	|current	|提示小技巧	|tips
图标	|icon|	注释|	note
指南	|guide	|服务	|service
热点	|hot	|新闻	|news
下载	|download	|投票	|vote
合作伙伴	|partner	|友情链接	|link
版权|	copyright|	演示|	demo
下拉框	|select	|摘要	|summary
翻页	|pages|	主题风格|	themes
设置	|set	|成功|	suc
按钮	|btn|	文本|	txt
颜色	|color/c|	背景	|bg
边框	|border/bor|	居中|	center
上	|top/t	|下|	bottom/b
左	|left/l	|右	|right/r
添加	|add	|删除	|del
间隔	|sp|	段落	|p
弹出层	|pop	|公共	|global/gb
操作|	op	|密码	|pwd
透明	|tran|	信息	|info
重点	|hit	|预览	|pvw
单行输入框|	input|	首页	|index
日志	|blog	|相册|	photo
留言板	|guestbook|	用户|	user
确认	|confirm	|取消	|cancel
报错	|error||


####(5)全局皮肤样式

######文字颜色(命名空间text-xxx)

text-c1, text-c2,text-c3……

######背景颜色(命名空间bg -xxx)

bg-c1,bg-c2,bg-c3……

######边框颜色(命名空间border-xxx)

border-c1,border-c2,border-c3……







