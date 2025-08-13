from arts import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def caesar(original_text, shift_amount,direction):
    if direction=="encode":

        encrypted_text = ""

        for letter in original_text:
            if letter not in alphabet:
                encrypted_text+=letter
            elif letter in alphabet:
                position = alphabet.index(letter)
                shifted_position = position + shift_amount
                shifted_position = shifted_position % len(alphabet)
                encrypted_text = encrypted_text + alphabet[shifted_position]
        print(f"Your encrypted text is {encrypted_text}")

    elif direction=="decode":

        decrypted_text=""
        for letter in original_text:
            shifted_position=alphabet.index(letter)
            shifted_position = shifted_position - shift_amount
            shifted_position = shifted_position % len(alphabet)
            decrypted_text += alphabet[shifted_position]
        print(f"Your decrypted text is {decrypted_text}")
game_over=False
while not game_over:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    again=input("Do you want to go again,Type:Yes or No").lower()
    if again!="yes":
        game_over=True
        print("Goodbye")