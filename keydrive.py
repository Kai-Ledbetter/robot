import curses
import sys
import time
import RPi.GPIO as GPIO
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

done = False
speed = 40
# right side
p1=GPIO.PWM(25,speed)
# left side
p2=GPIO.PWM(26,speed)

def reverse():
   GPIO.output(17, True)
   GPIO.output(22, Fale)
   GPIO.output(23, True)
   GPIO.output(24, False)

def forward():
   GPIO.output(17, False)
   GPIO.output(22, True)
   GPIO.output(23, False)
   GPIO.output(24, True)

def right():
   GPIO.output(17, True)
   GPIO.output(22, False)
   GPIO.output(23, False)
   GPIO.output(24, True)

def left():
   GPIO.output(17, False)
   GPIO.output(22, True)
   GPIO.output(23, True)
   GPIO.output(24, False)

def stop():
   GPIO.output(17, False)
   GPIO.output(22, False)
   GPIO.output(23, False)
   GPIO.output(24, False)

stop()
p1.start(speed)
p2.start(speed)

# initalize
#pygame.init()
#pygame.display.set_mode((100,100))
# set to check keys every 100 miliseconds
#pygame.key.set_repeat(100,100)

#while done == False:
#    events = pygame.event.get()
#    print("running..." + str(len(events)))
#    for event in events:
#       print("event:" + event.type)
#        if event.type == pygame.KEYDOWN:
#           print("KEYDOWN")
#            if event.key == pygame.K_w:
#               p.ChangeDutyCycle(speed)
#                forward()
#            if event.key == pygame.K_a:
#                p.ChangeDutyCycle(speed)
#               left()
#           if event.key == pygame.K_s:
#                p.ChangeDutyCycle(speed)
#               reverse()
#            if event.key == pygame.K_d:
#                p.ChangeDutyCycle(speed)
#               right()
#            if event.key == pygame.K_q:
#                speed++10
#            if event.key == pygame.K_e:
#                speed--10
#            if event.key == pygame.K_z:
#               done = True
#        if event.type == pygame.KEYUP:
#            stop()

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
curses.noecho()
curses.curs_set(0)

print("initialized")

stdscr.refresh()
stdscr.clear()
stdscr.addstr(1,30,"'z' to quit")
stdscr.addstr(2,30,"arrow keys to move")
stdscr.addstr(3,30,"'q' to go faster")
stdscr.addstr(4,30,"'e' to go slower")
stdscr.addstr(10,40,"speed = ")

key = ''
while key != ord('z'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    if key == curses.KEY_UP: 
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
        forward()
        #stdscr.clear()
        stdscr.addstr(10, 48, str(speed) + " ", curses.A_BOLD)
        stdscr.addstr(10, 30, "FORWARD", curses.A_BOLD)
    elif key == curses.KEY_DOWN: 
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
        reverse()
        stdscr.addstr(10, 48, str(speed) + " ", curses.A_BOLD)
        stdscr.addstr(10, 30, "REVERSE", curses.A_BOLD)
    elif key == curses.KEY_LEFT: 
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
        left()
        stdscr.addstr(10, 48, str(speed) + " ", curses.A_BOLD)
        stdscr.addstr(10, 30, "LEFT    ", curses.A_BOLD)
    elif key == curses.KEY_RIGHT: 
        p1.ChangeDutyCycle(speed
        p2.ChangeDutyCycle(speed)
        right()
        stdscr.addstr(10, 48, str(speed) + " ", curses.A_BOLD )
        stdscr.addstr(10, 30, "RIGHT    ", curses.A_BOLD)
    elif key == ord('q'): 
        if speed < 100:
            speed += 10
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
        stdscr.addstr(10, 48, str(speed) + " ", curses.A_BOLD
    elif key == ord('e'): 
        if speed > 10:
            speed -= 10
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
        stdscr.addstr(10, 48, str(speed) + " ", curses.A_BOLD)
    elif key == ord('x'): 
        stop()
        stdscr.addstr(10, 30, "STOP     ", curses.A_BOLD)
        
curses.endwin()
GPIO.cleanup()
p1.stop()
p2.stop()
stdscr.clear()
