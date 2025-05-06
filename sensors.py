import csv
import random
from datetime import datetime

def simulate_sensor_data(file_path="data/sensor_data.csv", num_rows=100):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "temperature", "humidity", "co2", "energy"])
        for _ in range(num_rows):
            writer.writerow([
                datetime.now().isoformat(),
                round(random.uniform(18, 28), 2),
                round(random.uniform(30, 60), 2),
                random.randint(400, 1200),
                round(random.uniform(100, 500), 2)
            ])