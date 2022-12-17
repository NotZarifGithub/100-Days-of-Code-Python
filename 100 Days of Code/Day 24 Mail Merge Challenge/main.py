PLACEHOLDER = "[name]"


with open("./venv/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./venv/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./venv/Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
        