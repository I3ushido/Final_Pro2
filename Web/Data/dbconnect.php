<?php 
if($_SERVER['SERVER_NAME'] == "localhost")
{
  $serverName = "localhost";
  $userName = "root";
  $userPassword = "";
  $dbName = "project";
  $conn = mysqli_connect($serverName,$userName,$userPassword,$dbName);
    if($conn->connect_error){
        die("Connection failed: " .$conn->connect_error);
    } 
  mysqli_set_charset($conn, "utf8");
}

else
{
  $serverName = "localhost";
  $userName = "cars99";
  $userPassword = "admin99";
  $dbName = "car_detection";
  $conn = mysqli_connect($serverName,$userName,$userPassword,$dbName);
    if($conn->connect_error){
        die("Connection failed: " .$conn->connect_error);
    }  
  mysqli_set_charset($conn, "utf8");
}

?>