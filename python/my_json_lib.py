import json
import os.path
import time
from datetime import date

def get_file_date(filename):
    mod_time = os.path.getmtime(filename)
    mod_time_str = time.strftime("%Y-%m-%d", time.localtime(mod_time))

    file_date = [int(x) for x in mod_time_str.split('-')]
    file_date = date(file_date[0],file_date[1],file_date[2])

    return file_date

def data_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def json_to_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def update_file(filename, new_data):
    if not os.path.exists(filename):
        data_to_json(new_data, filename)

    today = date.today()
    file_date = get_file_date(filename)

    if today != file_date:
        data_to_json(new_data, filename)