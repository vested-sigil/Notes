# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app.py file into the container at /app
COPY app.py .

# Copy the rest of the current directory contents into the container at /a
# Install any needed dependencies specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variables
ENV TOKEN="secret_wI9CKXWopeJQf8yTqDSLDU9EU8scbHwEw168a64zCSe"
ENV rootuuid="803e81098952428bb8fd30cf5c0fbd99"

# Define the command to run your application
CMD ["python", "app.py"]
