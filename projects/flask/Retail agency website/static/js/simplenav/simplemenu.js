$(document).ready(function () {
    $(".simplenavicon").on("click",function() {
        $(".mobilenav").fadeToggle(500);
        $(".top-menu").toggleClass("top-animate");
        $(".mid-menu").toggleClass("mid-animate");
        $(".bottom-menu").toggleClass("bottom-animate");
		<!--$("body").css("overflow", "hidden");-->
    });
	
	$(".menu a").on("click",function() {
        $(".mobilenav").fadeToggle(500);
        $(".top-menu").toggleClass("top-animate");
        $(".mid-menu").toggleClass("mid-animate");
        $(".bottom-menu").toggleClass("bottom-animate");
		<!--$("body").css("overflow", "auto");-->
    });
	
	$(".simplenavicon2").on("click",function() {
        $(".mobilenav").fadeToggle(500);
        $(".top-menu").toggleClass("top-animate");
        $(".mid-menu").toggleClass("mid-animate");
        $(".bottom-menu").toggleClass("bottom-animate");
		<!--$("body").css("overflow", "auto");-->
    });
	
	
});
