#!/usr/bin/env python3


import socket
import argparse
from random import randint, random
import threading


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', required=False, default='')
    parser.add_argument('--port', required=False, default=randint(1024,65535))
    return parser.parse_args()


def boadcast_msg(msg, connections):
    for c in connections:
        c.send(msg.encode())

def connection_handler(username, connection, connections):
    while True:
        data = connection.recv(1024)
        boadcast_msg(f'{username}: {data.decode()}', connections)


def main():
    args = init_args()

    HOST = args.host
    PORT = int(args.port)

    usernames   = []
    connections = []

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f'[*] Server is listening on: {"0.0.0.0" if HOST == "" else HOST}:{PORT}')

    while True:
        connection, address = server.accept()
        print(f'[+] Got connection from: {address[0]}:{address[1]}')

        data = connection.recv(1024).decode()

        if 'USERNAME=' in data:
            username = data.replace('USERNAME=', '')
            usernames.append(username)
            connections.append(connection)

            print(f'[{username}] entered tha chat!')
            boadcast_msg(f'[{username}] entered tha chat!', connections=connections)

        connection_thread = threading.Thread(target=connection_handler, args=(username, connection, connections))
        connection_thread.start()




if __name__ == '__main__':
    main()