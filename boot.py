# from machine import Pin
import machine
import time
import mfrc522
import esp
from umqttsimple import MQTTClient
import ubinascii
import micropython
import network

esp.osdebug(None)

import gc
gc.collect()

led = Pin(2, Pin.OUT)
card_reader = mfrc522.MFRC522(0, 2, 4, 5, 14)

ssid = 'FabLabSaar'
password = 'FabLabSaar'
mqtt_server = 'mqtt'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
#topic_sub = b'notification'
topic_pub = b'WerDa'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())