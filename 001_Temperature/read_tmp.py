import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time
 
sensor_pin = 'P9_40'
led_green = 'P9_13'
led_red = 'P9_11'
TEMP_LIMIT = 24

ADC.setup()
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)

while True:
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
  
  time.sleep(2)
