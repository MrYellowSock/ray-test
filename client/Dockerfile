from python:3.11.9-slim

WORKDIR /app
RUN pip install ray[serve] ray[client]==2.32.0

COPY . .


CMD python3 client.py && sleep infinity
