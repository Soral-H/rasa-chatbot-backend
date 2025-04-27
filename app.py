# start.py
import os
import subprocess

def run_rasa():
    # Get the port from the environment or default to 5005
    port = os.environ.get("PORT", 5005)

    # Construct the rasa run command
    command = [
        "rasa", "run",
        "--enable-api",
        "--cors", "*",
        "--port", str(port),      # <-- Explicitly use --port instead of -p (same thing, but clearer)
        "--model", "models"       # <-- Important: tell Rasa where the model folder is
    ]

    # Run the command
    subprocess.run(command, check=True)

if __name__ == "__main__":
    run_rasa()
