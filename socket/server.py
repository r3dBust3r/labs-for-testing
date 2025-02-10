#!/usr/bin/env python3

import socket
import argparse
import threading
import os


def init_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--host', default='')
	parser.add_argument('--port', required=True)
	return parser.parse_args()


def check_port(server_port):
	if server_port < 0 or server_port > 65535:
		print('[!] Port must be in this range: 0-65535')
		exit(0)

	if server_port < 1024:
		if os.getuid() != 0:
			print(f'[!] root privilege required to start a server on this port {server_port}.')
			print(f'Run with `sudo` or choose another port not in 0-1023 range.')
			exit(0)


def client_handler(client_socket):
	data = client_socket.recv(1024)
	print(f'{data.decode()}')
	client_socket.send('Thanks client for this data'.encode())


def main():
	args = init_args()

	server_host = args.host
	server_port = int(args.port)

	check_port(server_port)

	try:
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.bind((server_host, server_port))
		server_socket.listen(1)
		print(f'[*] Listening on {"0.0.0.0" if server_host == "" else server_host}:{server_port}')

		while 1:
			client_socket, address = server_socket.accept()
			print(f'[*] Got connection from {address[0]}:{address[1]}')
			client = threading.Thread(target=client_handler, args=(client_socket,))
			client.start()

	except BaseException as e:
		print(f'[!] {e}')


if __name__ == '__main__': main()