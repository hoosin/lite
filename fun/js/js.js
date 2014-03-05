 
<!--#include virtual="../lib/jquery-2.1.0.js"-->
<!--#include virtual="../lib/returnTop.js"-->

// 按需加载
(function(){
    <!--#include virtual="../lib/jquery.lazyLoad.js"-->
    $("#list li img.J_lazyLoad").scrollLoading({attr:"data-original"});
})();