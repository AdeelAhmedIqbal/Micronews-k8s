# Use an official Python runtime as a parent image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy the application code and requirements file
COPY app.py .
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8002 for the frontend service
EXPOSE 8002

# Define the command to run the application
CMD ["python", "app.py"]
