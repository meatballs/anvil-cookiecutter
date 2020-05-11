from ._anvil_designer import MainTemplate
from anvil import *
from .. import navigation

menu = [
  {"text": "Home", "target": "home", "icon": "fa:home"},
]

class Main(MainTemplate):
  
  def __init__(self, **properties):
    navigation.build_menu(self.menu_column_panel, menu)
    self.init_components(**properties)
