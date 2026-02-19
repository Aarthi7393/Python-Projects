from art import logo
import random
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

print("Welcome to the Number Guessing Game!")

def check_answer(number, guess, attempts):
    if guess == number:
        print("You won! The number was ", number)
        attempts = 0
    else:
        if guess > number:
            print("Too high!")
        elif guess < number:

            print("Too low!")
        attempts -= 1
    return attempts

def attempts_detection():
    difficulty_state = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty_state == 'easy':
        attempts = EASY_ATTEMPTS
    else:
        attempts = HARD_ATTEMPTS
    return attempts

def game():
    print ("I am thinking of a number between 1 and 100")
    number = random.randint(1, 100)
    print(f"Psst, the correct answer is {number} ")
    attempts = attempts_detection()
    while attempts > 0:
        print("You have " + str(attempts) + " attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts= check_answer (number, guess, attempts)
        if attempts == 0:
            print(f"You lost! The correct answer was {number}")
        else:
            print("Guess again!")


game()