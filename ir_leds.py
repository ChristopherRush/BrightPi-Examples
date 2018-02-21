import atexit
from brightpi import *

brightPi = BrightPi()

# This method is used to reset the SC620 to its original state.
brightPi.reset()

LED_ALL = (1, 2, 3, 4, 5, 6, 7, 8)
LED_IR = LED_ALL[4:8]
LED_WHITE = LED_ALL[0:4]

ON = 1
OFF = 0

leds = LED_WHITE
while True:
    brightPi.set_led_on_off(leds, OFF)

    brightPi.set_led_on_off(LED_IR, ON)

def exit_handler():
    switch_leds_off()

atexit.register(exit_handler)
