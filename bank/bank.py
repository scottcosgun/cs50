# Prompt user for greeting
greeting = input("Greeting: ")

# Strip white space and change to lowercase
greeting = greeting.strip().lower()

# Check if string starts with hello
if greeting.startswith("hello"):
    print("$0")
# Check if string starts with h
elif greeting.startswith("h"):
    print("$20")
# Otherwise, user gets $100
else:
    print("$100")