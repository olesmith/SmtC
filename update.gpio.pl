#!/usr/bin/perl

use strict;

system("./inc.pl");
system("/usr/local/Perl/bin/CleanTree.pl /usr/local/Php");

my $echo="echo ";
my $echo="";

my $name="Python";
my $indir="/usr/local/".$name;
my $outdir="/usr/local/".$name;
my $tardir="/usr/local/tars/".$name;
my $dir="Python";
my @desthosts=("sade","pi1");

sub Main::TimeHash
{
   my ($mtime)=@_;

   if ( $mtime ) {}
   else { $mtime=time(); }

   my %time;
   (
     $time{sec},$time{min},$time{hour},
     $time{date},$time{month},$time{year},
     $time{weekday}
   )=localtime($mtime);

   $time{mtime}=$mtime;

   $time{year}+=1900;

   $time{month}++;
   unless ( $time{month}=~/\d\d/ )
   {
       $time{month}="0".$time{month};
   }

   unless ( $time{date}=~/\d\d/ )
   {
       $time{date}="0".$time{date};
   }


   unless ( $time{hour}=~/\d\d/ )
   {
       $time{hour}="0".$time{hour};
   }

   unless ( $time{min}=~/\d\d/ )
   {
       $time{min}="0".$time{min};
   }

   unless ( $time{sec}=~/\d\d/ )
   {
       $time{sec}="0".$time{sec};
   }

   return %time;
}


my %timehash=Main::TimeHash();
my $timestamp=join
(
   ".",
   $timehash{ 'year' },
   $timehash{ 'month' },
   $timehash{ 'date' },
);


chdir("/usr/local");
system("/usr/local/bin/CleanTree.pl Python");


my $tarname=$tardir."/".$name.".".$timestamp.".tgz";

system
(
   $echo."/bin/tar cvfz ".$tarname." ".
   "Python ".
   "--exclude=Pythin/curves"
);

foreach my $desthost (@desthosts)
{
   system($echo."/usr/bin/scp ".$tarname." ".$desthost.":".$tarname);
}

1;

