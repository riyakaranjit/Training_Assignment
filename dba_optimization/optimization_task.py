import random
from collections import defaultdict
from faker import Faker
from pprint import pprint
import pandas as pd
import pyodbc
from pyodbc import Error, OperationalError
from sqlalchemy import create_engine
import urllib

import config


def seeding_data(n_records: int, company_records: int):
    """
    Seeding the Employee and company table with n_records.
    :param n_records: Number of records to insert into Employees Table
    :param company_records: Number of records to insert into Companies Table
    :return: Dataframe of Employees and Companies table.
    """
    fake_employee_data = defaultdict(list)
    fake_company_data = defaultdict(list)
    fake = Faker()
    Faker.seed(42)
    for _ in range(company_records):
        fake_company_data['company_name'].append(fake.company())
    for _ in range(n_records):
        fake_employee_data["first_name"].append(fake.first_name())
        fake_employee_data["last_name"].append(fake.last_name())
        fake_employee_data["email"].append(fake.email())
        fake_employee_data["phone_number"].append(fake.phone_number())
        fake_employee_data["salary"].append(random.randint(10000, 99999))
        fake_employee_data["company_id"].append(random.randint(1, company_records))

    # fake_employee_data["company_id"] = random.sample(range(1, 100 + 1), n_records)
    # print(fake_employee_data)
    df_fake_employee_data = pd.DataFrame(fake_employee_data)
    # print(df_fake_employee_data)
    df_fake_company_data = pd.DataFrame(fake_company_data)
    print(df_fake_company_data)

    return df_fake_employee_data, df_fake_company_data


def main():
    df_emp_data, df_comp_data = seeding_data(n_records=100000, company_records=100)
    params = urllib.parse.quote_plus(
        "Driver={" + config.DATABASE_CONFIG["Driver"] + "};"
        "Server=" + config.DATABASE_CONFIG["Server"] + ";"
        "Database=" + config.DATABASE_DETAILS['database'] + ";"
        "UID=" + config.DATABASE_CONFIG["UID"] + ";"
        "PWD=" + config.DATABASE_CONFIG["Password"] + ";"
                    )
    try:
        engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
        df_comp_data.to_sql('companies', con=engine, schema=config.DATABASE_DETAILS['schema'], if_exists='append',
                            index=False)
        print('Companies table created!')

        df_emp_data.to_sql('Employees', con=engine, schema=config.DATABASE_DETAILS['schema'], index=False,
                           if_exists='append')
        print('Employees table created!')

    except (Error, OperationalError) as e:
        print("Main sql server error", e)


if __name__ == '__main__':
    main()
