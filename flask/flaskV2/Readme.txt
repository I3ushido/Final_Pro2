
http://127.0.0.1:5000/
/Users/mac/Desktop/flask

autocomplate
script

image
<img src="{{url_for('static', filename='image/arts.jpg')}}" /> #working



<div class="row-center">
  <ul class="nav nav-tabs">
    <li class="nav-item">
      <a class="nav-link active" href="/home">Home</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="/inserts">Inserts</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="/">Index</a>
    </li>
    <li class="nav-item">
      <!-- <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a> -->
    </li>
  </ul>


  image working{
  <section class="row">
    {% for image in images %}
      <!-- <section class="col-md-4 col-sm-6" style="background-color: green;"> -->
        <!-- <a href="{{ url_for('static', filename='images/' + image) }}">{{ image }}</a> -->
        <img src="{{ url_for('static', filename='images/' + image) }}" alt="image">
      <!-- </section> -->
    {% endfor %}
  </section>

  }

--image from static -- in code
  loop Image {
  <section class="row">
    {% for image in images %}
      <!-- <section class="col-md-4 col-sm-6" style="background-color: green;"> -->
        <!-- <a href="{{ url_for('static', filename='images/' + image) }}">{{ image }}</a> -->
        <img src="{{ url_for('static', filename='images/' + image) }}" alt="image">
      <!-- </section> -->
    {% endfor %}
  </section>
  }

  css {
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Data</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"> -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
  </head>
  <style>
  body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
  </style>
  }


   text {
  <p>hello_world</p>
  <p>&emsp;hi</p>
  <pre>    fsdlk sdlf s     sdld </pre>
เว้นวรรค 2 ครั้ง - พิมพ์ &ensp;
เว้นวรรค 4 ครั้ง - พิมพ์ &emsp;
เว้นวรรคเหมือนกด Tab - พิมพ์ &nbsp;&nbsp;&nbsp;&nbsp;
  }

  google style icon {
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  }
