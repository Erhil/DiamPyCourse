import socket
import json

sock = socket.socket()
sock.connect(("127.0.0.1", 12345))

# data = input()
# sock.send(data.encode())

raw_data = sock.recv(1024).decode()
data = json.loads(raw_data)
print(data)
print(type(data))
sock.close()