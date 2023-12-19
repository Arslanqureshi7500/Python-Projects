from hangman_word import word_list

def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
        if cipher_direction == "decode":
for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text = alphabet[new_position]
    else:
        end_text += char
print(f"Here/'s the {cipher_direction}, reult: {end_text}")