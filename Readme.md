## PHiSideDriver Python example

![](https://github.com/lawsonkeith/PHiSideDriver/raw/master/images/PhiSide.PNG)

# PCB description
The PCB has the following functionality:

* 24 x 5-24V High side outputs
* One user controlled user LED for diagnostics
* One LED to indicate field supply present
* Overload fault LED
* 24 x 3.5mm terminal blocks for high side outputs
* 350mA max output per channel with overcurrent protection (High side)
* 1 x Field supply to power high side drivers
* 1 x 5V terminal block for Pi 5V optional power
* 1 x Output enable to enable / disable all outputs, this also resets faults

The device uses Darlington transistors with a saturation voltage of 1.6-1.8V, therefore the output voltage of will be VField - Vsat.
In some applications this will cause problems with driving  relay coils:

VField | Rated VCoil | VCoil | Note
------- | ------ | ------- | -----
5 | 5 | 3.2 | Will not work
5 | 3V3 | 3.2 | Ok
12 | 12 | 10.2 | Ok
24 | 24 | 22.2 | Ok


* The LED is designed to be cycled by the user program to show that is is running.
* VField can range from 5-24V

# PCB Pinout

Output | RPI GPIO number
---- | ----
O1 | 17
O2 | 15
O3 | 14
O4 | 4
O5 | 3
O6 | 2
O7 | 18
O8 | 27
O9 | 24
O10 | 10
O11 | 9
O12 | 25
O13 | 11
O14 | 8
O15 | 7
O16 | 5
O17 | 6
O18 | 12
O19 | 13
O20 | 19
O21 | 16
O22 | 26
O23 | 20
O24 | 21
RUN | 22
OE | 23


# Software description

A python example is provided to test PCB functionality.  This includes a class to handle the GPIO to output pin mapping.
The example uses the GPIOZero library.

