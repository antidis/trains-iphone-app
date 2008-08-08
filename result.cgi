#!/usr/bin/perl -w

use strict;
use CGI;
use CGI::Carp qw/fatalsToBrowser/;
use URI::Escape;
use LWP::Simple;
use Time::Local;
$ENV{TZ} = ':/usr/share/zoneinfo/Europe/Dublin';

# Construct URL
my $query = new CGI;
my $from = $query->param('txtFromStation');
my $to = $query->param('txtToStation');
my @day_name = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday");
my @month_name = ("", "January", "February", "March", "April", "May", "Jun", "July", "August", "September", "October", "November", "December");
my @stations = ();
my $date = $query->param('date');
my $mday;
my $mon;
my $year;
my $hour = 0;
my $min = 0;
my $wday = 0;

if ( $date =~ /(\d\d)(\d\d)(\d\d\d\d)/ ) {
  $mday = $1;
  $mon = $2;
  $year = $3;
  my $epoch = timelocal(0, 0, 0,$mday,($mon - 1),( $year - 1900));
  my @dateArr = localtime ( $epoch );
  $wday = $dateArr[6];
} else {
  my $epoch = time;
  if ( $date eq "Tomorrow" ) { $epoch += 86400; }
  my @dateArr = localtime $epoch;
  $min  = $dateArr[1];
  $hour = $dateArr[2];
  $mday = $dateArr[3];
  $mon  = $dateArr[4];
  $year = $dateArr[5];
  $wday = $dateArr[6];
  $mon += 1;
  $year += 1900;
  if ( $mday < 10 ) { $mday = "0" . $mday; }
  if ( $mon < 10 ) { $mon = "0" . $mon; }  
}

my $url = "http://irishrail.ie/your_journey/timetables_junction1.asp?txtFromStation=" . uri_escape($query->param('txtFromStation')) . "&txtToStation=" . uri_escape($query->param('txtToStation')) . "&OutSelectDate=" . $mday . "-" . $mon . "-"  . $year . "&timeband=00,24&ReturnSelectDate=&NumPass=01&returnrequired=0&RadioOutDirect=all&RadioRtnDirect=&RadioOutStatus=D&RadioRtnStatus=&OutFromTime=00&OutToTime=24&RtnFromTime=00&RtnToTime=24&RadioReserve=&OutSelectDay=" . $mday . "&outSelectMonth=" . $mon . "&RtnSelectDay=&RtnSelectMonth=&hidOutDate=&hidRtnDate=&RadioRetReqd=&direction=&radioservice=1&radioservice1=1&optionWalk=yes&optionBus=yes";

my $response = get $url;

print $query->header();

print<<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <meta name="viewport" content="width = 320, user-scalable=no" />
  <link rel="stylesheet" href="css/master.css" type="text/css" media="screen" title="iPhone" charset="utf-8" />
  <link rel="apple-touch-icon" href="http://antidis.com/demos/trains/img/apple-touch-icon.png" />
HTML

print "<title>From " . $query->param('txtFromStation') . " to " . $query->param('txtToStation') . "</title>\n";

print<<HTML;
</head>

<body>
  
  <div id="TitleBar">
    <h1>Results</h1>
    <a id="backButton" class="button" href="day.cgi?txtFromStation=$from&amp;txtToStation=$to">Day</a>
    <a class="button" href="index.cgi">Find more</a>
  </div>
  
  <div id="Results">
HTML

print "<h2>Trains from <span class=\"station\">" . $query->param('txtFromStation') . "</span> to <span class=\"station\">" . $query->param('txtToStation') . "</span> on <span class=\"date\">" . $day_name[$wday] . " " . $mday . " " . $month_name[$mon] . "</span></h2>\n";

print<<HTML;
      <table width="100%" cellspacing="0">
        <thead>
          <th>Leaves</th>
          <th>Arrives</th>
          <th>&nbsp;</td>
        </thead>
        <tbody id="MissedTrains">
HTML

my $class = "";
my $changes = "";
my $dep_date = "";
my $dep_time = "";
my $arr_date = "";
my $arr_time = "";
my $changebuffer = "";
my $at_missed = 1;
my $has_missed = 0;
my $count = 0;

if ( $date ne "Today" ) {
  $at_missed = 0;
  print "</tbody>\n<tbody>\n";
}

#           <input type="hidden" name="From" value="Leixlip (Louisa Bridge)">
#           <input type="hidden" name="To" value="Maynooth">
#
#           <input type="hidden" name="Month" value="07">
#           <input type="hidden" name="Day" value="19">
#           <input type="hidden" name="Changes" value="0">
#           <input type="hidden" name="DepDate" value="19/07/2008">
#           <input type="hidden" name="DepTime" value="10:15:00">
#           <input type="hidden" name="ArrDate" value="19/07/2008">
#           <input type="hidden" name="ArrTime" value="10:21:00">



