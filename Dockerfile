FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY frontend ./frontend
COPY start.sh .
RUN chmod +x start.sh

EXPOSE 8000
EXPOSE 8501

ENV OLLAMA_HOST=http://host.docker.internal:11434

CMD ["./start.sh"] 