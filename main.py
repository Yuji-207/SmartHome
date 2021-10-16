import json
from hue import Lights, Config


path = 'keys.json'
with open(path) as f:
    df = json.load(f)

address = df['address']
config = Config(address)
r = config.create('developer')
print(r)