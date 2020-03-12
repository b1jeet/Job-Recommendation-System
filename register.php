
<script>
function c2()
	{
		window.location = "1STPAGE.html";
	}
	</script>
<?php
/* Attempt MySQL server connection. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
$link = mysqli_connect("localhost", "root", "", "carrier");
 
// Check connection
if($link == false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
 
// Escape user inputs for security
$userid = mysqli_real_escape_string($link, $_REQUEST['user']);
$email = mysqli_real_escape_string($link, $_REQUEST['email']);
$phone = mysqli_real_escape_string($link, $_REQUEST['phone']);
$gender = mysqli_real_escape_string($link, $_REQUEST['gender']);
$password = mysqli_real_escape_string($link, $_REQUEST['pass']); 
// Attempt insert query execution
#session_start();
#$_SESSION['varname']=$first_name;
$sql = "INSERT INTO users (user_id,email,phone,gender,password) VALUES ('$userid','$email','$phone','$gender','$password')";
if(mysqli_query($link, $sql)){
    echo "<script>c2();</script>";
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}
 #$_SESSION['id']=mysqli_query($link,"SELECT id FROM users WHERE email=".$email);
// Close connection
mysqli_close($link);
?>