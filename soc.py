import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the syslog port (514)
sock.bind(('0.0.0.0', 514))

# Listen for incoming syslog messages
while True:
    data, addr = sock.recvfrom(1024)
    print(f'Received syslog message from {addr}: {data.decode()}')
