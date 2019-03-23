import asyncio
import json
import websockets

from .clock import Clock
from .stage_display import StageDisplay


class PP6RemoteAPIClient:

    def __init__(self, host, port, password, ws_settings=None):
        self.PROPRESENTER_URL = f'ws://{host}:{port}/remote'
        self._password = password
        self.ws_settings = ws_settings or {}

    def async_send(self, command, expect_response=True):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.send(command, expect_response))

    async def send(self, command, expect_response=True):
        command = json.dumps(command)

        async with websockets.connect(
                self.PROPRESENTER_URL, **self.ws_settings) as websocket:
            await websocket.send(command)
            if expect_response:
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
        command = {'action': 'stageDisplaySets'}
        response = self.async_send(command)

        stage_displays = []
        for index, name in enumerate(response.get('stageDisplaySets', [])):
            stage_displays.append(
                StageDisplay(
                    index,
                    name,
                    index == response.get('stageDisplayIndex')
                )
            )

        return stage_displays

    def stage_display_sets_names(self):
        stage_display_sets_response = self.stage_display_sets()
        return stage_display_sets_response.get('stageDisplaySets', [])

    def change_stage_display_to(self, name):
        names = self.stage_display_sets_names()
        index = names.index(name)
        command = {
            'action': 'stageDisplaySetIndex',
            'stageDisplayIndex': index,
        }
        return self.async_send(command)

    def stage_display_send_message(self, message):
        command = {
            'action': 'stageDisplaySendMessage',
            'stageDisplayMessage': message,
        }
        return self.async_send(command, expect_response=False)

    def get_clocks(self):
        command = {'action': 'clockRequest'}
        response = self.async_send(command)

        return [
            Clock(index, _clock)
            for index, _clock in enumerate(response.get('clockInfo'))
        ]

    def clock_update(self, clock_settings):
        command = {'action': 'clockUpdate'}
        command.update(clock_settings)
        return self.async_send(command, expect_response=False)

    def clock_update_time(self, clock, time):
        settings = clock.export_settings()
        settings['clockTime'] = time
        return self.clock_update(settings)

    def clock_start(self, clock):
        command = {
            'action': 'clockStart',
            'clockIndex': clock.index,
        }
        return self.async_send(command, expect_response=False)

    def clock_stop(self, clock):
        command = {
            'action': 'clockStop',
            'clockIndex': clock.index,
        }
        return self.async_send(command, expect_response=False)

    def clock_reset(self, clock):
        command = {
            'action': 'clockReset',
            'clockIndex': clock.index,
        }
        return self.async_send(command, expect_response=False)

    @property
    def clocks(self):
        return self.get_clocks()

    @property
    def stage_displays(self):
        return self.stage_display_sets()
