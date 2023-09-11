# Python paho-mqtt

To install

```bash
pip3 install paho-mqtt
```

## To send (sender/client):

```python
import paho.mqtt.client as mqtt 
import time
import json

mqttBroker ="127.0.0.1" 
TOPIC = "TopicName"

def send(mqtt_client, leg, power):
    data = {"test": "test"}
    mqtt_client.publish(TOPIC, str(data))

client = mqtt.Client("ClientUniqueName")
client.connect(mqttBroker) 

send(client)
```

## To recieve (reciever):

```python
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

mqttBroker ="127.0.0.1"

client = mqtt.Client("AnotherClientUniqueName")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("TopicName")
client.on_message=on_message 

time.sleep(30)
client.loop_stop()
```
