import sys
import os.path
from PIL import Image, ImageOps

def main():
    check_command_line()
    # Try opening input photo
    input = sys.argv[1]
    output = sys.argv[2]
    try:
        before = Image.open(input)
    # Handle exception and exit if file not found
    except FileNotFoundError:
        sys.exit(f"{input} not found")
    # Open shirt.png
    shirt = Image.open("shirt.png")
    # Save the size of the shirt and crop input image to be the same size
    size = shirt.size
    after = ImageOps.fit(before, size)
    # Paste shirt onto input photo
    after.paste(shirt, mask=shirt)
    # Save the resulting photo
    after.save(output)

    # Close files
    before.close()
    after.close()
    shirt.close()

def check_command_line():
    # Ensure correct # command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Ensure files are image files and that file types match up
    allowed = [".png", ".jpg", ".jpeg"]
    # Check extensions
    root1, ext1 = os.path.splitext(sys.argv[1])
    root2, ext2 = os.path.splitext(sys.argv[2])
    if ext1 not in allowed or ext2 not in allowed:
        sys.exit("Incorrect file type")
    elif ext1 != ext2:
        sys.exit("File types do not match")

if __name__ == "__main__":
    main()