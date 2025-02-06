FROM python:3.11.1

WORKDIR /app

COPY ../backend-service .

# Installing dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Start the application
CMD ["python", "src/start_api.py"]