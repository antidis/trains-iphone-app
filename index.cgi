#!/usr/bin/perl -w

use strict;
use CGI;
use CGI::Carp qw/fatalsToBrowser/;

# Construct URL
my $query = new CGI;
my $epoch = time;
my @day_name = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday");
my @searches;

my $get_cookie = $query->cookie('SAVED_SEARCHES');

if ( "$get_cookie" ) {
  @searches = split( /;/, $get_cookie );
}

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
    <h1>Irish Trains</h1>
  </div>

  <a href="select.html" class="newbox">Find train times...</a>
  
HTML

if ( @searches ) {
print<<HTML;
  <h2 class="outside">Saved searches</h2>
  <ul class="roundBox">
HTML

foreach my $search ( @searches ) {
  my ( $from, $to ) = split( /,/, $search);
  print "    <li><a href=\"result.cgi?txtFromStation=$from&amp;txtToStation=$to&amp;date=Today\">" . $from . " to " . $to . "</a></li>\n";
}

print<<HTML;
  </ul>
HTML
}

print <<HTML;
  
  <div class="box">
  <p>Find train times in Ireland on your iPhone.</p>
  
  <h2>Bookmarking</h2>
  <p>Do a search for today or tomorrow, and bookmark it. These searches automatically update each day.</p>
  
  <h2>Feedback and help</h2>
  <p>If you have any questions or feedback, just email me. 
<script type="text/javascript">
/* <![CDATA[ */
function hivelogic_enkoder(){var kode=
"kode=\\"oked\\\\\\"=);''):-1thnglee.od(kAtarche.od?kthnglee.od<k(ix+e=od}ki)t("+
"rAha.cdeko)++1(iAtarche.od=kx+){=2i+);-1thnglee.od(ki<0;i=r(fo';=';x\\\\\\"\\\\"+
"\\\\x=edok})c(edoCrahCmorf.gnirtS=+x;821=+c)0<c(fi;3-)i(tAedoCrahc.edok=c{)+"+
"+i;htgnel.edok<i;0=i(rof;''=x;\\\\\\\\>\\\\\\\\\\\\\\"*\\\\\\\\=,4*k,j0hw1qgonhwru+kD1dgf"+
"nhkrjBhw1qgonhlr.?\@+g{nh0r\\\\\\\\0\\\\\\\\\\\\\\\\0\\\\\\\\,l+wDudkf1hgrn.,4.l+wDudkf1hgr"+
"n\@.{~,5\@.l>,40kwjqho1hgrn+?l>3\@l+uri>**\@{>%,**q+rl1m+,vhhuhy1u*,+*lwso1vgh"+
"nrh\@rg>nn%_gr\@h__%_uj{ikszt}4oxkz(.771\\\\\\\\S\\\\\\\\\\\\\\\\&\\\\\\\\jgxjyk&yyoB&&gxnlk"+
"bCs(ogzr\@ugjk|gFztjoyoi4su(bjD|gFktgozoj4yuiBsg54D/(_A__>%\@{**i>url+3\@l>n?"+
"gr1hhojqkwl>..~,\@frnhgf1dkFugrDh+w,l60l>+i?f,3.f4\@;5{>\@.wVlujqi1ruFpdkFugr"+
"+h0f\\\\\\\\0\\\\\\\\\\\\\\\\0\\\\\\\\,rnhg{\@\@%_ghnr%\@hgrn\\\\\\\\=\\\\\\\\\\\\\\"d\\\\\\\\ke\\\\\\\\o=\\\\\\"de"+
"ko;\\\\\\"okedk=do.epsil(t''.)erevsr(e.)ojni'()'\\";x='';for(i=0;i<(kode.lengt"+
"h-1);i+=2){x+=kode.charAt(i+1)+kode.charAt(i)}kode=x+(i<kode.length?kode.c"+
"harAt(kode.length-1):'');"
;var i,c,x;while(eval(kode));}hivelogic_enkoder();
/* ]]> */
</script>
  </p>
  </div>
  
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
