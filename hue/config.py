import requests


class Config():
    
    def __init__(self, address, username=None):
        self.username = username
        self.url = f'http://{address}/api'

    def create(self, device, key=False):
        query = {}
        query['devicetype'] = device
        if key:
            query['generateclientkey'] = True
        r = requests.post(url=self.url, json=query)
        r = r.json()[0]
        if r.get('success') is not None:
            return  r['success']['username']
        else:
            return r['error']