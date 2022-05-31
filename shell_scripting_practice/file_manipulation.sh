#!/usr/bin/bash

# CREATE FOLDER AND WRITE TO A FILE
mkdir hello
touch "hello/world.txt"
echo "Hello, World! I made a new file on  my own." >> "hello/world.txt"
echo "Created hello/world.txt"

#Reading File line by line
LINE=1
while read -r CURRENT_LINE
 do
   echo "$LINE: $CURRENT_LINE"
  ((LINE++))
done < "sample_file.txt"

#Adding Complex argument using back ticks `
var=`egrep hi *`
echo "$var"




