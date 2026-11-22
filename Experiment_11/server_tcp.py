import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
print("Server waiting for connection...")
conn, addr = s.accept()
print("Connected with", addr)
data = conn.recv(1024)
print("Received from client:", data.decode())
conn.send(b"Hello from Server")
conn.close()
