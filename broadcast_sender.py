import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
UDP_IP = "255.255.255.255"
UDP_PORT = 5005
MESSAGE = b"Broadcast Test from Sender Node!"
print(f"Sending broadcast message to {UDP_IP}:{UDP_PORT}")
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
sock.close()
