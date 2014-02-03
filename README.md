RaspberryPi car python driver
=====================

V1.xx

See blog post about project :

http://www.digitalarti.com/fr/blog/artlab/raspberry_pi_wifi_car_prototype_de_tom_wersinger


---------------
GPIO/python driver for 

* 2 dc motor uses a L293D chip
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

TODO
----


map raspicam streaming - vlc 
raspivid -rot 180 -o - -t 0 -n -w 300 -h 200 -fps 24 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
VLC : rtsp://192.168.1.(*12/yourIP):8554/

