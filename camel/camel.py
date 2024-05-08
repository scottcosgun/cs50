# Prompt user for name in camelCase
camel = input("camelCase: ")

print("snake_case: ", end="")
# Iterate over characters in camelCase name
for letter in camel:
    # If letter is lowercase, print it out
    if letter.islower():
        print(letter, end="")
    # If letter is capital, print out _ + lowercase letter
    else:
        print("_" + letter.lower(), end="")
print()