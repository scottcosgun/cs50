from validator_collection import validators

def main():
    print(validate(input("Email: ")))


def validate(s):
    try:
        if s == validators.email(s):
            return "Valid"
    except ValueError or TypeError:
        return "Invalid"


if __name__ == "__main__":
    main()