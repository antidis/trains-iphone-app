#!/usr/bin/perl -w

use strict;
use CGI;
use CGI::Carp qw/fatalsToBrowser/;

# Construct URL
my $query = new CGI;
my $from = $query->param('txtFromStation');

print $query->header();

print<<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <meta name="viewport" content="width = 320, user-scalable=no" />
  <link rel="stylesheet" href="css/master.css" type="text/css" media="screen" title="iPhone" charset="utf-8" />
  <link rel="apple-touch-icon" href="http://antidis.com/demos/trains/img/apple-touch-icon.png" />
	<title>iPhone Irish Train Times</title>	
</head>

<body>
  
  <div id="TitleBar">
    <h1>To Station</h1>
    <a id="backButton" class="button" href="select.html">From</a>
  </div>
  
  <div class="undernote">From $from</div>

  <div class="button-group">
    <a class="button" href="#arrive_a">A</a>
    <a class="button" href="#arrive_b">B</a>
    <a class="button" href="#arrive_c">C</a>
    <a class="button" href="#arrive_d">D</a>
    <a class="button" href="#arrive_e">E</a>
    <a class="button" href="#arrive_f">F</a>
    <a class="button" href="#arrive_g">G</a>
    <a class="button" href="#arrive_h">H</a>
    <a class="button" href="#arrive_k">K</a>
    <a class="button" href="#arrive_l">L</a>
    <a class="button" href="#arrive_m">M</a>
    <a class="button" href="#arrive_n">N</a>
    <a class="button" href="#arrive_p">P</a>
    <a class="button" href="#arrive_r">R</a>
    <a class="button" href="#arrive_s">S</a>
    <a class="button" href="#arrive_t">T</a>
    <a class="button" href="#arrive_w">W</a>
  </div>

  <ul class="internal_list">
    <li class="group" id="arrive_a">A</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Adamstown">Adamstown</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Arklow">Arklow</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Ashtown">Ashtown</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Athenry">Athenry</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Athlone">Athlone</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Athy">Athy</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Attymon">Attymon</a></li>
        <li class="group" id="arrive_b">B</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Balbriggan">Balbriggan</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Ballina">Ballina</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Ballinasloe">Ballinasloe</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Ballybrophy">Ballybrophy</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Ballycullane">Ballycullane</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Ballyhaunis">Ballyhaunis</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Ballymote">Ballymote</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Banteer">Banteer</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Bayside">Bayside</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Belfast%20Central">Belfast Central</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Birdhill">Birdhill</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Blackrock">Blackrock</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Booterstown">Booterstown</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Botanic">Botanic</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Boyle">Boyle</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Bray">Bray</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Bridgetown">Bridgetown</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Broombridge">Broombridge</a></li>
        <li class="group" id="arrive_c">C</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Cahir">Cahir</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Campile">Campile</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Carlow">Carlow</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Carrick%20on%20Shannon">Carrick on Shannon</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Carrick%20on%20Suir">Carrick on Suir</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Carrigaloe">Carrigaloe</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Castlebar">Castlebar</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Castleconnell">Castleconnell</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Castleknock">Castleknock</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Castlerea">Castlerea</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Charleville">Charleville</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Cherry%20Orchard%20Park%20West">Cherry Orchard Park West</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Clara">Clara</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Claremorris">Claremorris</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Clondalkin">Clondalkin</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Clonmel">Clonmel</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Clonsilla">Clonsilla</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Clontarf%20Road">Clontarf Road</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Cloughjordan">Cloughjordan</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Cobh">Cobh</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Collooney">Collooney</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Connolly">Connolly</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Coolmine">Coolmine</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Cork">Cork</a></li>
        <li class="group" id="arrive_d">D</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Dalkey">Dalkey</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Docklands">Docklands</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Donabate">Donabate</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Drogheda">Drogheda</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Dromod">Dromod</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Drumcondra">Drumcondra</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Dublin%20City%20Centre">Dublin City Centre</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Dublin%20Connolly">Dublin Connolly</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Dublin%20Heuston">Dublin Heuston</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Dublin%20Pearse">Dublin Pearse</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Dun%20Laoghaire">Dun Laoghaire</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Dundalk">Dundalk</a></li>
        <li class="group" id="arrive_e">E</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Edgeworthstown">Edgeworthstown</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Enfield">Enfield</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Ennis">Ennis</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Enniscorthy">Enniscorthy</a></li>
        <li class="group" id="arrive_f">F</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Farranfore">Farranfore</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Fota">Fota</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Foxford">Foxford</a></li>
        <li class="group" id="arrive_g">G</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Galway">Galway</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Glanmire">Glanmire</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Glenageary">Glenageary</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Glounthaune">Glounthaune</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Gorey">Gorey</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Gormanston">Gormanston</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Grand%20Canal%20Dock">Grand Canal Dock</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Greystones">Greystones</a></li>
        <li class="group" id="arrive_h">H</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Harmonstown">Harmonstown</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Hazelhatch">Hazelhatch</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Heuston">Heuston</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Howth">Howth</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Howth%20Junction">Howth Junction</a></li>
        <li class="group" id="arrive_k">K</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Kilbarrack">Kilbarrack</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Kilcock">Kilcock</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Kilcoole">Kilcoole</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Kildare">Kildare</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Kilkenny">Kilkenny</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Killarney">Killarney</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Killester">Killester</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Killiney">Killiney</a></li>
        <li class="group" id="arrive_l">L</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Lansdowne%20Road">Lansdowne Road</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Laytown">Laytown</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Leixlip%20(Confey)">Leixlip (Confey)</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Leixlip%20(Louisa%20Bridge)">Leixlip (Louisa Bridge)</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Limerick">Limerick</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Limerick%20Junction">Limerick Junction</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Lisburn">Lisburn</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Littleisland">Littleisland</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Longford">Longford</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Lurgan">Lurgan</a></li>
        <li class="group" id="arrive_m">M</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Malahide">Malahide</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Mallow">Mallow</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Manulla%20Junction">Manulla Junction</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Maynooth">Maynooth</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Millstreet">Millstreet</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Monasterevin">Monasterevin</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Monkstown">Monkstown</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Muine%20Bheag">Muine Bheag</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Mullingar">Mullingar</a></li>
        <li class="group" id="arrive_n">N</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Nenagh">Nenagh</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Newbridge">Newbridge</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Newry">Newry</a></li>
        <li class="group" id="arrive_p">P</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Pearse">Pearse</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Phoenix%20Park">Phoenix Park</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Portadown">Portadown</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Portarlington">Portarlington</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Portlaoise">Portlaoise</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Portmarnock">Portmarnock</a></li>
        <li class="group" id="arrive_r">R</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Raheny">Raheny</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Rathdrum">Rathdrum</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Rathmore">Rathmore</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Roscommon">Roscommon</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Roscrea">Roscrea</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Rosslare%20Europort">Rosslare Europort</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Rosslare%20Strand">Rosslare Strand</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Rush%20and%20Lusk">Rush and Lusk</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Rushbrooke">Rushbrooke</a></li>
        <li class="group" id="arrive_s">S</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Sallins">Sallins</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Sallins%20and%20Naas">Sallins and Naas</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Salthill">Salthill</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Sandycove">Sandycove</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Sandymount">Sandymount</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Seapoint">Seapoint</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Shankill">Shankill</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Skerries">Skerries</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Sligo">Sligo</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Sutton">Sutton</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Sydney%20Parade">Sydney Parade</a></li>
        <li class="group" id="arrive_t">T</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Tara%20Street">Tara Street</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Templemore">Templemore</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Thomastown">Thomastown</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Thurles">Thurles</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Tipperary">Tipperary</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Tralee">Tralee</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Tullamore">Tullamore</a></li>
        <li class="group" id="arrive_w">W</li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Waterford%20(Plunkett)">Waterford (Plunkett)</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Wellingtonbridge">Wellingtonbridge</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Westport">Westport</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Wexford">Wexford</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Wicklow">Wicklow</a></li>
<li><a href="day.cgi?txtFromStation=$from&amp;txtToStation=Woodlawn">Woodlawn</a></li>

    </ul>

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-823538-4");
pageTracker._initData();
pageTracker._trackPageview();
</script></body>
</html>
HTML
