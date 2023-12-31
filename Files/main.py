# File operations.

# Opening a file.
#file = open("my_file.txt")

# Using 'with' keyword will automatically close the file once the file operations are over.
# File should be open in mode="r" for reading.
# File should be open in mode="w" for writing.
# File should be open in mode="a" for appending.
# If the mode is "w" and a file does not exist, it will create the file
with open("my_file.txt", mode="r") as file:

    # Read file
    content = file.read()
    print(content)

    # Close file
    # This is not needed since the 'with' keyword is used
    #file.close()

# Open file for appending
with open("my_file.txt", mode="a") as file:

    # Appending to the file
    file.write("This is the new appended text!\n")
