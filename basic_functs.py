#!/usr/bin/python3
#  example usage of PHiSideDriver PCB
#  ==================================
#
#  K Lawson April 2019
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
from PiIO import PiIO_Redge
from PiIO import PiIO_TP
from PiIO import PiIO_Fedge
from PiIO import PiIO_TON
from time import sleep

print("Testing PiIO Utility functions")
sleep(2)

# Test Redge
#
print("TESTING REDGE")
t = PiIO_Redge(0);

print(0, t.redge(0));
print(1, t.redge(1));
print(1, t.redge(1));
print(1, t.redge(1));
print(0, t.redge(0));
print(1, t.redge(1));
print(0, t.redge(0));
print(0, t.redge(0));

# Test Fedge
#
print("TESTING FEDGE")
t = PiIO_Fedge(0);

print(0, t.fedge(0));
print(1, t.fedge(1));
print(1, t.fedge(1));
print(1, t.fedge(1));
print(0, t.fedge(0));
print(1, t.fedge(1));
print(0, t.fedge(0));
print(0, t.fedge(0));

# Test TP
#
print("TESTING TP 2.2s")
tp = PiIO_TP(0,2.2)

tp.tp(0)
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(1, tp.tp(1))
sleep(1)
print(1, tp.tp(1))
sleep(1)
print(1, tp.tp(1))
sleep(1)
print(1, tp.tp(1))
sleep(1)
print(1, tp.tp(1))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(1, tp.tp(1))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(1, tp.tp(1))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(1, tp.tp(1))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(0, tp.tp(0))
sleep(1)
print(tp.tp(0))


# Test TON
#
print("TESTING TON 2.2s")
ton = PiIO_TON(0,2.2)

sleep(1)
print(0, ton.ton(0))
sleep(1)
print(0, ton.ton(0))
sleep(1)
print(1, ton.ton(1))
sleep(1)
print(1, ton.ton(1))
sleep(1)
print(1, ton.ton(1))
sleep(1)
print(1, ton.ton(1))
sleep(1)
print(1, ton.ton(1))
sleep(1)
print(1, ton.ton(1))
sleep(1)
print(1, ton.ton(1))
sleep(1)
print(1, ton.ton(1))
sleep(1)
print(0, ton.ton(0))
sleep(1)
print(1, ton.ton(1))
sleep(1)
print(0, ton.ton(0))
sleep(1)
print(1, ton.ton(1))
sleep(1)
print(0, ton.ton(0))
sleep(1)
print(0, ton.ton(0))

