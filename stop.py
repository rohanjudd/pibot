import pigpio

pig = pigpio.pi()

pig.set_servo_pulsewidth(23, 0)
pig.set_servo_pulsewidth(24, 0)
