
#🌹Reorganizing start.py

from art import logo
import os

#Create a function with all inputs
def caesar(action, start_text, shift_amount):
    
        final_text = ""

        if action == "decode":
            shift_amount *= -1
            #🌹index<0可以，list[-2]就是从后面取值

        for char in start_text:

            if char not in alphabet:
                final_text += char
            else:
                position = alphabet.index(char) # give the first index it find

                new_position = position + shift_amount
                    
                final_text += alphabet[new_position]

        print(f"Here's the {action}d result: {final_text}" )

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

 
print(logo)
use_cipher = True

while use_cipher == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(action = direction, start_text = text, shift_amount = shift)

    ask = input("Type 'yes' if you want to go again. Otherwise type'no'\n")
    
    os.system("clear")

    if ask == "no":
        use_cipher = False
        print("Than you for using Caesar Cipher, Goodbye.")


        
