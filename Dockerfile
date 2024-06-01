FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime AS base

# Install system dependencies
RUN apt update && \
    apt install -y build-essential

# Upgrade pip, setuptools, and wheel
RUN pip install -U pip setuptools wheel

# Install so-vits-svc-fork
RUN pip install -U so-vits-svc-fork

# Set working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run the FastAPI app using Uvicorn server
CMD ["python", "app.py"]
