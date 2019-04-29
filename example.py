# example usage of PHiSideDriver PCB
# ==================================
#
# K Lawson April 2019
# 
# see https://gpiozero.readthedocs.io/en/stable/recipes.html
# for info on GPIOZero
#
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from time import sleep

# IO Mapper class
#
class HSD(object):
	# Map IO numbers to GPIO Numbers
	O1 = 17
	O2 = 15
	O3 = 14
	O4 = 4
	O5 = 3
	O6 = 2
	O7 = 18
	O8 = 27
	O9 = 24
	O10 = 10
	O11 = 9
	O12 = 25
	O13 = 11
	O14 = 8
	O15 = 7
	O16 = 5
	O17 = 6
	O18 = 12
	O19 = 13
	O20 = 19
	O21 = 16
	O22 = 26
	O23 = 20
	O24 = 21
 	RUN = 22
	OE = 23

	def __setattr__(self, *_):
		pass

HSD = HSD()

#----------


# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#
output = PWMLED(HSD.O6,True,0,10)
enable = LED(HSD.OE);
run = LED(HSD.RUN);

# enable outputs
enable.on()

# flash LED and drive output at variable rate 0-100% duty cycle 
while True:
	for b in range(100):
		# flash LED
		run.blink()
		# PWM to output
		output.value  = b / 100.0
		sleep(1)
		print b, "% duty"
