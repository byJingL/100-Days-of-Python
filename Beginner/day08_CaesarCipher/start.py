alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

len_alphabet = len(alphabet)

#Create a function called 'encrypt'

def encrypt(plain_text, shift_amount):

    cipher_text = ""

    for letter in plain_text:
        position = alphabet.index(letter) # give the first index it find
        new_position = position + shift_amount
        cipher_text += alphabet[new_position] #只重复一遍字母表
        
    print(f"The encode text is {cipher_text}.")        

def decrypt(cipher_text, shift_amount):

    plain_text = ""

    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        #🌹index<0可以，list[-2]就是从后面取值
        plain_text += alphabet[new_position]

    print(f"The decode text is {plain_text}.")

if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decrypt(cipher_text = text, shift_amount = shift)