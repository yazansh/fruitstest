# Getting Started with the Project 🚀
## Prerequisites
Ensure you have the following tools installed on your system:

- Docker (version 20.10 or later)
- Docker Compose (version 1.29 or later) 
- Git


## Project Setup Instructions
Follow these steps to get the project up and running:

### step 1: Create the docker-compose.yml file in the root directory of the project
```yml

services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: parcelsDB
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: Fruits.123
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7
    restart: always
    ports:
      - "6379:6379"

  web:
    build: ./fruitstest
    command: >
      sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - ./fruitstest:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis

  celery:
    build: ./fruitstest
    command: celery -A fruitstest worker --loglevel=INFO
    volumes:
      - ./fruitstest:/code
    user: celery
    depends_on:
      - db
      - redis

  celery-beat:
    build: ./fruitstest
    command: celery -A fruitstest beat --loglevel=INFO
    volumes:
      - ./fruitstest:/code
    depends_on:
      - db
      - redis

volumes:
  postgres_data:
```

### Step 2: Build and Run Docker Containers
Run the following command to build and start the containers:

```bash
docker-compose up --build
```
