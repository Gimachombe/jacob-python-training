# Q5) Create a Python program that reads data from a CSV file ("data.csv") containing student information (e.g., name, age, grade). Parse the CSV file and print out the student information. Implement exception handling to handle any errors that may occur during file reading or parsing.

try:
    file=open('data.csv')
    file.close()
    print(file.read())
except Exception as e:
    file=open('data.csv')
    print(file.read())  
    

    

  
    
    



