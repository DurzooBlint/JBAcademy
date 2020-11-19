import argparse
import socket

parser = argparse.ArgumentParser(description='Connects to the given IP address.')

parser.add_argument('ip', metavar='ip', type=str, help='server IP')
parser.add_argument('port', metavar='port', type=int, help='port')
parser.add_argument('message', metavar='message', type=str, help='message to be send to server')

# Execute the parse_args() method
args = parser.parse_args()

with socket.socket() as client_socket:
    address = (args.ip, args.port)
    client_socket.connect(address)

    data = args.message
    data = data.encode()
    client_socket.send(data)
    response = client_socket.recv(1024)
    response = response.decode()
    print(response)