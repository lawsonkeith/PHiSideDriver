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


	
