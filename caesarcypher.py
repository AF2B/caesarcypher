import logo

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    caesar(start_text=text, shift_amount=shift, cipher_direction="encode")
elif direction == "decode":
    caesar(start_text=text, shift_amount=shift, cipher_direction="decode")
