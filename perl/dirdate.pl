#!/usr/bin/perl
# dirdate.pl
#

$dirFile = 'temp.dir';
$drvPath = $ARGV[0];
$oldDate = $ARGV[1];
$descDate = (Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec)[substr($oldDate,2,2)-1];
$descDate = substr($oldDate,4) . " $descDate 19" . substr($oldDate,0,2);

# exit if bogus arguments are given 
if (!(-e $drvPath) || ($drvPath eq '') || ($oldDate eq '')) {
   print STDERR "Reports the total size of all files in the system which\n";
   print STDERR "were last written to before the given date.\n\n";
   print STDERR "   PERL DIRDATE.PL [drive:][path][filename] [date]\n\n";
   print STDERR "   Date format must be YYMMDD (ie 980521 for May 21 1998)\n";
   goto Finito;
}

# log file name is script name + the ".LOG" extension
$logFile = substr($0, 0, length($0)-2) . "log";
open(LOG, ">$logFile") || print LOG "Error opening $logFile!";
($sec,$min,$hr,$mday,$mon,$yr,$wday,$yday,$isdst) = localtime;
$dow = (Mon,Tue,Wed,Thu,Fri,Sat,Sun)[$wday-1]; 
$moy = (Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec)[$mon];
printf LOG "Script Name = %s\n", $0;
printf LOG "Date        = %s %d %s %d\n", $dow, $mday, $moy, $yr;
printf LOG "Start Time  = %d:%02d:%02d\n\n", $hr, $min, $sec;

$oldSize = 0; $flag = 0;
@DIRLIST = `dir $drvPath /-c /s /tw`;
for ($i = 0; $i <= $#DIRLIST; $i++ ) {
   $_ = $DIRLIST[$i];
   next if /^ Volume/ || /^$/ || /<DIR>/ || /Directory of/;
   $flag = 1, next if /Total Files/;
   $totalSize = $1 if /.*File\(s\)\s*(\d+).*/ && ($flag eq 1); 
   next if /File\(s\)/;

   # remember to adjust regular expression to suit DATE separator in system!
   ($d1,$d2,$d3,$fileSize) = /^(\d+).(\d+).(\d+).{8}\s*(\d+).*/;

   $fileDate = "$d3$d2$d1";
   $oldSize += $fileSize if ($fileDate lt $oldDate);
}

# report
$percentage = (100 * ($oldSize/$totalSize)) if ($totalSize > 0);
printf LOG "\n   %-45s = %16s bytes\n\n", "Total size of files in $drvPath", &commas($totalSize);
printf LOG "   %-45s = %16s bytes\n\n", "Total size of files older than $descDate", &commas($oldSize);
printf LOG "   %-45s = %16u percent\n\n", "Pecentage of data older than $descDate", $percentage;

# log end time
($sec,$min,$hr,$mday,$mon,$yr,$wday,$yday,$isdst) = localtime;
printf LOG "\nEnd time    = %d:%02d:%02d\n\n", $hr, $min, $sec;
close(LOG);

# put commas in number (xxx,xxx,xxx,xxx is max)
sub commas {
   local($_) = @_;
   for ($i = 0; $i < length($_); $i += 3) {
     
   }
   }
   }
   if (length($_) > 9) {
      s/(.*\d)(\d\d\d)(\d\d\d)(\d\d\d)/$1,$2,$3,$4/;
   } elsif (length($_) > 6) {
      s/(.*\d)(\d\d\d)(\d\d\d)/$1,$2,$3/;
   } elsif (length($_) > 3) {
      s/(.*\d)(\d\d\d)/$1,$2/;
   }
   $_;
}
