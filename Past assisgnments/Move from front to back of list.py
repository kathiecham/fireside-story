

def rotation(message):
    for char in message:
        key_word_list = [1,10,10,13]
        rotation = key_word_list[0]
        key_word_list += [key_word_list.pop(0)]
        print(rotation, key_word_list)

# define and populate list
# take and use the first item of the list but assigning it as a variable
# print the value so we can see that it works
# remove the first item in the list and place the return to the end of the list
# print the new list to make sure I it work


def main():
    message = 12345678
    rotation(message)
