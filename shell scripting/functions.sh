#!/usr/bin/bash


# FOR LOOPS
for i in {1..5}
do
    echo "$i"
done

NUMBERS="12 31 25 16"
for NUMBER in $NUMBERS
 do
  echo "NUMBER $NUMBER"
done

# FOR LOOPS taking arguments from command line.
for x in $@
do
    echo "Entered arg is $x"
done

# Alternative way to get argument from command line
for arg
 do
  echo "$arg"
done

#While LOOP
NUM=1
while [[ "$NUM" -le 10 ]];  do
  echo "Number is $NUM"
    (( NUM +=1 ))
done

# Functions with params
function age_func() {
  echo Hi! I am $1 and I am $2 years old.
}

age_func "RK" "100"

# One line FUNCTIONS
function hello_world_func { echo Hello I\'m World.; echo Bye!; }
hello_world_func


#cURL API call

#curl -s -k -X <<COMMAND>> –header Content-Type: application/json’ \
#        –header ‘Accept:application/json’  \
#        <<AUTHENTICATION>>  <<OPTIONAL_DATA>> \
#        <<RESTAPI_ENDPOINT>>

curl -X POST https://reqbin.com/echo/post/json2 -H "Content-Type: application/json" -d '{"productId": 123456, "quantity": 100}'
