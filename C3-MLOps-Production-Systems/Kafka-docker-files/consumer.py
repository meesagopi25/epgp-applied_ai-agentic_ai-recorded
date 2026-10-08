import json
from kafka import KafkaConsumer

# Initialize Consumer
consumer = KafkaConsumer(
    'weather_updates',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Monitoring weather for heatwaves...")

for message in consumer:
    report = message.value
    city = report['city']
    temp = report['temp']
    
    if temp > 35.0:
        print(f"🔥 ALERT: Heatwave in {city}! Current Temp: {temp}°C")
    else:
        print(f"Normal: {city} is at {temp}°C")