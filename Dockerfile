FROM python:3.11-slim

WORKDIR /p_simple_shop

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY alembic.ini .

COPY /app app

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "4225"]
