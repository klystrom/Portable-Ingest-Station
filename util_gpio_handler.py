import os
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

# Do not use GPIO18 as it's being used for case PWM fan!!!
btn_input = 16
LED1_output = 20    #Start
LED2_output = 21    #Local sync completed
LED3_output = 26    #All completed
LED4_output = 19    #Ready
buzzer_output = 13

# GPIO btn_input set up as input.
GPIO.setup(btn_input, GPIO.IN)
GPIO.setup(LED1_output, GPIO.OUT)
GPIO.setup(LED2_output, GPIO.OUT)
GPIO.setup(LED3_output, GPIO.OUT)
GPIO.setup(LED4_output, GPIO.OUT)
GPIO.setup(buzzer_output, GPIO.OUT)

def gpio_owncloud_sync_led(arg_state):
    if True == arg_state:
        GPIO.output(LED3_output, GPIO.HIGH)
    else:
        GPIO.output(LED3_output, GPIO.LOW)

def gpio_all_complete():
    GPIO.output(buzzer_output, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(buzzer_output, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(buzzer_output, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(buzzer_output, GPIO.LOW)
    time.sleep(0.5)

# this function is expected to be looped by caller
def gpio_general_failure():
    GPIO.output(buzzer_output, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzzer_output, GPIO.LOW)
    time.sleep(0.1)

def gpio_start_indication():
    GPIO.output(LED1_output, GPIO.HIGH)
    GPIO.output(buzzer_output, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer_output, GPIO.LOW)
    time.sleep(0.1)

def gpio_reset_all():
    GPIO.output(LED1_output, GPIO.LOW)
    GPIO.output(LED2_output, GPIO.LOW)
    #GPIO.output(LED3_output, GPIO.LOW) #Do not set this to low as it's used by owncloud sync checker app
    GPIO.output(LED4_output, GPIO.LOW)
    GPIO.output(buzzer_output, GPIO.LOW)

def gpio_set_all():
    GPIO.output(LED1_output, GPIO.HIGH)
    GPIO.output(LED2_output, GPIO.HIGH)
    #GPIO.output(LED3_output, GPIO.HIGH) #Do not set this to low as it's used by owncloud sync checker app
    GPIO.output(LED4_output, GPIO.HIGH)
    GPIO.output(buzzer_output, GPIO.HIGH)

def gpio_local_sync_complete():
    GPIO.output(LED2_output, GPIO.HIGH)

def gpio_pend_button_press():
    GPIO.output(LED4_output, GPIO.HIGH)
    GPIO.wait_for_edge(btn_input, GPIO.RISING)
    print("Button was pushed!")
    GPIO.output(LED4_output, GPIO.LOW)


if __name__== "__main__":
    gpio_reset_all()
    #gpio_start_indication()
    gpio_all_complete()
    for x in range(0, 3, 1):
        gpio_general_failure()

    gpio_reset_all()