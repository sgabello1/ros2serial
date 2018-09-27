#!/usr/bin/env python

import serial
from xbee import XBee
from digi.xbee.devices import XBeeDevice

serial_port = serial.Serial('/dev/ttyUSB0', 9600)
xbee = XBee(serial_port)

while True:
    try:
        print xbee.wait_read_frame()
    except KeyboardInterrupt:
        break

serial_port.close()