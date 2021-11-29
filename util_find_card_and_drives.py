import os
import subprocess

def check_sd_card(arg_path):
    result_sd = subprocess.call("mount | " + arg_path, shell=True)

    print ("mount = " + str(result_sd))

    if result_sd != 127:
        return True
    else:
        return False

def check_ssd(arg_path):
    result_ssd = subprocess.call("mount | " + arg_path, shell=True)

    print ("mount = " + str(result_ssd))

    if result_ssd != 127:
        return True
    else:
        return False

if __name__== "__main__":
    check_sd_card()
    check_ssd()
    os.system('pause')