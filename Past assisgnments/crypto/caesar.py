from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted = ''
    for char in text: 
        if not char.isalpha():
            encrypted = encrypted + str(char)
        else:
            #call rotate_chartacer which gives me the new letter
            encrypted_letter = rotate_character(char, rot)
            encrypted = encrypted + str(encrypted_letter)
    return encrypted



def main():
    # message input
    text = input("Type a message: ")
    # rotation input
    rot = input("Rotate by: ")
    # Is input always a string? Do I need to make it an interger?
    rot = int(rot)
    print(encrypt(text, rot))
    # print out encrypted_message. 
        # Can I do this by calling the function encrypted_message?
        # do I print encrypted which is the return?
    

if __name__ == "__main__":
    main()

