FROM python:3.8-slim-buster 

WORKDIR /app


# Copy entire project
COPY . /app

# Install your package
RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt



# Run Flask application
CMD ["python", "application.py"]


