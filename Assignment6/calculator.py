import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# These variables will store the first number and operator
first_number = ""
selected_operator = ""

# Entry box where numbers will appear
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5)
entry.pack(pady=10)

# This function runs when a number button is clicked
def click_number(number):
    entry.insert(tk.END, number)

# This function clears everything from the screen
def clear_screen():
    entry.delete(0, tk.END)

# This function saves the first number and operator
def set_operator(op):
    global first_number, selected_operator
    
    first_number = entry.get()   # store first number
    selected_operator = op       # store operator (+, -, *, /)
    entry.delete(0, tk.END)      # clear screen for second number

# This function performs the calculation
def calculate():
    global first_number, selected_operator
    
    second_number = entry.get()

    # Basic validation so it doesn’t crash
    if first_number == "" or second_number == "":
        entry.delete(0, tk.END)
        entry.insert(0, "Enter Number")
        return

    num1 = float(first_number)
    num2 = float(second_number)

    # Manual arithmetic logic (no eval used)
    if selected_operator == "+":
        result = num1 + num2
    elif selected_operator == "-":
        result = num1 - num2
    elif selected_operator == "*":
        result = num1 * num2
    elif selected_operator == "/":
        if num2 == 0:
            entry.delete(0, tk.END)
            entry.insert(0, "Cannot Divide")
            return
        result = num1 / num2
    else:
        result = "Error"

    entry.delete(0, tk.END)
    entry.insert(0, result)

# -------------------
# Number Buttons
# -------------------

tk.Button(root, text="1", command=lambda: click_number("1")).pack()
tk.Button(root, text="2", command=lambda: click_number("2")).pack()
tk.Button(root, text="3", command=lambda: click_number("3")).pack()

tk.Button(root, text="4", command=lambda: click_number("4")).pack()
tk.Button(root, text="5", command=lambda: click_number("5")).pack()
tk.Button(root, text="6", command=lambda: click_number("6")).pack()

tk.Button(root, text="7", command=lambda: click_number("7")).pack()
tk.Button(root, text="8", command=lambda: click_number("8")).pack()
tk.Button(root, text="9", command=lambda: click_number("9")).pack()

tk.Button(root, text="0", command=lambda: click_number("0")).pack()

# -------------------
# Operator Buttons
# -------------------

tk.Button(root, text="+", command=lambda: set_operator("+")).pack()
tk.Button(root, text="-", command=lambda: set_operator("-")).pack()
tk.Button(root, text="*", command=lambda: set_operator("*")).pack()
tk.Button(root, text="/", command=lambda: set_operator("/")).pack()

# -------------------
# Equal and Clear
# -------------------

tk.Button(root, text="=", command=calculate).pack()
tk.Button(root, text="C", command=clear_screen).pack()

root.mainloop()
