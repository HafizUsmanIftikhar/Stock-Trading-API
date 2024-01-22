# Stock-Trading-API

This repository contains the implementation of a stock trading system with various endpoints for user registration, stock data management, transaction handling, and more. The system is designed to use Redis for caching and Celery for asynchronous task processing.

---

## Features 🚀

- **Django** web application framework
- **Django-Rest-Framework** RESTful API Development Framework
- **PostgreSQL** database
- **Redis** in-memory data structure store
- **Celery** worker and beat services for running background tasks asynchronously
- **Swagger** API Documentation and Testing
- **Docker** Containerization and Deployment Tool
  

## Requirements 📋

- Docker & Docker Compose - [Install and Use Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
- Python 3.10 or higher
- Make (optional for shortcuts)

---

### Table of Contents
    Data Models
    API Endpoints
    Setup Guide
    Assumptions

### Data Models
#### Users

   - 'user_id': Unique identifier for each user.
   - 'username': User's username.
   - 'balance': User's current balance.

#### StockData

   - 'ticker': Stock ticker symbol.
   -  'open_price': Opening stock price.
   -  'close_price': Closing stock price.
   -  'high': Highest stock price.
   -  'volume': Stock trading volume.
   -  'timestamp': Timestamp of stock data.
     

#### Transactions

   - 'transaction_id': Unique identifier for each transaction.
   - 'user_id': Foreign key referencing the Users table.
   - 'ticker': Stock ticker symbol.
   - 'transaction_type': Type of transaction (buy/sell).
   - 'transaction_volume': Volume of the transaction.
   - 'transaction_price': Price of the transaction.
   - 'timestamp': Timestamp of the transaction.

---


## Getting Started 🏁

### Development Prerequisites

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
You can now access the application at http://localhost:8000. The development environment allows for immediate reflection of code changes.


#### Access Swagger Documentation:

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


#### Monitor Celery Tasks with Flower:
```
celery -A DjangoProject flower
```
Visit [http://localhost:5555/](http://localhost:5555/) to monitor Celery tasks using Flower.

---


## For Docker Setup ⚙️

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

## Assumptions
- The system assumes a PostgreSQL database for storing user data, stock data, and transactions.
- Redis is used for caching user data and stock data to reduce database load.
- Celery is employed for handling asynchronous tasks, especially for processing transactions.
- Swagger documentation is available for easy exploration of the API endpoints.
- Flower is used for monitoring Celery tasks and their states

Feel free to modify the setup based on your specific requirements


