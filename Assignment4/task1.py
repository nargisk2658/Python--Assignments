''' Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
try:
    
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:

    print("Error: The file 'sample.txt' does not exist.")
