import socket
import threading

def handle_client(conn, addr):
    print("Connected with", addr)
    data = conn.recv(1024)
    print("Received from", addr, ":", data.decode())
    conn.send(b"Hello from Server")
    conn.close()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 12345))
s.listen(5)
print("Multi-client server waiting for connections...")
threads = []
for i in range(2):
    conn, addr = s.accept()
    t = threading.Thread(target=handle_client, args=(conn, addr))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
s.close()
