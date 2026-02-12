import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x500")
root.resizable(False, False)

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        if expression == "":
            messagebox.showwarning("Warning", "Please enter an expression!")
        else:
            result = str(eval(expression))
            equation.set(result)
            expression = result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by Zero is not allowed!")
        clear()
    except Exception:
        messagebox.showerror("Error", "Invalid Input!")
        clear()

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

equation = tk.StringVar()

entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, relief="ridge", justify="right")
entry_field.pack(fill="both", ipadx=8, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(button_frame, text=text, height=2, width=8,
                        font=('Arial', 14), bg="lightgreen",
                        command=equalpress)
    else:
        btn = tk.Button(button_frame, text=text, height=2, width=8,
                        font=('Arial', 14),
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(button_frame, text="C", height=2, width=8,
                      font=('Arial', 14), bg="lightcoral",
                      command=clear)
clear_btn.grid(row=5, column=0, padx=5, pady=5)

back_btn = tk.Button(button_frame, text="⌫", height=2, width=8,
                     font=('Arial', 14), bg="lightblue",
                     command=backspace)
back_btn.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
