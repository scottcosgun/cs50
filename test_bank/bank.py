def main():
    # Prompt user for greeting
    greeting = input("Greeting: ")
    # Print value
    print(f"${value(greeting)}")

def value(greeting):
    # Strip white space and change to lowercase
    greeting = greeting.strip().lower()
    # Check if string starts with hello
    if greeting.startswith("hello"):
        return 0
    # Check if string starts with h
    elif greeting.startswith("h"):
        return 20
    # Otherwise, user gets $100
    else:
        return 100

if __name__ == "__main__":
    main()