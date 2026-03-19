FROM python:3.11-slim  

WORKDIR /app
COPY . /app

ENV RUNNING_IN_DOCKER=1

RUN pip install awscli && \
    pip install -r requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt
CMD ["python3", "application.py"]