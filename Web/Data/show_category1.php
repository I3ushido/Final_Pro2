<?php 
  include("dbconnect.php");
  

  $catagorie_id = $_POST['catagories'];
  $catagorie_ce = $_POST['catagories3'];

  $query = "select * from car where car_vid='$catagorie_id' and car_category='$catagorie_ce'";
  
  $result = mysqli_query($conn, $query);
  $num=mysqli_num_rows($result);
  // var_dump($result);
  
 echo "<td>" .'Total   ' , $num , '   Car' ."</td>";