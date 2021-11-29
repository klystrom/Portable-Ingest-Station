import os
import time
import atexit
import RPi.GPIO as GPIO
from util_sync_folders import *
from util_find_card_and_drives import *
from util_gpio_handler import *
from util_network_handler import *

# In my instance, the SD cards (I've tried 32GB Sandisk and 64GB Lexar) mount points are at /media/pi/disk.
# If yours are different, edit the 2 lines below.
PATH_TO_SD_ROOT = '/media/pi/disk'
PATH_TO_SD_SYNC_SOURCE = '/media/pi/disk/DCIM/*_FUJI/'

# In my instance, the SSD is mounted as /media/pi/SSD since that's the partition name.
# If yours are different, edit the 2 lines below.
PATH_TO_STORAGE_ROOT = '/media/pi/SSD'
PATH_TO_STORAGE_SYNC_DESTINATION = '/media/pi/SSD/SYNC_TARGET/'

def app_portable_ingest_station():
    continue_process = False

    # First step is to check if both the SD Card and SSD is connected
    if (check_sd_card(PATH_TO_SD_ROOT) == True) and (check_ssd(PATH_TO_STORAGE_ROOT) == True):
        print("Both devices found!!!")
        continue_process = True
        gpio_start_indication()
    else:
        for x in range(0, 3, 1):
            gpio_general_failure()

    # Next is to start copying from SD Card to SSD
    # The copy function should have taken care of diff between folders
    if (continue_process == True):
        continue_process = copy_from_sd_to_ssd(PATH_TO_SD_SYNC_SOURCE, PATH_TO_STORAGE_SYNC_DESTINATION)
        
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