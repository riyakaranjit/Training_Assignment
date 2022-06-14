import pyodbc
from pyodbc import Error, OperationalError

from sqlite_crud import SqliteConnection, SqliteConnectionHandler
import config


class SqlServerConnectionHandler(SqliteConnectionHandler):
    def __init__(self, db_name, autocommit=True):
        self.db_name = db_name
        self.autocommit = autocommit
        connection_string = ("Driver={" + config.DATABASE_CONFIG["Driver"] + "};"
                             "Server=" + config.DATABASE_CONFIG["Server"] + ";"
                             "Database=" + db_name + ";"
                             "UID=" + config.DATABASE_CONFIG["UID"] + ";"
                             "PWD=" + config.DATABASE_CONFIG["Password"] + ";")
        self.connection = pyodbc.connect(connection_string)
        self._cursor = self.connection.cursor()
        self.connection.autocommit = self.autocommit


class SqLServerConnection(SqliteConnection):
    def __init__(self, db_name):
        """
        Create a connection to the SQL Server Database.
        :param db_name: Name of the database you want to connect to.
        """
        try:
            self.conn_handler = SqlServerConnectionHandler(db_name)

            print('SQL server connected')
        except Error as e:
            print("New SQL server connection Error", e)

    def sql_server_table_creation(self):
        """
        Create a Student and Gender  table in the sql server database
        :return:
        """
        with open(config.CREATE_SQLSERVER_TABLES, 'r') as fptr:
            sql_file = fptr.read()

        # all SQL commands (split on ';')
        sql_commands = sql_file.split(';')
        try:
            for command in sql_commands:
                self.conn_handler.execute_non_returning_query(command, 'Student')
            print('Gender Table created successfully')
            print('Student Table created successfully')

        except (Error, OperationalError) as e:
            print("New connection or table creation Error", e)

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
            self.return_student_table(item)
            confirm = input('Are you sure to delete this record (Y/N)?')

            # Delete after confirmation
            if confirm.lower() == 'y':
                deleteQuery = "Delete From Student Where StudentId = ?"
                reset_student_id = '''CREATE TRIGGER sampleDeleteTrigger
                                        ON Student
                                        FOR DELETE
                                    AS
                                        DECLARE @maxID int;

                                        SELECT @maxID = MAX(StudentId)
                                        FROM ?;

                                        DBCC CHECKIDENT (Student, RESEED, @maxID)'''
                self.conn_handler.execute_non_returning_query(deleteQuery, [student_id])
                self.conn_handler.execute_non_returning_query(reset_student_id, ['Student'])
                print('Student record deleted successfully!')
            else:
                print('Wrong Entry!!!')
        except Error as e:
            print('Table delete error', e)
        finally:
            self.conn_handler.close()
