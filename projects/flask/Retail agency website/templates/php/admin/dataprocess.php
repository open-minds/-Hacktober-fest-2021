<?php
	error_reporting(0);
	function csvTable() {
		$row = 1;
		if (($handle = fopen("../formcsv.csv", "r")) !== false) {
			echo '<table class="display" cellspacing="0" width="100%" id="sfTable">';
		   
			while (($data = fgetcsv($handle, 1000)) !== false) {
				$num = count($data);
				if ($row == 1) {
					echo '<thead><tr>';
				}else{
					echo '<tr>';
				}
				for ($c=0; $c < $num; $c++) {
					if(empty($data[$c])) {
					   $value = "&nbsp;";
					}else{
					   $value = $data[$c];
					}
					if ($row == 1) {
						echo '<th>'.$value.'</th>';
					}else{
						echo '<td>'.$value.'</td>';
					}
				}
				if ($row == 1) {
					echo '</tr></thead><tbody>';
				}else{
					echo '</tr>';
				}
				$row++;
			}
			echo '</tbody></table>';
			fclose($handle);
		}
	}
?>
