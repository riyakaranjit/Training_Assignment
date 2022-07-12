import snowflake.connector
import json
import base64
import json


def main():
    password = base64.b64decode("RjJEelhUVDlaMm5UZUNR").decode("utf-8")

    with open("cred.json", "r") as f:
        cred = json.load(f)

    conn = snowflake.connector.connect(
        user=cred["userid"],
        password=password,
        account=cred["account"],
        session_parameters={
            "QUERY_TAG": "EndOfMonthFinance",
        }
    )

    print("Successfully connected to snowflake!!!")
    conn.cursor().execute("use role sysadmin")

    # Creating a Database, Schema, and Warehouse
    # conn.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")
    # conn.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb_mg")
    # conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS testschema_mg")

    # Using the Database, Schema, and Warehouse
    conn.cursor().execute("USE WAREHOUSE tiny_warehouse_mg")
    conn.cursor().execute("USE DATABASE testdb_mg")
    conn.cursor().execute("USE SCHEMA testdb_mg.testschema_mg")

    # Creating Tables and Inserting Data

    # conn.cursor().execute(
    #     "CREATE OR REPLACE TABLE "
    #     "test_table(col1 integer, col2 string)")
    #
    # conn.cursor().execute(
    #     "INSERT INTO test_table(col1, col2) VALUES " +
    #     "    (123, 'indian Cricket'), " +
    #     "    (100, 'Kapil Dev')")

    # Putting Data
    # conn.cursor().execute("PUT file://C:\\temp\\data\\crick* @testdb_mg.testschema_mg.%test_table1")
    conn.cursor().execute(r"PUT file://C:\temp\data\crick1.csv @testdb_mg.testschema_mg.test_stage")

    conn.cursor().execute("""COPY INTO test_table1 from @testdb_mg.testschema_mg.%test_table/crick1.csv.gz
                          file_format = (type = csv field_delimiter=',')
                            pattern = '.*.csv.gz'
                            on_error= 'skip_file'""")

    # For S3
    #
    # Copying Data
    conn.cursor().execute("""
    COPY INTO test_table FROM s3://bucket-to-store-snowflake-data/data/
        CREDENTIALS = (
            aws_key_id='{aws_access_key_id}',
            aws_secret_key='{aws_secret_access_key}')
        FILE_FORMAT=(field_delimiter=',')
    """.format(
        aws_access_key_id=cred['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=cred['AWS_SECRET_ACCESS_KEY'])
    )

    # Querying Data
    cur = conn.cursor()

    try:
        cur.execute("SELECT col1, col2 FROM test_table1 ORDER BY col1")
        for (col1, col2) in cur:
            print(f'{col1}, {col2}')
    finally:
        cur.close()

    # Use fetchone or fetchmany if the result set is too large to fit into memory.

    # results = conn.cursor().execute("SELECT col1, col2 FROM test_table").fetchall()
    #
    #
    # for rec in results:
    #     print('%s, %s' % (rec[0], rec[1]))

    conn.close()


if __name__ == "__main__":
    main()
