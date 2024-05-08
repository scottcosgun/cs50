from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

# Check for proper # of command line arguments:
if len(sys.argv) == 2 or len(sys.argv) > 3:
    sys.exit("Invalid usage")

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "-font":
        sys.exit("Invalid usage")

# Store list of available fonts
fonts = figlet.getFonts()

# Input text from user
text = input("Input: ")

# Select font from list
if len(sys.argv) == 1:
    font = random.sample(fonts, k=1,)[0]
else:
    font = sys.argv[2]
    if font not in fonts:
        sys.exit("Font is not available")

# Set font and print text
figlet.setFont(font=font)
print(figlet.renderText(text))





