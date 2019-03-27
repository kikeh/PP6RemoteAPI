import os


class Presentation:
    DEFAULT_QUALITY = 400

    def __init__(self, abs_name, client=None):
        self.abs_name = abs_name
        self.path = os.path.dirname(abs_name)
        filename = os.path.basename(abs_name)
        self.name = '.'.join(filename.split('.')[:-1])
        self.extension = filename.split('.')[-1]
        self.client = client

    # Not sure what this request does.
    def request(self, quality=DEFAULT_QUALITY):
        command = {
            'action': 'presentationRequest',
            'presentationPath': self.abs_name,
            'presentationName': self.abs_name,
            'presentationSlideQuality': quality,
        }
        return self.client.async_send(command, expect_response=False)

    def to_slide(self, index):
        command = {
            'action': 'presentationTriggerIndex',
            'presentationPath': self.abs_name,
            'slideIndex': index,
        }
        return self.client.async_send(command, expect_response=False)

    def next_slide(self):
        command = {'action': 'presentationTriggerNext'}
        return self.client.async_send(command, expect_response=False)

    def previous_slide(self):
        command = {'action': 'presentationTriggerPrevious'}
        return self.client.async_send(command, expect_response=False)

    def current_slide(self):
        command = {'action': 'presentationSlideIndex'}
        return self.client.async_send(command, expect_response=False)

    def __repr__(self):
        return f'<Presentation: {self.name}>'
