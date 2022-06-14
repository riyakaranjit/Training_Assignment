from sqlite_crud import SqliteConnection
from sqlserver_crud import SqLServerConnection


def main():
    database_type = int(input("Enter the type of database Sqlite(1) or Sqlserver (2) you want to use: "))
    connection_type = None

    if database_type == 1:
        sqlite_conn = SqliteConnection('traineeshipDB.db')
        connection_type = sqlite_conn
        # sqlite_conn.sqlite_table_creation()
    elif database_type == 2:
        sqlserver_conn = SqLServerConnection('test_db')
        connection_type = sqlserver_conn
        sqlserver_conn.sql_server_table_creation()
    else:
        print('Wrong Choice!')
        exit()
    operation_type = input("Create(C)/Read(R)/Update(U)/Delete(D)?: ")

    if operation_type.lower() == 'c':
        connection_type.create_records()
    elif operation_type.lower() == 'r':
        connection_type.read_records()
    elif operation_type.lower() == 'u':
        connection_type.update_record()
    elif operation_type.lower() == 'd':
        connection_type.delete_record()

    else:
        print('Wrong Choice!!!')
        exit()


if __name__ == '__main__':
    main()
