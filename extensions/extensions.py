# Prompt user for file name
name = input("File name: ")

name = name.strip().lower()

# Store extensions in lists based on file type
image = ["gif", "jpeg", "png"]
application = ['pdf', 'zip']
text = ['txt']

found = False

# Check in images list for extension
if found == False:
    for extension in image:
        if name.endswith(extension):
            print("image/" + extension)
            found = True
            break

# If not found, check application list
if found == False:
    for extension in application:
        if name.endswith(extension):
            print("application/" + extension)
            found = True
            break

# Check special conditions
if found == False:
    if name.endswith("txt"):
        print("text/plain")
        found = True
    elif name.endswith("jpg"):
        print("image/jpeg")
        found = True
    else:
        print("application/octet-stream")