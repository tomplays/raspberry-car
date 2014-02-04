RaspberryPi car python driver
=====================

V1.xx

## See blog post about project :

http://www.digitalarti.com/fr/blog/artlab/raspberry_pi_wifi_car_prototype_de_tom_wersinger

don't hesite to mail me for support


---------------
GPIO/python driver for 

* 2 DC motors (orginal toy)  uses a L293D chip
* 2 leds

how to use
---------------
<pre>
$ sudo python run.py
</pre>

z and w (back/forward)
a and e to turn

h,l for leds fx
p for demo mode


functions

* drive()
* turn(dir)
* glow()
* stopall()


* 

### TODO

Add a schema :-)

map raspicam streaming - vlc 
raspivid -rot 180 -o - -t 0 -n -w 300 -h 200 -fps 24 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
VLC : rtsp://192.168.1.(*12/yourIP):8554/

### AUTHOR

Tom Wersinger homeof@gmail.com

### COPYRIGHT

Copyright (C) 2014 Tom Wersinger homeof@gmail.com

### LICENSE

see License.md

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

### DISCLAIMER

The author disclaims any responsibility for any mangling of your system etc, that this script may cause.
