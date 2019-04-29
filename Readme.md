##PHiSideDriver Python example

![](https://github.com/lawsonkeith/PHiSideDriver/raw/master/images/PhiSide.PNG)

# PCB description
The PCB has the following functionality:

(1) 24 x 5-24V High side outputs
(2) One user controlled user LED for diagnostics
(3) One LED to indicate field supply present
(4) Overload fault LED
(5) 24 x 3.5mm terminal blocks for high side outputs
(6) 350mA max output per channel with overcurrent protection
(7) 1 x Field supply 
(8) 1 x 5V terminal block for Pi 5V

The device uses Darlington transistors with a saturation voltage of 1.6-1.8V, therefore the output voltage of will be VField - Vsat.
In some applications this will cause problems with driving  relay coils:

VField | VCoil | Note
---------------------
5 | 5 | Will not work
5 | 3V3 | Ok
12 | 12 | Ok
24 | 24 | Ok

* The LED is designed to be cycled by the user program to show that is is running.
* VField can range from 5-24V


Check out the awesome performace!
 http://youtu.be/g5DNjcppkYU Schematic and BOM:
 https://github.com/lawsonkeith/budget-balance-bot/blob/master/A0015_schematic.pdf 
(TinyCAD)
 https://github.com/lawsonkeith/budget-balance-bot/blob/master/BOM.txt
# Introduction
The aim of this project is to create a low cost bala
