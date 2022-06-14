import base64
import os

password = base64.b64decode("NzdtbjQ4dXNAcms=").decode("utf-8")
# SQL Server Database Connection Properties
DATABASE_CONFIG = {
    'Driver': 'SQL Server Native Client 11.0',
    'Server': '10.104.29.50',
    'UID': 'riya',
    'Password': password
}

CREATE_SQLITE_TABLES = os.path.abspath("C:/Users/i35914/PycharmProjects/curriculum_training/training_assignments"
                                       "/sql_in_python/sqlite_scripts.txt")
CREATE_SQLSERVER_TABLES = os.path.abspath("C:/Users/i35914/PycharmProjects/curriculum_training/training_assignments"
                                          "/sql_in_python/sqlserver_scripts.txt")
