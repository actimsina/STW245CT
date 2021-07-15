<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
        integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <title>Alternate Login</title>

</head>


<body>

<div class="container-lg">

  <div class="row">
    <div class="col-4">

      <h3>Instructions</h3>
      <p>A pretty standard SQL injection login bypass.  Try to login as any user</p>
      <p> This time you are not getting any SQL statement</p>
    </div>
  </div>

  <div class="row">
    <div class="col-4">
      
      <form class="form-signin">
	<h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
	<label for="inputEmail" class="sr-only">Email address</label>
	<input type="email" id="inputEmail" name="email" class="form-control" placeholder="Email address" required autofocus>
	<label for="inputPassword" class="sr-only">Password</label>
	<input type="password" id="inputPassword" name="password" class="form-control" placeholder="Password" required>
	<button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
	<p class="mt-5 mb-3 text-muted">&copy; 2017-2018</p>
      </form>
    </div>    
  </div>

  <div class="row">
  <div class="column">
      <?php

      require_once("conn.php");

      if (isset($_GET["email"])){
	  // TODO Could check a Token Here
	  $inName = $_GET["email"];
	  $inPass = $_GET["password"];

      $sql = "SELECT * FROM user WHERE email = '$inName' AND password = '$inPass';";
      
      $result = $conn -> query($sql) or die(mysqli_error($conn));
      
	  if ($result->num_rows == 1){
	      //Grab the First Row.
	      $row = $result->fetch_assoc();
          echo "<div class='alert alert-success'>Login as ".$row["name"]."</div>";
          if ($row["name"] == "dan"){
              echo "<div class='alert alert-success'>User is Admin</div>";
          }
        else{
            echo "<div class='alert alert-info'>Try to login as an Admin user</div>";
        }
      }
      else if ($result->num_rows >0){ 
        echo "<div class='alert alert-info'>Unable to login, too many users match</div>";
      }
	  else {
	      echo "<div class='alert alert-info'>Login Fails</div>";
	  }
      }
      ?>


      </div>
  </div>
</div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <!--
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
        integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
        crossorigin="anonymous"></script>
        -->
</body>

</html>
