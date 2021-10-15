class Controlling():  # Add /state to url

    def __init__(self):
        self.address = None
        self.username = None
        self.id = None
        self.url = f'https://{self.address}/api/{self.username}/lights/{self.id}/state'
    
    def on(self):  # light on
        self.query['on'] =  True
        return self
