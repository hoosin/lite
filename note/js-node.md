```html
<!doctype html>
<html lang="en">
<head>
<title>JavaScript节点操作</title>
</head>
<body>
	<div id="container">
		<h1 id="header">DOM Header</h1>
		<p>页面中的P标签</p>
		<div id="oDiv">页面中的Div标签</div>
		<div id="cloneNode">克隆一个节点</div>
	</div>
	<script type="text/javascript">
		//常用的节点属性
		/*
		    nodeType----节点类型，元素节点是1，文本节点是3
		    nodeValue----节点值，元素节点为空，文本节点的nodeValue属性即为文本内容
		    firstChild----该元素包含的第一个子节点
		    lastChild----该元素包含的最后一个子节点
		    nextSibling----该节点的后一个兄弟节点
		    previousSibling----该节点的前一个兄弟节点
		    childNodes----子节点列表
		    nodeName----节点名称，对于元素节点，返回tagName，对于文本节点，返回#text
		*/
		window.onload = function() {
			var container = document.getElementById("container");
			var nodesAll = container.childNodes; //子节点列表
			nodesAll = filterSpaceNode(nodesAll); //过滤掉空白子节点
			//alert(nodesAll.length);
			var header = document.getElementById("header");
			var nextNode = nextSibling(header);
			//alert(nextNode.nodeName);
			var oDiv = document.getElementById("oDiv");
			/*
		    var a=[];
		    for(var item in Node)  //Node在火狐下是自带的
		    {
		        a.push(item+":"+Node[item]);
		    }
		    oDiv.innerHTML=a.join("<br />");   */
			alert(lastChild(header)); //null

			//创建节点   常用的有两个createElement()和createTextNode()
			var newDiv = document.createElement("div");
			newDiv.innerHTML = "动态创建的的节点";
			document.body.appendChild(newDiv); //要将创建的节点添加至页面中，才能显示（不然只是在内存中，不会显示出来）

			//用新节点替换旧节点
			//node.replaceChild(newNode,oldNode)  //其中oldNode一定要是node的子节点
			//在某个节点前插入一个新节点
			//node.insertBefore(newNode,whichNode) //其中的某个节点也一定要是node的子节点

			//克隆节点 cloneNode()
			//注意要带一个bool型的参数:true表示该节点的子元素也跟着克隆，flase则只克隆该元素
			var cloneNode = document.getElementById("cloneNode");
			var ncloneNode = cloneNode.cloneNode(true);
			document.body.appendChild(ncloneNode);

		}

		function filterSpaceNode(nodes) { //用于给FF过滤掉空白文本节点（因为FF会把元素之间的空白文本当作节点）
			for (var i = 0, ret = []; i < nodes.length; i++) {
				if (nodes[i].nodeType === 3 && /^\s+$/.test(nodes[i].nodeValue)) //如果是文本节点，并且只是空白
				{
					continue;
				}
				ret.push(nodes[i]); //将不是空白的节点保存到一个数组中，最后返回这个数组
			}
			return ret;
		}

		function nextSibling(node) //返回节点的下一个兄弟节点，过滤掉空白文本节点
		{
			var n = node.nextSibling;
			if (n != null && n.nodeType === 3 && /^\s+$/.test(n.nodeValue)) {
				return n.nextSibling;
			}
			return n;
		}

		function preSibling(node) //返回节点的前一个兄弟节点，过滤掉空白文本节点
		{
			var n = node.preSibling;
			if (n != null && n.nodeType === 3 && /^\s+$/.test(n.nodeValue)) {
				return n.preSibling;
			}
			return n;
		}

		function firstChild(node) //第一个子节点(元素节点)
		{
			//此处用的是三元运算符，判断节点的firstChild是否是元素节点，如果不是，则返回节点firstChild的下一个兄弟节点
			return node.firstChild.nodeType == 1 ? node.firstChild : node.firstChild.nextSibling;
		}

		function lastChild(node) //最后一个子节点(元素节点)
		{
			return node.lastChild.nodeType == 1 ? node.lastChild : node.lastChild.previousSibling;
		}

		function before(newNode, oldNode) //在某个节点前插入一个新节点
		{
			oldNode.parentNode.insertBefore(newNode, oldNode);
		}

		function delNode(node) //删除某个节点
		{
			node.parentNode.removeChild(node);
		}
		//处理IE下的取得属性名问题，如取class的时候要用className
		var specialNames = {
			"class": "className",
			"for": "htmlFor"
		};

		function getAttr(node, attrName) {
			var attr = node.getAttribute(attrName);
			if (attr == null) {
				if (attrName in specialNames) {
					attrName = specialNames[attrName];
					attr = node.getAttribute(attrName);
				}
			}
			return attr;
		}
		//在某个节点后面插入一个节点
		function insertAfter(newNode, whichNode) { //将newNode插入到whichNode的后面
			//如果whichNode有下一个兄弟节点的话，就将newNode插入到whichNode.nextSibling的前面
			//如果whichNode没有下一个兄弟节点，则将newNode插入到whichNode.parentNode的最后
			var pn = whichNode.parentNode;
			if (whichNode.nextSibling) { //如果存在兄弟节点
				pn.insertBefore(newNode, whichNode.nextSibling);
			} else {
				pn.appendChild(newNode);
			}
			return newNode; //最后返回这个新插入的节点
		}
	</script>
</body>
</html>
```
