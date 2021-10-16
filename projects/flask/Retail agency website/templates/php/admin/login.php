<?php
	if ($_SERVER['REQUEST_METHOD'] == "POST") {
		if (!ereg("^[A-Za-z0-9]", $_POST['username']))
			exit('<div class="flo-notification alert-error">Invalid characters in the username.</div>');
	
		$username = $_POST['username'];
		$password = md5($_POST['password']);
		
		require('users.php');
		if (array_key_exists($username, $users)) {
			if ($password == $users[$username]) {
				session_start();
				$_SESSION['loggedin'] = md5($username.$password.$salt);
				echo('<div class="flo-notification alert-success">Login Sucessful</div>');
				exit;
			} else {
				exit('<div class="flo-notification alert-error">Invalid username or password </div>');
			}
		} else {
			exit('<div class="flo-notification alert-error">Invalid username or password </div>');
		}
	}
?>
<!DOCTYPE html>
<html lang="en"> 
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Smart Form Login</title>
        <link rel="stylesheet" href="css/login.css">
        <link rel="stylesheet" href="css/font-awesome.min.css">
        <script src="js/jquery-1.9.1.min.js"></script>
        <script src="js/plugins.js"></script>
        <script src="js/login.js"></script>        
    </head>
    <body class="smartbg">
        <form method="post" action="login.php" class="smartLogin" id="loginfm">
        <div class="smart-container">
            <div class="frm-header">
            	<h4><i class="fa fa-lock"></i> Admin Login </h4>
            </div><!-- end .frm-header section -->            
            <div class="frm-body">
                <div class="elem-group colm colm6">
                    <label class="field">
                        <input type="text" name="username" id="username" class="flo-input" placeholder="Username">
                    </label>                            
                </div><!-- end .colm .elem-group section -->
                <div class="elem-group colm colm6">
                    <label class="field">
                        <input type="password" name="password" id="password" class="flo-input" placeholder="Password">
                    </label>                            
                </div><!-- end .colm .elem-group section -->
                <div class="response"></div><!-- end .response  section -->
            </div><!-- .frm-body -->
            <div class="frm-footer">
                <button type="submit" class="flo-button">Login</button>
            </div><!-- end .frm-footer section -->
        </div>                  
        </form>
    </body>
</html>