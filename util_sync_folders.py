import os
import subprocess
import pathlib
import glob

def copy_from_sd_to_ssd(arg_sd_path, arg_local_storage_path):
    result = subprocess.call("rsync -aP " + arg_sd_path + " " + arg_local_storage_path, shell=True)

    print("Rsync result: " + str(result))

    if result == 0:
        return True
    else:
        return False

def check_nextcloud_sync_complete(arg_local_storage_path):
    #fileDir = '/media/pi/SSD/SYNC_TARGET/'
    fileExt = r"*.db-wal"
    file_list = list(pathlib.Path(arg_local_storage_path).glob(fileExt))

    print(file_list)
    local_result = os.path.getsize(str(file_list[0]))

    print("Size of " + str(file_list[0]) + " is " + str(local_result))

    if local_result == 0:
        return True
    else:
        return False

if __name__== "__main__":
    result = check_nextcloud_sync_complete()
    print("Sync is " + str(result))
    result = copy_from_sd_to_ssd()
    print("Rsync result: " + str(result))
    os.system('pause')