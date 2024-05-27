#Daisy chain w/ ADXL, BME MQ yet

import time
import board
import busio
import sys
import adafruit_adxl34x
import adafruit_bme680


#ADXL
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
accelerometer.enable_freefall_detection(threshold=10, time=25)
accelerometer.enable_motion_detection(threshold=18)
accelerometer.enable_tap_detection(tap_count=1, threshold=20, duration=50, latency=20, window=255)

#BME
i2c = board.I2C()  # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
bme680.sea_level_pressure = 1013.25

time.sleep(1)
