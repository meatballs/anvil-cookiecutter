from ._anvil_designer import HomeTemplate
from anvil import *
from ... import navigation


@navigation.register(name="home", title="Home")
class Home(HomeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
