from python:3.11.9-slim

RUN pip install ray[all]==2.32.0 virtualenv

WORKDIR /app
COPY . /app

CMD ["sh", "start.sh"]


