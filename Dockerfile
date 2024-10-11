FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "dev", "./api/run.py", "--host", "0.0.0.0"]
