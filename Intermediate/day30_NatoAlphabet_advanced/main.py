import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# !!!important: for loop ---> list comprehension
is_translate = True
while is_translate:
    user_input = input("Enter a word: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output)
        is_translate = False

# output = []
# for letter in user_input:
#     output.append(phonetic_dic[letter])
