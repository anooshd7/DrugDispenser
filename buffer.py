from gpiozero import AngularServo
from time import sleep

def rotat():

    servo1 = AngularServo(24,min_pulse_width=0.0006, max_pulse_width=0.0023)
    servo2 = AngularServo(18,min_pulse_width=0.0006, max_pulse_width=0.0023)


    #servo1.angle = 90
    servo2.angle = 90
    sleep(2)
    servo2.angle = 0


rotat()
