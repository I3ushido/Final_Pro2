<?php 
include("dbconnect.php");
$catagorie_id = $_POST['catagories'];
$query = "select * from car where car_vid='$catagorie_id'";
$result = mysqli_query($conn, $query);
$num=mysqli_num_rows($result);
  // var_dump($result);
echo "<td>" .'Total   ' , $num , '   Car' ."</td>";

