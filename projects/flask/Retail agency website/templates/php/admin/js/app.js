$(document).ready(function() {
						   

	$('.toggle-smartadmin').on('click', function(e){
		e.preventDefault();
		$('body').toggleClass('nav-collapsed');
	});
	
	var SideNav = (function() {
		var sideNav = $('.offcanvas');
		var topNav = $('.top-nav');
		var navItems = $("li a", sideNav);
		
		init();
		function init() { }
		function collapse() {
			$('body').addClass('nav-collapsed');
		}
		
		function expand() {
			$('body').removeClass('nav-collapsed');
		}
	})();
  
	function openMenu() {
		$("body").removeClass('nav-collapsed');
	}
	
	function closeMenu() {
		$("body").addClass('nav-collapsed');
	}
	
	$('.swipe-panel, .top-toggle').hammer().on('dragright', function(e) {
		openMenu();
	});
	
	$('.swipe-panel, .top-toggle').hammer().on('dragleft', function(e) {
		closeMenu();
	}); 
	
	$(window).scroll(function() {
		if ($(this).scrollTop()>100) {
			$('.top-toggle').slideDown( "slow" );
		} else {
			$('.top-toggle').slideUp("fast");
		}
	}); 

});