import re


class FrontMessage:
    VARIABLE = r'\$\{(.*)\}'

    def __init__(self, index, message, client=None):
        self.components = []
        self.variables = []

        self.index = index
        self.name = message.get('messageTitle')
        self.client = client

        self.parse_components(message.get('messageComponents'))

    def is_variable(self, component):
        return re.match(self.VARIABLE, component) is not None

    def is_complex(self, variable):
        return len(variable.split(':')) > 1

    def parse_components(self, components):
        for component in components:
            if self.is_variable(component):
                variable = re.match(self.VARIABLE, component).groups()[0]
                self.variables.append(variable)
                self.components.append(f'[{variable}]')
            else:
                self.components.append(component)

    def send(self, values):
        command = {
            "action": "messageSend",
            "messageIndex": self.index,
            "messageKeys": self.variables,
            "messageValues": values,
        }
        return self.client.async_send(command, expect_response=False)

    def hide(self):
        command = {
            "action": "messageHide",
            "messageIndex": self.index,
        }
        return self.client.async_send(command, expect_response=False)

    @property
    def template(self):
        return ' '.join(self.components)

    def __repr__(self):
        return f'<FrontMessage: {self.name}>'
