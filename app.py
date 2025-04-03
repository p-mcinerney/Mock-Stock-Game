import random
import time
from MockStock import *

player = Player("Patrick")
print(Stock.initial_value)
print(player.username)
while True:
    playerinput = input("Type view market to view the market value")
    if playerinput.lower() == "view market":
        Player.view_market()
    else:
        print("that wasnt right );")

