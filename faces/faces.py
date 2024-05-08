# This program will take user text as input and convert :) and :( into emojis

def main():
    # Collect user input as a str and store it in variable, text
    text = input("Text: ")
    # Convert the text and print it on the screen
    print(convert(text))

def convert(text):
    # Convert smiley faces
    text = text.replace(":)", "🙂")
    # Convert sad faces
    text = text.replace(":(", "🙁")
    return text

# Call main function
main()