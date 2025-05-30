# Use an official Python runtime as a parent image
FROM python:3.10

WORKDIR /app

# Install dependencies (including NLTK)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Download the NLTK punkt and punkt_tab tokenizers
RUN python -m nltk.downloader punkt punkt_tab

# Add service code
COPY app.py ./

EXPOSE 8001
CMD ["python", "app.py"]
