import pigpio
import time
from wheels import Wheels
left_servo_pin = 23
right_servo_pin = 24
pig = pigpio.pi()

wheels = Wheels(pig, left_servo_pin, right_servo_pin)

def forward():
    wheels.set_speeds(20,20)

def backward():
    wheels.set_speeds(-20, -20)

def left():
    wheels.set_speeds(-20, 20)

def right():
    wheels.set_speeds(20, -20)

def stop():
    wheels.set_speeds(0, 0)

def close():
    wheels.disable()
    quit()

while (True):
    inp = inp("wasd controls")
    if inp == 'w':
        forward()
    elif inp == 'a':
        forward()
    elif inp == 's':
        forward()
    elif inp == 'd':
        forward()
    elif inp == 'x':
        forward()
    elif inp == 'q':
        close()




