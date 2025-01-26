import pymongo
import paho.mqtt.client as mqtt
from datetime import datetime, timezone

# MongoDB configuration
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["smart_agriculture"]
collection = db["paddy"]

# MQTT configuration
mqtt_broker_address = "34.16.126.118"  # Replace with your MQTT broker IP
mqtt_topic = "smart_agriculture"

# Define the callback function for connection
def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print("Successfully connected to MQTT broker")
        client.subscribe(mqtt_topic)
    else:
        print(f"Failed to connect, return code {reason_code}")

# Define the callback function for ingesting data into MongoDB
def on_message(client, userdata, message):
    try:
        payload = message.payload.decode("utf-8")
        print(f"Received message: {payload}")

        # Add a UTC timestamp to the data
        timestamp = datetime.now(timezone.utc)
        datetime_obj = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        # Process the payload and insert it into MongoDB
        document = {
            "timestamp": datetime_obj,
            "data": payload  # Assuming payload is in JSON format
        }
        collection.insert_one(document)
        print("Data ingested into MongoDB successfully")

    except Exception as e:
        print(f"Error processing message: {e}")

# Create a MQTT client instance
client = mqtt.Client()

# Attach the callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
try:
    client.connect(mqtt_broker_address, 1883, 60)
    print("Connected to MQTT broker")
except Exception as e:
    print(f"Error connecting to MQTT broker: {e}")

# Start the MQTT loop
client.loop_forever()
