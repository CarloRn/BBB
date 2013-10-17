#!/usr/bin/env python

import signal
import sys
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time
import thread

## Global var temp_c
temp_c = 0

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

## Display the temperature on the 7seg 4dig display  
def display_temp()
  dtemp = temp_c * 10
  d4 = dtemp % 10
  d3 = int((dtemp / 10)) % 10
  d2 = int((dtemp / 100)) % 10
  d1 = int((dtemp / 1000)) % 10
   
  while True:
    if (d1 != 0):
      display_digit (d1, 1)
    time.sleep(0.2)
    if (d2 != 0 or  (d1 != 0 and d2 == 0) ):
      display_digit (d2, 2)
    time.sleep(0.2)
    display_digit (d3, 3)
    time.sleep(0.2)
    display_digit (d4, 4)
    time.sleep(0.2)
  
## Display the digit  
def display_digit(digit, pos)  
  GPIO.output(segment_a, GPIO.LOW)
  GPIO.output(segment_b, GPIO.LOW)
  GPIO.output(segment_c, GPIO.LOW)
  GPIO.output(segment_d, GPIO.LOW)
  GPIO.output(segment_e, GPIO.LOW)
  GPIO.output(segment_f, GPIO.LOW)
  GPIO.output(segment_dp, GPIO.LOW)
  GPIO.output(digit1_pin, GPIO.LOW)
  GPIO.output(digit2_pin, GPIO.LOW)
  GPIO.output(digit3_pin, GPIO.LOW)
  GPIO.output(digit4_pin, GPIO.LOW)  

  if pos == 1:
    GPIO.output(digit1_pin, GPIO.HIGH)
  elif pos == 2:
    GPIO.output(digit2_pin, GPIO.HIGH)
  elif pos == 3:
    GPIO.output(digit3_pin, GPIO.HIGH)
    GPIO.output(segment_dp, GPIO.HIGH)
  elif pos == 4:
    GPIO.output(digit4_pin, GPIO.HIGH)
  else:
    print 'Fatal error!!'
    sys.exit(1)	
  
  if digit == 0:
    GPIO.output(segment_a, GPIO.HIGH)
    GPIO.output(segment_b, GPIO.HIGH)
    GPIO.output(segment_c, GPIO.HIGH)
    GPIO.output(segment_d, GPIO.HIGH)
    GPIO.output(segment_e, GPIO.HIGH)
    GPIO.output(segment_f, GPIO.HIGH)
  elif digit == 1:
    GPIO.output(segment_b, GPIO.HIGH)
    GPIO.output(segment_c, GPIO.HIGH)
  elif digit == 2:
    GPIO.output(segment_a, GPIO.HIGH)
    GPIO.output(segment_b, GPIO.HIGH)
    GPIO.output(segment_d, GPIO.HIGH)
    GPIO.output(segment_e, GPIO.HIGH)
    GPIO.output(segment_g, GPIO.HIGH)
  elif digit == 3:
    GPIO.output(segment_a, GPIO.HIGH)
    GPIO.output(segment_b, GPIO.HIGH)
    GPIO.output(segment_c, GPIO.HIGH)
    GPIO.output(segment_d, GPIO.HIGH)
    GPIO.output(segment_g, GPIO.HIGH)	
  elif digit == 4:
    GPIO.output(segment_b, GPIO.HIGH)
    GPIO.output(segment_c, GPIO.HIGH)
    GPIO.output(segment_f, GPIO.HIGH)
    GPIO.output(segment_g, GPIO.HIGH)	
  elif digit == 5:
    GPIO.output(segment_a, GPIO.HIGH)
    GPIO.output(segment_c, GPIO.HIGH)
    GPIO.output(segment_d, GPIO.HIGH)
    GPIO.output(segment_f, GPIO.HIGH)
    GPIO.output(segment_g, GPIO.HIGH)	
  elif digit == 6:
    GPIO.output(segment_a, GPIO.HIGH)
    GPIO.output(segment_c, GPIO.HIGH)
    GPIO.output(segment_d, GPIO.HIGH)
    GPIO.output(segment_e, GPIO.HIGH)
    GPIO.output(segment_f, GPIO.HIGH)
    GPIO.output(segment_g, GPIO.HIGH)
  elif digit == 7:
    GPIO.output(segment_a, GPIO.HIGH)
    GPIO.output(segment_b, GPIO.HIGH)
    GPIO.output(segment_c, GPIO.HIGH)
  elif digit == 8:
    GPIO.output(segment_a, GPIO.HIGH)
    GPIO.output(segment_b, GPIO.HIGH)
    GPIO.output(segment_c, GPIO.HIGH)
    GPIO.output(segment_d, GPIO.HIGH)
    GPIO.output(segment_e, GPIO.HIGH)
    GPIO.output(segment_f, GPIO.HIGH)	
    GPIO.output(segment_g, GPIO.HIGH)	
  elif digit == 9:
    GPIO.output(segment_a, GPIO.HIGH)
    GPIO.output(segment_b, GPIO.HIGH)
    GPIO.output(segment_c, GPIO.HIGH)
    GPIO.output(segment_d, GPIO.HIGH)
    GPIO.output(segment_f, GPIO.HIGH)
    GPIO.output(segment_g, GPIO.HIGH)	
  else:
    print 'Fatal error!!'
    sys.exit(1)	




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

thread.start_new_thread( display_temp, ( ) )

while True:
  try:
    read_temp()
    time.sleep(2)
   
  except KeyboardInterrupt:
    reset_pins()
    sys.exit()	  
  except:
    print "Error: unable to start thread"
    reset_pins()
    sys.exit()

