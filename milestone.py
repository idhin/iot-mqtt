import paho.mqtt.client as mqtt
import time
import json
import pandas as pd
import numpy
import random
from collections import deque
from datetime import datetime


# MQTT Details
broker_address = '192.168.1.5'
client_id = '1301188611'
sub_topic_accx = 'AccX'
pub_topic_accx = 'AccX'
sub_topic_accy = 'AccY'
pub_topic_accy = 'AccY'
sub_topic_accz = 'AccZ'
pub_topic_accz = 'AccZ'
sub_topic_gyrx = 'GyrX'
pub_topic_gyrx = 'GyrX'
sub_topic_gyry = 'GyrY'
pub_topic_gyry = 'GyrY'
sub_topic_gyrz = 'GyrZ'
pub_topic_gyrz = 'GyrZ'

try:
    # pandas reas csv file
    df = pd.read_csv('dataRiset.csv')
    print(df)
except:
    timest = datetime.now().strftime('%H:%M:%S.%f')[:-3]
    print ('error reading csv file, creating dataframe')
    df_create = pd.DataFrame([[timest, "0", "0", "0", "0", "0", "0" ]],
                             columns=['time', 'accx', 'accy', 'accz', 'gyrx', 'gyry', 'gyrz'])
    df_create.to_csv('dataRiset.csv', mode='a',index=None, header=True)


accx='0'
accy='0'
accz='0'
gyrx='0'
gyry='0'
gyrz='0'
# Callback function on message receive
def on_message(client, userdata, message):
    if message.topic == sub_topic_accx:
        global accx
        accx=(str(message.payload.decode("utf-8")))
    if message.topic == sub_topic_accy:
        global accy
        accy=(str(message.payload.decode("utf-8")))
    if message.topic == sub_topic_accz:
        global accz
        accz=(str(message.payload.decode("utf-8")))
    if message.topic == sub_topic_gyrx:
        global gyrx
        gyrx=(str(message.payload.decode("utf-8")))
    if message.topic == sub_topic_gyry:
        global gyry
        gyry=(str(message.payload.decode("utf-8")))
    if message.topic == sub_topic_gyrz:
        global gyrz
        gyrz = (str(message.payload.decode("utf-8")))
    timest = datetime.now().strftime('%H:%M:%S.%f')[:-3]
    data = [timest,accx,accy,accz,gyrx,gyry,gyrz]
    print (data)
    df2 = pd.DataFrame([data])
    df2.to_csv('dataRiset.csv', mode='a',index=None, header=False)
    print ('message topic=', message.topic)
    print ('message qos=', message.qos)
    print ('message retain flag=', message.retain)


# callback function on log
def on_log(client, userdata, level,buf):
       print("log: ", buf)

#MQTT init
print("Initalizing MQTT Client instance: " + client_id)
client =  mqtt.Client(client_id)

# Bind function to callback
client.on_message = on_message
client.on_log = on_log

#Connect to broker
print("connecting to broker: " + broker_address)
client.connect(broker_address)

try:
    client.loop_start()
    print("subscribing to topic " + sub_topic_accx)
    client.subscribe(sub_topic_accx)
    print("subscribing to topic " + sub_topic_accy)
    client.subscribe(sub_topic_accy)
    print("subscribing to topic " + sub_topic_accz)
    client.subscribe(sub_topic_accz)
    print("subscribing to topic " + sub_topic_gyrx)
    client.subscribe(sub_topic_gyrx)
    print("subscribing to topic " + sub_topic_gyry)
    client.subscribe(sub_topic_gyry)
    print("subscribing to topic " + sub_topic_gyrz)
    client.subscribe(sub_topic_gyrz)
    while True:
        print("waiting")
        time.sleep(1000)
except:

    print ('error')
    client.loop_stop()