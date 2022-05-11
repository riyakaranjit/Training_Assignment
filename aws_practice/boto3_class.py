import os

import boto3
import uuid

from botocore.exceptions import ClientError


class S3Manager:
    def __init__(self):
        self.session = boto3.session.Session()
        current_region = self.session.region_name

        self.s3_client = boto3.client('s3')

    @staticmethod
    def create_bucket_name(bucket_name_prefix):
        """
            The bucket name must always be unique across the entire AWS platform.
        :param bucket_name_prefix: Prefix for bucket name
        :return: Bucket Name prefix + 36 char long uuid
        """
        return '-'.join([bucket_name_prefix, str(uuid.uuid4())])

    def create_bucket(self, bucket_name_prefix):
        """
        When creating a bucket you'll need to explicitly define the region unless its United States. You can use session
        object as it will create session from the credentials.
        The following params must be added inside create_bucket if not 'us-east-1'
        # CreateBucketConfiguration=None if current_region == 'us-east-1' else {'LocationConstraint': current_region})
        :param bucket_name_prefix
        :return: bucket_name , bucket_response: dict
        """
        bucket_name = self.create_bucket_name(bucket_name_prefix)
        bucket_response = self.s3_client.create_bucket(
            Bucket=bucket_name)

        print("Bucket created successfully!!!")
        return bucket_name

    @staticmethod
    def create_temp_file(size, file_name, file_content):
        random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
        with open(random_file_name, 'w') as f:
            f.write(str(file_content) * size)
        print("Created temporary file!")
        return random_file_name

    def upload_file(self, file_name, bucket_name, object_name=None) -> bool:
        """
        Upload a file to S3 bucket
        :param file_name: File to be uploaded
        :param bucket_name: Bucket to upload to
        :param object_name: S3 object name. If not specified file name is used.
        :return: True if the file is uploaded, else False
        """
        if object_name is None:
            object_name = os.path.basename(file_name)
        try:
            self.s3_client.upload_file(
                Filename=file_name,
                Bucket=bucket_name,
                Key=object_name
            )
            print('File uploaded successfully!!!')
        except ClientError as e:
            return False
        return True

    def download_file(self, bucket_name, object_name, file_download_name) -> bool:
        """
        Download an S3 object to a file.
        :param bucket_name: Bucket to upload to
        :param object_name: S3 object name to download from
        :param file_download_name: name of the downloaded file
        :return:
        """
        try:
            self.s3_client.download_file(bucket_name, object_name,
                                         f'{file_download_name}')
            print('File downloaded successfully!!!')
        except ClientError as e:
            return False
        return True

    def delete_bucket(self, bucket_name):
        """
        Deletes entire bucket. As the bucket needs to be emptied before its deletion so if bucket is not empty, first
        all objects are deleted then bucket is deleted.
        param bucket_name: Bucket to be deleted
        """
        response = self.s3_client.list_objects(Bucket=bucket_name)
        if 'Contents' in response:
            for r in response['Contents']:
                print(r['Key'])
                self.s3_client.delete_object(Bucket=bucket_name,
                                             Key=r['Key'])
                print('Object deleted!!!')
            self.delete_bucket(bucket_name)
        else:
            self.s3_client.delete_bucket(Bucket=bucket_name)

        print('Bucket deleted successfully!!!')

    def move_bucket(self, bucket_name, object_name, target_name):
        copy_source = {
            'Bucket': bucket_name,
            'Key': object_name
        }
        self.s3_client.copy(copy_source, bucket_name, target_name)
        print('Bucket moved successfully!!!')


def main():
    s3_manager_object = S3Manager()
    # bucket_one = s3_manager_object.create_bucket('my-second-bucket')
    first_file = s3_manager_object.create_temp_file(10, 'first_file', 'second ')
    bucket_name = 'my-second-bucket-cebeb0dc-0b34-4c30-a998-dee51fb32938'

    s3_manager_object.upload_file(first_file, bucket_name,
                                  object_name='new_folder/third_object')

    s3_manager_object.move_bucket(bucket_name, 'hello_object', 'new_folder/new')
    s3_manager_object.download_file(bucket_name, 'new_folder/new', 'my_first_download')
    bucket_to_be_deleted = 'my-first-bucket-47c6c0f6-8e05-455d-9bcb-04e2ccae5ce0'
    s3_manager_object.delete_bucket(bucket_to_be_deleted)


if __name__ == '__main__':
    main()
