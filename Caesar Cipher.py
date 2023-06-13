from art import logo
again = True
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(texto, deslocamento, direction):
    if direction == "encode":
        dirct = 1
    else:
        dirct = -1
    message = ""
    for letter in texto:
        if letter not in alphabet:
            new_letter = letter
        else:
            indice = alphabet.index(letter)
            indice += deslocamento * dirct
            indice = indice % 26
            new_letter = alphabet[indice]
        message += new_letter
    print(f'The {direction}d text is: "{message}"')

def yes():
    answer = input("Do you want to restart the cipher program? ").lower()
    if answer == "no":
        print("Goodbye")
        return False
    else:
        return True



while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift, direction)
    again = yes()