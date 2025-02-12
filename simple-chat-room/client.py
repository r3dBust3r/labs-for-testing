#!/usr/bin/env python3


import socket
import argparse
import threading


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', required=False, default='127.0.0.1')
    parser.add_argument('--port', required=True)
    return parser.parse_args()

def handle_typing(connection, username):
    while True:
        msg = input(f"[{username}]: ")
        connection.send(msg.encode())

def handle_recieving(connection):
    while True:
        msg = connection.recv(1024)
        print(msg.decode())

def main():
    args = init_args()
    HOST = args.host
    PORT = int(args.port)

    username = input("What is your username?\n>> ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    
    msg = f'USERNAME={username.encode()}'
    client.send(msg.encode())

    typing_thread = threading.Thread(target=handle_typing, args=(client, username))
    recieving_thread = threading.Thread(target=handle_recieving, args=(client,))

    typing_thread.start()
    recieving_thread.start()


if __name__ == '__main__':
    main()