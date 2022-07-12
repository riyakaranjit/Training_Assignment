#!/usr/bin/bash

# configure AWS CLI (e.g. use IAM role for S3 access)
#export AWS_DEFAULT_REGION=us-east-1
#export AWS_ACCESS_KEY_ID=AKIASO36CAQHFWSIVTXR
#export AWS_SECRET_ACCESS_KEY=FlrvTqpuHdh0ioUKIG3reto1Y08nGOQmL1eAYbm5

# space-separated string (contains dates etc.)
#file_list=$(aws s3 ls s3://my-first-bucket-28305cc8-ecdc-4296-9ba3-25d208b7a0d8 --recursive)

# file list as an array

#file_list=(`aws s3 ls s3://my-first-bucket-28305cc8-ecdc-4296-9ba3-25d208b7a0d8 | awk '{print $4}'`)
# first element
file1="s3://my-first-bucket-28305cc8-ecdc-4296-9ba3-25d208b7a0d8/python_questions.zip"
file2="s3://my-first-bucket-28305cc8-ecdc-4296-9ba3-25d208b7a0d8/first_file.csv"
file3="s3://my-first-bucket-28305cc8-ecdc-4296-9ba3-25d208b7a0d8/second_file.csv"

file_list=("$file1" "$file2" "$file3")
#all elements

for file in ${file_list[@]}
do
  # shellcheck disable=SC2027
  echo "The file is: "$file""
  echo "The first part of file: "${file%/*}""
  echo "The second part of file: "${file##*/}""

  if [[ "${file##*/}" == *.zip ]]
   then
    continue;
  else
    echo "Downloading the csv files from s3..."

#    python boto3_class.py "${file##*/}" > tempfile.txt
#    var=`cat tempfile.txt`
#    echo "This is var" "$var"
#    rm tempfile.txt

    text=`python boto3_class.py "${file##*/}"`
    echo "This is text: " "$text"

#    python boto3_class.py "${file##*/}"
#
#    echo "This is 1" "$1"
#    echo "This is 2" "$2"
    echo "Hello" $INPUT_LIST
     for i in $INPUT_LIST
      do
        echo "This is from LIST: ""$i"
      done

    exitStatus=$?
    echo "Conversion Status " "$exitStatus"
    if [[ "$exitStatus" -eq 1 ]]
     then
      echo "Error occurred in conversion script"
      exit $exitStatus
      echo "Download incomplete!!!"
    else
     echo "Download complete!!!"
     echo "$LIST"

   fi

    echo "Complete!!!"
  fi


done