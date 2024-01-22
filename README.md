# Stock-Trading-API
##### Docker Compose for Django, Celery, Redis, and Postgres
This repository contains the implementation of a stock trading system with various endpoints for user registration, stock data management, transaction handling, and more. The system is designed to use Redis for caching and Celery for asynchronous task processing.

### Setup Guide
Follow the steps below to set up the stock trading system:

#### Clone the Repository:

```
git@github.com:HafizUsmanIftikhar/Stock-Trading-API.git
cd Stock-Trading-API
```
#### Create Virtual Environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

```
#### Install Dependencies:

```
pip install -r requirements.txt

```

#### Run Migrations:
```
python manage.py makemigrations
python manage.py migrate

```
#### Run Redis server
```
redis-server
```

#### Run Celery Worker:
```
celery -A DjangoProject worker -l INFO

```

#### Run Django Development Server:

```
python manage.py runserver
```

#### Access Swagger Documentation:

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


#### Monitor Celery Tasks with Flower:
```
celery -A DjangoProject flower
```

## For Docker Setup

#### Build docker

```
sudo docker-compose build
```

#### Start docker

```
sudo docker-compose up
```

#### Build and run in detached mode

```
sudo docker-compose up --build -d
```

### Stop docker-compose

```
sudo docker-compose down
```
