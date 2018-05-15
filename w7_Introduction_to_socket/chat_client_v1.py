import socket
import threading
import select
import time


sock = socket.socket()
sock.settimeout(1)

sock.connect(("127.0.0.1", 12345))
data = input("Введите ваше имя\n")
sock.send(data.encode())

def monitor_connections():
    while True:
        read_sockets, write_sockets, error_sockets = select.select([sock], [], [])
        for s in read_sockets:
            if s == sock:
                data = sock.recv(4096).decode()
                if not data:
                    print("No data")
                else:
                    print(data)

t = threading.Thread(target=monitor_connections)
t.start()

print("Добро пожаловать в чат!")
while True:
    text = input()
    if text == "/close":
        break
    sock.send(text.encode())
sock.close()