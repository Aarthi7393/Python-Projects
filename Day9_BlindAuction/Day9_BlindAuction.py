# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def highest_bidder(bidding_data):
    highest_bid = 0
    winner = ""
    for bid in bidding_data:
        if  bidding_data[bid] > highest_bid:
            highest_bid = bidding_data[bid]
            winner = bid
    print("\n" * 10)
    print(f"The winner is {winner} with bid ${highest_bid}")

bidding_data = {}
bidding_ongoing = True
while bidding_ongoing:
    user_name = input("Type your name:\n").lower()
    user_bid = int(input("Type your bid:\n"))
    bidding_data.update({user_name: user_bid})
    game_continue = input("Is there any other bids? Type 'yes' or 'no':\n").lower()

    if game_continue == 'no':
        bidding_ongoing = False
        highest_bidder(bidding_data)
    if game_continue == 'yes':
        print("\n" * 10)
