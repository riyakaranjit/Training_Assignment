import os
import sys
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

    def download_file(self, bucket_name, object_name, file_download_name=None) -> bool:
        """
        Download an S3 object to a file.
        :param bucket_name: Bucket to upload to
        :param object_name: S3 object name to download from
        :param file_download_name: name of the downloaded file. If not specified object name is used.
        :return:
        """
        if file_download_name is None:
            file_download_name = os.path.basename(object_name)
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
    bucket_name = 'my-first-bucket-ccdc6624-4309-4e21-95b4-0be07470aa8a'

    # s3_manager_object.move_bucket(bucket_name, 'hello_object', 'new_folder/new')
    print("Argument from bash script: ", sys.argv[1])
    print(bucket_name)

    # s3_manager_object.download_file(bucket_name, sys.argv[1])
    # s3_manager_object.download_file(bucket_name, 'second_file.csv', 'second_file.csv')

    # bucket_to_be_deleted = 'my-first-bucket-47c6c0f6-8e05-455d-9bcb-04e2ccae5ce0'
    # s3_manager_object.delete_bucket(bucket_to_be_deleted)

    # input_list = ['A', 'B', 'C', 'D']
    # os.environ['INPUT_LIST'] = ' '.join(input_list)
    # print("INPUT_LIST", os.environ['INPUT_LIST'])

    # import subprocess
    # subprocess.call(['bash', 's3_bash.sh', 'foo', 'bar'])


if __name__ == '__main__':
    main()
