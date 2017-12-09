
def alphabet_position (char):
    upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    loweralpha = 'abcdefghijklmnopqrstuvwxyz'
    if char.isupper():
        letter_position = upperalpha.index(char)
    else:
        letter_position = loweralpha.index(char)
    return letter_position


def rotate_character (char, rotation):
    letter_position = alphabet_position(char)
    upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    loweralpha = 'abcdefghijklmnopqrstuvwxyz'
    if char.isupper():
        new_letter = letter_position + rotation
        return upperalpha[new_letter % 26]
    else:
        new_letter = letter_position + rotation
        return loweralpha[new_letter % 26]


def encrypt(text, key_word):
    encrypted = ''
    key_index = 0
    key_lenght = len(key_word)
    for char in text: 
        if not char.isalpha():
            encrypted = encrypted + str(char)
        else:
            # variable = name_of_string[location]
            current_key_letter = key_word[key_index % key_lenght]
            rotation = alphabet_position(current_key_letter)
            encrypted_letter = rotate_character(char, rotation)
            key_index = key_index + 1
            encrypted = encrypted + str(encrypted_letter)
    return encrypted


        
def main():
    text = input("Type a message: ")
    key_word = input("Encryption key word: ")
    print(encrypt(text, key_word))

    

if __name__ == "__main__":
    main()

