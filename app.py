# start.py
import os
import subprocess

def run_rasa():
    # Get the port from the environment or default to 4000
    port = int(os.environ.get("PORT", 4000))

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
