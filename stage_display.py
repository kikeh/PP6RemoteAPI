class StageDisplay:

    def __init__(self, index, name, is_current_display=False):
        self.index = index
        self.name = name
        self.is_current_display = is_current_display

    def __repr__(self):
        current = ' | current' if self.is_current_display else ''
        return f'<StageDisplay: {self.name}{current}>'
