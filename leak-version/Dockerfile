FROM python:3.7-stretch

RUN apt-get update -y

RUN pip install --no-cache-dir tensorflow==1.13.1 \
    && pip install --no-cache-dir memory-profiler \
    && pip install --no-cache-dir google-cloud-storage

COPY gcs-secret.json /var/secrets/google/gcs-secret.json
COPY leak_example.py leak_example.py


ENV GOOGLE_APPLICATION_CREDENTIALS=/var/secrets/google/gcs-secret.json

CMD python -m memory_profiler leak_example.py