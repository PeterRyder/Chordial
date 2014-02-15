<?php
  @ $db = new mysqli('localhost', 'root', 'chordial', 'chordial');

  $dbOK = false;

  if ($db->connect_error) {
    echo '<div class="messages">Could not connect to the database. Error: ';
    echo $db->connect_errno . ' - ' . $db->connect_error . '</div>';
  } else {
    $dbOk = true; 
  }

  $result = $db->query("SELECT * FROM `chordial` WHERE `ID` = 1 ");
  $row = $result->fetch_array(MYSQLI_ASSOC);
  $title = $row["Title"];
  $comp = $row["Composer"];
  $prog = $row["Progression"];

?>




<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <title>Lab 10: Databases and SQL, Intro ITWS</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <script>
      function hello () {
        var title = <?php echo json_encode($title);?>;
        var composer = <?php echo json_encode($comp);?>;
        var progression = <?php echo json_encode($prog);?>;
        var header = title + "\nBy\n" + composer;
        document.getElementById('title').innerHTML=header;
      }
    </script>
    <style type="text/css">
      body{
        background-color: green;
      }
      #border{
        width: 1600px;
        height: 900px;
        position: relative;
      }
      #title{
        text-align: center;
      }
      #I {
       background-color: red; 
       text-align: center;
       width: 175px;
       height: 175px;
       position: absolute;
       top:475px;
       left: 20px;
      }
      #II{
       background-color: red; 
       text-align: center;
       width: 175px;
       height: 175px;
       position: absolute;
       top: 650px;
       left: 1000px;
      }
      #III{
       background-color: red; 
       text-align: center;
       width: 175px;
       height: 175px;
       position: absolute;
       top:50px;
       left:450px;
      }
      #IV{
       background-color: red; 
       text-align: center;
       width: 175px;
       height: 175px;
       position: absolute;
       top:400px;
       left: 875px;
      }
      #V{
       background-color: red; 
       text-align: center;
       width: 175px;
       height: 175px;
       position: absolute;
       top: 475px;
       right:20px;
      }
      #VI{
       background-color: red; 
       text-align: center;
       width: 175px;
       height: 175px;
       position: absolute;
       top:275px;
       left: 550px;
      }
      #VII{
       background-color: red; 
       text-align: center;
       width: 175px;
       height: 175px;
       position: absolute;
       top: 50px;
       left: 1050px;
      }
      #G{
       background-color: red; 
       text-align: center;
       width: 175px;
       height: 175px;
       position: absolute;
       top: 650px;
       left: 500px;
      }

    </style>
  </head>
  <body onload="hello()">
    <div id='border'>
      <div id='title'></div>
      <div id='I'><p>I</p></div>
      <div id='II'><p>II</p></div>
      <div id='III'><p>III</p></div>
      <div id='IV'><p>IV</p></div>
      <div id='V'><p>V</p></div>
      <div id='VI'><p>VI</p></div>
      <div id='VII'><p>VII</p></div>
      <div id='G'>G</div>
    </div>
  </body>
</html>
