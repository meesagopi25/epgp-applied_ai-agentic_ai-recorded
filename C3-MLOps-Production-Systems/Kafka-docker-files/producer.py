import json
import time
import random
from kafka import KafkaProducer

# Initialize Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

cities = ["New York", "London", "Tokyo", "Mysuru", "Sydney"]

print("Simulation started. Press Ctrl+C to stop.")

try:
    while True:
        data = {
            "city": random.choice(cities),
            "temp": round(random.uniform(10.0, 45.0), 1),
            "timestamp": time.time()
        }
        producer.send('weather_updates', value=data)
        print(f"Sent: {data}")
        time.sleep(2)
except KeyboardInterrupt:
    producer.close()