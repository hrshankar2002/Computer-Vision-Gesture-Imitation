from matplotlib.pyplot import fignum_exists
import pyfirmata
from pyfirmata import Arduino, SERVO
from time import sleep

comport='COM4'
board=pyfirmata.Arduino(comport)
pin1=5
pin2=6
pin3=9
pin4=10
pin5=11

board.digital[pin1].mode=SERVO
board.digital[pin2].mode=SERVO
board.digital[pin3].mode=SERVO
board.digital[pin4].mode=SERVO
board.digital[pin5].mode=SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(angle)

def led(total,fingers):

    if total==0:
        rotateServo(pin1,180)
        rotateServo(pin2,180)
        rotateServo(pin3,180)
        rotateServo(pin4,180)
        rotateServo(pin5,180)

    elif total==1:
        if fingers[0]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,180)
            rotateServo(pin3,180)
            rotateServo(pin4,180)
            rotateServo(pin5,180)
        elif fingers[1]==1:
            rotateServo(pin2,0)
            rotateServo(pin1,180)
            rotateServo(pin3,180)
            rotateServo(pin4,180)
            rotateServo(pin5,180)
        elif fingers[2]==1:
            rotateServo(pin3,0)
            rotateServo(pin2,180)
            rotateServo(pin4,180)
            rotateServo(pin1,180)
            rotateServo(pin5,180)
        elif fingers[3]==1:
            rotateServo(pin4,0)
            rotateServo(pin2,180)
            rotateServo(pin3,180)
            rotateServo(pin1,180)
            rotateServo(pin5,180)
        elif fingers[4]==1:
            rotateServo(pin5,0)
            rotateServo(pin2,180)
            rotateServo(pin3,180)
            rotateServo(pin4,180)
            rotateServo(pin1,180)
    elif total==2:
        if fingers[0] and fingers[1]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,0)
            rotateServo(pin3,180)
            rotateServo(pin4,180)
            rotateServo(pin5,180)
        elif fingers[1] and fingers [2]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,0)
            rotateServo(pin3,0)
            rotateServo(pin4,180)
            rotateServo(pin5,180)
        elif fingers[2] and fingers[3]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,180)
            rotateServo(pin3,0)
            rotateServo(pin4,0)
            rotateServo(pin5,180)
        elif fingers[3] and fingers[4]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,180)
            rotateServo(pin3,180)
            rotateServo(pin4,0)
            rotateServo(pin5,0)
        elif fingers[0] and fingers[4]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,180)
            rotateServo(pin3,180)
            rotateServo(pin4,180)
            rotateServo(pin5,0)
        elif fingers[0] and fingers[2]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,180)
            rotateServo(pin3,0)
            rotateServo(pin4,180)
            rotateServo(pin5,180)
        elif fingers[1] and fingers[3]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,0)
            rotateServo(pin3,180)
            rotateServo(pin4,0)
            rotateServo(pin5,180)
        elif fingers[2] and fingers[4]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,180)
            rotateServo(pin3,0)
            rotateServo(pin4,180)
            rotateServo(pin5,0)
        elif fingers[1] and fingers[4]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,0)
            rotateServo(pin3,180)
            rotateServo(pin4,180)
            rotateServo(pin5,0)
        elif fingers[0] and fingers[3]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,180)
            rotateServo(pin3,180)
            rotateServo(pin4,0)
            rotateServo(pin5,180)
    elif total==3:
        if fingers[0]&fingers[1]&fingers[2]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,0)
            rotateServo(pin3,0)
            rotateServo(pin4,180)
            rotateServo(pin5,180)
        elif fingers[1]&fingers[2]&fingers[3]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,0)
            rotateServo(pin3,0)
            rotateServo(pin4,0)
            rotateServo(pin5,180)
        elif fingers[2]&fingers[3]&fingers[4]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,180)
            rotateServo(pin3,0)
            rotateServo(pin4,0)
            rotateServo(pin5,0)
        elif fingers[0]&fingers[2]&fingers[4]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,180)
            rotateServo(pin3,0)
            rotateServo(pin4,180)
            rotateServo(pin5,0)
        elif fingers[0]&fingers[3]&fingers[4]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,180)
            rotateServo(pin3,180)
            rotateServo(pin4,0)
            rotateServo(pin5,0)
        elif fingers[0]&fingers[1]&fingers[4]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,0)
            rotateServo(pin3,180)
            rotateServo(pin4,180)
            rotateServo(pin5,0)
        elif fingers[1]&fingers[2]&fingers[4]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,0)
            rotateServo(pin3,0)
            rotateServo(pin4,180)
            rotateServo(pin5,0)
        elif fingers[0]&fingers[2]&fingers[3]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,180)
            rotateServo(pin3,0)
            rotateServo(pin4,0)
            rotateServo(pin5,180)
        elif fingers[0]&fingers[1]&fingers[3]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,0)
            rotateServo(pin3,180)
            rotateServo(pin4,0)
            rotateServo(pin5,180)
        elif fingers[1]&fingers[3]&fingers[4]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,0)
            rotateServo(pin3,180)
            rotateServo(pin4,0)
            rotateServo(pin5,0)
    elif total==4:
        if fingers[0]&fingers[1]&fingers[2]&fingers[3]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,0)
            rotateServo(pin3,0)
            rotateServo(pin4,0)
            rotateServo(pin5,180)
        elif fingers[1]&fingers[2]&fingers[3]&fingers[4]==1:
            rotateServo(pin1,180)
            rotateServo(pin2,0)
            rotateServo(pin3,0)
            rotateServo(pin4,0)
            rotateServo(pin5,0)
        elif fingers[0]&fingers[1]&fingers[3]&fingers[4]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,0)
            rotateServo(pin3,180)
            rotateServo(pin4,0)
            rotateServo(pin5,0)
        elif fingers[0]&fingers[2]&fingers[3]&fingers[4]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,180)
            rotateServo(pin3,0)
            rotateServo(pin4,0)
            rotateServo(pin5,0)
        elif fingers[0]&fingers[1]&fingers[2]&fingers[4]==1:
            rotateServo(pin1,0)
            rotateServo(pin2,0)
            rotateServo(pin3,0)
            rotateServo(pin4,180)
            rotateServo(pin5,0)
    elif total==5:
        rotateServo(pin1,0)
        rotateServo(pin2,0)
        rotateServo(pin3,0)
        rotateServo(pin4,0)
        rotateServo(pin5,0)
