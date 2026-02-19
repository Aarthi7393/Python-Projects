# Rules of the game
# Reach near 21 wins
# Over 21 loses
# A can be considered as 11 or 1
import random
from art import logo
def card_pick():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate(cards):
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Draw!")
    elif user_score == 21:
        print("You won! Blackjack")
    elif computer_score == 21:
        print("You lose ! Blackjack by computer")
    elif user_score > 21:
        print("You lose")
    elif computer_score < user_score <= 21:
        print("You win")
    elif user_score <= 20 and computer_score > 21:
        print("You win")
    else:
        print("You lose")
def game_play():
    print(logo)
    #Initialize cards
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    #Append cards
    for i in range(2):
        user_cards.append(card_pick())
        computer_cards.append(card_pick())
    game_over = False
    while not game_over:
        user_score= calculate(user_cards)
        computer_score = calculate(computer_cards)
        print(f"Your cards: {user_cards}")
        print(f"Computer cards: {computer_cards}")
        if user_score == 21 or computer_score == 21 or user_score > 21:
             game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_choice == 'y':
                user_cards.append(card_pick())
            else:
                game_over = True

    while computer_score != 21 and computer_score < 17:
        computer_cards.append(card_pick())
        computer_score = calculate(computer_cards)

    print(f"Your cards: {user_cards} , your score: {user_score}")
    print(f"Computer cards: {computer_cards} , computer score: {computer_score}")
    compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    game_play()
