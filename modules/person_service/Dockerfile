# Use Python 3.9 Alpine as base image
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache gcc g++ musl-dev linux-headers geos libc-dev postgresql-dev

# Copy the requirements.txt file from the service directory and install Python dependencies
COPY modules/person_service/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port 5000 for the service
EXPOSE 5000

# Copy the service directory into /app/person_service
COPY modules/person_service /app/modules/person_service

# Copy the shared directory into /app/shared
COPY modules/shared /app/modules/shared

# Set the context to the service directory
WORKDIR /app

# Run the Python application module
CMD ["python", "-m", "modules.person_service.app"]