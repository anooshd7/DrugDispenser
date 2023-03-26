from gpiozero import AngularServo
from time import sleep


def rotat(d1,d2):

    servo1 = AngularServo(18,min_pulse_width=0.0006, max_pulse_width=0.0023)
    servo2 = AngularServo(24,min_pulse_width=0.0006, max_pulse_width=0.0023)

    def l_servo(d1):
        
        serv_wait1 = 0
        
        if d1 == 0:
            serv_wait1 = 0

        if d1 == 1:
            serv_wait1 = 0.20

        if d1 == 2:
            serv_wait1 = 0.30

        if d1 == 3:
            serv_wait1 = 0.40

        if d1 == 4:
            serv_wait1 = 0.55

        if d1 == 5:
            serv_wait1 = 0.70
        
        
        servo1.angle = 0
        servo1.angle = 90
        
        sleep(serv_wait1)
        servo1.angle = 0
        
        return
    
    serv_wait1 = 0

    def r_servo(d2):
        
        serv_wait2 = 0
        
        if d2 == 0:
            serv_wait2 = 0

        if d2 == 1:
            serv_wait2 = 0.25

        if d2 == 2:
            serv_wait2 = 0.40

        if d2 == 3:
            serv_wait2 = 0.40

        if d2 == 4:
            serv_wait2 = 0.55

        if d2 == 5:
            serv_wait2 = 0.70
            
            
        servo2.angle = 0
        servo2.angle = 90
        
        sleep(serv_wait2)
        servo2.angle = 0
        
        return
    
    l_servo(d1)
    sleep(4)
    r_servo(d2)