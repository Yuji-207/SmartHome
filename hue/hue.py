import json
import requests


class Hue():

    def __init__(self, path, id=None):

        with open(path) as f:
            df = json.load(f)

        self.address = df['address']  # IP address of the hue bridge
        self.username = df['username']  # username
        self.id = id  # The ID of a light
        self.url = f'http://{self.address}/api/{self.username}/lights'

    def get(self, query):  # fetch all information about the addressed resource
        pass

    def put(self, query):  # modify an addressed resource
        requests.put(f'{self.url}/{self.light}/state', json=query)

    def post(self, query):  # create a new resource inside the addressed resource
        pass

    def delete(self, query):  # deleted the addressed resource  # delete?
        pass