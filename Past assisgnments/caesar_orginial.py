def encrypted_message(message, rotation):
# call up the function by inputting a message and rotation amount (in main function)
# before looping create an empty string to add to
    encrypted = ''
# before looping create an uppercase string for an index because case must be maintained
    upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# before looping create a lowercase string for an index because case must be maintained
    loweralpha = 'abcdefghijklmnopqrstuvwxyz'
# loop through the characters in the message to determine if they are
    for char in message: 
    # this loops through each character in the message and when a condition is met does something
    # 1 - non-letter such as space, symbol, number, quotation marks. 
            if not char.isalpha():
        # if True (isalpha is False) then add character to encrypted string as is
                encrypted = encrypted + str(char)

    # 2 - upper case letter. Determine using isupper
            elif char.isupper():
                # if True then use rotation amount and key to find the new upper case letter
                rotated_index = upperalpha.index(char) + rotation
                if rotated_index < 26:
                    # if the rotated_index is less than 26 add new letter to string
                    encrypted = encrypted + upperalpha[rotated_index]

                else:
                    # if the rotated_index is greater than 26 determine new index by remainer
                    # add to string
                    encrypted = encrypted + upperalpha[rotated_index % 26]

            else: # use else since what is left is lower case letters
                rotated_index = loweralpha.index(char) + rotation
                if rotated_index < 26:
                    # if the rotated_index is less than 26 add new letter to string
                    encrypted = encrypted + loweralpha[rotated_index]

                else:
                    # if the rotated_index is greater than 26 determine new index by remainer
                    # add to string
                    encrypted = encrypted + loweralpha[rotated_index % 26]
    print(encrypted)
    return encrypted
    # return encrypted so that it prints out the new line of encryped text
    
    

def main():
    # message input
    message = input("Type a message: ")
    # rotation input
    rotation = input("Rotate by: ")
    # Is input always a string? Do I need to make it an interger?
    rotation = int(rotation)
    encrypted_message(message, rotation)
    # print out encrypted_message. 
        # Can I do this by calling the function encrypted_message?
        # do I print encrypted which is the return?
    

if __name__ == "__main__":
    main()