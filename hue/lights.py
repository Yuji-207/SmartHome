import requests


class Lights():
    """
    Light API.
    色の変換 -> colour ライブラリ
    """

    def __init__(self, address, username, id=None):
        address = None
        username = None
        self.id = id
        self.url = f'https://{address}/api/{username}/lights'

    def get(self):
        """
        Gets a list of all lights that have been discovered by the bridge.
        Gets the attributes and state of a given light.

        Returns:
            r (dict): A dict of all lights in the system.
        """
        if self.id is None:
            url = self.url  # Get all lights
        else:
            url = self.url + f'/{self.id}'  # Get light attributes and state
        r = requests.get(url=url)
        r = r.json()
        return r

    def new(self, search=False):
        """
        Gets a list of lights that were discovered the last time a search for new lights was performed.
        The list of new lights is always deleted when a new search is started.
        

        Starts searching for new lights.

        The bridge will open the network for 40s. The overall search might take longer since the configuration
        of (multiple) new devices can take longer. If many devices are found the command will have to be issued
        a second time after discovery time has elapsed. If the command is received again during search the search
        will continue for at least an additional 40s.
        
        When the search has finished, new lights will be available using the get new lights command. In addition,
        the new lights will now be available by calling get all lights or by calling get group attributes on group 0.
        Group 0 is a special group that cannot be deletedand will always contain all lights known by the bridge.
        lights known by the bridge.


        Args:
            search (bool): Starts searching for new lights.

        Returns:
            r (dict): 
        """
        if search is None:
            url = self.url + '/new'
            r = requests.get(url=url)  # Get new lights
            r = r.json()
            return r
        else:
            r = requests.post(url=self.url)  # Search for new lights
            r = r.json()
            return r

    def set(self, on=None, bri=None, hue=None, sat=None, xy=None, ct=None, alert=None, effect=None, transitiontime=None):
        if self.id is not None:
            if on is not None:
                self.query['on'] = on
                state = True
            if bri is not None:
                self.query['bri'] = bri
                state = True
            if hue is not None:
                self.query['hue'] = hue
                state = True
            if sat is not None:
                self.query['sat'] = sat
                state = True
            if xy is not None:
                self.query['xy'] = xy
                state = True
            if ct is not None:
                self.query['ct'] = ct
                state = True
            if alert is not None:
                self.query['alert'] = alert
                state = True
            if effect is not None:
                self.query['effect'] = effect
                state = True
            if transitiontime is not None:
                self.query['transitiontime'] = transitiontime
                state = True
            if state is None:
                url = self.url + f'{self.id}'
                r = requests.pur(url=url)  # Set light attributes (rename)
                r = r.json()
                return r
            else:
                url = self.url + f'{self.id}/state'
                r = requests.put(url=url, json=self.query)  # Set light state
                r = r.json()
                return r
        else:
            print('You NEED the ID!')

    def on(self):  # Turn on
        self.query['on'] =  True
        return self

    def off(self):  # Turn off
        self.query['on'] = False
        return self

    def bri(self, value=None, per=None):  # Set brightness
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

    def hue(self, ):  # Set hue
        pass

    def sat(self):  # Set saturation
        pass

    def xy(self):  # Set xy coordinates of CIE color space
        pass

    def ct(self):  # Set Mired color temperatures
        pass