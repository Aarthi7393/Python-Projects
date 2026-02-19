import random
from hangman_art import stages
from hangman_words import word_list

selected_word = random.choice(word_list)
print(selected_word)

for letter in selected_word:
    print("_", end= "")
guessed_letter = []
guess_limit = 7
while guess_limit > 0:
    letter = input("\nGuess a letter: ")
    if letter in guessed_letter:
        print("You already guessed that letter")
    elif letter in selected_word:
        guessed_letter.append(letter)

    else:
        guess_limit -= 1
        print(stages[guess_limit])
        if guess_limit == 0:
            print("You lose and the secret word was", selected_word)
            break
    for letter in selected_word:
        if letter in guessed_letter:
            print(letter, end="")
        else:
            print("_", end="")