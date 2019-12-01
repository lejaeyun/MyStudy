
<?php
$id = (int)$_GET['id'];
$servername = "164.125.36.45";
$username = "201624548";
$password = "201624548";
$db = "test";
$conn = new mysqli($servername, $username, $password, $db);

$sql = "select * from problem where id=$id";
$result = mysqli_query($conn,$sql);

$row = mysqli_fetch_assoc($result);
$result = $row['title'] . ',' . $row['ans1'] . ',' . $row['ans2'] . ',' . $row['ans3'] . ',' . $row['ans4'] . ',' . $row['ans5'] . ',' . $row['ans'] . ',' . $row['exp'];

echo json_encode($result);

mysqli_close($conn);
?>