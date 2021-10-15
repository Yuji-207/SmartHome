import json
import requests


class Hue():

    def __init__(self, path, id):

        with open(path) as f:
            df = json.load(f)

        self.address = df['address']  # IP address of the hue bridge
        self.username = df['username']  # username
        self.id = id  # The ID of a light
        self.url = f'https://{self.address}/api/{self.username}'
        self.query = None

    def get(self):  # fetch all information about the addressed resource
        r = requests.get(url=self.url, json=self.query)
        r = r.json()
        return r

    def put(self):  # modify an addressed resource  # 1 put/min
        r = requests.put(url=self.url, json=self.query)
        r = r.json()
        return r

    def post(self):  # create a new resource inside the addressed resource
        pass

    def delete(self):  # deleted the addressed resource  # delete?
        pass