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
            name = conn.recv(1024).decode()
            print(f"Connected client: {addr}")
            connections[conn] = name
            for connection in connections:
                if connection != sock:
                    connection.send(f'User {name} connected, total users: {len(connections)-1}'.encode())
        else:
            try:
                data = s.recv(4096)

                if data.decode()[0] == "@":
                    name = data.decode().split()[0][1:]
                    for connection in connections:
                        if connections[connection] == name and connection != sock:
                            connection.send((f'{connections[s]} шепчет: ' +
                                             ' '.join(data.decode().split()[1:])).encode())
                else:
                    for connection in connections:
                        if s != connection and connection != sock:
                            connection.send(f'{connections[s]} пишет: '.encode() + data)
            except ConnectionResetError:
                for connection in connections:
                    if connection != sock and connection != s:
                        connection.send(f'User {connections[s]} disconnected, total users: {len(connections)-2}'.encode())
                del(connections[s])
print("Server was terminated")
sock.close()
