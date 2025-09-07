FROM python:3.11-slim

WORKDIR /app

# Add the app directory to the Python path
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all local files into the container's working directory
COPY . .

EXPOSE 8000

# Tell uvicorn to look for the 'app' object inside 'src.server'
CMD ["python", "-m", "uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]