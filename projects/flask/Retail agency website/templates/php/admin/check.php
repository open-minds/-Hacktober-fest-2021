<?php
	session_start(); 
	if (!isset($_SESSION['loggedin'])) {
		header("Location: login.php");
		exit;
	} else {
		require('users.php');
		$userexists = false;
		foreach($users as $username => $password) {
			if (md5($username.$password.$salt) == $_SESSION['loggedin'])
				$userexists = true;
		}
		
		if ($userexists !== true) {
			header("Location: login.php");
			exit;
		}
	}
	
	$showDisplayName = $displayName;
?>