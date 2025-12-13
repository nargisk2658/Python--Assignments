'''Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.'''

def fact(num):
    factorial = 1
    while num > 1:
        factorial *= num 
        num -= 1
    return factorial 
n = int(input("Enter a number: "))
print(f"factorial of {n} is: {fact(n)}")
