# Use Python base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt
RUN pip install openpyxl

# port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "mlopstask4.py"]

