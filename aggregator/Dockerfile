FROM python:3.10

# Set working directory
WORKDIR /app

# Copy app code and requirements
COPY app.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the correct port
EXPOSE 8000

# Run the app
CMD ["python", "app.py"]
