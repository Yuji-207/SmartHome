import json
import requests

address = None  # IP address of the Hue Bridge  # GitHubに公開しないよう隠す
username = None  # username
light = {  # IDs of the lights  # . でアクセスしたい -> タプル？
    'myroom1': None,
    'myroom2': None,
    'genkan': None  # 玄関
}




class Hue():

    def __init__(self, address, username=None, id=None):
        self.address = address
        if username is None:
            print('Push the button of your hue bridge!')
            url = f'https://{self.address}/api/newdeveloper'
            r = requests.post(url=url)
            self.username = r.json()[0]['success']['username']  # あってる？
        else:
            self.username = username
        self.id = id
        self.url = f'http://{self.address}/api/{self.username}/lights'

    def get(self, query):  # fetch all information about the addressed resource
        pass

    def put(self, query):  # modify an addressed resource
        requests.put(f'{self.url}/{self.light}/state', json=query)

    def post(self, query):  # create a new resource inside the addressed resource
        pass

    def delete(self, query):  # deleted the addressed resource  # delete?
        pass


class Room():  # 必要ない？ a group of lights?
    pass