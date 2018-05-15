import socket
import numpy as np

color = input()

sock = socket.socket()
sock.connect(("127.0.0.1", 12345))

sock.send(color.encode())