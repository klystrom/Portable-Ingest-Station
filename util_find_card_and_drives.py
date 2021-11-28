import os
import subprocess

PATH_FUJI_SD_CARD = '/media/pi/32 GB Volume/DCIM/'

def check_sd_card():
    result_sd = subprocess.call("mount | /media/pi/disk", shell=True)

    print ("mount = " + str(result_sd))

    if result_sd != 127:
        return True
    else:
        return False

def check_ssd():
    result_ssd = subprocess.call("mount | /media/pi/SSD", shell=True)

    print ("mount = " + str(result_ssd))

    if result_ssd != 127:
        return True
    else:
        return False

if __name__== "__main__":
    check_sd_card()
    check_ssd()
    os.system('pause')