<script type='text/javascript'>
	function c1()
	{
		window.location = "1STPAGE.html";
	}
</script>
<?php

$userid=$_POST['user'];
$password=$_POST['pass'];
$userid = stripcslashes($userid);
$password = stripcslashes($password);
#session_start();
#$_SESSION['varname']=$first_name;
$con=mysqli_connect("localhost","root","","carrier");

$result = mysqli_query($con," select * from users where user_id='$userid' and password='$password'")
    or die("Failed to query database".mysqli_error());
$row=mysqli_fetch_array($result);
if($row['user_id'] == $userid && $row['password'] == $password){
	$message1 = "WELCOME ".$userid;
  echo "<script>c1();</script>";

}else{
	$message = "Username and/or Password incorrect.\\nTry again.";
}
?>
