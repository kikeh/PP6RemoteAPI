from .presentation import Presentation


class Library:

    def __init__(self, library, client=None):
        self.paths = set()
        self.presentations = []

        for presentation_info in library:
            presentation = Presentation(presentation_info, client)
            self.presentations.append(presentation)
            self.paths.add(presentation.path)

    def find_presentation_by_name(self, name):
        for presentation in self.presentations:
            if presentation.name == name:
                return presentation

    def __repr__(self):
        return f'<Library: {len(self.presentations)} presentations>'
