from picamera import PiCamera
from time import sleep
from bmp180 import BMP180
from machine import I2C, Pin                        
bus = I2C(1, baudrate=100000)           

bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325
try:
  while True:
    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude

    if  altitude == 2713:
      camera = PiCamera()
      camera.start_preview()
      camera.start_recording('/home/pi/Desktop/video.h264')
      sleep(1200)
      camera.stop_recording()
      camera.stop_preview()
      camera.close()
      break
finally: 
  bus.close()
  
