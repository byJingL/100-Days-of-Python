alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

len_alphabet = len(alphabet)


#Create a function called 'encrypt'

def encrypt(plain_text, shift_amount):

    cipher_text = ""

    for position in range(len(plain_text)):

        for i in range(len_alphabet):

            if plain_text[position] == alphabet[i]:

                if i+3 < len_alphabet:
                    cipher_text += alphabet[i+shift_amount]
                else:
                    cipher_text += alphabet[i+shift_amount-len_alphabet]
                
    print(f"The encode text is {cipher_text}.")        

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)