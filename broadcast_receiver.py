import socket

UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", UDP_PORT))
print(f"Listening for boradcast message on port {UDP_PORT}...")
while True:
    data, addr = sock.recvfrom(1024)
    print("Received message %s" % data)
