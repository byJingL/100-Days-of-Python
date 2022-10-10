
#Step 1 

import os
import random
import Hangman_art as art #way01
from Hangman_words import word_list #way02

print(art.logo)
end_of_game = False

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list) #remember this function
word_length = len(chosen_word)
print(f"The solution is {chosen_word}")

#TODO-1-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#TODO-1-2: - Create an empty List called display.
display = []

for _ in range(word_length): #range(3), [0,3)
    display.append("_")


#TODO-2-1 - Ask the user to guess a letter and make guess lowercase.
#TODO-2-2 - Check if the guess is one of the letters in the chosen_word and replace.
#TODO-2-3: - Use a while loop to let the user guess again. 
#          The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
#          Then you can tell the user they've won.
#TODO-2-4: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."


while not end_of_game: 

    guess = input("Guess a letter:").lower()
    os.system("clear")
    is_in = False

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess
            is_in = True
    
        
    if not is_in: #==
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life")
        
    #Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    print(art.stages[lives])

    #very important: change the while condition
    if "_" not in display: #remembet this function
        end_of_game = True
        print("You win")
    
    if lives == 0:
            end_of_game = True
            print("You lose.")


