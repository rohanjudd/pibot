import pigpio
import time
from servo_motor import Servo_Motor
servo_1_pin = 23
servo_2_pin = 24
pig = pigpio.pi()

servo_1 = Servo_Motor(pig, servo_1_pin, True)
servo_2 = Servo_Motor(pig, servo_2_pin, False)

while (True):
    pw = int(input("input pw"))
    servo_1.set_pw(pw)
    servo_2.set_pw(pw)


