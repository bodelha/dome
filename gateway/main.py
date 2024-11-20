import paho.mqtt.client as mqtt
import requests
import os
import json

# Configurações
broker = "mqtt-broker"
port = 1883
api_url = os.getenv("API_URL")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")
    
    try:
        received_data = json.loads(msg.payload.decode())
        
        data = {
            "time": received_data.get("timestamp"),
            "internalHumidity": received_data.get("umid_int"),
            "externalHumidity": received_data.get("umid_ext"),
            "internalTemperature": received_data.get("temp_int"),
            "externalTemperature": received_data.get("temp_ext"),
            "luminosity": received_data.get("luz"),
            "batteryLevel": received_data.get("bateria", None)
        }
        
        response = requests.post(api_url + "/endpoint", json=data)
        print(f"API Response: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error processing message: {e}")

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, port, 60)
client.subscribe("sensor/#")

client.loop_forever()
