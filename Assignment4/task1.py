'''Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
 
Expected Output:

If the file exists:
Reading file content :
Line 1:  This is a sample text file.
Line 2: It contains multiple lines.

If the file does not exist:
Error: The file 'sample.txt' does not exist.
provide me the pythoņcode
'''

try:
    print("Reading file content :")
    file = open("sample.txt", "r")
    line_no = 1
    for line in file:
        print("Line", line_no, ":", line.strip())
        line_no += 1
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

