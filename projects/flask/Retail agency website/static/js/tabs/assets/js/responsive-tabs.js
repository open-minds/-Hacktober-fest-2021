//	Responsive Tabs v1.0, Copyright 2014, Joe Mottershaw, https://github.com/joemottershaw/
//	=======================================================================================

	// Tabs function
		function jQueryTabs() {
			$('.tabs').each(function(e) {
				// Hide all tab panels except for the first
					$('.tabs-panel').not(':first').hide();

				// Add active statuses to first tab and show display
					$('li', this).removeClass('active');
					$('li:first-child', this).addClass('active');
					$('.tabs-panel:first-child').show();

				// Tab clicked
					$('li', this).click(function(e) {
						// Corresponding tabs panel
							var panel = $('a', this).attr('href');

						// Remove active statuses to other tabs
							$(this).siblings().removeClass('active');

						// Add active status to this tab
							$(this).addClass('active');

						// Hide other tab panels
							$(panel).siblings().hide();

						// Showing the clicked tabs' panel
							$(panel).fadeIn(400);

						// Prevent the anchor's default click action
							e.preventDefault();
					});

				// Responsive
					if ($(window).width() < 768) {
						$('.tabs-panel').show();
					}
			});
		}

	$(document).ready(function() {
		// Execute
			jQueryTabs();

		// Prepend tab titles to panels
			$('.tabs li a').each(function() {
				var	tabID		=	$(this).attr('href');
				var	tabTitle	=	$(this).html();

				$(tabID + ' .tab-title').prepend('<p><strong>' + tabTitle + '</strong></p>');
			});
	});

	$(window).resize(function() {
		// Execute
			jQueryTabs();
	});