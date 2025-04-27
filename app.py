import os
import subprocess

def run_rasa():
    # Get the port from the environment variable or default to 5005
    port = os.environ.get("PORT", 5005)
    
    # Construct the command to run Rasa
    command = [
        "rasa", "run",
        "--enable-api",
        "--cors", "*",
        "-p", str(port)
    ]
    
    # Run the command
    subprocess.run(command)

if __name__ == "__main__":
    run_rasa()
