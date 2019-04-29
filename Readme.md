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

VField | VCoil | Note
------- | ------ | -------
5 | 5 | Will not work
5 | 3V3 | Ok
12 | 12 | Ok
24 | 24 | Ok

* The LED is designed to be cycled by the user program to show that is is running.
* VField can range from 5-24V

# PCB Pinout

---- | ----
O1 | GPIO 17
O2 | GPIO 15
O3 | GPIO 14
O4 | GPIO 4
O5 | GPIO 3
O6 | GPIO 2
O7 | GPIO 18
O8 | GPIO 27
O9 | GPIO 24
O10 | GPIO 10
O11 | GPIO 9
O12 | GPIO 25
O13 | GPIO 11
O14 | GPIO 8
O15 | GPIO 7
O16 | GPIO 5
O17 | GPIO 6
O18 | GPIO 12
O19 | GPIO 13
O20 | GPIO 19
O21 | GPIO 16
O22 | GPIO 26
O23 | GPIO 20
O24 | GPIO 21

RUN | GPIO 22
OE | GPIO 23


# Software description

A python example is provided to test PCB functionality.  This includes a class to handle the GPIO to output pin mapping.
The example uses the GPIOZero library.

