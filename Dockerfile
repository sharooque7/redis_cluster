# Dockerfile
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY redis-cluster.py .

# Install the Redis library
RUN pip install redis

# Command to run the Python script
CMD ["python3", "redis-cluster.py"]
