from .presentation import Presentation


class Library:
    paths = set()
    presentations = []

    def __init__(self, library, client=None):
        for presentation_info in library:
            presentation = Presentation(presentation_info, client)
            self.presentations.append(presentation)
            self.paths.add(presentation.path)
