# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy code into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Pathway ingestion
CMD ["python", "src/pathway_ingest.py"]
