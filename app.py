from sensors import simulate_sensor_data
from analysis import load_data, analyze
from dashboard import create_dashboard
from iot import adjust_thermostat, control_lights
from security import encrypt_data, decrypt_data

simulate_sensor_data("data/sensor_data.csv")
data = load_data("data/sensor_data.csv")
alerts = analyze(data)

# Test IoT and Encryption
adjust_thermostat(22)
control_lights(True)
encrypted = encrypt_data(b"Sample building data")
decrypted = decrypt_data(encrypted)
print(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")

app = create_dashboard(data, alerts)
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)