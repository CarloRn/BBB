#!/usr/bin/env python

import signal
import sys
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

## Read temperature from LM35
def read_temp(): 
  reading = ADC.read(sensor_pin)
  millivolts = reading * 1800  # 1.8V reference = 1800 mV
  
  temp_c = (millivolts) / 10
  temp_f = (temp_c * 9/5) + 32
  
  if (temp_c <= TEMP_LIMIT):
    GPIO.output(led_green, GPIO.HIGH)
    GPIO.output(led_red, GPIO.LOW)
  else:
    GPIO.output(led_red, GPIO.HIGH)
    GPIO.output(led_green, GPIO.LOW)

  print('C=%.1f F=%.1f' % (temp_c, temp_f))

## Set to LOW the value of the output pins
def reset_pins():
  GPIO.output(led_red, GPIO.LOW)
  GPIO.output(led_green, GPIO.LOW)
  GPIO.output(digit1_pin, GPIO.LOW)
  GPIO.output(digit2_pin, GPIO.LOW)
  GPIO.output(digit3_pin, GPIO.LOW)
  GPIO.output(digit4_pin, GPIO.LOW)

## Set up the GPIO
def setup_GPIO():
  ADC.setup()
  GPIO.setup(led_green, GPIO.OUT)
  GPIO.setup(led_red, GPIO.OUT)
  GPIO.setup(digit1_pin, GPIO.OUT)
  GPIO.setup(digit2_pin, GPIO.OUT)
  GPIO.setup(digit3_pin, GPIO.OUT)
  GPIO.setup(digit4_pin, GPIO.OUT)

## main flow 
sensor_pin = 'P9_40'
led_green = 'P8_13'
led_red = 'P8_12'
digit1_pin = 'P8_19'
digit2_pin = 'P8_16'
digit3_pin = 'P8_18'
digit4_pin = 'P8_11'
segment_a = 'P8_22'
segment_b = 'P8_'
segment_c = 'P8_'
segment_d = 'P8_'
segment_e = 'P8_'
segment_f = 'P8_23'
segment_dp = 'P8_'
TEMP_LIMIT = 24


setup_GPIO()

while True:
  try:
    read_temp()
    GPIO.output(digit1_pin, GPIO.HIGH)
    GPIO.output(digit2_pin, GPIO.HIGH)
    GPIO.output(digit3_pin, GPIO.HIGH)
    GPIO.output(digit4_pin, GPIO.HIGH)
    time.sleep(2)

  except KeyboardInterrupt:
    reset_pins()
    sys.exit()	  

 


  
