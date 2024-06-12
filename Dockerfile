FROM python:3.10-slim

WORKDIR /code

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install --no-cache-dir --upgrade -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
