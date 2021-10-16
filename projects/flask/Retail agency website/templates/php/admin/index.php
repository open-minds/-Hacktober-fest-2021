<?php
	require('check.php');
	require "dataprocess.php";
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <title> SmartForms Dashboard </title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel='stylesheet' href='css/app.css'>
        <link rel="stylesheet" href="css/font-awesome.min.css">    
        <link rel="stylesheet" href="http://cdn.datatables.net/1.10.7/css/jquery.dataTables.min.css" />
        <link rel="stylesheet" href="http://cdn.datatables.net/tabletools/2.2.2/css/dataTables.tableTools.css" />
        <link rel="stylesheet" href="http://cdn.datatables.net/responsive/1.0.6/css/dataTables.responsive.css" />
        <link rel="stylesheet" href="css/tables-custom.css" />
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
        <script src="http://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js"></script>
        <script src="http://cdn.datatables.net/tabletools/2.2.2/js/dataTables.tableTools.min.js"></script>
        <script src="http://cdn.datatables.net/responsive/1.0.6/js/dataTables.responsive.js"></script>
        <script src="js/jquery.hammer.min.js"></script>
        <script src="js/app.js"></script>    
        <script>
            $(document).ready( function () {
                $('#sfTable').dataTable( {
                    responsive: true,
					"pageLength": 25,
                    "dom": 'T<"clear">lfrtip',
                    "tableTools": {
                        "sSwfPath": "http://cdn.datatables.net/tabletools/2.2.2/swf/copy_csv_xls_pdf.swf"
                    }
                });
            });		
        </script> 
        <!--[if lte IE 8]>
            <link rel='stylesheet' href='css/old-ie.css'>
        <![endif]-->       
    </head>
    <body class="nav-collapsed">
        <div class="smart-admin">
            <div class="page-frame">
                <div class="page">
                    <div class="offcanvas" role="navigation">
                        <div class="top-toggle">
                            <a href="#" class="toggle-smartadmin" ><i class="fa fa-bars"></i></a>  
                        </div><!-- .top-toggle -->
                        <div class="admin-profile">
                            <span class="profile-pic"></span>
                            <!--<span class="profile-user"><b>Hello:</b> Steve1455 </span>-->
                        </div><!-- .admin-profile -->
                        <ul class="smart-navigation">
                            <li><a href="#"><i class="fa fa-dashboard"></i> Dashboard </a></li>
                            <li><a href="../formcsv.csv?v=v1"><i class="fa fa-download"></i> Download CSV </a></li>
                            <li><a href="logout.php"><i class="fa fa-sign-out"></i> Logout </a></li>
                        </ul>
                    </div><!-- end offcanvas -->
                    <div class="content-frame">    
                        <div class="swipe-panel" role="banner">
                            <a href="#" class="toggle-smartadmin" ><i class="fa fa-bars"></i></a>
                            <div class="dwnload">
                            	<span> Hello: <b><?php echo $showDisplayName; ?></b> </span>
                                <a href="logout.php"> <i class="fa fa-sign-out"></i> Logout </a>
                            </div>    
                        </div><!-- end header -->
                        <div class="container">
                            <div class="smart-app-content">
                                <div class="sftables">
                                    <div class="sftable-wrap">
                                        <?php echo csvTable(); ?>
                                    </div>        
                                </div><!-- .sftables -->                            
                            </div><!-- .smart-app-content -->
                        </div><!-- end container -->
                    </div><!-- END .content-frame -->
                </div><!-- END .page -->
            </div><!-- END .page-frame -->
        </div><!-- END .smart-admin -->
    </body>
</html>