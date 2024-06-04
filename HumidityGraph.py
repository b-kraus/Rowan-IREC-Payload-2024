import time
import board
import busio
import sys
import adafruit_bme680
import datetime as dt
import matplotlib.pyplot as plt

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

def create_humidity_graph(): 
  fig = plt.figure()
  ax = fig.add_subplot(1,1,1)
  xs = []
  ys = []

def humiditygraphs():
  xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
  ys.append( bme680.relative_humidity)
   
def draw_humiditygraphs():
  ax.plot(xs, ys)
  plt.xticks(rotation=45, ha='right')
  plt.subplots_adjust(bottom=0.30)
  plt.title('Humidity over Time')
  plt.ylabel('Humidity d ohm')
  plt.savefig('humidity.png', dpi = 300, bbox_inches='tight')
