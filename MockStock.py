import random
class Stock:
    def __init__(self):
        all_names = ["Tesla", "Amazon", "Google", "Facebook", "Netflix"]
        self.name = random.choice(all_names)
        self.initial_value = random.randint(5, 100)
        self.current_value = self.initial_value
        self.last = None

    def update_value(self):
            self.current_value = self.current_value + random.randint(-10, 10)
                
class Player:
    def __init__(self, name):
        self.username = name
        self.balance = 1000
        self.numstock = 0

    def sell(self, stock_price, player_numstock, player_balance):
        amount = int(input("How much would you like to sell?: "))
        while True:
            if player_numstock >= amount:
                player_balance = player_balance + (amount * stock_price)
                player_numstock = player_numstock - amount
                break
            else:
                print("You do not have enough stock to sell.")
        return player_numstock, player_balance

    def buy(self, stock_price, player_numstock, player_balance):
        amount = int(input("How much would you like to buy?: "))
        while True:
            if player_balance >= amount * stock_price:
                player_balance = player_balance - (amount * stock_price)
                player_numstock = player_numstock + amount
                break
            else:
                print("You do not have enough money.")
        return player_numstock, player_balance

    def view_market(self, stock_price):
        print(f"The current price is {stock_price}")
        return
