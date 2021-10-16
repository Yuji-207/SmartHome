import json
from hue import Lights

ids = {  # IDs of lights
    'entrance': None,
    'myroom1': None,
    'myroom2': None,
}

path = 'keys.json'
with open(path) as f:
    df = json.load(f)

address = df['address']
username = df['username']
lights = Lights(address, username)
print(lights)