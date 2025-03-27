# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies for Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code AND model/data files
COPY app.py .
COPY tfidf.pkl ./  # Explicitly copy IDF file
# If your IDF file is in a subdirectory:
# COPY data/idf_vector.pkl ./data/

# Alternative for multiple data files:
# COPY data/ ./data/

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the app with explicit host setting
CMD ["streamlit", "run", "--server.port=8501", "--server.address=0.0.0.0", "app.py"]