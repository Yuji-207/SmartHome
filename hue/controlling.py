class Controlling():

    def __init__(self):
        self.address = None
        self.username = None
        self.id = None
        self.url = f'https://{self.address}/api/{self.username}/lights/{self.id}/state'
    
    def on(self):  # Turn on
        self.query['on'] =  True
        return self

    def off(self):  # Turn off
        self.query['on'] = False
        return self

    def bri(self, bri=None, per=None):  # Change brightness
        """
        Note minimum brightness is not off, and the light will actually 
        return 1 when set to 0 and return 254 when set to 255.
        """
        if bri is not None and per is not None:
            print('Both args is not None!')
        elif bri is not None:
            self.query['bri'] = bri
        elif per is not None:
            per.query['bri'] = 255 * per * 0.01
        else:
            print('Both args is None!')


