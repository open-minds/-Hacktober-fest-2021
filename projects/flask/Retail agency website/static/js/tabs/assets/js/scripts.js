//	Backbone v1.0, Copyright 2014, Joe Mottershaw, https://github.com/joemottershaw/
//	=======================================================================================

//	Table of Contents
//	==================================================
//		#Scroll To Top


//	#Scroll To Top
//	==================================================

	$(document).ready(function() {
		$('.scroll-to-top').on("click",function() {
			$('html, body').animate({ scrollTop: 0 }, 1600, 'easeInOutQuart');
			return false;
		});
	});