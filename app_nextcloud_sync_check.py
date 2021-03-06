import os
import time
from util_sync_folders import *
from util_find_card_and_drives import *
from util_gpio_handler import *
from util_network_handler import *

gpio_nextcloud_sync_led(True)
time.sleep(3)
gpio_nextcloud_sync_led(False)

while True:
    time.sleep(5)

    if (True == check_network_connection()):
        gpio_nextcloud_sync_led(True)

        while (False == check_nextcloud_sync_complete()):
            print("NextCloud is still syncing...")
            time.sleep(0.5)
            gpio_nextcloud_sync_led(False)
            time.sleep(0.5)
            gpio_nextcloud_sync_led(True)
    else:
        gpio_nextcloud_sync_led(False)
        print("No network!!!")