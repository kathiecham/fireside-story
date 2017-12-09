def rotate_character (char, rot):
    letter_position = alphabet_position(char)
    upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    loweralpha = 'abcdefghijklmnopqrstuvwxyz'
    if char.isupper():
        new_letter = letter_position + rot
        if new_letter < 26:
            return upperalpha[new_letter]
        else:
            return upperalpha[new_letter % 26]
    else:
        new_letter = letter_position + rot
        if new_letter < 26:
            return loweralpha[new_letter]
        else:
            return loweralpha[new_letter % 26]


def alphabet_position (char):
    upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    loweralpha = 'abcdefghijklmnopqrstuvwxyz'
    if char.isupper():
        letter_position = upperalpha.index(char)
    else:
        letter_position = loweralpha.index(char)
    return letter_position