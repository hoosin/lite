 
<!--#include virtual="../lib/jquery-2.1.0.js"-->

// 按需加载


var html='<li><img class="J_lazyLoad" data-original="http://placekitten.com/300/400" src="https://raw.github.com/hoosin/lite/master/fun/img/loading.gif"></li>'
var list=document.getElementById('list');
list.innerHTML=html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html+html;

window.onload = function() {
	(function() {
		<!--#include virtual="../lib/jquery.lazyLoad.js"-->
		$("#list li img.J_lazyLoad").scrollLoading({
			init: false,
			attr: "data-original"
		});
	})();
};