import socket
import os
import time

port = int(os.getenv("PORT", 5005))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', port))
sock.listen(1)
print(f"⚡ Port {port} pre-bound for Render's scanner")

# Keep alive while Rasa starts
while True: time.sleep(1)
