#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
import time
from motors import (
    run_forwards,
    turn_left,
    turn_right,
    brake,
    sneaking_up
)


ev3 = EV3Brick()

motor_A = Motor(Port.A)
motor_B = Motor(Port.B)
motor_C = Motor(Port.C)
motor_D = Motor(Port.D)

sensor_1 = UltrasonicSensor(Port.S1)
sensor_2 = UltrasonicSensor(Port.S2)
sensor_3 = UltrasonicSensor(Port.S3)

ev3.speaker.beep(frequency=1000)

time_m = 700

while True:
    motor_C.run_time(speed=500, time=time_m)
    motor_D.run_time(speed=500, time=time_m)
    time.sleep(1000)
    motor_A.run_time(speed=500, time=time_m)
    motor_B.run_time(speed=500, time=time_m)

# while True:
    # brake()

    # distance = 500
    # velocidad = -1000

    # while sensor_3.distance() < distance:   
    #     ev3.speaker.beep(frequency=250)
    #     run_forwards()

    # while sensor_1.distance() < distance:
    #     ev3.speaker.beep(frequency=200)
    #     turn_left()

    # while sensor_2.distance() < distance:
    #     ev3.speaker.beep(frequency=300)
    #     turn_right()
    
    # sneaking_up()