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
RUN npm install -g back4app-cli

# Create a non-root user and switch to it
RUN useradd -ms /bin/bash appuser
USER appuser

# Expose the port your app runs on
EXPOSE   6969

# Define environment variables
ENV TOKEN="secret_wI9CKXWopeJQf8yTqDSLDU9EU8scbHwEw168a64zCSe"
ENV ROOT_UUID="803e81098952428bb8fd30cf5c0fbd99"
ENV ACCOUNT_KEY="tmK2z3J3D0QTMvSPR5kH6lkvzRKsTxmET0RsSZxa"
ENV APP_ID="VjljzeX4SAvbflidjbQB8TTM7R221pvlyat6IkkE"

# Define the command to run your application
CMD ["python", "app.py"]
