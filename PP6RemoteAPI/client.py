import asyncio
import json
import websockets

from .clock import Clock
from .library import Library
from .message import FrontMessage
from .playlist import Playlist
from .presentation import Presentation
from .stage_display import StageDisplay
from .exceptions import AuthenticationError


class PP6RemoteAPIClient:
    AUTHENTICATION_PROTOCOL = '600'
    DEFAULT_TIMEOUT = 15.0

    def __init__(self, host, port, password, ws_settings=None):
        self.PROPRESENTER_URL = f'ws://{host}:{port}/remote'
        self._password = password
        self.ws_settings = ws_settings or {}

    def authenticate(self):
        '''
        Throws TimeoutError when wrong IP is set
        Throws ConnectionRefusedError when wrong port is set
        '''
        command = {
            'action': 'authenticate',
            'protocol': self.AUTHENTICATION_PROTOCOL,
            'password': self._password,
        }

        response = self.async_send(command)

        if response.get('authenticated') != 1:
            raise AuthenticationError(response.get('error'))

        return response

    def async_send(self, command, expect_response=True):
        return asyncio.run(
            asyncio.wait_for(
                self._send(command, expect_response),
                timeout=self.DEFAULT_TIMEOUT,
            )
        )

    async def _send(self, command, expect_response=True):
        command = json.dumps(command)

        async with websockets.connect(self.PROPRESENTER_URL,
                                      **self.ws_settings) as websocket:
            await websocket.send(command)
            if expect_response:
                response = await websocket.recv()
                return json.loads(response)

    def clear_all(self):
        command = {'action': 'clearAll'}
        return self.async_send(command, expect_response=False)

    def clear_background(self):
        command = {'action': 'clearVideo'}
        return self.async_send(command, expect_response=False)

    def clear_audio(self):
        command = {'action': 'clearAudio'}
        return self.async_send(command, expect_response=False)

    def clear_text(self):
        command = {'action': 'clearText'}
        return self.async_send(command, expect_response=False)

    def clear_props(self):
        command = {'action': 'clearProps'}
        return self.async_send(command, expect_response=False)

    def clear_to_logo(self):
        command = {'action': 'clearToLogo'}
        return self.async_send(command, expect_response=False)
        return self.async_send(command)

    def stage_display_sets(self):
        command = {'action': 'stageDisplaySets'}
        return self.async_send(command)

    def stage_display_set_display(self, name):
        names = self.stage_display_sets_names()
        index = names.index(name)
        command = {
            'action': 'stageDisplaySetIndex',
            'stageDisplayIndex': index,
        }
        return self.async_send(command, expect_response=False)

    def telestrator_settings(self):
        command = {'action': 'telestratorSettings'}
        return self.async_send(command)

    def get_playlists(self):
        command = {'action': 'playlistRequestAll'}
        response = self.async_send(command)

        return [
            Playlist(playlist, self)
            for playlist in response.get('playlistAll')
        ]

    def get_audio_playlists(self):
        command = {'action': 'audioRequest'}
        response = self.async_send(command)

        return [
            Playlist(playlist, self)
            for playlist in response.get('audioPlaylist')
        ]

    def get_front_messages(self):
        command = {'action': 'messageRequest'}
        response = self.async_send(command)

        return [
            FrontMessage(index, message, self)
            for index, message in enumerate(response.get('messages'))
        ]

    def get_library(self):
        command = {'action': 'libraryRequest'}
        response = self.async_send(command)

        return Library(response.get('library'), self)

    def get_stage_display_sets(self):
        response = self.stage_display_sets()

        stage_displays = []
        for index, name in enumerate(response.get('stageDisplaySets', [])):
            stage_displays.append(
                StageDisplay(
                    index,
                    name,
                    index == response.get('stageDisplayIndex'),
                    self
                )
            )

        return stage_displays

    def get_clocks(self):
        command = {'action': 'clockRequest'}
        response = self.async_send(command)

        return [
            Clock(index, _clock, self)
            for index, _clock in enumerate(response.get('clockInfo'))
        ]

    def get_current_presentation(self, quality=Presentation.DEFAULT_QUALITY):
        command = {
            'action': 'presentationCurrent',
            'presentationSlideQuality': quality,
        }
        return self.async_send(command)

    def get_current_audio(self):
        command = {'action': 'audioCurrentSong'}
        return self.async_send(command)

    def _stage_display_sets_names(self):
        response = self.stage_display_sets()
        return response.get('stageDisplaySets', [])

    @property
    def library(self):
        return self.get_library()

    @property
    def current_presentation(self):
        return self.get_current_presentation()

    @property
    def current_audio(self):
        return self.get_current_audio()

    @property
    def playlists(self):
        return self.get_playlists()

    @property
    def audio_playlists(self):
        return self.get_audio_playlists()

    @property
    def front_messages(self):
        return self.get_front_messages()

    @property
    def clocks(self):
        return self.get_clocks()

    @property
    def current_stage_display(self):
        for stage_display in self.stage_displays:
            if stage_display.is_current_display:
                return stage_display

    @property
    def stage_displays(self):
        return self.get_stage_display_sets()
