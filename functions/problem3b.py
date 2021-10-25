import pandas as pd
from functions.problem2 import group_data

def read_and_calculate_data(dest_url: str, filename: str,
                group_key: str = 'roomArea') -> object:
    print('Reading sensor data.')
    destination = dest_url + filename + '.json'
    data = pd.read_json(destination)
    data = group_data(data, group_key)
    print('Data has been calculated.')
    json_data = data.to_json(orient='index', indent=4)
    return json_data
