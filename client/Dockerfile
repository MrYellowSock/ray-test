from python:3.11.9-slim

WORKDIR /app
RUN pip install ray[all]==2.32.0 smart_open boto3

COPY . .


CMD python3 deploy_api_composite_app.py && sleep infinity
