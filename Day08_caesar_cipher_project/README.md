# Caesar Cipher Encryption & Decryption

This is a simple **Caesar Cipher** program written in Python.  
It allows you to **encrypt** and **decrypt** messages by shifting each letter of the alphabet by a given number of positions.

---

## Features
- Encrypt a message with a given shift.
- Decrypt a message back to the original.
- Preserves spaces, punctuation, and non-alphabet characters.
- Supports continuous play until the user chooses to exit.

---

## How It Works
The Caesar Cipher works by shifting each letter in the text by a certain number of positions down the alphabet.

Example: Shift: 3
Plaintext: hello
Ciphertext: khoor
 f you choose **decode**, it shifts in the opposite direction to retrieve the original message.

---

## Usage
1. Run the Python script.
2. Select either:
   - `encode` → to encrypt text
   - `decode` → to decrypt text
3. Enter your message.
4. Enter the shift number.
5. The program will return the encrypted or decrypted message.

---

## Example Run
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
5
Your encrypted text is mjqqt btwqi!
Do you want to go again, Type: Yes or No
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt btwqi!
Type the shift number:
5
Your decrypted text is hello world!
