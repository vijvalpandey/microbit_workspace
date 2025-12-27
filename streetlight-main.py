# Add your Python code here. E.g.
from microbit import *
red = pin2
green = pin1
blue = pin0

def rgb(r,g,b):
    red.write_analog(r)
    green.write_analog(g)
    blue.write_analog(b)

while True:
    motion_sensor = pin8.read_digital()
    display.show(motion_sensor)
    if motion_sensor == 1:
        rgb(1023,1023,1023)
    else:
        rgb(0,0,0)
    sleep(200)