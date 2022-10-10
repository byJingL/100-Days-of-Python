
#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list) #remember this function
word_length = len(chosen_word)
print(f"The solution is {chosen_word}")

#TODO-1-1: - Create an empty List called display.
display = []

for letter in chosen_word:
    display.append("_")

#TODO-2 - Ask the user to guess a letter and make guess lowercase.
#TODO-3 - Check if the guess is one of the letters in the chosen_word and replace.
#TODO-1: - Use a while loop to let the user guess again. 
#          The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
#          Then you can tell the user they've won.

while '_' in display: #remembet this function:
    guess = input("Guess a letter:").lower()

    #check guessed letter
    i = 0
    for letter in chosen_word:#dont need to change word to list(word)

        if letter == guess:
            display[i] = guess
        i += 1
    print(display)

print("you win")