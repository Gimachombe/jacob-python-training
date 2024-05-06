# Q3) Write a Python program that reads the text file created above named "data.txt" and prints the contents of the file. Implement exception handling to handle the case where the file does not exist.
try:
    file = open("data.txt", "r")
    print(file.read())

except Exception as e:
    print("File does not exist")
