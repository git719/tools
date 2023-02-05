#!/usr/bin/perl
# puzzle-12ball.pl
#
# Answer to the OTTER billiard ball puzzle presented in the June 1997 CACM.
# See end of file for logic.
#
# There are twelve billiard balls, eleven of which are identical in weight. The remainin
# all—the odd one—has a different weight. You are not told whether it is heavier or lighter.
# 
# You have a balance scale for weighing the balls. Can you ﬁnd which ball is the odd ball in
# three weighings, and can you also ﬁnd out whether it is lighter or heavier than the others?


# create array of 12 balls with 2 as default weight
for ($i = 1; $i < 13; $i++) {
   $B[$i] = 2;
}


# select one of them at random and give it a weight of 3
srand;
$randball = 1 + int(rand(11));
$B[$randball] = 3; 


# printout the weigh of the 12 balls
print STDOUT "\n";
for ($i = 1; $i < 13; $i++) {
   print STDOUT $B[$i];
   print STDOUT " " unless ($i % 4);
}
print STDOUT "\n\n";


# now select the odd one out
print STDOUT "1st Weighing Follows:\n";
$result = &weigh($B[1].$B[2].$B[3].$B[4],$B[5].$B[6].$B[7].$B[8]);
print STDOUT "\n";

if ($result eq 'less') {
   #
   # HEAVY in SET2 or LIGHT in SET1
   #
   print STDOUT "2nd Weighing Follows:\n";
   $result = &weigh($B[1].$B[2].$B[9],$B[3].$B[4].$B[5]);
   print STDOUT "\n";
   if ($result eq 'less') {
      #
      # 1,2 is LIGHT or 5 is HEAVY
      #
      print STDOUT "3rd Weighing Follows:\n";
      $result = &weigh($B[1],$B[2]);
      print STDOUT "\n";
      if ($result eq 'less') {
         print STDOUT "Result = ball 1 is the light one out.\n";         
      } elsif ($result eq 'more') {
         print STDOUT "Result = ball 2 is the light one out.\n";         
      } elsif ($result eq 'same') {
         print STDOUT "Result = ball 5 is the heavy one out.\n";         
      }
   } elsif ($result eq 'more') {
      #
      # 3,4 is LIGHT
      #
      print STDOUT "3rd Weighing Follows:\n";
      $result = &weigh($B[3],$B[4]);
      print STDOUT "\n";
      if ($result eq 'less') {
         print STDOUT "Result = ball 3 is the light one out.\n";         
      } elsif ($result eq 'more') {
         print STDOUT "Result = ball 4 is the light one out.\n";         
      } elsif ($result eq 'same') {
         print STDOUT "Result = they're all the same!!\n";         
      }
   } elsif ($result eq 'same') {
      #
      # 6, 7, or 8 must be the HEAVY ball
      #
      print STDOUT "3rd Weighing Follows:\n";
      $result = &weigh($B[6],$B[7]);
      print STDOUT "\n";
      if ($result eq 'less') {
         print STDOUT "Result = ball 7 is the heavy one out.\n";         
      } elsif ($result eq 'more') {
         print STDOUT "Result = ball 6 is the heavy one out.\n";         
      } elsif ($result eq 'same') {
         print STDOUT "Result = ball 8 is the heavy one out.\n";         
      }
   }
} elsif ($result eq 'more') {
   #
   # HEAVY in SET1 or LIGHT in SET2
   #
   print STDOUT "2nd Weighing Follows:\n";
   $result = &weigh($B[1].$B[2].$B[9],$B[3].$B[4].$B[5]);
   print STDOUT "\n";
   if ($result eq 'less') {
      #
      # 3 or 4 are the HEAVY ball
      #
      print STDOUT "3rd Weighing Follows:\n";
      $result = &weigh($B[3],$B[4]);
      print STDOUT "\n";
      if ($result eq 'less') {
         print STDOUT "Result = ball 4 is the heavy one out.\n";         
      } elsif ($result eq 'more') {
         print STDOUT "Result = ball 3 is the heavy one out.\n";         
      } elsif ($result eq 'same') {
         print STDOUT "Result = they're all the same!!\n";         
      }
   } elsif ($result eq 'more') {
      #
      # 1,2 is HEAVY or 5 is LIGHT
      #
      print STDOUT "3rd Weighing Follows:\n";
      $result = &weigh($B[1],$B[2]);
      print STDOUT "\n";
      if ($result eq 'less') {
         print STDOUT "Result = ball 2 is the heavy one out.\n";         
      } elsif ($result eq 'more') {
         print STDOUT "Result = ball 1 is the heavy one out.\n";         
      } elsif ($result eq 'same') {
         print STDOUT "Result = ball 5 is the light one out.\n";         
      }
   } elsif ($result eq 'same') {
      #
      # 6, 7, or 8 must be the LIGHT ball
      #
      print STDOUT "3rd Weighing Follows:\n";
      $result = &weigh($B[6],$B[7]);
      print STDOUT "\n";
      if ($result eq 'less') {
         print STDOUT "Result = ball 6 is the light one out.\n";         
      } elsif ($result eq 'more') {
         print STDOUT "Result = ball 7 is the light one out.\n";         
      } elsif ($result eq 'same') {
         print STDOUT "Result = ball 8 is the light one out.\n";         
      }
   }
} elsif ($result eq 'same') {
   #
   # HEAVY or LIGHT ball is in SET3
   #
   print STDOUT "2nd Weighing Follows:\n";
   $result = &weigh($B[1].$B[2].$B[3],$B[9].$B[10].$B[11]);
   print STDOUT "\n";
   if ($result eq 'less') {
      #
      # 9, 10, or 11 must be the HEAVY ball
      #
      print STDOUT "3rd Weighing Follows:\n";
      $result = &weigh($B[9],$B[10]);
      print STDOUT "\n";
      if ($result eq 'less') {
         print STDOUT "Result = ball 10 is the heavy one out.\n";         
      } elsif ($result eq 'more') {
         print STDOUT "Result = ball 9 is the heavy one out.\n";         
      } elsif ($result eq 'same') {
         print STDOUT "Result = ball 11 is the heavy one out.\n";         
      }
   } elsif ($result eq 'more') {
      #
      # 9, 10, or 11 must be the LIGHT ball
      #
      print STDOUT "3rd Weighing Follows:\n";
      $result = &weigh($B[9],$B[10]);
      print STDOUT "\n";
      if ($result eq 'less') {
         print STDOUT "Result = ball 9 is the light one out.\n";         
      } elsif ($result eq 'more') {
         print STDOUT "Result = ball 10 is the light one out.\n";         
      } elsif ($result eq 'same') {
         print STDOUT "Result = ball 11 is the light one out.\n";         
      }
   } elsif ($result eq 'same') {
      #
      # ball 12 is either HEAVY or LIGHT
      #
      print STDOUT "3rd Weighing Follows:\n";
      $result = &weigh($B[1],$B[12]);
      print STDOUT "\n";
      if ($result eq 'less') {
         print STDOUT "Result = ball 12 is the heavy one out.\n";         
      } elsif ($result eq 'more') {
         print STDOUT "Result = ball 12 is the light one out.\n";         
      } elsif ($result eq 'same') {
         print STDOUT "Result = they're all the same!!\n";         
      }
   }
}


