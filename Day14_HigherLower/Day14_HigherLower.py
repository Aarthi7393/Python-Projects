from art import logo,vs
from game_data import data
import random

def pick_celebrity(data):
    celebrity = random.choice(data)
    return celebrity


def print_celebrity(celebrity):
    return f"{celebrity["name"]}, {celebrity["description"]} , from {celebrity_1['country']}. "

def compare_followers(guess, celebrity_1, celebrity_2):
    if celebrity_1["follower_count"] > celebrity_2["follower_count"]:
        #checks if the guess is A, if A then return True else False. It does a check in return statement and outputs based on it
        return guess=="A"
    else:
        return guess== "B"

celebrity_1 = pick_celebrity(data)
print(logo)
total_score = 0
game_continue = True
while game_continue:
    celebrity_2 = pick_celebrity(data)

    #if both celebrity are same, redo the pickup
    if celebrity_1 == celebrity_2:
        celebrity_1 = pick_celebrity(data)

    print(f"Compare A: {print_celebrity(celebrity_1)}")
    print(vs)
    print(f"Against B: {print_celebrity(celebrity_2)}")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    #Clear the screen
    print("\n" * 20)
    print(logo)


    if compare_followers(user_answer, celebrity_1, celebrity_2):
        total_score += 1
        print(f"You're right! Current score: {total_score}.")
        celebrity_1 = celebrity_2

    else:
        total_score = total_score
        print(f"Sorry, that's wrong. Final score: {total_score}")
        game_continue = False