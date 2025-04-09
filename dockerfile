# Base image
FROM python:3.12-slim

# Create a group and user
# RUN groupadd -r containergroup && useradd -r -g containergroup containeruser

RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy requirements file
COPY config/requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set working directory
WORKDIR /app

# Copy the rest of the application code
COPY . /app

# Set environment variable
ENV PYTHONPATH="/app/"

ENV ENV="dev"

# Expose the desired port
EXPOSE 8040
EXPOSE 8501

# Use the entrypoint script to run migrations and start the app
CMD ["dotenv", "-f", "config/.env", "run", "--", "gunicorn", "api:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8045"]