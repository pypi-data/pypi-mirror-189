import socket
import json

TCP_PORT = 55443


def get_socket(ip_address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, TCP_PORT))
    return s


def serialize_command(command):
    message = json.dumps(command) + "\r\n"
    return message.encode()


def send_command(ip_address, command):
    s = get_socket(ip_address)

    s.send(serialize_command(command))
    response = s.recv(1024)

    s.close()

    return response.decode()

