import socket
import threading

sock = socket.socket()

name = input("Введите имя\n")
sock.connect(("127.0.0.1", 12345))
sock.send(name.encode())

def listen_data():
    while True:
        data = sock.recv(4096).decode()
        if data:
            print(data)

thread = threading.Thread(target=listen_data)
thread.start()

while True:
    message = input()
    if message == "/stop":
        break
    else:
        sock.send(message.encode())

sock.close()