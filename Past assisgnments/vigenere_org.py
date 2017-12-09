def rotation_key(key_word):
    key_word = key_word.lower()
    key_word.list = []
    loweralpha = 'abcdefghijklmnopqrstuvwxyz'
    for letter in key_word:
        letter_position = loweralpha.index(letter)
        key_word_list = key_word_list.append(letter_position)
    return key_word_list

def rotation(message, key_word_list):
    for char in message:
        # the key_word+list has to be called here
        rotation = key_word_list[0]
        key_word_list += [key_word_list.pop(0)]

def alphabet_position (char):
    upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    loweralpha = 'abcdefghijklmnopqrstuvwxyz'
    if char.isupper():
        letter_position = upperalpha.index(char)
    else:
        letter_position = loweralpha.index(char)


def rotate_character (char):
    letter_position = alphabet_position(char)
    upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    loweralpha = 'abcdefghijklmnopqrstuvwxyz'
    # but I need to pull in the rotation which I get from the rotation key
    # Create the key here first
    # do the rotation - how
    if char.isupper():
        new_letter = letter_position + rotation
        if new_letter < 26:
            return upperalpha[new_letter]
        else:
            return upperalpha[new_letter % 26]
    else:
        new_letter = letter_position + rotation
        if new_letter < 26:
            return loweralpha[new_letter]
        else:
            return loweralpha[new_letter % 26]


def encrypted_message(message):
    encrypted = ''
    for char in message: 
        if not char.isalpha():
            encrypted = encrypted + str(char)
        else:
            encrypted_letter = rotate_character(char)
            encrypted = encrypted + str(encrypted_letter)
    return encrypted


        
def main():
    message = input("Type a message: ")
    key_word = input("Encryption key word: ")
    print(encrypted_message(message))

    

if __name__ == "__main__":
    main()