class Audio:

    def __init__(self, playlist_item, client=None):
        self.client = client
        self.name = playlist_item.name
        self.artist = playlist_item.artist
        self.path = playlist_item.path
        self.child_path = playlist_item.child_path

    def play(self):
        command = {
            'action': 'audioStartCue',
            'audioPath': self.path,
            'audioChildPath': self.child_path,
        }
        return self.client.async_send(command, expect_response=False)

    def play_pause(self):
        command = {'action': 'audioPlayPause'}
        return self.client.async_send(command, expect_response=False)

    def __repr__(self):
        return f'<Audio: {self.name} - {self.artist}>'
