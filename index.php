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
    <link rel="stylesheet" href="res/stylesheet.css" type="text/css"/>
    <script>
      var i = 0;
      var size;
      var title;
      var composer;
      var progression;
      function load () {
        title = <?php echo json_encode($title);?>;
        composer = <?php echo json_encode($comp);?>;
        progression = <?php echo json_encode($prog);?>;
        size = progression.length;
        var header = title + "\nBy\n" + composer;
        document.getElementById('title').innerHTML=header;
      }

      function color(prog, i){
          if(i < size){
            var rn = prog[i];
            if( i  == 0){
              
            } 
            else if (i == 1){

            }
            else {

            }
          }
      }
    </script>
    <style type="text/css">
      

    </style>
  </head>
  <body onload="load()">
    <div id='border'>
      <div id='title'></div>
      <div id='1'><p>I</p></div>
      <div id='2'><p>II</p></div>
      <div id='3'><p>III</p></div>
      <div id='4'><p>IV</p></div>
      <div id='5'><p>V</p></div>
      <div id='6'><p>VI</p></div>
      <div id='7'><p>VII</p></div>
      <div id='G'>G</div>
    </div>
  </body>
</html>
