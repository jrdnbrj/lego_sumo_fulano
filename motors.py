from pybricks.ev3devices import Motor
from pybricks.parameters import Port


motor_A = Motor(Port.A)
motor_B = Motor(Port.B)
motor_C = Motor(Port.C)
motor_D = Motor(Port.D)


def run_forwards():
    motor_A.run(-1000)
    motor_B.run(-1000)
    motor_C.run(-1000)
    motor_D.run(-1000)

def turn_left():
    motor_A.run(-1000)
    motor_B.run(-1000)
    motor_C.run(1000)
    motor_D.run(1000)

def turn_right():
    motor_A.run(1000)
    motor_B.run(1000)
    motor_C.run(-1000)
    motor_D.run(-1000)

def brake():
    motor_A.brake()
    motor_B.brake()
    motor_C.brake()
    motor_D.brake()


def sneaking_up():
    time = 1000
    motor_A.run_time(speed=-500, time=time)
    motor_B.run_time(speed=-500, time=time)
    motor_C.run_time(speed=500, time=time)
    motor_D.run_time(speed=500, time=time)

    motor_A.run_time(speed=500, time=time)
    motor_B.run_time(speed=500, time=time)
    motor_C.run_time(speed=-500, time=time)
    motor_D.run_time(speed=-500, time=time)