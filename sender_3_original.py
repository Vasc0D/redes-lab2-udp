import socket

UDP_IP = "172.20.10.4"
UDP_PORT = 5005
SENDER_ID = "Sender_3"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Starting UDP test...")

for i in range(1, 10001):
    message = f"{SENDER_ID} - Packet {i}".encode()
    sock.sendto(message, (UDP_IP, UDP_PORT))

print("Transmission complete.")
sock.close()
