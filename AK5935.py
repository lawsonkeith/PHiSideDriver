import time
import pygame
from pygame.locals import *
from gpiozero import LED     # in GPIOZero outputs are called LEDs???
import serial
import pprint


# IO Mapper class, maps GPIO # to output numbers
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


# @@@@ Hardware init @@@@
#
o1 = LED(HSD.O1); 
o2 = LED(HSD.O2); 
o3 = LED(HSD.O3); 
o4 = LED(HSD.O4); 
o5 = LED(HSD.O5); 
o6 = LED(HSD.O6) 
o7 = LED(HSD.O7); 
o8 = LED(HSD.O8); 
o9 = LED(HSD.O9); 
o10 = LED(HSD.O10); 
o11 = LED(HSD.O11); 
o12 = LED(HSD.O12); 
o13 = LED(HSD.O13); 
o14 = LED(HSD.O14); 
o15 = LED(HSD.O15); 
o16 = LED(HSD.O16); 
o17 = LED(HSD.O17); 
o18 = LED(HSD.O18); 
o19 = LED(HSD.O19); 
o20 = LED(HSD.O20); 
o21 = LED(HSD.O21); 
o22 = LED(HSD.O22); 
o23 = LED(HSD.O23); 
o24 = LED(HSD.O24); 

enable = LED(HSD.OE);
run = LED(HSD.RUN);
#

""" Work still to do:
        - handle other controllers
        - improve how the program detects that joypad has been disconnected
"""


def main():
        global timer # A timer to periodically check for joypad presence
        timer=35000

        while True:
                    #kl
                    run.toggle()

                    pygame.event.get()
                    timer = timer - 1
                    if timer == 0:
                           checkpad()
                           timer = 35000
                    
                    #Left joystick
                    #up
                    if  js.get_axis(1)<-.5:
                        pprint.pprint("Shoulder Up")
                        #GPIO.output(27,GPIO.LOW)
                        o1.on()
                        commslight()
                    else:
                        #GPIO.output(27,GPIO.HIGH)
                        o1.off()
                        
                    #Down
                    if js.get_axis(1)>.5:
                        pprint.pprint("Shoulder Down")
                        #GPIO.output(22,GPIO.LOW)
                        o2.on()
                        commslight()
                    else:
                        #GPIO.output(22,GPIO.HIGH)
                        o2.off()

                    #Left  
                    if js.get_axis(0)<-.7:
                        pprint.pprint("Slew Left")
                        #GPIO.output(17,GPIO.LOW)
                        o3.on()
                        commslight()
                    else:
                       #GPIO.output(17,GPIO.HIGH)
                        o3.off()
                       
                      #Right
                    if js.get_axis(0)>.7:
                        pprint.pprint("Slew Right")
                        #GPIO.output(4,GPIO.LOW)
                        o4.on()
                        commslight()
                    else:
                        #GPIO.output(4,GPIO.HIGH)
                        o4.off()
    
                    #Right joystick
                    #up
                    if  js.get_axis(5)<-.5:
                        #pprint.pprint("Elbow Up")
                        o5.on()
                        GPIO.output(10,GPIO.LOW)
                        commslight()
                    else:
                        #GPIO.output(10,GPIO.HIGH)
                        o5.off()

                    #down
                    if js.get_axis(5)>.5:
                        pprint.pprint("Elbow Down")
                        #GPIO.output(9,GPIO.LOW)
                        o6.on()
                        commslight()
                    else:
                        #GPIO.output(9,GPIO.HIGH)
                        o6.off()
      
                    #Right Hand: Triangle Star Square Circle
                    #Triangle
                    if js.get_button(3)== True:
                        pprint.pprint("Wrist Up")
                        #GPIO.output(11,GPIO.LOW)
                        o7.on()
                        commslight()
                    else:
                        #GPIO.output(11,GPIO.HIGH)
                        o7.off()

                    #X
                    if js.get_button(1)== True:
                        pprint.pprint("Wrist Down")
                        #GPIO.output(0,GPIO.LOW)
                        o8.on()
                        commslight()
                    else:
                        #GPIO.output(0,GPIO.HIGH)
                        o8.off()

                    #Square  
                    if js.get_button(0)== True:
                        pprint.pprint("Wrist Left")
                        #GPIO.output(5,GPIO.LOW)
                        o9.on()
                        commslight()
                    else:
                       #GPIO.output(5,GPIO.HIGH)
                        o9.off()

                    #Circle
                    if js.get_button(2)== True:
                        pprint.pprint("Wrist right")
                        #GPIO.output(6,GPIO.LOW)
                        o10.on()
                        commslight()
                    else:
                        #GPIO.output(6,GPIO.HIGH)
                        o10.off()
    
                    #L1    
                    if  js.get_button(4)== True :
                        pprint.pprint("Wrist CW")
                        #GPIO.output(19,GPIO.LOW)
                        o11.on()
                        commslight()
                    else:
                        #GPIO.output(19,GPIO.HIGH)
                        o11.off()

                    #L2
                    if  js.get_button(6)== True :
                        pprint.pprint("Wrist CCW")
                        #GPIO.output(13,GPIO.LOW)
                        o12.on()
                        commslight()
                    else:
                        #GPIO.output(13,GPIO.HIGH)
                        o12.off()
                         
                    #R1
                    if  js.get_button(5)== True :
                        pprint.pprint("Jaw Open")
                        #GPIO.output(3,GPIO.LOW)
                        o13.on()
                        commslight()
                    else:
                        #GPIO.output(3,GPIO.HIGH)
                        o13.off()

                    #R2
                    if  js.get_button(7)== True :
                        pprint.pprint("Jaw Close")
                        #GPIO.output(2,GPIO.LOW)
                        o14.on()
                        commslight()
                    else:
                        #GPIO.output(2,GPIO.HIGH)
                           o14.off()

