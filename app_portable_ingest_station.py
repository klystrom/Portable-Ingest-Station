import os
import time
import atexit
import RPi.GPIO as GPIO
from util_sync_folders import *
from util_find_card_and_drives import *
from util_gpio_handler import *
from util_network_handler import *


def app_portable_ingest_station():
    continue_process = False

    # First step is to check if both the SD Card and SSD is connected
    if (check_sd_card() == True) and (check_ssd() == True):
        print("Both devices found!!!")
        continue_process = True
        gpio_start_indication()
    else:
        for x in range(0, 3, 1):
            gpio_general_failure()

    # Next is to start copying from SD Card to SSD
    # The copy function should have taken care of diff between folders
    if (continue_process == True):
        continue_process = copy_from_sd_to_ssd()
        
        if (continue_process == True):
            gpio_local_sync_complete()
            print("Local copy done!!!")
        else:
            for x in range(0, 3, 1):
                gpio_general_failure()


gpio_set_all()
time.sleep(3)
while True: # Run forever
    print("ARMED.")
    gpio_reset_all()
    gpio_pend_button_press()
    app_portable_ingest_station()
    time.sleep(3)