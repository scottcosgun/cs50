# Prompt user for question on the meaning of life
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

# Strip answer of white space
answer = answer.strip()

# Check if answer is numeric or alphabetic
if answer.isnumeric() == True:
    # Print yes if 42, otherwise print no
    if int(answer) == 42:
        print("Yes")
    else:
        print("No")

else:
    # Convert string to lowercase
    answer = answer.lower()
    # Check conditions
    if answer == "forty two" or answer == "forty-two":
        print("Yes")
    else:
        print("No")
