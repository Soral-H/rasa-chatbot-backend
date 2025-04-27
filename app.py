import os
from rasa import run

if __name__ == "__main__":
    port = os.environ.get("PORT", 5005)  # Default to 5005 if PORT is not set
    run(port=port)
