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
	<div class="row">
	    <?php include("../nav.html") ?>
	    
	    <h1>PHP Blind RCE</h1>

         <p>This page lets you play with Remote Code Execution in PHP.
            This time the RCE is blind so the command runs but you dont get an output
        </p>
        <p>Do some research into Blind RCE,  what option do we have for working around it?</p>       
	<p>Then use RCE to do the following:
		<ul>
		    <li>Run a simple command (whoami)</li>
		    <li>Read a file (/etc/passwd)</li>
		    <li>Write a file</li>
		    <li>Create a netcat (or other) Remote Shell</li>
		</ul>
	    </p>
	    
	    <form>
	    <div class="form-group">
		<label for="payload">Command</label>
		<input id="payload" name="payload" placeholder="whoami"></input>
	    </div>
	    <button type="submit" class="btn btn-primary">Submit</button>
	    </form>
	</div>

	<div class="row mt-5">
	    <?php

	    if (isset($_GET["payload"])){
		$payload = $_GET["payload"];
		echo "<div class='alert alert-info'>Command String: ".$payload."</div>\n";

		echo '<pre>';
		exec($payload);
		echo '</pre>';
		}

	    ?>
	</div>
    </div>
</body>
</html>


            
