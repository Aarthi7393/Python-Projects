import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter :row.code for (index, row) in data.iterrows()}
print(nato_alphabet)
def generate_phonetic():
    user_name = input("Enter your name: ").upper()
    # letters = [ letter for letter in user_name ]
    # print(letters)
    try:
        nato_phonetic_alphabet = [nato_alphabet[letter] for letter in user_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(nato_phonetic_alphabet)

generate_phonetic()