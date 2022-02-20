import board
import time
import digitalio
import pwmio
import sys


# note: might have to change digitalio board values to whatever yall have as the physical setup

# configure the motor as output
in1 = digitalio.DigitalInOut(board.GP14)
in2 = digitalio.DigitalInOut(board.GP15)
in1.direction = digitalio.Direction.OUTPUT
in2.direction = digitalio.Direction.OUTPUT

# configure the LED setup as outputs
led_red = digitalio.DigitalInOut(board.GP13)
led_green = digitalio.DigitalInOut(board.GP18)
led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT


# configure the PIR as input
pir = digitalio.DigitalInOut(board.GP12)
pir.direction = digitalio.Direction.INPUT
pir_value = pir.value

# set up PWM output to motor driver
ena = pwmio.PWMOut(board.GP16)

# set initial duty cycle, direction, and step commands
ena.duty_cycle = 0
in1.value = False
in2.value = True

buzzbuzz = pwmio.PWMOut(board.GP19, duty_cycle = 1000, frequency = 150, variable_frequency = True)

"""
The following loop continuously runs, constantly checking if a) the ML code can be run and
b) the LED / motor needs to be run. I figured it'd be less demanding if the python code
ran non-stop compared to the ML code
"""

a = 0
while True:

    if pir_value:

        print(1)
        

    else:
        print(0)
        time.sleep(1)
        pir_value = pir.value

    if pir_value:

        content1 = sys.stdin.readline()
        
        contents = content1.split("\n")[-2]
        


        if contents == "with_mask":
 
            led_red.value, led_green.value = (False, True)
            time.sleep(1)
            ##time.sleep(5)
            ##led_red.value, led_green.value = (False, False)
        elif contents == "without_mask":

            led_red.value, led_green.value = (True, False)
            time.sleep(1)
            ##time.sleep(1)
            if a < 4:
                in1.value, in2.value = (False, True)  # CW rotation
                ena.duty_cycle = 60000
                time.sleep(6)
            a += 1
            ena.duty_cycle = 0
            for duty in range(0,40000,1000): 
            # increasing duty cycle 
                buzzbuzz.duty_cycle = duty 
                time.sleep(0.1) 
                buzzbuzz.duty_cycle = 0 
                time.sleep(0.01)
        elif contents == "mask_weared_incorrect":

            led_red.value, led_green.value = (True, False)
            time.sleep(1)
            # time.sleep(5)
            # led_red.value, led_green.value = (False, False)
        else:
            led_red.value, led_green.value = (False, False)