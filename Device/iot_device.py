import time
import random
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = "mqtt.eu.thingsboard.cloud"
ACCESS_TOKEN = "hJNEJ18xj9sYDJ1B9W3t"

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

while True:
    temp = round(random.uniform(0, 50), 2)
    humidity = round(random.uniform(40, 60), 2)
    moisture = round(random.uniform(250, 470), 2)

    payload = {
        "plant_id": random.randint(1,3),
        "temperature": temp,
        "humidity": humidity,
        "moisture": moisture
    }

    client.publish("v1/devices/me/telemetry", json.dumps(payload), 1)
    print("Sent:", payload)
    time.sleep(10)
