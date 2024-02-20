# Use an official Python runtime as a base image
FROM python:3.8-slim as builder

# Set the working directory in the container
WORKDIR /app

# Copy only necessary files for building
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs npm && \
    rm -rf /var/lib/apt/lists/*

# Install Back4App CLI
RUN curl -sL https://www.back4app.com/docs/platform/command-line-tool | bash

# Create a non-root user and switch to it
RUN useradd -ms /bin/bash appuser
USER appuser

# Expose the port your app runs on
EXPOSE   6969


# Define the command to run your application
CMD ["python", "app.py"]
