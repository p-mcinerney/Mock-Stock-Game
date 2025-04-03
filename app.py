import random
import time
from MockStock import *

username = input("Username: ")

# initialize the objects
player = Player(username)
stock = Stock()

# do a for loop for only 10 turns the user has, after 10 rounds the game ends
for i in range(10):
    # print simple information
    print(f"Round {i + 1}")
    print(f"Value of {stock.name}: {stock.current_value}")
    print(f"Bank: {player.balance} | Amount of stock: {player.numstock}")
    while True:
        msg = input("Action: ")
        # consider removing this because we can just put it above for the user to see
        """
        if msg.lower() == "view market":
            player.view_market()  
        """
        if msg.lower() == "sell":
            player.sell(stock.current_value)
            break
        elif msg.lower() == "buy":
            player.buy(stock.current_value)
            break
        else:
            print("That wasnt right")
    # update the stock value after the round is over
    stock.update_value()

