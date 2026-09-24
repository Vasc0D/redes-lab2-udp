# Laboratorio 2: UDP — CS4055

Códigos recuperados para el segundo informe. Python 3 y biblioteca estándar (`socket`, `struct`, `zlib`, `time`); no requieren paquetes adicionales. Las IP corresponden a la LAN de la práctica y deben ajustarse al repetirla.

## Procedencia

| Archivo | Origen y alcance |
|---|---|
| `broadcast_receiver.py`, `broadcast_sender.py` | Transcripción del código de Checkpoints-REDES-3.pdf, Checkpoint 5. Se normalizan sangrías y saltos de línea. Se conserva la errata `boradcast`. El literal Sender Node! del código difiere del DJZasco Node! visible en una terminal. |
| `stress_sender.py` | Transcripción del emisor Sender_1 de Checkpoints-REDES-3.pdf, Checkpoint 6. Conserva el import duplicado. |
| `sender_3_original.py` | Copia sin cambios del archivo local Redes/sender.py, variante Sender_3. Su existencia no prueba una ejecución completa ni recepción. |
| `udp_flood.py` | Transcripción de Checkpoints-REDES-5.pdf, páginas 1–2. Conserva límites de 15 segundos, 1024 bytes y 100 envíos/s nominales. |
| `loopback_receiver.py`, `loopback_sender.py` | Transcripción de los ejemplos de Sem04_LAB2_UDP_2.pdf, página 2. Se añade únicamente una aclaración al comentario del encabezado. La guía fuerza el campo de aplicación a 4; no valida un checksum UDP. |
| `p2p_sender_reconstruido.py`, `p2p_receiver_reconstruido.py` | Adaptaciones nuevas basadas en la guía y los bytes de las capturas del Checkpoint 4. Son ejemplos compatibles con el formato observado, NO los archivos originales. |

No se recuperó la fuente original completa de los programas P2P. El archivo local de Sender_3 sí se conserva exactamente. Los programas se comprobaron mediante análisis sintáctico, sin ejecutar transmisiones ni generar nuevas evidencias.

## Uso en la LAN del laboratorio

1. Configurar IP de destino y puerto antes de ejecutar. Iniciar el receptor antes del emisor.
2. Loopback: `python3 loopback_receiver.py` y, en otra terminal, `python3 loopback_sender.py`. Capturar en la interfaz loopback, filtro `udp.port == 5005`.
3. P2P: configurar la IP del receptor en `p2p_sender_reconstruido.py`; ejecutar el receptor y luego el emisor. Capturar en la interfaz LAN.
4. Broadcast: ejecutar `broadcast_receiver.py` en cada receptor y `broadcast_sender.py` una vez en el emisor. Los firewalls y el dominio de broadcast deben permitir la comunicación.
5. Carga: configurar receptor y un SENDER_ID distinto por emisor; iniciar captura y receptor, y ejecutar `stress_sender.py` en cada emisor. El programa agenda 10 000 envíos; no mide pérdidas. El receptor broadcast puede escuchar esos datagramas unicast, pero no registra secuencias en un archivo.
6. Ráfaga local: en el entorno de laboratorio acordado, configurar VICTIM_IP y ejecutar `udp_flood.py`. Finaliza a los 15 segundos o con Ctrl+C. Conservar el contador de cada emisor y capturar el flujo `udp.dstport == 9999`.
7. Netcat (CP7): `nc -u -v IP_DESTINO 1234`; en Windows, `ncat -u -v IP_DESTINO 1234`. Capturar `udp || icmp`.
8. UDP/TCP (CP8): receptor `nc -u -l 4444`, emisor `nc -u -v IP_DESTINO 4444`; repetir sin `-u` para TCP. En Windows receptor UDP: `ncat -u -l -p 4444`. Enviar las palabras de la guía y cerrar el receptor para observar el comportamiento.

## Interpretación

El encabezado construido con `!IIII` ocupa 16 bytes dentro de la carga. No configura los campos UDP del sistema; el socket determina el puerto origen real. En la guía, el valor 4 está forzado; en la reconstrucción P2P se calcula CRC32. Ningún receptor incluido valida ese CRC ni implementa ACK, recuperación, control adaptativo o detección de desconexiones.

Para verificar los checkpoints pendientes se necesitan capturas originales y registros por emisor/receptor. Estos scripts y una captura parcial no prueban que tres emisores finalizaron 30 000 envíos ni que tres receptores vieron el mismo broadcast.
