# Use Rasa SDK image
FROM rasa/rasa:3.6.21

# Copy everything
COPY . /app

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for API
EXPOSE 5005

# Run Rasa server with API and CORS
CMD ["run", "--enable-api", "--cors", "*", "--model", "models"]
