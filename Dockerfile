# Dockerfile
FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get -y install gcc libpq-dev

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]