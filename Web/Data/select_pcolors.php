<?php
	include("dbconnect.php");
	$catagorie_id = '2';
	$sql = "SELECT car_colors,count(*) as number FROM car where car_vid='$catagorie_id' GROUP BY car_colors";
  	$result = mysqli_query($conn, $sql);

  	while ($row = $result->fetch_assoc()) {
    echo $row['car_colors']."<br>";
	}
?>