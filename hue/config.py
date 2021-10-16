import requests


class Config():
    
    def __init__(self, address, username=None):
        self.username = username
        self.url = f'https://{address}/api'

    def create(self, device, key=False):
        query = {}
        query['deviceype'] = device
        query['key'] = key
        print(query)
        print('='*79)
        r = requests.get(url=self.url)
        print(r)
        print('='*79)
        r = r.json()
        print(type(r))
        print(r)
        r = r[0]
        if r.get('success') is not None:
            return  r['success']['username']
        else:
            return r['error']