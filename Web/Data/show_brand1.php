<?php 
include("dbconnect.php");


$catagorie_id = $_POST['catagories'];
$catagorie_ba = $_POST['catagories4'];

$query = "select * from car where car_vid='$catagorie_id' and car_brand = '$catagorie_ba'";
$result = mysqli_query($conn, $query);
$num=mysqli_num_rows($result);

  // var_dump($result);
echo "<td>" .'Total   ' , $num , '   Car' ."</td>";