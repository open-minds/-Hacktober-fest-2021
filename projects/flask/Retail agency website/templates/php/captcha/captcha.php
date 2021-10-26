<?php

	session_start();
	if(!isset($_SESSION['gfm_captcha']))
		$capt_string = 'ERROR!';
	else
		$capt_string = $_SESSION['gfm_captcha'];
		
	$rand_char = strtoupper(substr(str_shuffle('abcdefghjkmnpqrstuvwxyz'), 0, 4));
	$capt_string = rand(1, 7) . rand(1, 7) . $rand_char;
	$_SESSION['gfm_captcha'] = $capt_string;
	header('Cache-control: no-cache');
	//Set the font 
	$font  = 'fonts/zxxnoise.otf';
	// Set the image settings
	$image = imagecreatetruecolor(118, 15); 
	$black = imagecolorallocate($image, 0, 0, 0);
	$color = imagecolorallocate($image, 36,49,64);
	$white = imagecolorallocate($image, 189,195,199);
	imagefilledrectangle($image,0,0,399,99,$white);
	// Draw the image
	imagettftext($image, 15, 0, 15, 15, $color, $font, $capt_string);
	// Output image
	header('Content-type: image/png');
	imagepng($image);
	imagedestroy($image);

?>