#!/usr/bin/env python3
# modo programacion
# Se debe de enviar low al GPIO #0 mientras que se hace el reset
from gpiozero import OutputDevice
from time import sleep

# reset on pin 17, active low
rst = OutputDevice(17, False)
# flash mode select on pin 27, active low
flash = OutputDevice(27, False)

flash.on()
sleep(0.5)
rst.on()
sleep(0.5)
rst.off()
sleep(0.5)
flash.off()
rst.close()
flash.close()
