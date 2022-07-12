import base64
import os

password = base64.b64decode("NzdtbjQ4dXNAcms=").decode("utf-8")
# SQL Server Database Connection Properties
DATABASE_CONFIG = {
    'Driver': 'SQL Server Native Client 11.0',
    'Server': '10.104.29.50',
    'UID': 'riya',
    'Password': password,
}
DATABASE_DETAILS = {
    'database': 'test_db',
    'schema': 'riya'
}
