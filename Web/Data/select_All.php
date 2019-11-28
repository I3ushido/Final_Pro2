<?php 
  include("dbconnect.php");


  $catagorie_id = $_POST['catagories'];
  $query = "select car_image, car_colors, SUBSTRING(speed, 1, 2) AS Initial  ,car_category ,car_brand from car where car_vid='$catagorie_id'";
  $result = mysqli_query($conn, $query);
  $num=mysqli_num_rows($result);
  // var_dump($result);

  if ($num > 0 ) {
    while ($data = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
      echo "<tr>";
      echo "<td><img src='./" . $data['car_image'] ."'></td>";
      echo "<td>" . $data['car_colors'] ."</td>";
      echo "<td>" . $data['Initial'] , '  K/H' ."</td>";
      echo "<td>" . $data['car_category'] ."</td>";
      echo "<td>" . $data['car_brand'] ."</td>";
      echo "</tr>";
    }


  }

  
