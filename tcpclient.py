import socket

host = socket.gethostname()
port = 12345

string = str(input("Input message:" ))
msg = str.encode(string)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send(msg)

data = s.recv(1024)

print(data)
s.close()
