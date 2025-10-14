FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user and fix permissions
RUN groupadd -g 1000 app \
    && useradd --create-home --shell /bin/bash --uid 1000 --gid 1000 app \
    && mkdir -p /app \
    && chown -R app:app /app

# Switch to non-root user
USER app

EXPOSE 8080

CMD ["python", "server.py"]