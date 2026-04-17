from tkinter import *
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.connect((host, port))

def receive():
    while True:
        try:
            msg = s.recv(1024).decode()
            chat.insert(END, "Server: " + msg)
        except:
            break

def send():
    msg = entry.get()
    chat.insert(END, "Client: " + msg)
    s.send(msg.encode())
    entry.delete(0, END)

root = Tk()
root.title("Client")

chat = Listbox(root, width=50, height=15)
chat.pack()

entry = Entry(root, width=40)
entry.pack()

Button(root, text="Send", command=send).pack()

threading.Thread(target=receive).start()

root.mainloop()