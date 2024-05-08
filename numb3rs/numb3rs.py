import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Strip ip address of white space
    ip = ip.strip()
    # Search ip address for sequence #.#.#.#
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        # Split into 4 digits
        numbers = ip.split(".")
        # Ensure digits are in range 0-255
        for number in numbers:
            if int(number) > 255 or int(number) < 0:
                return False
        # If criteria is met, return true
        return True
    # If sequence is not in correct format, return false
    return False


if __name__ == "__main__":
    main()