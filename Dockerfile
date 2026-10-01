FROM docker.io/library/python:3.11-slim

WORKDIR /app

COPY persistent_auditor.py .

ENV DATA_PATH=/data
VOLUME ["/data"]
CMD ["python", "persistent_auditor.py"]
