# pip install paho-mqtt
############## Pub ####################
import paho.mqtt.client as mqtt

# *********************************************************************
# MQTT Config

MQTT_SERVER = "192.168.0.211"  
MQTT_PORT = 1883  
MQTT_ALIVE = 60  
MQTT_TOPIC1 = "myName/test" 

# *********************************************************************

mqtt_client = mqtt.Client()  
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
mqtt_client.loop_start()

import time
import json

myTime = time.asctime( time.localtime(time.time()) )
payload = {"time": myTime}

# The retain flag is used to Let other side to get back the result once connect
# mqtt_client.publish(topic=MQTT_TOPIC1, payload=json.dumps(payload), qos=1, retain=False)
mqtt_client.publish(topic=MQTT_TOPIC1, payload=json.dumps(payload), qos=2)


############## Sub  ####################

import paho.mqtt.client as mqtt

# *********************************************************************
# MQTT Config

MQTT_SERVER = "192.168.0.211"  
MQTT_PORT = 1883  
MQTT_ALIVE = 60  
MQTT_TOPIC1 = "myName/test" 

# *********************************************************************

mqtt_client = mqtt.Client()  
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)

# A way to receive

mqtt_client.subscribe(MQTT_TOPIC1, qos=2)

def on_message(client, userdata, message):
    print("Message Recieved: "+message.payload.decode())
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

mqtt_client.on_message = on_message

mqtt_client.loop_start()
