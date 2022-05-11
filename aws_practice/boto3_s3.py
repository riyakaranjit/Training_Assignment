import boto3
import uuid


def create_bucket_name(bucket_name_prefix):
    """
        The bucket name must always be unique across the entire AWS platform.
    :param bucket_name_prefix: Prefix for bucket name
    :return: Bucket Name prefix + 36 char long uuid
    """
    return '-'.join([bucket_name_prefix, str(uuid.uuid4())])


def create_bucket(bucket_name_prefix, s3_connection):
    """
        When creating a bucket you'll need to explicitly define the region unless its United States. You can use session
    object as it will create session from the credentials.
    The following params must be added inside create_bucket if not 'us-east-1'
    # CreateBucketConfiguration=None if current_region == 'us-east-1' else {'LocationConstraint': current_region})
    :param bucket_name_prefix
    :param s3_connection
    :return: bucket_name , bucket_response: dict
    """
    session = boto3.session.Session()
    current_region = session.region_name
    print(current_region)
    bucket_name = create_bucket_name(bucket_name_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name)

    print("Bucket created successfully!!!")
    return bucket_name, bucket_response


def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    print("Created temporary file!")
    return random_file_name


def upload_file(s3_resource, first_file, bucket_name):
    s3_resource.meta.client.upload_file(
        Filename=first_file,
        Bucket=bucket_name,
        Key=first_file
    )

    print('File uploaded successfully!!!')


def download_file(s3_resource, bucket_name, file_name):
    s3_resource.Object(bucket_name, file_name).download_file(
        f'{file_name}')
    print('File downloaded successfully!!!')


def main():
    # s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')

    # # Creating a bucket
    # first_bucket_name, first_response = create_bucket(bucket_name_prefix='my-first-bucket',
    #                                                   s3_connection=s3_resource.meta.client)
    # print(f'Bucket Name: {first_bucket_name}, Response: {first_response}')

    # Output the bucket names
    response = s3_resource.meta.client.list_buckets()
    bucket_name_to_list = 'my-first-bucket-b1f87bf6-6122-431a-be6a-5fe88fd56a03'
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'{bucket["Name"]}')

    # List the objects inside the bucket
    my_bucket = s3_resource.Bucket(name=bucket_name_to_list)
    print(f'Objects inside bucket {bucket_name_to_list} are: ')
    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)

    print('Objects inside this specified folder are: ')
    result = s3_resource.meta.client.list_objects(
        Bucket=bucket_name_to_list,
        Prefix="documents/",
        Delimiter='/')
    for objects in my_bucket.objects.filter(Prefix="documents/"):
        print(objects.key)

    # Create a temporary file
    # first_file = create_temp_file(10, 'my_first_file.txt', 'hi ')

    # # Uploading a file

    # upload_file(s3_resource, first_file, 'my-first-bucket-73f1a612-d386-4b3f-b2e4-98a648cc6d9b')

    # # Downloading a file
    # download_file(s3_resource, 'my-first-bucket-73f1a612-d386-4b3f-b2e4-98a648cc6d9b', 'bbef45my_first_file.txt')


if __name__ == '__main__':
    main()
