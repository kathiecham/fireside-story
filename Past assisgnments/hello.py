def analyze_text(text):
    letter_count = 0
    for char in text:
        if char.isalpha() is True:
            letter_count = letter_count + 1
        return (letter_count)
     
def analyze_e(text):
    letter_e = 0
    for letter in text:
        if letter == "e":
            letter_e = letter_e +1
        if letter == "E":
            letter_e = letter_e +1
        return (letter_e)

def figure_percent(letter_count, letter_e):
    if letter_e == 0:
        percentage = "0"
    else:
        percentage = (letter_e/letter_count)*100
        percentage = str(percentage)
    return (percentage)
       
def main(text):
    analyze_text(text)
    analyze_e(text)
    figure_percent

print("The text contains " +str(letter_count) +" alphabetic characters, of which " +str(letter_e) +" (" + percentage +"%) are 'e'.")