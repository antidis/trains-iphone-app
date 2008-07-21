#!/usr/bin/perl -w

use strict;
use CGI;
use CGI::Carp qw/fatalsToBrowser/;

# Construct URL
my $query = new CGI;
my $from = $query->param('txtFromStation');
my $to = $query->param('txtToStation');
my $date = $query->param('date');
my $current_search = $from . "," . $to;
my @searches;
my $already_saved = 0;

my $get_cookie = $query->cookie('SAVED_SEARCHES');

if ( "$get_cookie" ) {
  @searches = split( /;/, $get_cookie );

  foreach my $search (@searches) {
    if ( $search eq $current_search ) {
      $already_saved = 1;
    }
  }

}

unless ( $already_saved ) {
  push @searches, $current_search;
}

my $set_cookie = $query->cookie(-name=>'SAVED_SEARCHES', 
  -value=>'' . join( ';', @searches ),
  -expires=>'+1y',
  -path=>'/');

print $query->header(-cookie=>$set_cookie);

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
    <h1>Saved</h1>
    <a id="backButton" class="button" href="result.cgi?txtFromStation=$from&amp;txtToStation=$to&amp;date=$date">Times</a>
  </div>
  
  <div class="box">
    <h2>Search saved</h2>
    <p>The search from $from to $to will now be available from the <a href="index.cgi">homepage</a>.</p>
  </div>
  
  <a href="result.cgi?txtFromStation=$from&amp;txtToStation=$to&amp;date=$date" class="newbox">Back to times</a>
  <a href="select.html" class="newbox">Find more train times</a>

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
