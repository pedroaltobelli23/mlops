import pika
import os
from dotenv import load_dotenv
import random
import json

def generate_random_json():
    jobs = ["entrepreneur", "technician", "blue-collar", "admin.", "management", "services", "retired", "self-employed"]
    marital_statuses = ["married", "single", "divorced"]
    educations = ["primary", "secondary", "tertiary"]
    housing_options = ["yes", "no"]

    json_obj = {
        "age": random.randint(18, 70),  # random age between 18 and 70
        "job": random.choice(jobs),
        "marital": random.choice(marital_statuses),
        "education": random.choice(educations),
        "balance": random.randint(0, 100000),  # random balance
        "housing": random.choice(housing_options),
        "duration": random.randint(50, 600),  # random call duration in seconds
        "campaign": random.randint(1, 10)  # random number of contacts in this campaign
    }
    
    return json.dumps(json_obj, indent=4)

load_dotenv()

# Configure credentials
credentials = pika.PlainCredentials(
    os.getenv("RABBIT_USERNAME"), os.getenv("RABBIT_PASSWORD")
)

# Create a connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", credentials=credentials, heartbeat=0)
)

channel = connection.channel()

# Create a queue named "chitchat"
channel.queue_declare(queue="chitchat", durable=True)

while True:
    msg = input("Type a message: ")
    to_send = None
    
    if msg == "exit":
        # Close connection
        connection.close()
        break
    else:
        to_send = generate_random_json()

    # Send a message to queue
    channel.basic_publish(
        exchange="",
        routing_key="chitchat",
        body=to_send,
    )