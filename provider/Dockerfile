FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
# RUN python3 -m venv venv
RUN pip3 install -r requirements.txt


COPY provider.py .
COPY start.sh .

RUN chmod +x start.sh

ENTRYPOINT ["/bin/bash", "-c", "/app/start.sh"]
