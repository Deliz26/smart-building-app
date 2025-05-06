import pandas as pd

def load_data(path="data/sensor_data.csv"):
    return pd.read_csv(path)

def analyze(data):
    alerts = []
    if data['temperature'].mean() > 25:
        alerts.append("⚠️ High average temperature.")
    if data['co2'].max() > 1000:
        alerts.append("⚠️ CO₂ levels are too high.")
    if data['energy'].mean() > 400:
        alerts.append("⚠️ High average energy consumption.")
    return alerts