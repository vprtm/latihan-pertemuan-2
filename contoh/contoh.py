#!/usr/bin/env python
# encoding: utf-8

import time
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    # handle failed import
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)
print("Led must be on")
time.sleep(1)
print("Led must be off")
GPIO.output(18, GPIO.LOW)
GPIO.cleanup()
