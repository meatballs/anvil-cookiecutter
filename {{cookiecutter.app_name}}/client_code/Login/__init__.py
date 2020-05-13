import anvil.users
from anvil import open_form

from ._anvil_designer import LoginTemplate


class Login(LoginTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def form_show(self, **event_args):
        anvil.users.login_with_form()
        open_form("Main")
