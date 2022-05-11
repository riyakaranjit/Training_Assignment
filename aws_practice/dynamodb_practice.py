import os
from pprint import pprint

import boto3
import uuid

from botocore.exceptions import ClientError


class DynamodbManager:
    def __init__(self):
        self.session = boto3.session.Session()
        self.dynamodb = boto3.resource('dynamodb')

    def create_table(self, table_name, partition_key_name, sort_key_name):
        """
        Adds a new table to your account.
        :param table_name: Table name must be unique in every region
        :param partition_key_name: Primary key's attribute name
        :param sort_key_name: Composite key's attribute name
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
        table = self.dynamodb.Table(table_name)
        response = table.put_item(
            Item=item
        )
        print('Item inserted successfully!!!')
        return response

    def insert_multiple_items(self, table_name, *items):
        table = self.dynamodb.Table(table_name)
        for item in items:
            with table.batch_writer() as batch:
                batch.put_item(Item=item)
        print('Items inserted successfully!!!')
        return batch

    def get_item(self, table_name, name, email):
        """
        Set of attributes for the item with the given primary and secondary key.
        :param table_name: Table name
        :param name: Partition key item
        :param email: Sort Key item
        """
        table = self.dynamodb.Table(table_name)
        try:
            response = table.get_item(
                Key={
                    'Name': name,
                    'Email': email
                }
            )
            print(response['Item'])
        except ClientError as e:
            print('Client Error Occurred: ', e.response['Error']['Message'])

    def get_all_items(self, table_name):
        """
        Read all items in a table.
        :param table_name: Table name
        """
        table = self.dynamodb.Table(table_name)

        response = table.scan()
        pprint(response['Items'])

    def update_item(self, table_name, name, email, dept_name, qa_name, reporting_line):
        """
        Edits an existing item's attributes, or adds a new item to the table if it does not already exist
        :param table_name: Table name
        :param name: Partition key item
        :param email: Sort Key item
        :param dept_name: Department Attribute to be updated
        :param qa_name: QA Attribute to be updated
        :param reporting_line: Reporting Line Attribute to be updated
        """
        table = self.dynamodb.Table(table_name)
        response = table.update_item(
            Key={
                'Name': name,
                'Email': email
            },
            ExpressionAttributeNames={
                '#section': 'Section',
                '#qa': 'QA',
                '#reporting_line': 'Reporting Line',
                '#dept': 'Department'
            },
            ExpressionAttributeValues={
                ':dept_name': dept_name,
                ':qa_value': qa_name,
                ':reporting_line_value': reporting_line
            },
            UpdateExpression="SET #dept = :dept_name, #section.#qa = :qa_value, "
                             "#section.#reporting_line = :reporting_line_value",
            ReturnValues='ALL_NEW'  # Returns all the attributes of the item after the UpdateItem operation
        )
        print('Item updated successfully!!!')
        return response

    def delete_item(self, table_name, name, email, dept_name):
        """
        Deletes a single item in a table by the primary key.
        :param table_name: Table name
        :param name: Primary key item
        :param email: Secondary key item
        :param dept_name: The item will be deleted if the dept_name matches

        """
        table = self.dynamodb.Table(table_name)
        try:
            response = table.delete_item(
                Key={
                    'Name': name,
                    "Email": email
                },
                ExpressionAttributeNames={
                    '#dept': 'Department'
                },
                ExpressionAttributeValues={
                    ':dept_name': dept_name,
                },
                ConditionExpression='#dept = :dept_name'
            )
            print("Item deleted successfully!!!")
            return response
        except ClientError as er:
            if er.response['Error']['Code'] == "ConditionalCheckFailedException":
                print(er.response['Error']['Message'])
            else:
                raise


if __name__ == '__main__':
    employee_table = DynamodbManager()
    # employee = employee_table.create_table('Employees', 'Name', 'Email')  # Create a employee table
    # print('Status: ', employee.table_status)
    emp1 = {"Name": "Lucas John", "Email": "john@handson.cloud", "Department": "IT",
            "Section": {"QA": "QA-1", "Reporting Line": "L1"}}
    emp2 = {"Name": "Louis Legend", "Email": "john@handson.cloud",
            "Department": "IT", "Section": {"QA": "QA-1", "Reporting Line": "L1"}}
    emp3 = {"Name": "Logo Joshua", "Email": "joshua@handson.cloud",
            "Department": "IT", "Section": {"Development": "SD-1", "Reporting Line": "L1"}}
    emp4 = {"Name": "Robert Neil", "Email": "robert@handson.cloud",
            "Department": "IT", "Section": {"PM": "PM-1", "Reporting Line": "L1"}}
    employee_table.insert_item('Employees', emp1)
    employee_table.insert_multiple_items('Employees', emp2, emp3, emp4)
    employee_table.get_item('Employees', "Lucas John", "john@handson.cloud")
    employee_table.update_item('Employees', "Lucas John", "john@handson.cloud", 'Science', 'QA-2', 'L4')
    employee_table.delete_item('Employees', "Lucas John", "john@handson.cloud", "Science")
    employee_table.get_all_items('Employees')
