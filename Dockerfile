FROM python:3-slim-buster

COPY webhook/receiver.py /opt/webhook/receiver.py

CMD ["python", "-u", "/opt/webhook/receiver.py"]