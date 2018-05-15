import socket
import select

sock = socket.socket()

sock.bind(("", 12345))
sock.listen(10)

print("Server was launched")

connections = {sock: "__main"}

working = True
while working:
    read_sockets, write_sockets, error_sockets = select.select(connections, [], [])

    for s in read_sockets:
        if s == sock:
            conn, addr = sock.accept()
            color = conn.recv(1024).decode()
            print(f"Connected client: {addr}")
            connections[conn] = color
        else:
            pass