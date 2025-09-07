FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "src.server:app", "--host","0.0.0.0", "--port","8080"]