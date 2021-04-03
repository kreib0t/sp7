import socket

host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

print("Waiting for client...")
conn,addr = s.accept()
print("Connected by ", addr)

while True:
    data = conn.recv(1024)
    if not data: break
    print("received data:", data)
    conn.send(data)
conn.close()
