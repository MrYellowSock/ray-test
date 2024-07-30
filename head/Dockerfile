from python:3.11.9-slim

WORKDIR /app

RUN pip install ray[all]==2.32.0 virtualenv fastapi smart_open boto3

CMD ray start --head --port=6379 --dashboard-host 0.0.0.0 --ray-client-server-port=10001 --dashboard-port=8265 && sleep infinity


