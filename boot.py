from machine import Pin
import time
import mfrc522

led = Pin(2, Pin.OUT)
card_reader = mfrc522.MFRC522(0, 2, 4, 5, 14)