from ._anvil_designer import MainTemplate


class Main(MainTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
