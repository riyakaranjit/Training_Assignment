import snowflake.connector
import base64

password = base64.b64decode("RjJEelhUVDlaMm5UZUNR").decode("utf-8")

# Gets the version
ctx = snowflake.connector.connect(
    user='RiyaKaranjit5',
    password=password,
    account='oe01039.ap-southeast-1',
    warehouse='SNOWFLAKE_TEST_WH',
    database="SF_TEST_DB",
    schema="SF_TEST_SCHEMA"
)
con = ctx.cursor()
try:
    con.execute("SELECT CURRENT_DATABASE(), CURRENT_SCHEMA(), current_warehouse()")
    one_row = con.fetchone()
    print(one_row)
    original = r"C:\Users\i35914\PycharmProjects\curriculum_training\training_assignments\snowflake\files\employees0" \
               r"*.csv "
    con.execute("PUT file:///C:\\Users\\i35914\\PycharmProjects\\curriculum_training\\training_assignments\\snowflake\\files\\employees0* @SF_TEST_DB.SF_TEST_SCHEMA.%emp_basic")
    con.execute("""COPY INTO emp_basic FROM @%emp_basic
                      file_format = (type = csv field_optionally_enclosed_by='"')
                        pattern = '.*employees0[1-5].csv.gz'
                        on_error= 'skip_file'""")

    con.execute("SELECT * from emp_basic")
    print(con.fetchall())
finally:
    con.close()
ctx.close()
