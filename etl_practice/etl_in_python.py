from datetime import datetime
from glob import glob
import pandas as pd
import numpy as np


def log(message):
    timestamp_format = '%H:%M:%S-%h-%d-%Y'
    # Hour-Minute-Second-MonthName-Day-Year
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("dealership_logfile.txt", "a") as f:
        f.write(timestamp + ',' + message + 'n')


def extract_from_csv(csv_file):
    df_csv_file = pd.read_csv(csv_file)
    return df_csv_file


def extract():
    extracted_data = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])

    for csv_file in glob("dealership_data/*.csv"):
        print('extract_from_csv \n', extract_from_csv(csv_file))
        extracted_data = pd.concat([extracted_data, extract_from_csv(csv_file)], ignore_index=True)
        print('extracted_data', extracted_data)
    return extracted_data


def transform(data):
    a = data.price
    print("data price: ", np.around(a.astype(np.double), 3))
    data['price'] = np.around(a.astype(np.double), 3)
    return data


def load(target_file, data_to_load):
    data_to_load.to_csv(target_file)


def main():
    target_file = "dealership_transformed_data.csv"  # transformed data is stored

    log("ETL process started. \n")
    log("Extract phase started. \n")
    extracted_data = extract()
    log("Extract phase ended. \n")
    log("Transform phase started. \n")
    transformed_data = transform(extracted_data)
    log("Transform phase ended. \n")
    log("Load phase started. \n")
    load(target_file, transformed_data)
    log("Load phase ended. \n")
    log("ETL process ended. \n")


if __name__ == "__main__":
    main()
