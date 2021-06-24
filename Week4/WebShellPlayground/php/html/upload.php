<!doctype html>

<html lang="en">
<head>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  
    <title>PHP Shells</title>
</head>

<body>
    <div class="container">
	<?php include("nav.html") ?>

	<div class="row">
	    <h1>PHP Uploads</h1>
	    <p>In this example we can upload a file.

		There is no input sanitisation here, so you can use
		this to try getting a reverse shell via file upload</p>

		<form action="upload.php" method="post" enctype="multipart/form-data">
		<div class="form-group">
		    <label for="fileToUpload">File:</label>
		    <input type="file" name="fileToUpload" id="fileToUpload" class="form-control-file">
		</div>
		
		<button type="submit" class="btn btn-primary" name="submit">Submit</button>
	    </form>
	</div>

	<div class="row">	    
	    <?php
	    if(isset($_POST["submit"])) {
		$target_dir = "uploads/";
		$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
		$uploadOk = 1;
		$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
		// Check if image file is a actual image or fake image

		/*
		   $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
		   if($check !== false) {
		   echo "File is an image - " . $check["mime"] . ".";
		   $uploadOk = 1;
		   } else {
		   echo "File is not an image.";
		   $uploadOk = 0;
		   }
		 */

		// Check if file already exists
		/*
		if (file_exists($target_file)) {
		    echo "Sorry, file already exists.";
		    $uploadOk = 0;
		   }
		 */

		/*
		// Check file size
		if ($_FILES["fileToUpload"]["size"] > 500000) {
		    echo "Sorry, your file is too large.";
		    $uploadOk = 0;
		}

		// Allow certain file formats
		if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
		   && $imageFileType != "gif" ) {
		    echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
		    $uploadOk = 0;
		}
		*/
		
		// Check if $uploadOk is set to 0 by an error
		if ($uploadOk == 0) {
		    echo "<div class='alert alert-warning'>Sorry, your file was not uploaded.</div>";
		    // if everything is ok, try to upload file
		} else {
		    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
			echo "<div class='alert alert-success'>Upload to /uploads/". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " success!</div>";
		    } else {
			echo "<div class='alert alert-critical'>Sorry, there was an error uploading your file.</div>";
		    }
		}
		
	    }

	    ?>

	</div>
    </div>
</body>
    
