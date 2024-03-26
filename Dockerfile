# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt file into the container at /app
# Doing this separately allows Docker to cache the pip install layer
# when there are no changes to the requirements.txt file, speeding up builds
COPY requirements.txt /app/

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# After the pip install layer is cached, copy the rest of the application files
# Any change to the application source code will only invalidate the layers
# from this point forward
COPY . /app/

# Expose the Flask default port 5000
EXPOSE 5000

# Define default command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
