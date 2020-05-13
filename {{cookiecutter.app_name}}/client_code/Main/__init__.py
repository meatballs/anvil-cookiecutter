from ._anvil_designer import MainTemplate
import anvil
from .. import navigation

menu = [
    {"text": "Home", "target": "home", "icon": "fa:home"},
]


class Main(MainTemplate):
    def __init__(self, **properties):
        navigation.build_menu(self.menu_column_panel, menu)
        self.init_components(**properties)

    {% if cookiecutter.with_authorisation == "yes" %}
    def logout_link_click(self, **event_args):
        anvil.users.logout()
        anvil.open_form("Login")
    {% endif %}
