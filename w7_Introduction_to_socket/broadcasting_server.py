import socket

sock = socket.socket()

sock.bind(("", 12345))
sock.listen(1)

print("Server was launched")

connections = []
working = True
while working:
    conn, addr = sock.accept()
    print(f"Connected client: {addr}")
    connections.append(conn)

    for connection in connections:
        connection.send(f'User {addr} connected, total users: {len(connections)}'.encode())
print("Server was terminated")
sock.close()
