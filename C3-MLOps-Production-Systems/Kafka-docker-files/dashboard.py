import json
import matplotlib.pyplot as plt
from kafka import KafkaConsumer
from collections import deque

# Setup Consumer
consumer = KafkaConsumer(
    'weather_updates',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Data structures to hold the last 20 readings for each city
history_length = 20
data_points = {
    "New York": deque([0]*history_length, maxlen=history_length),
    "London": deque([0]*history_length, maxlen=history_length),
    "Tokyo": deque([0]*history_length, maxlen=history_length),
    "Mysuru": deque([0]*history_length, maxlen=history_length),
    "Sydney": deque([0]*history_length, maxlen=history_length)
}

# Setup Plot
plt.ion() # Turn on interactive mode
fig, ax = plt.subplots(figsize=(10, 6))
lines = {}
for city in data_points.keys():
    lines[city], = ax.plot(range(history_length), data_points[city], label=city)

ax.set_ylim(0, 50)
ax.set_title("Real-Time Weather Monitoring (Kafka Stream)")
ax.set_xlabel("Recent Events")
ax.set_ylabel("Temperature (°C)")
ax.legend(loc='upper left')

print("Dashboard started. Waiting for data...")

try:
    for message in consumer:
        report = message.value
        city = report['city']
        temp = report['temp']

        if city in data_points:
            # Update the specific city's data
            data_points[city].append(temp)
            lines[city].set_ydata(data_points[city])
            
            # Refresh the plot
            plt.draw()
            plt.pause(0.01)
except KeyboardInterrupt:
    print("Dashboard stopped.")