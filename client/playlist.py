from .audio import Audio


class Playlist:

    def __init__(self, playlist, client=None):
        self.client = client
        self.index = playlist.get('playlistLocation')
        self.name = playlist.get('playlistName')
        self.type = playlist.get('playlistType')
        self.items = self.playlist_items(playlist.get('playlist'))

    def playlist_items(self, items):
        return [PlaylistItem(item, self.client) for item in items]

    def __repr__(self):
        return f'<Playlist: {self.name} ({len(self.items)})>'


class PlaylistItem:
    PRESENTATION = 'playlistItemTypePresentation'
    IMAGE_OR_VIDEO = 'playlistItemTypeVideo'
    AUDIO = 'playlistItemTypeAudio'

    def __init__(self, item, client=None):
        self.client = client
        self.name = item.get('playlistItemName')
        self._type = item.get('playlistItemType')
        self.artist = item.get('playlistItemName')
        self.location = item.get('playlistItemLocation')

    @property
    def path(self):
        return self.location.split(':')[0]

    @property
    def child_path(self):
        return self.location

    @property
    def linked_element(self):
        if self._type == self.PRESENTATION:
            return self.client.library.find_presentation_by_name(self.name)
        if self._type == self.AUDIO:
            return Audio(self, self.client)

    @property
    def type(self):
        if self._type == self.PRESENTATION:
            return 'Presentation'
        elif self._type == self.IMAGE_OR_VIDEO:
            return 'ImageOrVideo'
        elif self._type == self.AUDIO:
            return 'Audio'

    def __repr__(self):
        return f'<PlaylistItem: {self.name} ({self.type})>'
