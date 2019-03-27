class StageDisplay:

    def __init__(self, index, name, is_current_display=False, client=None):
        self.index = index
        self.name = name
        self.is_current_display = is_current_display
        self.client = client

    def send_message(self, message):
        if self.client:
            command = {
                'action': 'stageDisplaySendMessage',
                'stageDisplayMessage': message,
            }
            return self.client.async_send(command, expect_response=False)

    def __repr__(self):
        current = ' | current' if self.is_current_display else ''
        return f'<StageDisplay: {self.name}{current}>'
