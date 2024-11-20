import paho.mqtt.client as mqtt
import time
import requests
import os
import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Configurações
broker = "mqtt-broker"
port = 1883
api_url = os.getenv("API_URL")


def on_connect(client, userdata, flags, rc):
    logging.info(f"Connected to MQTT broker with result code {rc}")
    client.subscribe("sensor/#")

def on_message(client, userdata, msg):
    logging.info(f"Received message: {msg.payload.decode()} on topic {msg.topic}")
    
    try:
        received_data = json.loads(msg.payload.decode())
        
        data = {
            "time": int(time.time()),
            "internalHumidity": received_data.get("umid_int"),
            "externalHumidity": received_data.get("umid_ext"),
            "internalTemperature": received_data.get("temp_int"),
            "externalTemperature": received_data.get("temp_ext"),
            "luminosity": received_data.get("luz"),
            "batteryLevel": received_data.get("bateria", None)
        }
        
        response = requests.post(api_url + "/v1/measurements", json=data)
        logging.info(f"API Response: {response.status_code}, {response.text}")
    except Exception as e:
        logging.error(f"Error processing message: {e}")


if __name__ == "__main__":
    logging.info("o o aue ai o")
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect

    client.connect(broker, port, 60)
    client.subscribe("estufa.dados")

    client.loop_forever()
