import socket
import select

sock = socket.socket()

sock.bind(("", 12345))
sock.listen(1)
print("Server was launched")

connections = {sock: "__main"}
working = True
while working:
    read_data, _, _ = select.select(connections, [], [])

    for connection in read_data:
        if connection == sock:
            conn, addr = sock.accept()
            print(f"Connected client: {addr}")
            name = conn.recv(1024).decode()
            connections[conn] = name
            for client in connections:
                if client != sock:
                    client.send(f'User {name} connected, total users: {len(connections) - 1}'.encode())
        else:
            try:
                data = connection.recv(4096).decode()
                if data[0] == "@":
                    for client in connections:
                        message = data.split()
                        if (client != sock and
                                connections[client] == message[0][1:]):
                            client.send(
                            (f"{connections[connection]} шепчет: " +
                             " ".join(message[1:])).encode()
                        )
                else:
                    for client in connections:
                        if (client != sock and
                                client != connection):
                            client.send(
                            (f"{connections[connection]} пишет: " +
                             data).encode()
                        )
            except ConnectionResetError:
                for client in connections:
                    if client != sock and client != connection:
                        client.send(f'User {name} disconnected, total users: {len(connections)- 2}'.encode())
                connection.close()
                del(connections[connection])
print("Server was terminated")
sock.close()
