# Write a Python program that reads a text file named "data.txt" and prints its contents.

# file = open("data.txt", "x")

file = open("data.txt", "a")
file.write("\nMy name is Stephen")
file.write("\nMy name is Jacob")
file.write("\nMy name is Brian")
file.write("\nMy name is Jackline")
file.write("\nMy name is Lucas")

file = open("data.txt", "r")
print(file.read())