def checkpad():
        # function to check for that joypad has not been disconnected
        # commands sent from joypad are lost when this function is called
        # so function is only called roughly every 5 seconds during inactivity
        pygame.quit()
        pygame.init()
        num_joysticks = pygame.joystick.get_count()

        if num_joysticks < 1:
                while num_joysticks < 1:
                        # status LED is turned red and stays in loop until joystick is detected
                        print("You didn't plug in a joystick!")
                        #GPIO.output(15,GPIO.HIGH)
                        o15.off()
                        #GPIO.output(14,GPIO.LOW)
                        o16.on()
                        pygame.quit()
                        pygame.init()
                        num_joysticks = pygame.joystick.get_count()
               
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        js=joystick
        #GPIO.output(14,GPIO.HIGH)
        o16.off()
        #GPIO.output(15,GPIO.LOW)
        o15.on()

def commslight():
        # illuminates 'comms' LED when button on joypad is pressed
        # resets timer to avoid commands being lost when joypad is used
        global timer
        timer = 50000
        #GPIO.output(23,GPIO.HIGH) #comms LED on
        time.sleep(0.1)
        #GPIO.output(23,GPIO.LOW) #comms LED off
        run.toggle()

def ledstart():
        # LED initialisation sequence
        #GPIO.output(15,GPIO.HIGH)
        #GPIO.output(14,GPIO.HIGH)
        o15.off()
        o16.off()
        time.sleep(1)
        #GPIO.output(15,GPIO.LOW)
        #GPIO.output(14,GPIO.LOW)
        o15.on()
        o16.on()
        time.sleep(1)
        #GPIO.output(15,GPIO.HIGH)
        #GPIO.output(14,GPIO.HIGH)
        o15.off()
        o16.off()
        time.sleep(1)
        #GPIO.output(15,GPIO.LOW)
        #GPIO.output(14,GPIO.LOW)
        o15.on()
        o16.on()
        time.sleep(1)
        #GPIO.output(15,GPIO.HIGH)
        #GPIO.output(14,GPIO.HIGH)
        o15.off()
        o16.off()
        time.sleep(1)
        #GPIO.output(14,GPIO.HIGH)        
        #GPIO.output(15,GPIO.LOW)

        #GPIO.output(25,GPIO.LOW) # switch to local control
        o17.on()

def initpad():
        # first initialisation of joypad
        pygame.init()
        num_joysticks = pygame.joystick.get_count()
        if num_joysticks < 1:
                while num_joysticks < 1:
                        print("You didn't plug in a joystick!")
                        # status LED is turned red and stays in loop until joystick is detected
                        #GPIO.output(15,GPIO.HIGH)
                        #GPIO.output(14,GPIO.LOW)
                        o15.off()
                        o16.on()
                        pygame.quit()
                        pygame.init()
                        num_joysticks = pygame.joystick.get_count()
                        #kl
                        run.toggle()
               
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        global js
        js=joystick
        #GPIO.output(14,GPIO.HIGH)
        #GPIO.output(15,GPIO.LOW)  
        o15.on()
        o16.off()

ledstart()
initpad()     
main()
GPIO.cleanup()
# fin.
