import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

@anvil.server.callable
def say_hello(name):
  print("Hello, " + name + "!")
  return 42

@anvil.server.callable
def get_games_meta():
  print ('In games server def')
  games = tables.app_tables.games.get()
#  games = anvil.users.get_user(allow_remembered=True)
  if not games:
    print ('No games')
    return None
  print (games)
  #if not user['height'] or not user['gender']:
  #  raise Exception("You must set your gender and height.")
  
  #ave = app_tables.averages.get(Gender=user['gender'], Height=user['height'])
  #return ave

