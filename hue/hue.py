import json
import requests


class Hue():

    def __init__(self, path, id):

        with open(path) as f:
            df = json.load(f)

        self.address = df['address']  # IP address of the hue bridge
        self.username = df['username']  # username
        self.id = id  # The ID of a light
        self.url = f'https://{self.address}/api/{self.username}/'

    def get(self, lights=None, groups=None, config=None, schedules=None, scenes=None, sensors=None, rules=None):  # fetch all information about the addressed resource
        url = self.url + 'lights/{self.id}'
        query = None
        r = requests.get(url=url, json=query)
        r = r.json()
        return r

    def put(self, query):  # modify an addressed resource
        url = self.url + 'lights/{self.id}/state'
        r = requests.put(url=url, json=query)
        r = r.json()
        return r

    def post(self, query):  # create a new resource inside the addressed resource
        pass

    def delete(self, query):  # deleted the addressed resource  # delete?
        pass