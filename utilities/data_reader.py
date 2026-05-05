import json
import pandas as pd

def read_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

def read_excel_file(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')