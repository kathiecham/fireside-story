def analyze_text(text):
    letter_count = 0
    for letter in text:
        if letter_count == True:
            letter_count += 1
    return letter_count
    
     
def analyze_e(text):
    letter_e = text.count('e') + text.count('E')
    return letter_e
    

def figure_percent(letter_count, letter_e):
    if letter_e == 0:
        percentage = "0"
    else:
        percentage = (letter_e/letter_count)*100
        percentage = str(percentage)
    return (percentage)
       
def main(text):
    letter_count = analyze_text(text)
    letter_e = analyze_e(text)
    percentage = figure_percent(letter_count, letter_e)
    print("The text contains " +str(letter_count) +" alphabetic characters, of which " +str(letter_e) +" (" + percentage +"%) are 'e'.")


if __name__ == "__main__":
    main()
