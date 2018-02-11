IN_CENTRE = 0
IN_MIN = -127
IN_MAX = 127

OUT_CENTRE = 1500
OUT_MIN = 900
OUT_MAX = 2100

def speed_to_width(x):
    return (x - IN_MIN) * (OUT_MAX - OUT_MIN) / (IN_MAX - IN_MIN) + OUT_MIN;

class Servo_Motor:
    def __init__(self, pig, pin, invert):
        self.pig = pig
        self.pin = pin
        self.invert = invert

    def set_pulse_width(self, pw):
        self.pig.set_servo_pulsewidth(self.pin, pw)

    def stop(self):
        self.set_pulse_width(OUT_CENTRE)

    def enable(self):
        self.set_pulse_width(OUT_CENTRE)

    def disable(self):
        self.set_pulse_width(0)

    def set_speed(self, speed):
        if self.invert:
            speed = speed * -1
        pw = speed_to_width(speed)
        print("speed: {}  pw: {}".format(speed, pw))
        self.set_pulse_width(speed_to_width(speed))


