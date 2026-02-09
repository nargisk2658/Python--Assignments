'''Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
Expected Output:
 For example, if the user enters 25, the output should be:
 Enter text to write to the file : Hello, Python!
 Data successfully written in output.txt.  
 
Enter additional text to append: Learning file handling in Python.
Data successfully appended. 

Final content of the output.txt:
Hello, Python!
Learning file handling in Python.
'''


text = input("Enter text to write to the file : ")

file = open("output.txt", "w")
file.write(text + "\n")
file.close()

print("Data successfully written in output.txt.\n")

append_text = input("Enter additional text to append: ")

file = open("output.txt", "a")
file.write(append_text + "\n")
file.close()

print("Data successfully appended.\n")

print("Final content of the output.txt:")

file = open("output.txt", "r")
content = file.read()
print(content)
file.close()

