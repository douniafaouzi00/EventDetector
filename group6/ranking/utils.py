import json
import geohash
from datetime import datetime
import itertools

import dateutil

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def flatten_object(json_dict):
    flattened = {}
    for item in json_dict[:-1]:  # The last item contains properties and other details by other groups
        for k, v in item.items():
            flattened[k] = v
    return flattened

def parse_body(json_data, flatten=True):
    json_dict = json.loads(json_data)

    if flatten:
        flattened_data = [
            flatten_object(json_dict),
            json_dict[-1]
        ]
        return flattened_data

    return json_dict

def parse_file(name='group5_output.json', flatten=True):
    with open(name, 'r') as file:
        json_dict = json.load(file)

    if flatten:
        flattened_data = [
            flatten_object(json_dict),
            json_dict[-1]
        ]
        return flattened_data

    return json_dict

def get_timestamp(string, date_format = "%Y-%m-%dT%H:%M"):
    return datetime.strptime(string, date_format)

def interpolate(left_val, right_val, weight):
    return left_val * weight + right_val * (1-weight)

def validate_date(date):
    try:
        dateutil.parser.parse(date)
        return True
    except Exception as e:
        return False

    
def extract_polygon_from_geohash(geo_hash_str):
    bounding_box = geohash.bbox(geo_hash_str)
    min_lat = bounding_box["e"]
    max_lat = bounding_box["w"]
    min_lon = bounding_box["s"]
    max_lon = bounding_box["n"]

    # Create a polygon from the bounding box coordinates
    polygon_bb = [[[min_lat, min_lon], [min_lat, max_lon], [max_lat, max_lon], [max_lat, min_lon]]]

    return polygon_bb


