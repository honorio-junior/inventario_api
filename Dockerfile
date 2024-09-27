FROM python:3

WORKDIR /app

COPY api/ .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python database.py

CMD ["fastapi", "dev", "run.py", "--host", "0.0.0.0"]
