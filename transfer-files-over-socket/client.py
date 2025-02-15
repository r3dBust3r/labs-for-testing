import socket
import os

HOST = '127.0.0.1'
PORT = 1290

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


print(f'[*] Connected to {HOST}:{PORT}')

filename = input('which file you want to transfer: ')
# filename = 'me.txt'

if not os.path.isfile(filename):
    print(f'[-] No such file or directory: {filename}')
    exit(0)

filebasename = os.path.basename(filename).encode()
filesize = str(os.path.getsize(filename)).encode()

file = open(filename, 'rb')
filedata = file.read()

client.send(filebasename)
client.send(filesize)
client.sendall(filedata)
client.send('<EOF>'.encode())


file.close()
client.close()