import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter :row.code for (index, row) in data.iterrows()}
print(nato_alphabet)

user_name = input("Enter your name: ").upper()
# letters = [ letter for letter in user_name ]
# print(letters)
nato_phonetic_alphabet = [nato_alphabet[letter] for letter in user_name]
print(nato_phonetic_alphabet)

