from tkinter import *
import socket
import threading

# Socket setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
client.connect((host, port))

# GUI setup
root = Tk()
root.title("Client")

chat = Listbox(root, width=50, height=20)
chat.pack()

entry = Entry(root, width=40)
entry.pack()

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            chat.insert(END, "Server: " + msg)
        except:
            break

def send():
    msg = entry.get()
    chat.insert(END, "Client: " + msg)
    client.send(msg.encode())
    entry.delete(0, END)

Button(root, text="Send", command=send).pack()

# Thread for receiving messages
thread = threading.Thread(target=receive)
thread.daemon = True
thread.start()

root.mainloop()