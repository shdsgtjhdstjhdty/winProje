<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data = $_POST;
    $ip = $_SERVER['REMOTE_ADDR'];
    $file = fopen("saved.ip.txt", "a");
    fwrite($file, "IP: $ip, Data: " . json_encode($data) . "\n");
    fclose($file);
    header("Location: index.php"); // Form gönderildikten sonra yönlendir
}
?>

