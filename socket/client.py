#!/usr/bin/env python3

import socket
import argparse



def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', required=True)
    parser.add_argument('--data', default='Demo data')
    return parser.parse_args()

def check_port(target_port):
	if target_port < 0 or target_port > 65535:
		print('[!] Port must be in this range: 0-65535')
		exit(0)

def main():
    args = init_args()

    target_host = args.host
    target_port = int(args.port)

    check_port(target_port)

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(( target_host, target_port ))

        data = args.data.encode()
        client_socket.send(data)

        recv_data = client_socket.recv(1024)
        print(recv_data.decode())

        client_socket.close()

    except BaseException as e: print(f'[!] {e}')


if __name__ == '__main__': main()