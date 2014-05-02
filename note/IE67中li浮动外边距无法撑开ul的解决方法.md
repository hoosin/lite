# IE6/7中li浮动外边距无法撑开ul的解决方法 #
```html
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
<style type="text/css">
*{ padding:0; margin:0; list-style:none; }
.wrap{ background-color:#9C9; width:960px; }
.wrap ul{ overflow:hidden; }
.wrap li{ width:50px; height:50px; float:left; *float:none; margin:0 10px 20px 0; border:1px solid #c00; display:inline-block; *display:inline; zoom:1; }
</style>
</head>
<body>
    <div class="wrap">
    	<ul class="q">
    		<li></li>
    		<li></li>
    		<li></li>
    		<li></li>
    		<li></li>
    		<li></li>
    	</ul>
    </div>
</body>
</body>
</html>
```