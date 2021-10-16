window.onload = function(){
	document.body.setAttribute("class","smartBounce");
}

$(function() {
	$("#loginfm").validate({
			errorClass: "state-error",
			validClass: "state-success",
			errorElement: "em",
			rules: {
				username: {
						required: true
				},
				password: {
						required: true
				}
			},
			messages:{
				username: {
						required: 'Please enter username'
				},
				password: {
						required: 'Please enter password'
				}
			},
			highlight: function(element, errorClass, validClass) {
					$(element).closest('.field').addClass(errorClass).removeClass(validClass);
			},
			unhighlight: function(element, errorClass, validClass) {
					$(element).closest('.field').removeClass(errorClass).addClass(validClass);
			},
			errorPlacement: function(error, element) {
			   if (element.is(":radio") || element.is(":checkbox")) {
						element.closest('.option-group').after(error);
			   } else {
						error.insertAfter(element.parent());
			   }
			},	
			submitHandler:function(form) {
				$(form).ajaxSubmit({
						target:'.response',			   
						beforeSubmit:function(){
						},
						error:function(){
						},
						 success:function(){
								$('.alert-success').show().delay(900).fadeOut();
								$('.field').removeClass("state-error, state-success");
								if( $('.alert-error').length == 0){
									$('#loginfm').resetForm();
									setTimeout(function () {
									   window.location.replace("index.php");
									   $('body').removeClass("smartBounce");
									}, 1500);									
								}
						 }
				  });
			}		
	});					

});	