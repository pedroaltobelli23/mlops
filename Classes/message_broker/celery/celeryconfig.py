import os
from dotenv import load_dotenv

load_dotenv()

usr = os.getenv("RABBIT_USERNAME")
psw = os.getenv("RABBIT_PASSWORD")
broker_url = f"amqp://{usr}:{psw}@localhost:5672//"
task_serializer = "json"
accept_content = ["json"]
timezone = "UTC"
enable_utc = True