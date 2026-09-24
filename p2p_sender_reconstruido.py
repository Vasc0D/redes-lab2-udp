"""Adaptacion reconstruida de la guia; no es el archivo original del grupo."""
import socket
import struct
import zlib

UDP_IP = "172.20.10.2"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"
header = struct.pack("!IIII", UDP_PORT, UDP_PORT, len(MESSAGE), zlib.crc32(MESSAGE))
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto(header + MESSAGE, (UDP_IP, UDP_PORT))
