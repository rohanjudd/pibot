import pigpio
import time
from wheels import Wheels
left_servo_pin = 23
right_servo_pin = 24
pig = pigpio.pi()

wheels = Wheels(pig, left_servo_pin, right_servo_pin)

s = 22

def forward():
    set_speeds(s,s)

def backward():
    set_speeds(-s, -s)

def left():
    set_speeds(0, s)

def right():
    set_speeds(s, 0)

def stop():
    set_speeds(0, 0)

def set_speeds(l, r):
    print("{} {}".format(l,r))
    wheels.set_speeds(l,r)

def close():
    wheels.disable()
    quit()

while (True):
    inp = input("wasd controls: ")
    if inp == 'w':
        forward()
    elif inp == 'a':
        left()
    elif inp == 's':
        backward()
    elif inp == 'd':
        right()
    elif inp == 'x':
        stop()
    elif inp == 'q':
        close()




