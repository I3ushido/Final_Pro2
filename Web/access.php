<?php

	function base64ToImage($base64_string) {
	$path = "images/";
	$image_name = "img_"."_".date("Y-m-d-H-m-s").".jpg";
	$namepic = $path."".$image_name;
    $file = fopen($namepic,"wb");

    $data = explode(',', $base64_string);

    fwrite($file, base64_decode($data[1]));
    fclose($file);

    return $namepic ;
}


$data = json_decode(file_get_contents('php://input'),true);
echo ($data);
$photo = base64ToImage($data["image"]);
echo ($photo);
// function base64ToImage($base64_string,$filename) {
// 	$path = "images/";
// 	$image_name = $filename.".jpg";
// 	$namepic = $path."".$image_name;
//     $file = fopen($namepic,"wb");

//     $data = explode(',', $base64_string);

//     fwrite($file, base64_decode($data[1]));
//     fclose($file);

//     return $namepic ;
// }


// $data = json_decode(file_get_contents('php://input'),true);
// echo ($data);
// $photo = base64ToImage($data["image"],$data["name"]);
// echo ($photo);
?>