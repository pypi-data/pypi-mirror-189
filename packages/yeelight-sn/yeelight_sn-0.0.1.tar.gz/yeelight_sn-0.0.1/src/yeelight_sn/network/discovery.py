import socket

UDP_PORT = 46791

DISCOVERY_ADDRESS = '239.255.255.250'
DISCOVERY_PORT = 1982

DISCOVERY_MESSAGE = "M-SEARCH * HTTP/1.1\r\n"
DISCOVERY_MESSAGE += "MAN: \"ssdp:discover\"\r\n"
DISCOVERY_MESSAGE += "ST: wifi_bulb\r\n"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', UDP_PORT))

sock.sendto(DISCOVERY_MESSAGE.encode(), (DISCOVERY_ADDRESS, DISCOVERY_PORT))
msg = sock.recv(1024)
response = msg.decode()

lines = response.split("\r\n")

for line in lines:
    if line.find('Location:') == 0:
        print(line)