foreach my $line (split("\n", $response)) {

  if ( $line =~ /<input type=\"hidden\" name=\"Changes\" value=\"([^\"]+)\"/ ) {
    $changes = $1;
  }
  if ( $line =~ /<input type=\"hidden\" name=\"DepDate\" value=\"([^\"]+)\"/ ) {
    $dep_date = $1;
  }
  if ( $line =~ /<input type=\"hidden\" name=\"DepTime\" value=\"([^\"]+)\"/ ) {
    $dep_time = $1;
  }
  if ( $line =~ /<input type=\"hidden\" name=\"ArrDate\" value=\"([^\"]+)\"/ ) {
    $arr_date = $1;
  }
  if ( $line =~ /<input type=\"hidden\" name=\"ArrTime\" value=\"([^\"]+)\"/ ) {
    if ( $#stations == 0 ){
      print "<td class=\"changes\">Direct</td></tr>\n";
      @stations = ();
      $changebuffer = "";
    } elsif ( $changebuffer ne "" ) {
      for ( my $i = 0; $i < $#stations; $i++ ) {
        if ( $i == ( $#stations - 1 ) and ( $#stations > 1 ) ) { $changebuffer .= " and "; }
        elsif ( $i > 0 ) { $changebuffer .= ", "; }
        $changebuffer .= $stations[$i];
      }
      print "<td class=\"changes\"><a href=\"#\" onclick=\"alert('" . $changebuffer . "');\">Details</a></td></tr>\n";
      @stations = ();
      $changebuffer = "";
    }
    $arr_time = $1;
    $dep_time =~ s/\:\d\d$//;
    $arr_time =~ s/\:\d\d$//;
    my @dep_time_ar = ( 23, 59 );
    if ( $dep_time =~ /^(\d+)\:(\d+)$/ ) {
      @dep_time_ar = ( $1, $2 );
    }
    
    if ( ( $at_missed ) and ( ( $dep_time_ar[0] > $hour ) or ( ( $dep_time_ar[0] == $hour ) and ( $dep_time_ar[1] >= $min ) ) ) ) {
      $at_missed = 0;
      print "</tbody>\n<tbody>\n";
      if ( $count > 0 ) { $has_missed = 1; }
    }
    
    unless ( $at_missed ) { $class = ( $class eq "" ) ? "stripe" : ""; }
    
    print "          <tr class=\"" . $class ."\"><td>" . $dep_time . "</td><td>" . $arr_time  . "</td>";
    
    $dep_date = "";
    $dep_time = "";
    $arr_date = "";
    $arr_time = "";
    $count += 1;
  }
  
  # Pick up changes
  if ( $line =~ /<input type=\"hidden\" name=\"arrSta(\d+)\" value=\"([^\"]+)\"/ ) {
    my $i = $1;
    my $station = $2;
    
      if ( $i eq "1" ) {
        $changebuffer .= "Change at ";
      }
      push @stations, $station;
      
  }

}

# Final buffer stuff
if ( $#stations == 0 ){
  print "<td class=\"changes\">Direct</td></tr>\n";
  @stations = ();
  $changebuffer = "";
} elsif ( $changebuffer ne "" ) {
  for ( my $i = 0; $i < $#stations; $i++ ) {
    if ( $i == ( $#stations - 1 ) and ( $#stations > 1 ) ) { $changebuffer .= " and "; }
    elsif ( $i > 0 ) { $changebuffer .= ", "; }
    $changebuffer .= $stations[$i];
  }
  print "<td class=\"changes\"><a href=\"#\" onclick=\"alert('" . $changebuffer . "');\">Details</a></td></tr>\n";
  @stations = ();
  $changebuffer = "";
}


print<<HTML;
        </tbody>
      </table>
HTML

if ( $has_missed ) {
  print "<p>Missed trains are hidden. You can <a href=\"#Results\" onclick=\"document.getElementById('MissedTrains').style.display=\'table-row-group\';\">show trains you&rsquo;ve missed</a>.</p>";
}

print<<HTML;
    </div>
    
    <a href="save.cgi?txtFromStation=$from&amp;txtToStation=$to&amp;date=$date" class="newbox">Save this search...</a>

    <a href="$url" class="newbox">Perform this search at Irish Rail</a>

HTML

# print "<h2>Debug: URL</h2>\n";
# print "<div style=\"margin: 10px;background-color: #fff;\">" . $url . "</div>\n";
# print "<h2>Debug: Response</h2>\n";
# print "<div style=\"margin: 10px;background-color: #fff;\">" . $response . "</div>\n";

print<<HTML;
  <div id="Footer">Another little something from <a href="http://antidis.com/">Antidisinformation</a></div>

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
