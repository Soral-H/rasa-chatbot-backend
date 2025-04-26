import os
import socket
from threading import Thread
from flask import Flask
import random

app = Flask(__name__)
@app.route('/')
def health_check():
    return "OK", 200

class PortHolder:
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('0.0.0.0', self.port))
        self.socket.listen(1)
        print(f"🔒 Port {self.port} permanently held open")

def start_flask():
    port = int(os.getenv("FLASK_PORT", random.randint(10001, 20000)))  # Dynamic fallback
    try:
        app.run(host='0.0.0.0', port=port)
    except OSError:
        print(f"⚠️ Port {port} occupied, retrying...")
        start_flask()  # Recursive retry

if __name__ == "__main__":
    # Hold Rasa port
    PortHolder(int(os.getenv("PORT", 5005)))
    
    # Start Flask on dynamic port
    Thread(target=start_flask).start()
    
    # Start Rasa
    os.system(f"rasa run --enable-api --cors '*' --port {os.getenv('PORT', '5005')}")
