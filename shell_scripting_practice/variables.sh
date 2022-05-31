#!/usr/bin/bash

# ECHO COMMAND
echo Hello, World!

# Current Shell
echo "$SHELL"

#Variables
# Command line arguments are separated by whitespace unless tha argumnets are quoted.
NAME="Riya Karanjit"

echo "My name is $NAME."

#Arithmetic Expressions Expr

expr 16 / 4
var=$((3**3))
echo $var

# Scale defines the number of decimal places required in the output
#echo "scale=3;10/3" | bc
printf "%.2f \n" $((10/3))

# String Manipulation
# To find the length of the variable.
echo ${#NAME}

#Concatenate strings using variables
Address="Teku"
#echo "${NAME}--${Address}"
echo ""$NAME" from "$Address""

#Concatenation of string using array
arr1=("$NAME" "$Address")
# shellcheck disable=SC2068
echo "The array string concatenation is: " ${arr1[@]}
echo "The first element can be accessed as: " ${arr1[0]}


#Shortest Substring Matching

filename="bash.string.hello.txt"

echo "Delete the shortest substring from front that matches *.: " ${filename#*.}
echo "Delete the shortest substring from back that matches .*: " ${filename%.*}

echo "Delete the longest substring from front that matches *.: " ${filename##*.}
echo "Delete the longest substring from front that matches .*: " ${filename%%.*}


#Splitting a string
string="KSI,Simon,Vik,Tobi,Ethan"

#Setting IFS -- Input Field Separator ','
IFS=','

#reading the split string into array
read -ra sidemen_arr <<< "$string"

for val in "${sidemen_arr[@]}"
 do
  echo "name = $val"
done




