# Laboratorio UDP — códigos de los checkpoints del grupo

Python 3; únicamente biblioteca estándar. Los cuatro archivos transcriben el código incluido en nuestras respuestas, normalizando sangría y saltos de línea. Se conservan parámetros y lógica.

| Archivo | Procedencia |
|---|---|
| `broadcast_receiver.py` | Checkpoints-REDES-3.pdf, Checkpoint 5: receptor en puerto 5005. |
| `broadcast_sender.py` | Checkpoints-REDES-3.pdf, Checkpoint 5: envío a 255.255.255.255:5005. |
| `stress_sender.py` | Checkpoints-REDES-3.pdf, Checkpoint 6: 10 000 envíos con SENDER_ID y secuencia. |
| `udp_flood.py` | Checkpoints-REDES-5.pdf: prueba local de 15 segundos, carga de 1024 bytes y tasa nominal de 100 envíos/s. |

## Uso en la LAN de la práctica

Ajustar las IP al equipo receptor. Iniciar el receptor antes del emisor.

- Broadcast: ejecutar `python3 broadcast_receiver.py` en los receptores y `python3 broadcast_sender.py` en el emisor.
- Carga: configurar IP y un SENDER_ID distinto por emisor; ejecutar `python3 stress_sender.py`. Capturar `udp.port == 5005` en el receptor.
- Ráfaga local: configurar VICTIM_IP y ejecutar `python3 udp_flood.py` en los equipos de la práctica. Finaliza a los 15 segundos o con Ctrl+C.

El literal `Sender Node!` del código broadcast es la variante escrita en el checkpoint; la terminal muestra `DJZasco Node!`. Se conservan también la errata `boradcast` y el import duplicado del código de carga. Los contadores de envío no son confirmaciones de recepción. La comprobación de estos archivos fue sintáctica, sin nuevas transmisiones.
