import requests


class Config():
    
    def __init__(self, address, username=None):
        self.username = username
        self.url = f'http://{address}/api'

    def create(self, device, key=False):
        query = {}
        query['deviceype'] = device
        query['key'] = key
        r = requests.post(url=self.url)
        r = r.json()[0]
        if r.get('success') is not None:
            return  r['success']['username']
        else:
            return r['error']