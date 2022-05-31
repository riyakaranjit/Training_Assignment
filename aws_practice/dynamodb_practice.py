import datetime
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import uuid
from pprint import pprint


class DynamodbManager:
    def __init__(self):
        self.session = boto3.session.Session()
        self.dynamodb = boto3.resource('dynamodb')

    def create_table(self, table_name, partition_key_name, sort_key_name):
        """
        Adds a new table to your account.
        :param table_name: Table name must be unique in every region
        :param partition_key_name: Primary key's attribute name
        :param sort_key_name: Composite key's attribute name (Sort_keyword + uuid)
        :return: created table
        """
        table = self.dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': partition_key_name,
                    'KeyType': 'HASH'  # Partition key :
                },
                {
                    'AttributeName': sort_key_name,
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': partition_key_name,
                    'AttributeType': 'S'  # Partition key
                },
                {
                    'AttributeName': sort_key_name,
                    'AttributeType': 'S'  # Partition key
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print('Table Created successfully!!!')
        return table

    def insert_item(self, table_name, item: dict):
        """
        Insert an item with all the attributes.
        :param table_name: Table to be inserted
        :param item: all the attribute with primary key to be inserted
        """
        table = self.dynamodb.Table(table_name)
        response = table.put_item(
            Item=item
        )
        print('Item inserted successfully!!!')
        return response

    def insert_multiple_items(self, table_name, *items):
        table = self.dynamodb.Table(table_name)
        print(items)
        for item in items:
            print(item)
            with table.batch_writer() as batch:
                batch.put_item(Item=item)
        print('Items inserted successfully!!!')
        return batch

    def get_item(self, table_name, dept_name, date):
        """
        Set of attributes for the item with the given primary and secondary key.
        :param table_name: Table name
        :param dept_name: Partition key item
        :param date: Sort Key item
        """
        table = self.dynamodb.Table(table_name)
        try:
            response = table.get_item(
                Key={
                    'Department': dept_name,
                    'Full_date': date
                }
            )
            print(response['Item'])
        except ClientError as e:
            print('Client Error Occurred: ', e.response['Error']['Message'])

    def get_all_items(self, table_name):
        """
        Read all items in a table. Using scan has 1 MB limit on the amount of data it will return so we need to
        paginate through the results in a loop.
        :param table_name: Table name
        """
        table = self.dynamodb.Table(table_name)

        response = table.scan()
        pprint(response['Items'])

    def scan_filter(self, table_name, attribute_key, attribute_value):
        table = self.dynamodb.Table(table_name)
        response = table.scan(
            FilterExpression=Attr('Department').eq('IT')
        )
        print(f'Filter {attribute_key} with value {attribute_value} \n: {response["Items"]}')
        pprint(response['Items'])

    def query(self, table_name, value):
        """
        Always favour query over scan as it accesses the data in the desired partition directly.
        :param table_name: Table name
        :param value: value to filter for
        """
        table = self.dynamodb.Table(table_name)
        # using DynamoDB Client
        # response = table.query(
        #     KeyConditionExpression='Department= :dept_name AND begins_with(Full_date, :date_value)',
        #     ExpressionAttributeValues={
        #         ':dept_name': value,
        #         ':date_value': '2018'
        #     }
        # )
        response1 = table.query(
            KeyConditionExpression=Key('Department').eq(value) & Key('Full_date').begins_with('2018')
        )
        response2 = table.query(
            KeyConditionExpression=Key('Department').eq(value) & Key('Full_date').gt('2020')
        )
        print(f'{value} Department info with date starting from 2018: \n', response1['Items'])
        print(f'{value} Department info with date less than 2020: \n', response2['Items'])
        return response1, response2

    def update_item(self, table_name, dept_name, date, email, qa_name, reporting_line):
        """
        Edits an existing item's attributes, or adds a new item to the table if it does not already exist
        :param table_name: Table name
        :param dept_name: Partition key item
        :param date: Sort Key item
        :param email: Email Attribute to be updated
        :param dept_name: Department Attribute to be updated
        :param qa_name: QA Attribute to be updated
        :param reporting_line: Reporting Line Attribute to be updated
        """
        table = self.dynamodb.Table(table_name)
        response = table.update_item(
            Key={
                'Department': dept_name,
                'Full_date': date
            },
            ExpressionAttributeNames={
                '#section': 'Section',
                '#qa': 'QA',
                '#reporting_line': 'Reporting Line',
                '#email': 'Email'
            },
            ExpressionAttributeValues={
                ':email': email,
                ':qa_value': qa_name,
                ':reporting_line_value': reporting_line
            },
            UpdateExpression="SET #email = :email, #section.#qa = :qa_value, "
                             "#section.#reporting_line = :reporting_line_value",
            ReturnValues='ALL_NEW'  # Returns all the attributes of the item after the UpdateItem operation
        )
        print('Item updated successfully!!!')
        return response

    def delete_item(self, table_name, dept_name, date, email):
        """
        Deletes a single item in a table by the primary key.
        :param table_name: Table name
        :param dept_name: Primary key item
        :param date: Secondary key item
        :param email: The item will be deleted if the email matches
        """
        table = self.dynamodb.Table(table_name)
        try:
            response = table.delete_item(
                Key={
                    'Department': dept_name,
                    'Full_date': date
                },
                ExpressionAttributeNames={
                    '#email': 'Email'
                },
                ExpressionAttributeValues={
                    ':email': email,
                },
                ConditionExpression='#email = :email'
            )
            print("Item deleted successfully!!!")
            return response
        except ClientError as er:
            if er.response['Error']['Code'] == "ConditionalCheckFailedException":
                print(er.response['Error']['Message'])
            else:
                raise

    def delete_table(self, table_name):
        table = self.dynamodb.Table(table_name)
        table.delete()
        print("Table deleted successfully!!!")


if __name__ == '__main__':
    employee_table = DynamodbManager()
    # employee = employee_table.create_table('Employees', 'Department', 'Full_date')
    # print('Status: ', employee.table_status)
    emp1 = {"Name": "Lucas John", "Email": "john@handson.cloud", "Department": "IT",
            "Full_date": '-'.join([str(datetime.datetime.now()), str(uuid.uuid4().hex[:6])]),
            "Section": {"QA": "QA-1", "Reporting Line": "L1"}}
    emp2 = {"Name": "Louis Legend", "Email": "john@handson.cloud",
            "Full_date": '-'.join([str(datetime.datetime(2018, 6, 15, 2)), str(uuid.uuid4().hex[:6])]),
            "Department": "Civil", "Section": {"QA": "QA-1", "Reporting Line": "L1"}}
    emp3 = {"Name": "Logo Joshua", "Email": "joshua@handson.cloud",
            "Full_date": '-'.join([str(datetime.datetime(2020, 2, 2, 3)), str(uuid.uuid4().hex[:6])]),
            "Department": "Electronics", "Section": {"Development": "SD-1", "Reporting Line": "L1"}}
    emp4 = {"Name": "Robert Neil", "Email": "robert@handson.cloud",
            "Full_date": '-'.join([str(datetime.datetime(2018, 2, 12, 4)), str(uuid.uuid4().hex[:6])]),
            "Department": "IT", "Section": {"PM": "PM-1", "Reporting Line": "L1"}}
    # employee_table.insert_item('Employees', emp1)
    # employee_table.insert_multiple_items('Employees', emp2, emp3, emp4)
    # employee_table.update_item('Employees', "IT", "2022-05-11 15:42:51.174243-64cbf3", 'luke@b.com', 'QA-2', 'L4')
    # employee_table.get_item('Employees', "IT", "2022-05-11 15:42:51.174243-64cbf3")
    # employee_table.delete_item('Employees', "IT", "2018-02-12 04:00:00-3518f9", "john@handson.cloud")
    # employee_table.query('Employees', 'IT')
    # employee_table.get_all_items('Employees')
    # employee_table.scan_filter('Employees', 'Name', 'Robert Neil')

