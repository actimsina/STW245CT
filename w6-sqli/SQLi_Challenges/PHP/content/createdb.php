<h2>Creating Database</h2>

<?php
require_once("conn.php");

$sql = "CREATE TABLE user (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(20),
role VARCHAR(20),
password VARCHAR(20),
email VARCHAR(50)
)";

if ($conn->query($sql) === TRUE) {
  echo "<p>Table created successfully</p>";
} else {
  echo "<p>Error creating table: " . $conn->error . "</p>";
}


$sql = "CREATE TABLE secret (
id INT PRIMARY KEY AUTO_INCREMENT,
message VARCHAR(20)
)";

if ($conn->query($sql) === TRUE) {
  echo "<p>Table created successfully</p>";
} else {
  echo "<p>Error creating table: " . $conn->error . "</p>";
}


//Add people
$sql = "INSERT INTO user (id, name, role, password, email)
VALUES (1, 'james', 'user', 'swordfish', 'james@evil.org')";

echo "<p>";
if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
  echo "Error: " . mysqli_error($conn);
}
echo "</p>";

$sql = "INSERT INTO user (id, name, role, password, email)
VALUES (2, 'dan', 'admin', 'foobar', 'dan@quixote.codes')";

echo "<p>";
if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
  echo "Error: " . mysqli_error($conn);
}
echo "</p>";


$sql = "INSERT INTO user (id, name, role, password, email)
VALUES (3, 'john', 'user', 'pirate', 'argh@jim.lad')";

echo "<p>";
if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
  echo "Error: " . mysqli_error($conn);
}
echo "</p>";

echo "<p>";
$sql = "INSERT INTO user (id, name, role, password, email)
VALUES (4, 'tono', 'hidden', 'bacon', 'tono@dmc.org')";

if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
  echo "Error: " . mysqli_error($conn);
}
echo "</p>";


echo "<p>";

$sql = "INSERT INTO secret (id, message)
VALUES (1, 'Bank Details?' )";

if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
    echo "Error: " . mysqli_error($conn);
}
echo "</p>";
?>
