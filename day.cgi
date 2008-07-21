#!/usr/bin/perl -w

use strict;
use CGI;
use CGI::Carp qw/fatalsToBrowser/;
use Time::Local;
$ENV{TZ} = ':/usr/share/zoneinfo/Europe/Dublin';

# Construct URL
my $query = new CGI;
my $from = $query->param('txtFromStation');
my $to = $query->param('txtToStation');
my $epoch = time;
my @day_name = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday");


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
    <h1>Day of Travel</h1>
    <a id="backButton" class="button" href="to.cgi?txtFromStation=$from">To</a>
  </div>
  
  <div class="undernote">From $from to $to</div>

  <ul class="internal_list">
HTML

for ( my $i = 0; $i < 7; $i++ ) {
  my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime ( $epoch + ( $i * 86400 ) );

  $mon += 1;
  $year += 1900;
  if ( $mday < 10 ) { $mday = "0" . $mday; }
  if ( $mon < 10 ) { $mon = "0" . $mon; }

  if ( $i == 0 ) { print "<li><a href=\"result.cgi?txtFromStation=" . $from . "&amp;txtToStation=" . $to . "&amp;date=Today\">Today</a></li>\n"; }
  elsif ( $i == 1 ) { print "<li><a href=\"result.cgi?txtFromStation=" . $from . "&amp;txtToStation=" . $to . "&amp;date=Tomorrow\">Tomorrow</a></li>\n"; }
  else { print "<li><a href=\"result.cgi?txtFromStation=" . $from . "&amp;txtToStation=" . $to . "&amp;date=" . $mday . $mon . $year . "\">" . $day_name[$wday] . "</a></li>\n"; }
  
}

print<<HTML;
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
