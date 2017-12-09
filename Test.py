def encrypted_message(message, key_word):
    encrypted = ''
    key_index = 0
    key_lenght = len(key_word)
    for char in message: 
            # variable = name_of_string[location]
            current_key_letter = key_word[key_index % key_lenght]
            print(current_key_letter)
            rotation = alphabet_position(current_key_letter)
            print(rotation)
            key_index = key_index + 1

    return encrypted

def alphabet_position (char):
    upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    loweralpha = 'abcdefghijklmnopqrstuvwxyz'
    if char.isupper():
        letter_position = upperalpha.index(char)
    else:
        letter_position = loweralpha.index(char)
    return letter_position


        
def main():
    message = input("Type a message: ")
    key_word = input("Encryption key word: ")
    print(encrypted_message(message, key_word))

    

if __name__ == "__main__":
    main()
