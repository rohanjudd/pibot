from servo_motor import Servo_Motor

class Wheels:
    def __init__(self, pig, left_servo_pin, right_servo_pin):
        self.pig = pig
        self.left_servo = Servo_Motor(pig, left_servo_pin, False)
        self.right_servo = Servo_Motor(pig, right_servo_pin, True)

    def set_speeds(self, l, r):
        self.left_servo.set_speed(l)
        self.right_servo.set_speed(r)

    def enable(self):
        self.left_servo.enable()
        self.right_servo.enable()

    def disable(self):
        self.left_servo.disable()
        self.right_servo.disable()

    def stop(self):
        self.left_servo.stop()
        self.right_servo.stop()



