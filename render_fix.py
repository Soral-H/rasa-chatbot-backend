import os
import socket
from threading import Thread
from flask import Flask

# Create a basic Flask health check server
app = Flask(__name__)
@app.route('/')
def health_check():
    return "OK", 200

def run_flask():
    app.run(host='0.0.0.0', port=int(os.getenv("FLASK_PORT", 10000)))

def hold_rasa_port():
    """Permanently hold Rasa's port open"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', int(os.getenv("PORT", 5005))))
    s.listen(1)
    print(f"🔒 Permanently holding port {os.getenv('PORT', 5005)} open")
    while True: pass  # Keep port bound forever

if __name__ == "__main__":
    # Start Flask health check on Render's scanner port
    Thread(target=run_flask).start()
    
    # Hold Rasa's port open
    hold_rasa_port()
