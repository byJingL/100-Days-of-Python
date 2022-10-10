# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACE_HOLDER = "[name]"


with open("./Input/Names/invited_names.txt", mode="r") as name_file:
    # important: lines not line
    name_list = name_file.readlines()
with open("Input/Letters/starting_letter.txt", mode="r") as start:
    text = start.read()

    for name in name_list:
        real_name = name.strip()
        file_name = f"letter_to_{real_name}.txt"
        named_letter = text.replace(PLACE_HOLDER, real_name)

        with open(f"Output/ReadyToSend/{file_name}", mode="w") as file:
            file.write(named_letter)