# subroutine to weigh 2 sets of balls and print their contents also
sub weigh {
   local($a,$b) = @_;
   local($l) = length($a);
   local($i) = 0;
   if ($a < $b) {
      printf STDOUT "%-s %s\n", $a, $b;
      for ($i = 0;$i < $l;$i++) { print STDOUT " "; }
      print STDOUT "\\\n";
      return 'less';   
   } elsif ($a > $b) {
      printf STDOUT "%-s %s\n", $a, $b;   
      for ($i = 0;$i < $l;$i++) { print STDOUT " "; }
      print STDOUT "/\n";
      return 'more';
   } else {
      printf STDOUT "%-s %s\n", $a, $b;   
      for ($i = 0;$i < $l;$i++) { print STDOUT " "; }
      print STDOUT "-\n";
      return 'same';
   }
}

Finito:
__END__


12 Ball Brainteaser
====================
There are 12 balls. 11 of the balls weigh the same. 1 of the balls is either heavier or 
lighter than the rest. You have an unmarked balance scale. Using the scale only 3 times, 
determine which ball is different and whether it is heavier or lighter than the rest. 


One Solution
=============
The set of all balls (1,2,3,4,5,6,7,8,9,10,11,12)

1ST WEIGHING: (1,2,3,4) vs (5,6,7,8)

  If (1,2,3,4) weights the same as (5,6,7,8) then the odd ball is in (9,10,11,12)

    2ND WEIGHING: (1,2,3) vs (9,10,11)
      If (1,2,3) weights the same as (9,10,11) then the odd ball is (12)
        3RD WEIGHING: (1) vs (12)
          If (1) weights the same as (12)  then they all weigh the SAME (foul play!)
          If (1) weights less than (12)    then (12) is the HEAVY ONE out
          If (1) weights more than (12)    then (12) is the LIGHT ONE out
      If (1,2,3) weights less than (9,10,11) then the *heavy* ball is in (9,10,11)
        3RD WEIGHING: (9) vs (10)
          If (9) weights the same as (10)  then (11) is the HEAVY ONE out
          If (9) weights less than (10)    then (10) is the HEAVY ONE out
          If (9) weights more than (10)    then (9) is the HEAVY ONE out
      If (1,2,3) weights more than (9,10,11) then the *light* ball is in (9,10,11)
        3RD WEIGHING: (9) vs (10)
          If (9) weights the same as (10)  then (11) is the LIGHT ONE out
          If (9) weights less than (10)    then (9) is the LIGHT ONE out
          If (9) weights more than (10)    then (10) is the LIGHT ONE out

  If (1,2,3,4) weights less than (5,6,7,8) then *light* ball is in (1,2,3,4) or *heavy* ball is in (5,6,7,8)

    2ND WEIGHING: (1,2,9) vs (3,4,5)
      If (1,2,9) weights the same as (3,4,5) then the *heavy* ball is in (6,7,8)
        3RD WEIGHING: (6) vs (7)
          If (6) weights the same as (7)   then (8) is the HEAVY ONE out
          If (6) weights less than (7)     then (7) is the HEAVY ONE out
          If (6) weights more than (7)     then (6) is the HEAVY ONE out
      If (1,2,9) weights less than (3,4,5) then the *light* ball is in (1,2) or (5) is the *heavy* ball
        3RD WEIGHING: (1) vs (2)
          If (1) weights the same as (2)   then (5) is the HEAVY ONE out
          If (1) weights less than (2)     then (1) is the LIGHT ONE out
          If (1) weights more than (2)     then (2) is the LIGHT ONE out
      If (1,2,9) weights more than (3,4,5) then the *light* ball is in (3,4)
        3RD WEIGHING: (3) vs (4)
          If (3) weights the same as (4)   then they all weigh the SAME (foul play!)
          If (3) weights less than (4)     then (3) is the LIGHT ONE out
          If (3) weights more than (4)     then (4) is the LIGHT ONE out

  If (1,2,3,4) weights more than (5,6,7,8) then *light* ball is in (5,6,7,8) or *heavy* ball is in (1,2,3,4)

    2ND WEIGHING: (1,2,9) vs (3,4,5)
      If (1,2,9) weights the same as (3,4,5) then the *light* ball is in (6,7,8)
        3RD WEIGHING: (6) vs (7)
          If (6) weights the same as (7)   then (8) is the LIGHT ONE out
          If (6) weights less than (7)     then (6) is the LIGHT ONE out
          If (6) weights more than (7)     then (7) is the LIGHT ONE out
      If (1,2,9) weights less than (3,4,5) then the *heavy* ball is in (3,4)
        3RD WEIGHING: (3) vs (4)
          If (3) weights the same as (4)   then they all weigh the SAME (foul play!)
          If (3) weights less than (4)     then (4) is the HEAVY ONE out
          If (3) weights more than (4)     then (3) is the HEAVY ONE out
      If (1,2,9) weights more than (3,4,5) then the *heavy* ball is in (1,2) or (5) is the *light* ball
        3RD WEIGHING: (1) vs (2)
          If (1) weights the same as (2)   then (5) is the LIGHT ONE out
          If (1) weights less than (2)     then (2) is the HEAVY ONE out
          If (1) weights more than (2)     then (1) is the HEAVY ONE out





