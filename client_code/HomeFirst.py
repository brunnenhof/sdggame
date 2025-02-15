from ._anvil_designer import HomeFirstTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import navigation

class HomeFirst(HomeFirstTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_register_click(self, **event_args):
    user = anvil.users.signup_with_form(allow_cancel=True)
    navigation.go_home()

  def new_game_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    get_games_first(self)
    say_hello('Fidibus')
    get_games_meta(self)
    pass
  
def get_games_first(self, **event_args):
  print('in get_games_first')

#get_games_first(self)

