import os

print("Welcome to the secret auction program.")

bidding = True

bidder_dict = {}

while bidding:

    name = input("What is your name?: ")
    bid = int(input("What's your bid? $"))

    bidder_dict[name] = bid

    bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if bidders == "no":
        bidding = False
    
    os.system('cls')

bid_winner = ''
bid_win_amt = 0

# bid_win_amt = max(bidder_dict, key = bidder_dict.get)
for key in bidder_dict:
    if bidder_dict[key] > bid_win_amt:
        bid_winner = key
        bid_win_amt = bidder_dict[key]

print(f"The winner is {bid_winner} with a bid of ${bid_win_amt}.")