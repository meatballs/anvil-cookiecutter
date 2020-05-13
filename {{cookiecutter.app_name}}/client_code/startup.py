from anvil import open_form

from . import content_forms
{% if cookiecutter.with_authorisation == "yes" %}
import anvil.users

if anvil.users.get_user():
    open_form("Main")
else:
    open_form("Login")
{% else %}
open_form("Main")
{% endif %}
