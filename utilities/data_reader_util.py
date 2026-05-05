import pandas as pd
import json

def read_json_data(file_path: str):

    data = []
    try:
        file = open(file_path, "r")
        json_data = json.load(file)
        for record in json_data:
            data.append(tuple(record.values()))
    except Exception as e:
        print(f"error while reading the json file: {e}")
    return data

def read_csv_data(file_path: str):
    try:
        df = pd.read_csv(file_path)

        cols = ["email", "password", "validity"]
        return [tuple(row) for row in df[cols].values]
    except Exception as e:
        print(f"error reading while csv : {e}")
        return []

def read_excel_data(file_path: str, sheet_name=None):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        cols = ["email", "password", "validity"]
        return [tuple(row) for row in df[cols].values]

    except Exception as e:
        print(f"Error reading Excel: {e}")
        return []
