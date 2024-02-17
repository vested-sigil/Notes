# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app.py file and other necessary files into the container at /app
COPY app.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js, npm, and additional utilities needed for the installation script
RUN apt-get update && \
    apt-get install -y nodejs npm curl && \
    rm -rf /var/lib/apt/lists/*

# Install Back4App CLI using the provided installer script
RUN curl https://raw.githubusercontent.com/back4app/parse-cli/back4app/installer.sh | /bin/bash

# Expose the port your app runs on
EXPOSE 6969

# Set environment variables
ENV TOKEN="secret_wI9CKXWopeJQf8yTqDSLDU9EU8scbHwEw168a64zCSe"
ENV ROOT_UUID="803e81098952428bb8fd30cf5c0fbd99"
ENV ACCOUNT_KEY="tmK2z3J3D0QTMvSPR5kH6lkvzRKsTxmET0RsSZxa"
ENV APP_ID="VjljzeX4SAvbflidjbQB8TTM7R221pvlyat6IkkE"

# Define the command to run your application
CMD ["python", "app.py"]
