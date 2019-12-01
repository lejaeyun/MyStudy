
<?php
$id = (int)$_GET['id'];
$title = $_GET['title'];
$exp = $_GET['exp'];
$ans = $_GET['ans'];
$ans1 = $_GET['ans1'];
$ans2 = $_GET['ans2'];
$ans3 = $_GET['ans3'];
$ans4 = $_GET['ans4'];
$ans5 = $_GET['ans5'];

$servername = "164.125.36.45";
$username = "201624548";
$password = "201624548";
$db = "test";
$conn = new mysqli($servername, $username, $password, $db);

$sql = "DELETE FROM problem WHERE id = $id";
mysqli_query($conn,$sql);

$sql = "INSERT INTO problem	VALUES( $id, '$title', '$exp', '$ans1', '$ans2', '$ans3', '$ans4', '$ans5', '$ans')";
mysqli_query($conn,$sql);

mysqli_close($conn);
?>