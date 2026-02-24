PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt", "r") as file:
    #invited_names = file.readlines()
    invited_names = file.read().splitlines()
    #print(invited_names)

    for name in invited_names:
        letter_to_save = ""
        with open("Input/Letters/starting_letter.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if PLACEHOLDER in line:
                    line = line.replace(PLACEHOLDER, name)
                letter_to_save += line
            with open(f"Output/ReadyToSend/Letter_for_{name}", "w") as file:
                file.write(letter_to_save)

