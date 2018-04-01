#!/usr/bin/env python3
from gpiozero import OutputDevice
from time import sleep

# reset on pin 17, active low
rst = OutputDevice(17, False)

rst.on()
sleep(0.5)
rst.off()
rst.close()
root@esp:/home/nuria/ESP8266pHAT/phatsniffer# more reset_phat.py 
#!/usr/bin/env python3
from gpiozero import OutputDevice
from time import sleep

# reset on pin 17, active low
rst = OutputDevice(17, False)

rst.on()
sleep(0.5)
rst.off()
rst.close()

