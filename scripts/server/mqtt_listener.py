'''
Author: Khai Fahmi
Description: Main File to always listen as an MQTT broker. Currently, this is just the skeleton for the configuration setup
'''

import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
PORT = 1883

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # set topic that wants to be listened
    # client.subscribe('covid/test')

def on_publish(client, userdata, result):
    print("data published")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # msg.payload = json.loads(msg.payload) # might cause trouble

    print('Message Topic: ', msg.topic)
    print('Payload: ', msg.payload)

# create MQTT client and attach methods
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, PORT, 60)
client.loop_forever()
