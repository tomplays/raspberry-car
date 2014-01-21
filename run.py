#!/usr/bin/env python


# Raspberry Car v1.xx
#https://github.com/tomplays/raspberry-car
# GPL 2014 - Tom Wersinger 


import RPi.GPIO as io
import time

io.setmode(io.BCM)
in3_pin = 4
in4_pin = 17
in1_pin = 27
in2_pin = 22
glowtime = .1
turntime = .04
o_pin = 24
or_pin = 23

# always stop motors after xx seconds..
securetime = 10

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)
io.setup(o_pin, io.OUT)
io.setup(or_pin, io.OUT)

def demoa():
    # alone left and right
    glow(False, True, .2, 5, "yes")
    glow(True, False, .2, 5, "yes")

    # both together and together alternate
    glow(True, True, .1, 5, "yes")
    glow(True, True, .1, 5, "no")

    stopall()



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



def drive(dir, long):
    if dir == "ahead":
        io.output(in1_pin, False)
        io.output(in2_pin, True)
    if dir == "back":
        io.output(in1_pin, True)
        io.output(in2_pin, False)
    time.sleep(long)
    io.output(in1_pin, False)
    io.output(in2_pin, False)


def stopall():
    io.output(in1_pin, False)
    io.output(in2_pin, False)
    io.output(in3_pin, False)
    io.output(in4_pin, False)
    io.output(o_pin, False)
    io.output(or_pin, False)

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
        drive('ahead',1)
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


