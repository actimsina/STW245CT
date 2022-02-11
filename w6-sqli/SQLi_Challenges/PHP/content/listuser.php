<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
        integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <title>User List</title>
</head>


<body>

<div class="container-lg">
  <div class="row">
    <div class="col-12">
      <h2>User List</h2>
      <form>
	<div class="form-group">
	  <label for="theSelector">Filter by Role</label>
	  <select class="form-control" id="theSelector" name="theSelector">
	    <option selected>All</option>
	    <option value="user">User</option>
	    <option value="admin">Admin</option>
	  </select>
	</div>
	<button class="btn btn-lg btn-primary btn-block" type="submit">Filter</button>
      </form>

      <table class="table">
	<thead>
	  <tr>
	    <td>User</td>
	    <td>Role</td>
	    <td>Email</td>
	  </tr>
	</thead>
	<tbody>
<?php
         require_once("conn.php");
if (isset($_GET["theSelector"])){
    $theRole = $_GET["theSelector"];
    if ($theRole == "All"){
        $qry = "SELECT * FROM user WHERE role != 'hidden'";
    }
    else {
        $qry = "SELECT * FROM user WHERE role = '$theRole'";
    }
}
else {
    $qry = "SELECT * FROM user WHERE role != 'hidden'";
}
    echo "<p>".$qry."</p>";

//Run the Query
$result = $conn -> query($qry) or die(mysqli_error($conn));

if ($result->num_rows > 0) {
  // output data of each row
    while ($row = $result->fetch_row()){
        echo "<tr><td> $row[1] </td><td> $row[2]</td><td> $row[4]</td></tr>";
    }
    //while($row = $result->fetch_all()) {
    //echo "id: " . $row[0]. " - Name: " . $row["name"]. " " . $row["role"]. "<br>";
    //}
} else {
  echo "0 results";
}
?>
	  
	</tbody>
      </table>
	    
    </div>
  </div>
</div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
        integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
        crossorigin="anonymous"></script>
</body>

</html>
