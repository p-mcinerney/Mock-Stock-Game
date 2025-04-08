from MockStock import *
import time
# TODO - Add an input where the user can choose whether to play the game or look at high scores set
# TODO - Get an input where the user either types in "p" to play or "h" for highscores

    # TODO - If they ask to play, then run the program as normal and play the game
    # TODO - If they ask for highscores, load all the highscores from the score.txt file, and print the top 5 highest scores
while True:
    play = input("Press 'p' to play: ")
    
    if play.lower() == "p":
        username = input("Username: ")

        # initialize the objects
        player = Player(username)
        stock = Stock()

        # do a for loop for only 10 turns the user has, after 10 rounds the game ends
        for i in range(10):
            print("")
            # print simple information
            if i == 9:
                print("FINAL ROUND")
            else:
                print(f"Round {i + 1}")
            print(f"Value of {stock.name}: ${stock.current_value}")
            print(f"Bank: ${player.balance} | Amount of stock: {player.numstock}")
            
            while True:
                msg = input("Action: ")
                if msg.lower() == "sell":
                    if player.numstock > 0:
                        player.numstock, player.balance = player.sell(stock.current_value, player.numstock, player.balance)
                        break
                    else:
                        print("You have no stock to sell.")
                        continue
                elif msg.lower() == "buy":
                    player.numstock, player.balance = player.buy(stock.current_value, player.numstock, player.balance)
                    break
                elif msg.lower() == "skip":
                    break
                else:
                        print("That wasnt right.\nThe actions you may perform are 'buy', 'sell', or 'skip'.")
                # update the stock value after the round is over
            stock.update_value()

        print(f"\n\nFinal Score\n{player.username} | ${player.balance} | {stock.name}")

        time.sleep(10)

        with open("score.txt", "a") as file:
            file.write(f"{player.username}/{player.balance}\n")
        
        break
    """
    elif play.lower() == "h":
        try:
            with open("dist/score.txt", "r") as file:
                for line in file:
                    try:
                        name, score = line.split("/")
                    except ValueError:
                        continue
                    print(f"Username: {name} | Score: {score}", end="")
        except FileNotFoundError:
            try:
                with open("dist/score.txt", "w") as file:
                    file.write("Start\n")
            except FileNotFoundError:
                print("Error: No 'dist/' directory")
                time.sleep(10)
        break
    else:   
        print("Error: Use 'p' or 'h'")
    """
    