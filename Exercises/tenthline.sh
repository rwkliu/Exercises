#!/usr/bin/bash
#bash script to print every tenth line in input file
#chmod 755 to make it executable

x=0
while read line
do 
  ((x++))
  [ $(expr $x % 10) -eq 0 ] && echo $line;
done