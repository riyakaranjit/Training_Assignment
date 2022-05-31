#!/usr/bin/bash

# INPUTS
# shellcheck disable=SC2162
read -p "Enter a number: " NUMBER
echo "Your entered number is $NUMBER."


# CONDITIONALS
if [ "$NUMBER" -eq 1 ]
then
    echo "Number is 1."
elif [ "$NUMBER" -eq 2 ]
then
    echo "Number is 2."
else
    echo "Number is not 1 or 2."
fi

#If condition with and -a & or -o
read -p "Enter the side of a triangle: " tri1
read -p "Enter the side of next triangle: " tri2
read -p "Enter the side of next triangle: " tri3

if [ "$tri1" == "$tri2" -a "$tri2" == "$tri3" -a "$tri1" == "$tri3" ]
then
  echo "EQUILATERAL TRIANGLE"

elif [ "$tri1" == "$tri2" -o "$tri2" == "$tri3" -o "$tri1" == "$tri3" ]
then
  echo "ISOSCELES TRIANGLE"

else
  echo "SCALENE TRIANGLE"

fi


#Nested If condition

# Determine the day of week and store it inside the $day variable
# shellcheck disable=SC2046
echo $(date)
day=$(date +"%u")
echo "$day"
# Determine if it is morning or night and store it in the $time variable
time=$(date +"%p")
echo "$time"

# Check if the day of the week is between 1-5 (Mon-Fri) --> Date Formats
if [ "$day" -le 5 ]; then
        echo "today is a weekday"

        if [ "$time" == "AM" ]; then
                echo "it is morning"
        else
                echo "it is night"
        fi
else
        # if the first condition was not met, execute the following command
        echo "today is the weekend!"
fi

for i in {1..3}; do \
  curl -X POST -H "Content-Type: application/json" -d \
    '{"number":"'$i'"}' "https://httpbin.org/post"; \
done
