import os
import subprocess
import socket
from time import sleep

def hold_port():
    """Hold the port open immediately for Render's scanner"""
    port = int(os.getenv("PORT", 5005))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(1)
    print(f"🚀 Holding port {port} open for Render's scanner")
    return s  # Keep socket open

def start_rasa():
    """Start Rasa in a subprocess"""
    cmd = [
        "rasa", "run",
        "--enable-api",
        "--cors", "*",
        "--port", os.getenv("PORT", "5005"),
        "--debug"
    ]
    return subprocess.Popen(cmd)

if __name__ == "__main__":
    # Immediately bind to port
    sock = hold_port()
    
    # Start Rasa
    rasa_process = start_rasa()
    
    # Keep both running
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        sock.close()
        rasa_process.terminate()
