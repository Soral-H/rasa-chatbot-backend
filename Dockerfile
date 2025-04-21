FROM python:3.9.13-slim

WORKDIR /app

COPY . /app

# Install Rasa and dependencies
RUN pip install rasa==3.6.21

EXPOSE 5005

CMD ["rasa", "run", "--enable-api", "--cors", "*", "--model", "models"]
