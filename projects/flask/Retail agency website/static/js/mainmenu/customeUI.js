(function($) {
 "use strict";

$(document).ready(function() {
           
//    $(this).scroll(function() {
//        $('.navbar-default').toggleClass('navbar-fixed-top', $(this).scrollTop() >= 35);
//         if($(this).scrollTop() <= 35){
//            var currentTop = 27;
//            var logoTop = 14;
//            var imgRetio = 46;
//            $('.navbar-nav > li > a').css('paddingTop', (currentTop - ($(this).scrollTop() / 3)) + "px");
//            $('.navbar-nav > li > a').css('paddingBottom', (currentTop - ($(this).scrollTop() / 3)) + "px");
//            $('.navbar-brand').css('marginTop', (logoTop - ($(this).scrollTop() / 3)) + 1 + "px");
//            $('.navbar-brand').css('marginBottom', (logoTop - ($(this).scrollTop() / 3)) + "px");
//            $('.navbar-brand img').css('height', (imgRetio - ($(this).scrollTop() / 3)) + "px");
//        } 
//            else if ($(this).scrollTop() >= 35) {
//            $('.navbar-nav > li > a').css('paddingTop', "15.666666666666666px");
//            $('.navbar-nav > li > a').css('paddingBottom', "15.666666666666666px");
//            $('.navbar-brand').css('marginTop', "3.666666666666666px");
//            $('.navbar-brand').css('marginBottom', "2.666666666666666px");
//            $('.navbar-brand img').css('height', "34.666666666666664px");
//        }
//    });



  
  
    $('.dropdown-submenu').hover(function () {
        if ($(window).width() >= 479) {
            var p = $(this);
            var offset = p.offset();

            var multiLeft = offset.left;
            var multilevelWidth = $(".multilevel").width();
            var sublevelWidth = $(this).find(".dropdown-menu").width();

            var allWidth = multiLeft + multilevelWidth + sublevelWidth;

            if ($(window).width() <= allWidth) {
                $(this).find(".dropdown-menu").css("marginLeft", "-" + (multilevelWidth + sublevelWidth) + "px");
            } else {
                $(".dropdown-submenu>.dropdown-menu").css("marginLeft", " ");
            }
        } else {
            $(".dropdown-submenu>.dropdown-menu").css("marginLeft", " ");
        }
    });    
    
    
});

})(jQuery);
