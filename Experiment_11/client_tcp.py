import socket

s = socket.socket()
s.connect(('localhost', 12345))
s.send(b"Hello from Client")
data = s.recv(1024)
print("Received from server:", data.decode())
s.close()
