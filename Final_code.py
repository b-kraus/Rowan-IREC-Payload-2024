#Daisy chain w/ ADXL, BME MQ yet

import time
import board
import busio
import sys
import adafruit_adxl34x
import adafruit_bme680
import AltitudeGraph
import GasGraph
import HumidityGraph
import PressureGraph
import TemperatureGraph



i2c = board.I2C()
create_altitude_graph()
create_gas_graph()
create_humidity_graph()
create_pressure_graph()
create_temperature_graph()

while True:
    f = open("accceleration.csv", newline = "")
    rc = csv.writer(f)
    accelerometer = adafruit_adxl34x.ADXL343(i2c)
    rc.writerow(["%f %f %f" % accelerometer.acceleration])
    time.sleep(0.2)

    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
    bme680.sea_level_pressure = 1013.25
    temperature_offset = -5
    f = open("Temperature.csv", newline = "")
    rc = csv.writer(f)
    rc.writerow(["\nTemperature: %0.1f C" % (bme680.temperature + temperature_offset)])
    f = open("Gas.csv", newline = "")
    rc = csv.writer(f)
    rc.writerow(["Gas: %d ohm" % bme680.gas])
    f = open("Humidity.csv", newline = "")
    rc = csv.writer(f)
    rc.writerow([("Humidity: %0.1f %%" % bme680.relative_humidity])
    f = open("Pressure.csv", newline = "")
    rc = csv.writer(f)
    rc.writerow(["Pressure: %0.3f hPa" % bme680.pressure])
    f = open("Altitude.csv", newline = "")
    rc = csv.writer(f)
    rc.writerow(["Altitude = %0.2f meters" % bme680.altitude])
    time.sleep(.3)

    altitudegraphs()
    gasgraphs()
    humiditygraphs()
    pressuregraphs()
    temperaturegraphs()
