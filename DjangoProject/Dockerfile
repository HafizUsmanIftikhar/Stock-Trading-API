From python:3.10


RUN mkdir /app


# Set the working directory in the container
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


# Expose the port where your app runs (if applicable)
EXPOSE 8000


# Set the command to start Redis and Celery along with your Python app
CMD ["sh", "-c", "python manage.py runserver"]