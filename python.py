import RPi.GPIO as GPIO
import 
import board
import busio
from adafruit_adxl345 import ADXL345
import serial

#ultra sonic sensor#
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
def measure_distance():
    GPIO.output(17, True)
    time.sleep(0.00001)
    GPIO.output(17, False)
    start_time = time.time()
    while GPIO.input(27) == 0:
        start_time = time.time()

    stop_time = time.time()
    while GPIO.input(27) == 1:
        stop_time = time.time()
    distance = (stop_time - start_time) * 34300 / 2

    return distance
try:
    while True:
        distance = measure_distance()
        print("Distance: {:.2f} cm".format(distance))
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

#accelrometer#
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = ADXL345(i2c)
while True:
    x, y, z = accelerometer.acceleration
    print("X: {:.2f}  Y: {:.2f}  Z: {:.2f}".format(x, y, z))

#gsp module"
ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5)
while True:
    data = ser.readline().decode()
    if data.startswith("$GPRMC"):
        gprmc = data.split(",")
        if gprmc[2] == 'A':
            print("Latitude: {} {}".format(gprmc[3], gprmc[4]))
            print("Longitude: {} {}".format(gprmc[5], gprmc[6]))
