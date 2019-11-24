<?php
?>
<!DOCTYPE html>
<html>
<head>
<title>title</title>
</head>
<body oncontextmenu="return false" ondragstart="return false" onselectstart="return false">
<h2>_SERVER</h2><br>
<?php
  foreach ( $_SERVER as $key => $value ) {
	echo  $key . ' : '.  $value .'<br>';
  }
?>
<br>
<h2>_ENV</h2> <br>
<?php
  foreach ( $_ENV as $key => $value ) {
	echo  $key . ' : '.  $value .'<br>';
  }
?>
<br>
</body>
</html>
