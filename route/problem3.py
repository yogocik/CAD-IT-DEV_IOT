from flask import Blueprint
from functions.problem3a import write_file
from functions.problem3b import read_and_calculate_data
import multiprocessing
import time

def background_stream():
    while True:
        write_file('.//JSON//', 'stream_sensor')
        time.sleep(5)

def background_calculation(ret_value):
    while True:
        data = read_and_calculate_data('.//JSON//', 'stream_sensor')
        ret_value.put(data)
        time.sleep(10)

problem3 = Blueprint('problem3', __name__)
ret_value = multiprocessing.Queue()
t1 = multiprocessing.Process(target = background_stream)
t2 = multiprocessing.Process(target = background_calculation,  args=(ret_value, ))

@problem3.route("/")
def Welcome():
    return "This is initial page of sensor data streaming"

@problem3.route('/stream_data/start')
def stream_data():
    t1.start()
    return 'The logging process is running'

@problem3.route('/stream_data/stop')
def stop_stream():
    t1.terminate()
    return 'The logging process has been stopped permanently'

@problem3.route('/calculate_data/start')
def start_calculate_data():
    t2.start()
    return 'The calculation process is running'

@problem3.route('/show_calculation')
def show_calculation():
    return ret_value.get()

@problem3.route('/calculate_data/stop')
def stop_calculate_data():
    t2.terminate()
    return 'The calculation process has been stopped permanently'