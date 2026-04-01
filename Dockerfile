# Dockerfile for defining the environment for the application itself
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy your dependency list first (helps with build caching)
COPY requirements.txt .

# Install your Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your script files
COPY . .

# Run your script
CMD ["python", "main.py"]