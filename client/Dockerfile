from python:3.11.9-slim

WORKDIR /app
RUN pip install ray[serve] ray[client]

COPY . .


CMD python3 client.py && sleep infinity
