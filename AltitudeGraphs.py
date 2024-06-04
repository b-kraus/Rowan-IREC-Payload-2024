import time
import board
import busio
import sys
import adafruit_bme680
import datetime as dt
import matplotlib.pyplot as plt

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

def create_altitude_graph(): 
  fig = plt.figure()
  ax = fig.add_subplot(1,1,1)
  xs = []
  ys = []

def altitudegraphs():
  xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
  ys.append(bme680.altitude)
   
def draw_altitude_graphs():
  ax.plot(xs, ys)
  plt.xticks(rotation=45, ha='right')
  plt.subplots_adjust(bottom=0.30)
  plt.title('Altitude over time over Time')
  plt.ylabel('Altitude (meters)')
  plt.savefig('altitude.png', dpi = 300, bbox_inches='tight')
