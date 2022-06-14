import pandas as pd
import sqlite3
from sqlite3 import Error, OperationalError

import config


class SqliteConnectionHandler:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self._cursor = self.connection.cursor()

    def execute_non_returning_query(self, query, data=None):
        self._cursor.execute(query, data)
        self.commit()

    def execute_returning_one_query(self, query, data=None):
        self._cursor.execute(query, data)
        result = self._cursor.fetchone()
        return result

    def execute_returning_all_query(self, query, data=None):
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        return result

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        self.connection.close()


class SqliteConnection:
    def __init__(self, db_name):
        """
        Create a connection to the sqlite server.
        :param db_name: Name of the database you want to connect to.
        """
        try:
            self.conn_handler = SqliteConnectionHandler(db_name)

            print("Sqlite connection successfully")
        except Error as e:
            # exc_info = True prints out stack trace
            print("New connection Error: ", e)

    def sqlite_table_creation(self):
        """
        Create a Student and Gender  table in the sqlite database
        :return:
        """
        with open(config.CREATE_SQLITE_TABLES, 'r') as fptr:
            sql_file = fptr.read()

        # all SQL commands (split on ';')
        sql_commands = sql_file.split(';')

        try:
            for command in sql_commands:
                self.conn_handler.execute_non_returning_query(command, '')
            print('Student Table created successfully')
            print('Gender Table created successfully')

        except (Error, OperationalError) as e:
            print("Student Table create Error", e)

    @staticmethod
    def return_gender_id(gender: str) -> int:
        """
        Inpput gender and return the ihe gender id.
        :param gender: Specific Gender
        :return: gender id
        """
        gender_to_id_mapping = {'male': 1, "female": 2, "unknown": 3}

        try:
            return gender_to_id_mapping[gender.lower()]
        except IndexError:
            print("Invalid gender input exit.")
            exit(-1)

    @staticmethod
    def return_student_table(item: tuple):
        """
        Prints a table like structure for Student table
        :param item:
        """
        print('StudentId\t\t Name\t\t\t Age\t\t\t Address\t\t\t GenderId')
        print('----------------------------------------------------------------------------')
        print(f'{item[0]}\t\t\t\t {item[1]} \t\t\t\t{item[2]} \t\t\t{item[3]} \t\t\t\t{item[4]}')
        print('----------------------------------------------------------------------------')

    def create_records(self):
        """
        Insertion of record to the Student Table.
        """
        name = input('Enter Name: ')
        age = input('Enter Age: ')
        address = input('Enter Address: ')
        gender = input('Enter Gender: ')
        try:
            gender_id = self.return_gender_id(gender)
            student_insert_query = "Insert Into Student(Name, Age, Address, GenderId) Values(?,?,?,?)"
            data = [name.capitalize(), age, address.capitalize(), gender_id]

            self.conn_handler.execute_non_returning_query(student_insert_query, data)

            print('Student Data Inserted Successfully!')
        except Error as e:
            print('Table insertion error', e)
        finally:
            self.conn_handler.close()

    def read_records(self):
        """
        Read all the records from Student Table.
        """
        select_query = '''SELECT s.StudentId ,s.NAME ,s.AGE , s.ADDRESS ,g.Gender
                            FROM
                            Student s
                            JOIN Gender g ON
                            s.GenderId = g.GenderId
                            '''
        result = self.conn_handler.execute_returning_all_query(select_query)
        print('StudentId\t\t Name\t\t\t Age\t\t\t Address\t\t\t Gender')
        print('----------------------------------------------------------------------------')
        for row in result:
            print(f'{row[0]}\t\t\t\t {row[1]} \t\t\t\t{row[2]} \t\t\t{row[3]} \t\t\t\t{row[4]}')
            print('----------------------------------------------------------------------------')

    def update_record(self):
        """
        Update existing records in the Student Table.
        :return:
        """
        student_id = int(input("Enter the student id you want to update: "))
        try:
            select_update_query = "Select * from Student where StudentId = ?"
            # df = pd.read_sql_query(f"Select * from Student where StudentId = {student_id}", self.conn)
            # print(df)
            item = self.conn_handler.execute_returning_one_query(select_update_query, [student_id])

            print('Data Fetched for StudentId = ', student_id)
            self.return_student_table(item)
            print('Enter New Data To Update Student Record: ')
            name = input('Enter Name: ')
            age = input('Enter Age: ')
            address = input('Enter Address: ')
            gender = input('Enter Gender: ')
            gender_id = self.return_gender_id(gender)
            update_query = "Update Student Set Name = ?, Age =?, Address=?, GenderId=? Where StudentId =?"

            # Execute the update update_query
            # self.cur.execute(update_query, [name.capitalize(), age, address.capitalize(), gender_id, student_id])
            self.conn_handler.execute_non_returning_query(update_query, [name.capitalize(), age, address.capitalize(),
                                                                         gender_id, student_id])

            select_update_query = "Select * from Student where StudentId = ?"

            updated_item = self.conn_handler.execute_returning_one_query(select_update_query, [student_id])
            print('Student Data Updated for StudentId = ', student_id)
            self.return_student_table(updated_item)
            print('Student Table Updated Successfully')
        except Error as e:
            print('Table update error', e)
        finally:
            self.conn_handler.close()

    def delete_record(self):
        """
        Delete the existing table in the Student record.
        :return:
        """
        student_id = input('Enter Student Id you want to delete: ')

        try:
            select_delete_query = "Select * From Student Where StudentId = ?"

            item = self.conn_handler.execute_returning_one_query(select_delete_query, [student_id])
            print('Student Data Fetched for Id = ', student_id)
            # df = pd.read_sql_query(f"Select * from Student where StudentId = {student_id}", self.conn)
            # print(df)
            self.return_student_table(item)
            confirm = input('Are you sure to delete this record (Y/N)?')

            # Delete after confirmation
            if confirm.lower() == 'y':
                deleteQuery = "Delete From Student Where StudentId = ?"
                reset_student_id = "DELETE FROM `sqlite_sequence` WHERE `name` = ?"
                self.conn_handler.execute_non_returning_query(deleteQuery, [student_id])
                self.conn_handler.execute_non_returning_query(reset_student_id, ['Student'])
                print('Student record deleted successfully!')
            else:
                print('Wrong Entry!!!')
        except Error as e:
            print('Table delete error', e)
        finally:
            self.conn_handler.close()
