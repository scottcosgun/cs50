import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Search string, s, for appearances of "um" as it's own word, ignoring case
    if matches := re.findall(r"\bum\b", s, re.IGNORECASE):
        return len(matches)
    # If no matches, return 0
    return 0


if __name__ == "__main__":
    main()