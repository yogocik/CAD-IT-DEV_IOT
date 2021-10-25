# Sensor Data Aggregation

import pandas as pd
from utils.processing import load_json
from datetime import datetime
from typing import Optional

def group_data(data: pd.DataFrame, group_key: str) -> object:
    grouped = data.groupby(group_key).agg(['min', 'max', 'median', 'mean'])
    return grouped    

def aggregate_data(data: pd.DataFrame, group_key: Optional[list]) -> object:
    data['day'] = data['timestamp'].map(
        lambda x: str(datetime.fromtimestamp(x/1000).date()))
    grouped = group_data(data, group_key)
    return grouped

def load_data(json_url: str = 'JSON/sensor_data.json') -> object:
    loaded_data = load_json(json_url, 'array')
    json_data = loaded_data.to_json(orient='records')
    return json_data    

def load_and_aggregate_data(group_key: list = ['roomArea', 'day'],
                            json_url: str = 'JSON/sensor_data.json',
                            is_json: bool = False,
                            col_selection: list = []) -> object:
    loaded_data = load_json(json_url, 'array')
    if len(col_selection):
        loaded_data = loaded_data[col_selection]
    data = aggregate_data(loaded_data, group_key)
    data.drop('timestamp', axis=1, inplace=True)
    if is_json:
        data = data.to_json(orient='index', indent=4)
    return data



