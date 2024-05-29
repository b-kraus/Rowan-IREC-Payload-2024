#Daisy chain w/ ADXL, BME MQ yet

import time
import board
import busio
import sys
import adafruit_adxl34x
import adafruit_bme680

i2c = board.I2C()


while True:
    
    accelerometer = adafruit_adxl34x.ADXL343(i2c)
    print("%f %f %f" % accelerometer.acceleration)
    time.sleep(0.2)
 
    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
    bme680.sea_level_pressure = 1013.25
    temperature_offset = -5
    print("\nTemperature: %0.1f C" % (bme680.temperature + temperature_offset))
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.relative_humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)
    time.sleep(.3)

