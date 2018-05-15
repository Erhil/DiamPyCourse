import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 12345))

while True:
    print(sock.recv(1024).decode())
sock.close()