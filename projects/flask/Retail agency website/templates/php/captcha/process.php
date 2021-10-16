<?php

	session_start();
	if(strtoupper($_GET['captcha']) == $_SESSION['gfm_captcha']) {
		echo 'true';
	} else {
		echo 'false';
	}
	
?>