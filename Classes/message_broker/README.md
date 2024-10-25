# Class 6 - Message Broker

It is necessary to install rabbit, celery and flower

## RabbitMQ

RabbitMQ is a popular open-source message broker that simplifies messaging between distributed systems via AMQP (Advanced Message Queuing Protocol) and other protocols in a scalable and reliable manner.

We can implement the producer-consumer model with a queue

1. Inside the folder [rabbitMQ](./rabbitMQ/) start RabbitMQ by using:

```Bash
docker compose build
docker compose up
```

2. Go to http://localhost:15672/ to access the RabbitMQ Web admin

3. Send messages to Queue:

```Bash
python producer.py
```

This code also produce a queue called chitchat

4. Consume messages from queue

```Bash
python consumer.py
```

Will use the chitchat queue as well


## Celery

Celery uses a messaging broker, such as RabbitMQ or Redis, to facilitate communication between the client that initiates the task and the worker that executes it. This system allows for high availability and horizontal scaling, making it possible to distribute work efficiently across different threads or machines.

1. With the docker running, and inside the [celery](./celery/), run:

```Bash
celery -A my_ml_app worker
```

2. Run the ["use_ml_app.py"](./celery/use_ml_app.py) to send several messages:

```Bash
python use_ml_app.py
```

3. Initialize celery using Flower with:

```Bash
celery -A my_ml_app flower
```

4. Access http://0.0.0.0:5555 and browse the available options in the menu.

5. Initialize celery with a limit of up to 10 workers (horizontal scalling):

```Bash
celery -A my_ml_app worker --autoscale=10,2
```


### .env file format:

```Bash
RABBIT_USERNAME=""
RABBIT_PASSWORD=""
```