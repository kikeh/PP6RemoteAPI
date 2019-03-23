import asyncio
import json
import websockets

from .clock import Clock


class PP6RemoteAPIClient:

    def __init__(self, host, port, password, ws_settings=None):
        self.PROPRESENTER_URL = f'ws://{host}:{port}/remote'
        self._password = password
        self.ws_settings = ws_settings or {}

    def async_send(self, command):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.send(command))

    async def send(self, command):
        command = json.dumps(command)

        async with websockets.connect(
                self.PROPRESENTER_URL, **self.ws_settings) as websocket:
            await websocket.send(command)
            response = await websocket.recv()
            return json.loads(response)

    def authenticate(self):
        # TODO: Catch TimeoutError, ConnectionRefusedError
        command = {
            'action': 'authenticate',
            'protocol': '600',
            'password': self._password,
        }

        response = self.async_send(command)

        if response.get('authenticated') != 1:
            # TODO: Raise a proper exception
            raise Exception(response.get('error'))

        return response

    def stage_display_sets(self):
        command = {"action": "stageDisplaySets"}
        return self.async_send(command)

    def clocks(self):
        command = {"action": "clockRequest"}
        response = self.async_send(command)

        return [
            Clock(index, _clock)
            for index, _clock in enumerate(response.get('clockInfo'))
        ]
