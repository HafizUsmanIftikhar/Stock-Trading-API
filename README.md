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
- Django 4.2

---


## Data Models Overview
### 🤵 Users

   - 'user_id': Unique identifier for each user.
   - 'username': User's username.
   - 'balance': User's current balance.

### 📈  StockData

   - 'ticker': Stock ticker symbol.
   -  'open_price': Opening stock price.
   -  'close_price': Closing stock price.
   -  'high': Highest stock price.
   -  'volume': Stock trading volume.
   -  'timestamp': Timestamp of stock data.
     

### 🔄 Transactions

   - 'transaction_id': Unique identifier for each transaction.
   - 'user_id': Foreign key referencing the Users table.
   - 'ticker': Stock ticker symbol.
   - 'transaction_type': Type of transaction (buy/sell).
   - 'transaction_volume': Volume of the transaction.
   - 'transaction_price': Price of the transaction.
   - 'timestamp': Timestamp of the transaction.

---
## API Overview 📚
![Swagger Documentation](https://github.com/HafizUsmanIftikhar/Stock-Trading-API/assets/102325194/df66f3ac-f546-411e-b8e0-e55ad8502ed5)

![image](https://github.com/HafizUsmanIftikhar/Stock-Trading-API/assets/102325194/57ff1f17-7707-46dc-b9e0-20de619d8802)

![image](https://github.com/HafizUsmanIftikhar/Stock-Trading-API/assets/102325194/b32879a1-f126-40e9-b537-80cc0a2867c4)

![image](https://github.com/HafizUsmanIftikhar/Stock-Trading-API/assets/102325194/658d0fea-6b4b-4364-bfe8-1a228b81b125)

![image](https://github.com/HafizUsmanIftikhar/Stock-Trading-API/assets/102325194/f9f3f52e-5f5f-4ade-9252-02ed226afebe)
![image](https://github.com/HafizUsmanIftikhar/Stock-Trading-API/assets/102325194/e446774f-5e71-442f-b8f9-f726ec613a59)

![image](https://github.com/HafizUsmanIftikhar/Stock-Trading-API/assets/102325194/2a31f6ad-45a9-4f96-a93e-c99b91b02043)

![image](https://github.com/HafizUsmanIftikhar/Stock-Trading-API/assets/102325194/347372a8-6bdb-419c-839c-5faef028d755)

![image](https://github.com/HafizUsmanIftikhar/Stock-Trading-API/assets/102325194/78ce22e3-ea0b-4040-b241-92133b575540)

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
#### Run the Redis server
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
---

## Assumptions
- The system assumes a PostgreSQL database for storing user data, stock data, and transactions.
- Redis is used for caching user data and stock data to reduce database load.
- Celery is employed for handling asynchronous tasks, especially for processing transactions.
- Swagger documentation is available for easy exploration of the API endpoints.
- Flower is used for monitoring Celery tasks and their states

Feel free to modify the setup based on your specific requirements

---


