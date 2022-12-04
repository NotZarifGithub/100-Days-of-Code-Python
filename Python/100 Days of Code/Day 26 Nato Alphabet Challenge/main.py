import pandas

data = pandas.read_csv(r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 26 Nato Alphabet Challenge\nato_phonetic_alphabet.csv")

phoenetic_dict = {row.letter:row.code for (index, row) in data.iterrows() }

word =  input("Enter a word: ").upper()

def generate_phoenetic():
    
    try:
        word_list = [phoenetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_phoenetic()
    else:
        print(word_list)

generate_phoenetic()