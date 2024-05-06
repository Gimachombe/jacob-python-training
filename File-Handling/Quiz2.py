# Create a Python program that prompts the user to enter a message and writes it to a file named "output.txt".  Implement exception handling to handle any errors that may occur during file writing.

# file = open("output.txt", "x")

try:
    #prompt user to enter msg
    message = input("Enter your message:")

    #open the file  "output.txt" for writing
    file = open("output", "w")

    #write message to the file
    file.write(message)

    print("Message has been written to the file")


except Exception as e:
    print("An error occurred while trying to write to the file.", e)