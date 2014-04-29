/***
 *  model:returnTop.js
 *  author:hoosin
***/
$(function() {
	$.fn.returnTop = function(options) {
		var defaults = {			
			showHeight : 150,
			speed : 1000
		};
		var options = $.extend(defaults,options);
		// $("body").prepend("");
		var $toTop = $(this);
		var $top = $("#returnTop");
		var $ta = $("#returnTop a");
		var $topHide = $("#returnTop a.returnToptop");
		$toTop.scroll(function(){
			var scrolltop=$(this).scrollTop();		
			if(scrolltop>=options.showHeight){				
				$top.show();
			}
			else{
				$top.hide();
			}
		});	
		$topHide.click(function(){
			$("html,body").animate({scrollTop: 0}, options.speed);	
		});
	}
});
