import socket
import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# Define the syslog server's IP address and port
server_address = ('192.168.43.150', 514)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate a syslog message
message = '<14> This is a syslog message'

# Send the message to the syslog server
sock.sendto(message.encode(), server_address)

# Log a message to confirm that the syslog message was sent
logging.debug(f'Sent syslog message to {server_address}: {message}')
