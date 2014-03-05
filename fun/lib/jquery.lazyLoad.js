(function($) {
	$.fn.scrollLoading = function(options) {
		var defaults = {
			init:true,
			attr: "data-original",
			offset:200	
		};
		var params = $.extend({}, defaults, options || {});
		params.cache = [];
		$(this).each(function() {
			var node = this.nodeName.toLowerCase(), url = $(this).attr(params["attr"]);
			if (!url) { return; }
			//重组
			var data = {
				obj: $(this),
				tag: node,
				url: url
			};
			params.cache.push(data);
		});
		
		//动态显示数据
		var loading = function() {
			var st = $(window).scrollTop(), sth = st + $(window).height(),cache=[];
			$.each(params.cache, function(i, data) {
				var o = data.obj, tag = data.tag, url = data.url;
				if (o) {
					var post = o.offset().top, 
						posb = post + o.height(),
						act_post = post-params.offset,
						act_posb = posb+params.offset;
					if ((act_post > st && act_post < sth) || (act_posb > st && act_posb < sth)) {
						//在浏览器窗口内
						if (tag === "img") {
							//图片，改变src
							o.attr("src", url).hide().fadeIn("slow");
						} else {
							if (url.indexOf("javascript:") >= 0) {
								//$.globalEval(url);
								//this执行当前DOM
								(function(){
									eval(url);
								}).call(o[0]);
							}
						}	
						data.obj = null;
					}else{
						cache.push(data);
					}
				}
			});	
			params.cache = 	cache;
			return false;	
		};
		
		//事件触发
		//加载完毕即执行
		if(params.init){
			loading();
		}
		//滚动执行
		$(window).bind('scroll resize',function(){
			clearTimeout(params.scrollTimeId);
			params.scrollTimeId = setTimeout(function(){
				loading();
			}, 100)
		});
	};
})(jQuery);