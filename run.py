#!/usr/bin/env python

# Raspberry Car v1.xx
# MIT Licence - Tom Wersinger https://github.com/tomplays/raspberry-car/


import RPi.GPIO as io
import time


# pins attribution
#motor A
in3_pin = 4
in4_pin = 17

#motor B
in1_pin = 27
in2_pin = 22

#Blinking orange leds
o_pin = 24
or_pin = 23

# always stop motors after xx seconds..
securetime = 10

#misc def
glowtime = .1
turntime = .04

#GPIO inits
io.setmode(io.BCM)
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)
io.setup(o_pin, io.OUT)
io.setup(or_pin, io.OUT)

#demo mode for glow
def demoa():
    # alone left and right
    glow(False, True, .2, 5, "yes")
    glow(True, False, .2, 5, "yes")

    # both together and both alternate
    glow(True, True, .1, 5, "yes")
    glow(True, True, .1, 5, "no")

    stopall()

#make the two orange leds blink
def glow(a,b,tim, ran, alternate):
    for x in range(0, ran):
        if alternate == "yes":
            if a==True:
              io.output(o_pin, False)
            if b==True:
                io.output(or_pin, True)
            time.sleep(tim)
            if a==True:
                 io.output(o_pin, True)
            if b==True:
                io.output(or_pin, False)
            time.sleep(tim)
        else:
            if a==True:
                io.output(o_pin, False)
            if b==True:
                io.output(or_pin, False)
            time.sleep(tim)
            if a==True:
                io.output(o_pin, True)
            if b==True:
                io.output(or_pin, True)
            time.sleep(tim)
        print x
    io.output(o_pin, False)
    io.output(or_pin, False)

#params
#   dir: left|right
def turn(dir):
    if dir == "right":
        io.output(in3_pin, False)
        io.output(in4_pin, True)
        time.sleep(turntime)
        glow(False, True,.1, 5, "no")
    if dir == "left":
        io.output(in3_pin, True)
        io.output(in4_pin, False)
        time.sleep(turntime)
        glow(True, False, .1, 5, "no")
    io.output(in3_pin, False)
    io.output(in4_pin, False)


#params
#   dir: forward|backward
#   long: how long (to check)
def drive(dir, long):
    if dir == "forward":
        io.output(in1_pin, False)
        io.output(in2_pin, True)
    if dir == "back":
        io.output(in1_pin, True)
        io.output(in2_pin, False)
    time.sleep(long)
    io.output(in1_pin, False)
    io.output(in2_pin, False)

# turns all gpio off
def stopall():
    io.output(in1_pin, False)
    io.output(in2_pin, False)
    io.output(in3_pin, False)
    io.output(in4_pin, False)
    io.output(o_pin, False)
    io.output(or_pin, False)

# Main loop
# expects keyboard inputs:
# zw(drive) - ae(turn) - lm -hg(glows) - s(stop) p(demo) :
while True:
    cmd = raw_input("zw - ae - lm - hg - s :")
    direction = cmd[0]
    if direction == "e":
        turn('right')
    elif direction == "a":
        turn('left')
    elif direction == "s":
        stopall()
    elif direction == "z":
        drive('forward',1)
    elif direction == "w":
        drive('back', 1)
    elif direction == "p":
        demoa()
    elif direction == "h":
        glow(True, True, .1, 2, "no")
    elif direction == "l":
        glow(True, False, .1, 5, "yes")
    elif direction == "g":
        glow(True, True, .5, 5, "yes")
    else:
        stopall()


