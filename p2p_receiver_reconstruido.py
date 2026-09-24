"""Adaptacion reconstruida; imprime bytes y origen sin validar el CRC32."""
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(("0.0.0.0", 5005))
    print("Waiting for UDP messages...")
    while True:
        data, addr = sock.recvfrom(65535)
        print("Received from:", addr)
        print("Received message:", data)
