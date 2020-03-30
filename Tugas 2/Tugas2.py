#!/usr/bin/env python
# encoding: utf-8

import time

try:
    import importlib.util
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    # handle failed import
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)
print("Led 1 must be on")
GPIO.output(24, GPIO.HIGH)
print("Led 2 must be on")
GPIO.output(25, GPIO.HIGH)
print("Led 3 must be on")
time.sleep(1)
print("Led 1 must be off")
GPIO.output(18, GPIO.LOW)
print("Led 2 must be off")
GPIO.output(24, GPIO.LOW)
print("Led 3 must be off")
GPIO.output(25, GPIO.LOW)
GPIO.cleanup()