<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="ie=edge" />
  <title>Test Web Project</title>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
  <script src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.min.js"></script>
  <script src="https://cdn.datatables.net/1.10.12/js/dataTables.bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://cdn.datatables.net/1.10.12/css/dataTables.bootstrap.min.css" />

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:400,600" />
  <link rel="stylesheet" href="css/templatemo-style.css" />








  <!--   <script type="text/javascript" src="jquery.min.js"> </script> -->
  <style type="text/css" media="screen">



   img {
    width: 132px;
    height: 180px;
    border-radius: 10px;
    margin-left: auto;
    margin-right: auto;

  }



</style>
</head>

<body>

  <div class="container-fluid">

    <div class="row tm-brand-row">
      <div class="col-lg-4 col-10">
        <div class="tm-brand-container">
          <div class="tm-brand-texts">
            <h1 class="d-inline-block text-uppercase">Car Recognition And Speed Detection On Roads</h1>
          </div>
        </div>
      </div>
      <div class="col-lg-8 col-2 tm-nav-col">
        <div class="tm-nav">
          <nav class="navbar navbar-expand-lg navbar-light tm-navbar">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav ml-auto mr-0">


                <li class="nav-item ">
                  <div class="tm-nav-link-highlight"></div>
                  <a class="nav-link" href="index.html"
                  >Home </a
                  >
                </li>

                <li class="nav-item active">
                  <div class="tm-nav-link-highlight"></div>
                  <a class="nav-link" href="video.php">
                    Videos<span class="sr-only">(current)</span></a>
                  </li>

                </ul>
              </div>
            </nav>
          </div>
        </div>
      </div>

      <div class="row">

        <div class="col-md-2">
          <form name="dropdown" method="POST">
            <select name="catagories" id="catagories">
              <option value="">Select Video</option>
              <?php
              include("dbconnect.php");
              $sqrury = "Select * From video";
              $result = mysqli_query($conn, $sqrury);
              while ($data = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
                ?>
                <option value="<?php echo $data['video_id']; ?>">
                  <?php echo $data['video_time']; 
                  ?>
                </option>
              <?php } 
              ?>

            </select>
          </form>
        </div>

        <div class="col-md-2">
          <form name="dropdown" method="POST">
            <select name="catagories1" id="catagories1">
              <option value="1">All</option>
              <option value="2">Colos</option>
              <option value="3">Category</option>
              <option value="4">Brand</option>
            </select>
          </form>
        </div>
        <div class="col-md-2">
          <form name="dropdown" method="POST">
            <select name="catagories2" id="catagories2">
              <option value="AllCo">All colors</option>
              <option value="RED">RED</option>
              <option value="PINK">PINK</option> 
              <option value="ORANGE">ORANGE</option>
              <option value="YELLOW">YELLOW</option> 
              <option value="PURPLE">PURPLE</option>
              <option value="GREEN">GREEN</option>
              <option value="BLUE">BLUE</option>
              <option value="BROWN">BROWN</option>
              <option value="WHITE">WHITE</option>
              <option value="GRAY">GRAY</option>      
            </select>
          </form>



          <form name="dropdown" method="POST">
            <select name="catagories3" id="catagories3">
              <option value="AllCa">All Category</option> 
              <option value="Saloon">Saloon</option> 
              <option value="PickUp">PickUp</option> 
              <option value="SUV">SUV</option>
              <option value="other_Car">OtherCar</option>    
            </select>
          </form>



          <form name="dropdown" method="POST">
            <select name="catagories4" id="catagories4">
              <option value="AllBa">All Brand</option> 
              <option value="TOYOTA">TOYOTA</option> 
              <option value="HONDA">HONDA</option> 
              <option value="MISZUBISHI">MISZUBISHI</option>
              <option value="NISSAN">NISSAN</option> 
              <option value="MAZDA">MAZDA</option> 
              <option value="CHEVRORET">CHEVRORET</option> 
              <option value="FORD">FORD</option> 
              <option value="SUZUKI">SUZUKI</option>
              <option value="ISUZU">ISUZU</option> 
              <option value="OTHER">OTHER</option>     
            </select>
          </form>
        </div>
        <div class="col-md-2">
          <input type="" name="vdio" id="vdio">
          <input type="" name="vdio1" id="vdio1">
          <input type="" name="vdio2" id="vdio2">
          <input type="" name="vdio3" id="vdio3">
          <input type="" name="vdio4" id="vdio4">
        </div>
        <div class="col-md-2">
        </div>
        <div class="col-sm-2" id="show">
        </div>
      </div>

      <!-- row -->
      <section class="row tm-pt-4 tm-pb-6" id="contact1">
        <table class="table table-striped" id="table1">
          <thead class="thead-dark">
            <tr>
             <!--  <th scope="col">S.no</th> -->
             <th scope="col">Image</th>
             <th scope="col">Colos</th>
             <th scope="col">Speed</th>
             <th scope="col">Category</th>
             <th scope="col">Brand</th>
             <!-- <th scope="col">Time</th> -->
           </tr>
         </thead>
         <tbody name="sub" id="sub">
         </tbody>
       </table>      
     </section>

     <!-- row -->
     <section class="row tm-pt-4 tm-pb-6" id="contact2">
      <table class="table table-striped" id="table2">
        <thead class="thead-dark">
          <tr>
            <!-- <th scope="col">#</th> -->
            <th scope="col">Image</th>
            <th scope="col">Colos</th>            
          </tr>
        </thead>
        <tbody name="Colos" id="Colos">
        </tbody>
      </table>

    </section>

    <!-- row -->
    <section class="row tm-pt-4 tm-pb-6" id="contact3">
      <table class="table table-striped" id="table3">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Image</th>
            <th scope="col">Category</th>            
          </tr>
        </thead>
        <tbody name="category" id="category">
        </tbody>
      </table>      
    </section>

    <!-- row -->
        <section class="row tm-pt-4 tm-pb-6" id="contact4">
      <table class="table table-striped" id="table4">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Image</th>
            <th scope="col">Brand</th>            
          </tr>
        </thead>
        <tbody name="brand" id="brand">
        </tbody>
      </table>      
    </section>


    <!--   <div id="piechart_div"></div> -->


    <footer class="row tm-page-footer">
      <p class="col-12 tm-copyright-text mb-0">
        2019
      </p>
    </footer>
  </div>




  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

  <script type="text/javascript">
    $('#vdio').addClass('d-none');
    $('#vdio1').addClass('d-none');
    $('#vdio2').addClass('d-none');
    $('#vdio3').addClass('d-none');
    $('#vdio4').addClass('d-none');

    $(document).ready(function() {
      $('#contact1').addClass('d-none');
      $('#contact2').addClass('d-none');
      $('#contact3').addClass('d-none');
      $('#contact4').addClass('d-none');
      $('#catagories2').addClass('d-none');
      $('#catagories3').addClass('d-none');
      $('#catagories4').addClass('d-none');

      var catagories;
    // var catagories2;
    $("#catagories").change(function(){
        // var selectedCountry = $(this).children("option:selected").val();
        catagories = $(this).val();
        $('#vdio').val(catagories);
        $('#contact1').removeClass('d-none');
        $('#contact2').addClass('d-none');
        $('#contact3').addClass('d-none');
        $('#contact4').addClass('d-none');
        $('#catagories2').addClass('d-none');
        $('#catagories3').addClass('d-none');
        $('#catagories4').addClass('d-none');
        $.ajax({
          type: 'POST',
          data: {
            catagories: catagories,
          },
          url: 'select_All.php',
          success: function(data) {

            $('#sub').html(data);

          }
        }); 
        $.ajax({
          type: 'POST',
          data: {
            catagories: catagories,
          },
          url: 'show.php',
          success: function(data) {

            $('#show').html(data);
          }
        });
        return false;
      });

    $('#catagories1').change(function() {
      $('#vdio1').val($(this).val());
      if($('#vdio1').val() == '1'){
        $('#contact1').removeClass('d-none');
        $('#contact2').addClass('d-none');
        $('#contact3').addClass('d-none');
        $('#contact4').addClass('d-none');
        $('#catagories2').addClass('d-none');
        $('#catagories3').addClass('d-none');
        $('#catagories4').addClass('d-none');
        console.log(catagories1);
        $.ajax({
          type: 'POST',
          data: {
            catagories: catagories,
          },
          url: 'select_All.php',
          success: function(data) {
            console.log(data);
            $('#sub').html(data);
          }
        });
        $.ajax({
          type: 'POST',
          data: {
            catagories: catagories,
          },
          url: 'show.php.php',
          success: function(data) {
            console.log(data);
            $('#show').html(data);
          }
        });
        return false;
      }

      else if($('#vdio1').val() == '2'){
        $('#contact1').addClass('d-none');
        $('#contact2').removeClass('d-none');
        $('#contact3').addClass('d-none');
        $('#contact4').addClass('d-none');
        $('#catagories2').removeClass('d-none');
        $('#catagories3').addClass('d-none');
        $('#catagories4').addClass('d-none');

        //  console.log("55555");
        $.ajax({
          type: 'POST',
          data: {
            catagories: catagories,
          },
          url: 'select_colors.php',
          success: function(data) {
           //   console.log(data);
           $('#Colos').html(data);
         }
       });
        $.ajax({
          type: 'POST',
          data: {
            catagories: catagories,
          },
          url: 'show_colors.php',
          success: function(data) {
           //   console.log(data);
           $('#show').html(data);
         }
       });
        return false;
      }  

      else if($('#vdio1').val() == '3'){
        $('#contact1').addClass('d-none');
        $('#contact2').addClass('d-none');
        $('#contact3').removeClass('d-none');
        $('#contact4').addClass('d-none');
        $('#catagories2').addClass('d-none');
        $('#catagories3').removeClass('d-none');
        $('#catagories4').addClass('d-none');
        console.log("55555");       
        $.ajax({
          type: 'POST',
          data: {
            catagories: catagories,
          },
          url: 'select_category.php',
          success: function(data) {
            console.log(data);
            $('#category').html(data);
          }
        });
        $.ajax({
          type: 'POST',
          data: {
            catagories: catagories,
          },
          url: 'show_category.php',
          success: function(data) {
            console.log(data);
            $('#show').html(data);
          }
        });
        return false;
      } 
      else if($('#vdio1').val() == '4'){
        $('#contact1').addClass('d-none');
        $('#contact2').addClass('d-none');
        $('#contact3').addClass('d-none');
        $('#contact4').removeClass('d-none');
        $('#catagories2').addClass('d-none');
        $('#catagories3').addClass('d-none');
        $('#catagories4').removeClass('d-none');

        console.log("55555");
        $.ajax({
          type: 'POST',
          data: {
            catagories: catagories,
          },
          url: 'select_brand.php',
          success: function(data) {
            console.log(data);
            $('#brand').html(data);
          }
        });
        $.ajax({
          type: 'POST',
          data: {
            catagories: catagories,
          },
          url: 'show_brand.php',
          success: function(data) {
            console.log(data);
            $('#show').html(data);
          }
        });
        return false;
      } 
    });
    
    $('#catagories2').change(function() {

      $('#vdio2').val($(this).val());
      
      if($('#vdio2').val() == 'AllCo'){
        $('#contact1').addClass('d-none');
        $('#contact2').removeClass('d-none');
        $('#contact3').addClass('d-none');
        $('#contact4').addClass('d-none');
        $('#catagories3').addClass('d-none');
        console.log("55555");
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val()
          },
          url: 'select_colors.php',
          success: function(data) {
            console.log(data);
            $('#Colos').html(data);
          }
        });
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val()
          },
          url: 'show_colors.php',
          success: function(data) {
            console.log(data);
            $('#show').html(data);
          }
        });
        return false;
      }
      
      if($('#vdio2').val() == 'RED' || 'PINK' || 'ORANGE' || 'YELLOW' || 'PURPLE' || 'GREEN' || 'BLUE' || 'BROWN' || 'WHITE' || 'GRAY'){
        $('#contact1').addClass('d-none');
        $('#contact2').removeClass('d-none');
        $('#contact3').addClass('d-none');
        $('#contact4').addClass('d-none');
        $('#catagories3').addClass('d-none');
        //  console.log(catagories);

        console.log("666");
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val(),
            'catagories2': $('#catagories2').val()
          },
          url: 'select_colors1.php',
          success: function(data) {
            console.log(data);
            $('#Colos').html(data);
          }
        });
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val(),
            'catagories2': $('#catagories2').val()
          },
          url: 'show_colors1.php',
          success: function(data) {
            console.log(data);
            $('#show').html(data);
          }
        });
        return false;
      }
    });

    $('#catagories3').change(function() {

      $('#vdio3').val($(this).val());
      
      if($('#vdio3').val() == 'AllCa'){
        $('#contact1').addClass('d-none');
        $('#contact2').addClass('d-none');
        $('#contact3').removeClass('d-none');
        $('#contact4').addClass('d-none');
        console.log("55555");
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val()
          },
          url: 'select_category.php',
          success: function(data) {
            console.log(data);
            $('#category').html(data);
          }
        });
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val()
          },
          url: 'show_category.php',
          success: function(data) {
            console.log(data);
            $('#show').html(data);
          }
        });
        return false;
      }
      
      if($('#vdio3').val() == 'Saloon' || 'PickUp' || 'SUV' || 'other_Car'){
        $('#contact1').addClass('d-none');
        $('#contact2').addClass('d-none');
        $('#contact3').removeClass('d-none');
        $('#contact4').addClass('d-none');
        //  console.log(catagories);

        console.log("778");
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val(),
            'catagories3': $('#catagories3').val()
          },
          url: 'select_category1.php',
          success: function(data) {
            console.log(data);
            $('#category').html(data);
          }
        });
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val(),
            'catagories3': $('#catagories3').val()
          },
          url: 'show_category1.php',
          success: function(data) {
            console.log(data);
            $('#show').html(data);
          }
        });
        return false;
      }
    });


    $('#catagories4').change(function() {

      $('#vdio4').val($(this).val());
      
      if($('#vdio4').val() == 'AllBa'){
        $('#contact1').addClass('d-none');
        $('#contact2').addClass('d-none');
        $('#contact3').addClass('d-none');
        $('#contact4').removeClass('d-none');
        console.log("55555");
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val()
          },
          url: 'select_brand.php',
          success: function(data) {
            console.log(data);
            $('#brand').html(data);
          }
        });
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val()
          },
          url: 'show_brand.php',
          success: function(data) {
            console.log(data);
            $('#show').html(data);
          }
        });
        return false;
      }
      
      if($('#vdio4').val() == 'TOYOTA'|| 'HONDA' || 'MISZUBISHI' || 'NISSAN MAZDA' || 'CHEVRORET' || 'FORD' || 'SUZUKI' || 'ISUZU OTHER'){
        $('#contact1').addClass('d-none');
        $('#contact2').addClass('d-none');
        $('#contact3').addClass('d-none');
        $('#contact4').removeClass('d-none');
        //  console.log(catagories);

        console.log("4444");
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val(),
            'catagories4': $('#catagories4').val()
          },
          url: 'select_brand1.php',
          success: function(data) {
            console.log(data);
            $('#brand').html(data);
          }
        });
        $.ajax({
          type: 'POST',
          data: {
            'catagories': $('#catagories').val(),
            'catagories4': $('#catagories4').val()
          },
          url: 'show_brand1.php',
          success: function(data) {
            console.log(data);
            $('#show').html(data);
          }
        });
        return false;
      }
    });
  });
</script>




</body>

</html>