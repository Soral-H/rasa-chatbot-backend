import os
from rasa import run

if __name__ == "__main__":
    # Set the Python version if needed (optional)
    os.environ["PYTHON_VERSION"] = "3.9.13"  # Set your Python version

    # Start the Rasa server with the specified options
    run(
        enable_api=True,  # Enable the API
        cors="*",         # Allow all origins for CORS
        port=5005         # Default port for Rasa server
    )
