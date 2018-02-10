CENTRE = 1500
MAX = 2100
MIN = 900

class Servo_Motor:
    def __init__(self, pig, pin, left):
        self.pig = pig
        self.pin = pin
        self.left = left

    def stop(self):
        self.pig.set_servo_pulsewidth(self.pin, CENTRE)

    def max_cw(self):
        self.pig.set_servo_pulsewidth(self.pin, MAX)

    def min_cw(self):
        self.pig.set_servo_pulsewidth(self.pin, MIN)

    def set_pw(self, pw):
        self.pig.set_servo_pulsewidth(self.pin, pw)

