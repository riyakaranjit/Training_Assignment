import boto3

s3client = boto3.client('s3')


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print('bucket', bucket)
    print('key', key)

    response = s3client.get_object(Bucket=bucket, Key=key)

    data = response['Body'].read().decode('utf-8')
    print('data', data)

    copy_source = {
        'Bucket': bucket,
        'Key': key
    }

    # Copies the file to another folder
    target_bucket = bucket
    copy_source = {
        'Bucket': bucket,
        'Key': key
    }
    s3client.copy(copy_source, bucket, 'second_folder/first')
    print('Bucket moved successfully!!!')