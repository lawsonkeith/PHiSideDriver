#  example usage of PHiSideDriver PCB
#  ==================================
#
#  K Lawson April 2019
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
# IO Mapper class, maps GPIO # to output numbers
#
from ADS1x15 import ADS1015


class PiIO_Analog:
	# GPIO Mapping
	O1 = 13
	O2 = 16
	O3 = 19
	O4 = 20
	O5 = 26
	O6 = 21
	O7 = 18
	O8 = 27
	RUN=5
	OE=12
	PWM1=17
	PWM2=27
	# GPIO Mapping
	I1 = 17
	I2 = 25
	I3 = 8
	I4 = 7
	FAULT=6
	# Constants
	gain = 1;
	data = 0;
	rmin = [0,0,0,0]
	rmax = [0,0,0,0]
	smax = [0,0,0,0]
	smin = [0,0,0,0]
	amin = [0,0,0,0]
	amax = [0,0,0,0]

	def __init__(self,gain):
		self.adc = ADS1015()
		self.gain = gain
		#return self.adc

	def get_raw(self,channel):
		data = 0;
		data = self.adc.read_adc(channel, self.gain)
	#	print (channel,  "s:", data)
		return data

	def get_scaled(self,channel):
		data = 0;
		data = self.adc.read_adc(channel, self.gain)
	#	print (channel,  "s:", data)
		return data
	


#
class PiIO_DO24_Mapper(object):
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


# IO Mapper class, maps GPIO # to output numbers
#
class PiIO_DIO12_Mapper(object):
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
	I1 = 11
	I2 = 8
	I3 = 7
	I4 = 5
	I5 = 6
	I6 = 12
	I7 = 13
	I8 = 19
	I9 = 16
	I10 = 26
	I11 = 20
	I12 = 21
	RUN = 22
	OE = 23

	def __setattr__(self, *_):
		pass





#	def __init__(self, str):
#		print "KK" 
#		print str
#		return  
#
#PiIO_DO24_Mapper = PiIO_DO24_Mapper()


	
