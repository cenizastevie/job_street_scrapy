# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Scrapy project directory to the container
COPY . .

# # Run the tests
# RUN python -m unittest discover tests/

# # Set the default command to run the Scrapy spider
# CMD ["scrapy", "crawl", "myspider"]

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"