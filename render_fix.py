import os
import socket
from threading import Thread
from flask import Flask, jsonify
import subprocess

# 1. Health Check Server
app = Flask(__name__)
@app.route('/')
def health_check():
    return jsonify({"status": "OK", "service": "Rasa"}), 200

# 2. Port Holder Class
class PortHolder:
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('0.0.0.0', self.port))
        self.socket.listen(1)
        print(f"🔒 Port {self.port} permanently held open")

# 3. Rasa Launcher
def start_rasa():
    cmd = f"rasa run --enable-api --cors '*' --port {os.getenv('PORT', '5005')}"
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    # Hold both ports open
    rasa_port = PortHolder(int(os.getenv("PORT", 5005)))
    health_port = PortHolder(10000)  # Render's scanner port
    
    # Start services
    Thread(target=lambda: app.run(host='0.0.0.0', port=10000)).start()
    Thread(target=start_rasa).start()
    
    # Keep alive
    while True: pass
