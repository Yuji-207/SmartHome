import requests

address = None  # IP address of the Hue Bridge  # GitHubに公開しないよう隠す
username = None  # username
light = {  # IDs of the lights  # . でアクセスしたい -> タプル？
    'myroom1': None,
    'myroom2': None,
    'genkan': None  # 玄関
}


class Hue():

    def __init__(self, str: address, str: username, int: id):
        self.address = address
        self.username = username
        self.id = id
        self.url = f'http://{self.address}/api/{self.username}/lights'

    def get(self, query):
        requests.put(f'{self.url}/{self.id}/state', json=query)

    def post(self, query):
        requests.put(f'{self.url}/{self.id}/state', json=query)


class Room():
    pass