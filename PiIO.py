
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
import max31865
import time

# Rising edge detector
#
class PiIO_Redge:
	last_state=0

	def __init__(self,state):
		self.last_state = state

	def redge(self,state):
		if (self.last_state == 0 and state > 0):
			self.last_state = state
			return True

		self.last_state = state   
		return False


# Falling edge detector
#
class PiIO_Fedge:
	last_state=0

	def __init__(self,state):
		self.last_state = state

	def fedge(self,state):
		if (self.last_state > 0 and state == 0):
			self.last_state = state
			return True

		self.last_state = state   
		return False

# Timed pulse function
# On a REDGE set the output high for time period
# 
class PiIO_TP:
	last_state=0
	# pulse length
	time_pulse=0
	# end time
	end_time=0

	def __init__(self,state,time):
		self.last_state = state
		self.time_pulse = time

	def tp(self,state):
		tc = time.time()
		#print(tc)
		# pulse occring
		if (self.end_time > tc):
			self.last_state = state
			return True

		# redge
		if (self.last_state == 0 and state > 0):
			self.end_time = tc + self.time_pulse

		self.last_state = state
		return False

# Time delayed on
# If input high delay turn on by specified time
#
class PiIO_TON:
	last_state=0
	# pulse length
	time_delay=0
	# end time
	end_time=0

	def __init__(self,state,time):
		self.last_state = state
		self.time_delay = time

	def ton(self,state):
		tc = time.time()

		# redge
		if (self.last_state == 0 and state > 0):
			self.end_time = tc + self.time_delay

		self.last_state = state

		# on condition
		if (state > 0):
			if( tc > self.end_time):
				return True

		return False

class PiIO_Analog:
	# GPIO Mapping
	O1 = 5
	O2 = 31
	O3 = 13
	O4 = 16
	O5 = 19
	O6 = 20
	O7 = 26
	O8 = 21
	RUN=8
	OE=12
	PWM1=17
	PWM2=27
	# GPIO Mapping
	I1 = 22
	I2 = 23
	I3 = 24
	I4 = 25
	FAULT=7
	# Constants
	gain = 1;
	data = 0;
	rmin = [0,0,0,0]
	rmax = [0,0,0,0]
	smax = [0,0,0,0]
	smin = [0,0,0,0]
	amin = [0,0,0,0]
	amax = [0,0,0,0]
	# Alarm latches
	alarm = [0,0,0,0,0]
	alarm = False

	def __init__(self,gain):
		self.adc = ADS1015()
		self.gain = gain
		csPin = 8
		misoPin = 9
		mosiPin = 10
		clkPin = 11

		self.max = max31865.max31865(csPin,misoPin,mosiPin,clkPin)
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
	
	def get_temp(self):
		tempC = self.max.readTemp()
		return tempC

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


	
