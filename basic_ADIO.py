#!/usr/bin/python3
#  example usage of PHiSideDriver PCB
#  ==================================
#
#  K Lawson April 2019
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
#  This example turns on the outputs on this 24 output only board
#
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from time import sleep
from PiIO import PiIO_DO24_Mapper
from ADS1x15 import ADS1015

# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#

# @@@@ Hardware init @@@@
#
#io = PiIO_DO24_Mapper()
#o1 = LED(io.O1); 
#o2 = LED(io.O2); 
#o3 = LED(io.O3); 
#o4 = LED(io.O4); 
#o5 = LED(io.O5); 
#o6 = LED(O6) 
#o6 = PWMLED(io.O6,True,0,1000);
#o7 = LED(io.O7); 
#o8 = LED(io.O8); 
#o9 = LED(io.O9); 
#o10 = LED(io.O10); 
#o11 = LED(io.O11); 
#o12 = LED(io.O12); 
#o13 = LED(io.O13); 
#o14 = LED(io.O14); 
#o15 = LED(io.O15); 
#o16 = LED(io.O16); 
adc = ADS1015()
channel = 0
gain = 1
while True:
	data = adc.read_adc(channel, gain)
	print (channel,  "s:", data)
	sleep(0.1)
	channel += 1

	if channel > 3:
		channel = 0
