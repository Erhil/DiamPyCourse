import socket
import json

sock = socket.socket()

sock.bind(("", 12345))
sock.listen(1)

data = {"id" : "5532673ad15f",
        "title" : "Количество ребер в графе",
        "checker" : 0,
        "input" : [[[0, 1],
                    [1, 0]],
                   [[0]]
                   ],
        "output" : [1, 0]}

print("Server was launched")
working = True
while working:
    conn, addr = sock.accept()
    print(f"Connected client: {addr}")
    conn.send(json.dumps(data).encode())
    conn.close()
print("Server was terminated")
sock.close()
