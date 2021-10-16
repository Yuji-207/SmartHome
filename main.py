import json
from hue import Lights, Config

ids = {  # IDs of lights
    'entrance': None,
    'myroom1': None,
    'myroom2': None,
}


path = 'keys.json'
with open(path) as f:
    df = json.load(f)

address = df['address']
config = Config(address)
r = config.create('developer')
print(r)