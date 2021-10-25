from datetime import datetime
import random
import pandas as pd
import uuid

sensor_data = []

def write_file(dest_url: str, filename: str) -> object:
    print('Generate sensor data.')
    room_area = ['room_A', 'room_B', 'room_C', 'room_D', 'room_E']
    destination = dest_url + filename + '.json'
    for room in room_area:
        data = {
        'temperature' : random.uniform(20, 100),
        'humidity' : random.uniform(15, 80),
        'roomArea' : room,
        'id' : str(uuid.uuid4()),
        'timestamp' : datetime.timestamp(datetime.now())}
        sensor_data.append(data)
    data = pd.DataFrame.from_records(sensor_data)
    data.to_json(destination, orient='records', indent=4)
    print('Data has been written to destination log.')
