
<script type="text/javascript">   
   setTimeout('Redirect()', 10000);
function Redirect() 
{ 
    alert("Predict Now!!");
    window.location="predicted.php"; 
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
$os = mysqli_real_escape_string($link, $_REQUEST['os']);
$dsa = mysqli_real_escape_string($link, $_REQUEST['dsa']);
$cpp = mysqli_real_escape_string($link, $_REQUEST['cpp']);
$se = mysqli_real_escape_string($link, $_REQUEST['se']);
$cn = mysqli_real_escape_string($link, $_REQUEST['cn']);
$ec = mysqli_real_escape_string($link, $_REQUEST['ec']);
$coa = mysqli_real_escape_string($link, $_REQUEST['coa']);
$intsub = mysqli_real_escape_string($link, $_REQUEST['intsub']);
$intcar = mysqli_real_escape_string($link, $_REQUEST['intcar']);
$com = mysqli_real_escape_string($link, $_REQUEST['com']);
$intfid = mysqli_real_escape_string($link, $_REQUEST['intfid']);
// Attempt insert query execution
#session_start();
#$_SESSION['varname']=$first_name;
$sql = "INSERT INTO subjects (OS,DSA,CPP,SE,CN,EC,COA,INT_SUB,INT_CAR,COM,INT_FID) VALUES ('$os','$dsa','$cpp','$se','$cn','$ec','$coa','$intsub','$intcar','$com','$intfid')";
if(mysqli_query($link, $sql)){
    echo "<script>Redirect();</script>";
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}
 #$_SESSION['id']=mysqli_query($link,"SELECT id FROM users WHERE email=".$email);
// Close connection
mysqli_close($link);
?>