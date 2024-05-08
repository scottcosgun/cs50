import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Search string for iframe HTML element
    if re.search(r'<iframe(.)*><\/iframe>$', s):
        # Search for src="url"
        src = re.search(r'src="http(s)?://(www\.)?youtube\.com/embed/(\w+)"', s)
        if src:
            # Save the \w+ group as an extension to add to shortened url
            extension = src.group(3)
            # Return shortened url
            return "https://youtu.be/" + extension
        # If format is incorrect or url does not exist, return none
        return None


if __name__ == "__main__":
    main()