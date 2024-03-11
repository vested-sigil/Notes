# Define the dependencies
# # Define build dependencies
FROM python:3.10-buster
# # Define runtime dependencies
# # Install the required packages
RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade --no-cache-update --disable-pip-extensions requirements.jpg
#
