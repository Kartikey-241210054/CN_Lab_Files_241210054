import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 12345))
print("UDP Server is ready...")
data, addr = s.recvfrom(1024)
print("Received:", data.decode())
s.sendto(b"Hello from Server", addr)
