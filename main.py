import json
import pprint
from hue import Lights, Config


path = 'keys.json'
with open(path) as f:
    df = json.load(f)

address = df['address']
username = df['username']

lights = Lights(address, username, id=[1])
r = lights.set(on=False)
pprint.pprint(r)