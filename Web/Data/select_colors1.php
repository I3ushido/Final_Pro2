<?php 
  include("dbconnect.php");


  $catagorie_id = $_POST['catagories'];
  $catagorie_co = $_POST['catagories2'];

  $query = "select * from car where car_vid ='$catagorie_id' and car_colors ='$catagorie_co'";
  
  $result = mysqli_query($conn, $query);
  $num=mysqli_num_rows($result);
  // var_dump($result);
  if ($num > 0 ) {
    while ($data = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
      echo "<tr>";
      echo "<td><img src='./" . $data['car_image'] ."'></td>";
      echo "<td>" . $data['car_colors'] ."</td>";
      echo "</tr>";
    }
  }
?>