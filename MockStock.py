import random
class Stock:
    def __init__(self):
        last = ["up", "down", "same"]
        all_names = ["Tesla", "Amazon", "Google", "Facebook", "Netflix", "Red Hat", "Hooli", "OpenAI"]
        self.name = random.choice(all_names)
        self.initial_value = random.randint(5, 100)
        self.current_value = self.initial_value
        self.last = "same"

    def update_value(self):
        while True:
            if self.last == "up":
                new_val = random.randint(-5, 10)
            elif self.last == "down":
                new_val = random.randint(-10, 5)
            elif self.last == "same":
                new_val = random.randint(-5, 5)
            if new_val + self.current_value > 1:
                self.current_value = self.current_value + new_val
                break
        # this is where we update self.last
        if new_val > 0:
            self.last = "up"
        elif new_val < 0:
            self.last = "down" 
        elif new_val == 0:
            self.last = "same"
        return
        

                
class Player:
    def __init__(self, name):
        self.username = name
        self.balance = 1000
        self.numstock = 0

    def sell(self, stock_price, player_numstock, player_balance):
        while True:
            amount = input("How much would you like to sell?: ")
            try:
                amount = int(amount)
                if amount < 1:
                    print("You must buy 1 or more stocks.")
                    continue
                if player_numstock >= amount:
                    player_balance = player_balance + (amount * stock_price)
                    player_numstock = player_numstock - amount
                    break
                else:
                    print("You do not have enough stock to sell.")
                    continue
            except ValueError:
                print("That is not a number try again")
        return player_numstock, player_balance

    def buy(self, stock_price, player_numstock, player_balance):
        while True:
            amount = input("How much would you like to buy?: ")
            try:
                amount = int(amount)
                if amount < 1:
                    print("You must buy 1 or more stocks.")
                    continue
                if player_balance >= amount * stock_price:
                    player_balance = player_balance - (amount * stock_price)
                    player_numstock = player_numstock + amount
                    break
                else:
                    print("You do not have enough money.")
                    continue
            except ValueError:
                print("That is not a number try again")
        return player_numstock, player_balance
