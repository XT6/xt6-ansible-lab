#!/usr/bin/env python3

from influxdb import InfluxDBClient
import uuid
import random
import time
import math

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('Fruta')

measurement_name = 'trig'
number_of_points = 250000
data_end_time = int(time.time() * 1000) #milliseconds

function_tags = [ "sin",
"cos",
"tan" ]

freq_tags = [ "1d",
"1h",
"1m" ] 

id_tags = []
for i in range(100):
    id_tags.append(str(uuid.uuid4()))

data = []
data.append("{measurement},function={function},freq={freq},id={id} x={x} {timestamp}"
            .format(measurement=measurement_name,
                    function="sin",
                    freq="1h",
                    id=random.choice(id_tags),
                    x=0,
                    timestamp=data_end_time))

current_point_time = data_end_time
for i in range(number_of_points-1):
    # current_point_time = current_point_time - random.randint(1,100)
    current_point_time = current_point_time - i
    data.append("{measurement},function={function},freq={freq},id={id} x={x} {timestamp}"
                .format(measurement=measurement_name,
                        function="sin",
                        freq="1h",
                        id=random.choice(id_tags),
                        x=math.sin(2*math.pi*current_point_time/3600),
                        timestamp=data_end_time))

client_write_start_time = time.perf_counter()

client.write_points(data, database='Fruta', time_precision='ms', batch_size=10000, protocol='line')

client_write_end_time = time.perf_counter()

print("Client Library Write: {time}s".format(time=client_write_end_time - client_write_start_time))