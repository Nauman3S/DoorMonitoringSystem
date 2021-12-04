
import random
import json
import base64
import time
from datetime import datetime
import paho.mqtt.client as mqtt

msgV=""
topicV=""

def on_connect(client, userdata, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    clientMosquitto.subscribe("settings/config")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global msgV,topicV
    #print(msg.topic+" "+str(msg.payload))
    topicV=str(msg.topic)
    msgV=str((msg.payload).decode('utf-8'))

    if(topicV=='settings/config'):
        doSomethins=0
    
        
        
    
clientID_prefix=""
for i in range(0,6):
    clientID_prefix=clientID_prefix + str(random.randint(0,99999))


clientMosquitto = mqtt.Client("C1"+clientID_prefix)
#client.on_connect = on_connect
clientMosquitto.on_message = on_message

clientMosquitto.connect("broker.hivemq.com", 1883, 60)#change with your Mosquttio server ip address
clientMosquitto.subscribe("settings/config")


clientMosquitto.loop_start()
oldtime = time.time()
def publishData(topic, data):
    global clientMosquitto
    clientMosquitto.publish(topic, data)
