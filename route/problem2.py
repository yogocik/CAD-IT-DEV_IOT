from flask import Blueprint
from functions.problem2 import load_and_aggregate_data, load_data


problem2 = Blueprint('problem2', __name__)

@problem2.route("/")
def Welcome():
    return "This is initial page of sensor data aggregation"

@problem2.route('/load_data')
def load_raw_data():
    data = load_data()
    return data

@problem2.route("/sensor_agg")
def aggregate_sensor():
    data = load_and_aggregate_data(is_json=True,
        col_selection=['temperature', 'humidity', 'roomArea', 'timestamp'])
    return data