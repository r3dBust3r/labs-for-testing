import socket
import os

HOST = '127.0.0.1'
PORT = 1290

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f'[*] Server is listening for incomming connections on {HOST}:{PORT}')

client, addr = server.accept()
print(f'[*] Got connection from {addr[0]}:{addr[1]}')


filename = client.recv(1024).decode()
filesize = client.recv(1024).decode()

print(f'filename: {filename}\nfilesize: {filesize}')

data = b''
progress = 0

while True:
    recvd = client.recv(4096)
    data += recvd
    progress += 4096
    print(f'[{progress}/{filesize}]bytes', end="\r")
    if not recvd: break

with open(f'recvd_{filename}', 'ab') as file:
    file.write(data[0:-5])

client.close()
server.close()

