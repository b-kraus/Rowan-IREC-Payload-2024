import sqlite3

conn = sqlite3.connect("payload_sensors.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXIST ADXL345BCCZ (x,y,z)")
cursor.execute("CREATE TABLE IF NOT EXIST MQ4 (LPG, CO)")
cursor.execute("CREATE TABLE IF NOT EXIST BME680 (Temperature, Gas, Humidity, Pressure, Altitude)")
cursor.execute("CREATE TABLE IF NOT EXIST AM2320 (Temperature, Humidity)")

