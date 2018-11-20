# scp pi@192.168.0.113:/home/pi/Raspi_MotorHAT/drive.py drive.py
from Raspi_PWM_Servo_Driver import PWM
import sys
import time
import RPi.GPIO as GPIO
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_StepperMotor, Raspi_DCMotor
import atexit
import pygame

# setup
GPIO.setmode(GPIO.BCM)
# 25/26 PWM drive speed
GPIO.setup(25, GPIO.OUT) 
GPIO.setup(26, GPIO.OUT)
# setup for pins
GPIO.setup(17, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

speed = 40
p=GPIO.PWM(25,speed)
p=GPIO.PWM(26,speed)
pwm=PWM(0x6f)
mh = Raspi_MotorHAT(0x6F)

servoMin = 150
servoMax = 60
S1 = mh.getStepper(200, 1)
S2 = mh.getStepper(200, 2)

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

def forward():
   GPIO.output(17, True)
   GPIO.output(22, False)
   GPIO.output(23, True)
   GPIO.output(24, False)

def reverse():
   GPIO.output(17, False)
   GPIO.output(22, True)
   GPIO.output(23, Fale)
   GPIO.output(24, True)

def right():
   GPIO.output(17, False)
   GPIO.output(22, True)
   GPIO.output(23, True)
   GPIO.output(24, False)

def left()

   GPIO.output(17, True)
   GPIO.output(22, False)
   GPIO.output(23, False)
   GPIO.output(24, True)

def stop():
   GPIO.output(17, False)
   GPIO.output(22, False)
   GPIO.output(23, False)
   GPIO.output(24, False)

p.ChangeDutyCycle(speed)

print "Drive is initialized"

done=False

# Initialize the joysticks
pygame.init()
pygame.joystick.init()

# get joystick 0 and initialize it
joystick = pygame.joystick.Joystick(0)
joystick.init()
print ("Joystick 0 initialized: " + joystick.get_name())

# -------- Main Program Loop -----------
while done == False:
    # go through the events ... because we seem to need to?
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    button = joystick.get_button(0)
    if button == True:
       stop()

    button = joystick.get_button(1)
    if button  == True:
        done =  True
#       print('no')
    button = joystick.get_button(2)
#    if button == True:
#       print('no')

    button = joystick.get_button(3)

#    if button == True:
#       print('no')

    button = joystick.get_button(4)
    if button == True:
       pwm.setPWM(0, 0, servoMin)
       time.sleep(0.001)

    button = joystick.get_button(5)
    if button == True:
       pwm.setPWM(0, 0, servoMax)
       time.sleep(0.001)

    button = joystick.get_button(6)
#    if button == True:
#       print('no')

    button = joystick.get_button(7)
#    if button == True:
#       print('no')

    button = joystick.get_button(9)
#    if button == True:
#       print('no')

    button = joystick.get_button(11)
#    if button == True:
#       print('no')

    button = joystick.get_button(12)
#    if button == True:
#       print('no')

    button = joystick.get_button(13)

#    if button == True:
#       print('no')

    button = joystick.get_button(14)
#    if button == True:
#       print('no')

    button = joystick.get_button(15)
#    if button ==True:
#       print('no'

    button = joystick.get_button(16)
#    if button == True:
#       print('no')

    # stepper1: wrist right/left
    axis = joystick.get_axis(0)
    if axis >= 0.50
       #S1.step(1, Raspi_MotorHAT.FORWARD,  Raspi_MotorHAT.DOUBLE)
       S1.step(5, Raspi_MotorHAT.FORWARD,  Raspi_MotorHAT.SINGLE)

    elif axis <= -0.50:
       #S1.step(1, Raspi_MotorHAT.BACKWARD,  Raspi_MotorHAT.DOUBLE)
       S1.step(5, Raspi_MotorHAT.BACKWARD,  Raspi_MotorHAT.SINGLE)

    # stepper 2: wrist forward/backward
    axis = joystick.get_axis(1)
    if axis >= 0.50:
       #S2.step(1, Raspi_MotorHAT.FORWARD,  Raspi_MotorHAT.DOUBLE)
       S2.step(5, Raspi_MotorHAT.FORWARD,  Raspi_MotorHAT.SINGLE)

    elif axis <= -0.50:
       #S2.step(1, Raspi_MotorHAT.BACKWARD,  Raspi_MotorHAT.DOUBLE)
       S2.step(5, Raspi_MotorHAT.BACKWARD,  Raspi_MotorHAT.SINGLE)

    #DRIVE: right/left
    axislr = joystick.get_axis(3)

    #DRIVE: right
    if axislr >= 0.90:
       speed = 100
       p.ChangeDutyCycle(speed)
       right()

    elif axislr >= 0.80:
       speed = 90
       p.ChangeDutyCycle(speed)
       right()

    elif axislr >= 0.70:
       speed = 80
       p.ChangeDutyCycle(speed)
       right()

    elif axislr >= 0.60:
       speed = 70
       p.ChangeDutyCycle(speed)
       right()

    elif axislr >= 0.50:
       speed = 60
       p.ChangeDutyCycle(speed)
       right()

    elif axislr >= 0.40:
       speed = 50
       p.ChangeDutyCycle(speed)
       right()

    #DRIVE: left
    elif axislr >= -0.50:
       speed = 50
       p.ChangeDutyCycle(speed)
       left()

    elif axislr >= -0.60:
       speed = 60
       p.ChangeDutyCycle(speed)
       left()

    elif axislr >= -0.70:
       speed = 70
       p.ChangeDutyCycle(speed)
       left()
    elif axislr >= -0.80:
       speed = 80
       p.ChangeDutyCycle(speed)
       left()

    elif axislr >= -0.90:
       speed = 90
       p.ChangeDutyCycle(speed)
       left()

    elif axislr >= -1.00:
       speed = 100
       p.ChangeDutyCycle(speed)
       left()
