# Portable Ingest Station
**Backup and sync your photos on the go!!!**

## About Portable Ingest Station
This project is intended to solve my worries of backing up my photos while on trips. 

It aims to do the following:

<ol>
  <li>Backup from SD card to local storage (SSD or other targets)</li>
  <li>Backup from local storage to own storage server</li>
</ol>

## Software Requirements
<ol>
  <li>Raspberry Pi OS</li>
  <li>Python</li>
  <li>Git</li>
  <li>KiCAD (for GPIO board)</li>
  <li>NextCloud Server</li>
</ol>

## Hardware Requirements
<ol>
  <li>Raspberry Pi 4 (Only tested on Rpi4 and recommend it for the fast USB file transfer speed and WiFi capability)</li>
  <li>Power supply for Raspberry Pi</li>
  <li>Micro SD card (for Raspberry Pi OS)</li>
  <li>SD Card reader</li>
  <li>Local storage device (In my case it's an SSD in a USB to SATA enclosure)</li>
  <li>RPI GPIO Board</li>
</ol>

# Installation

## YouTube Video:
Overview:
<div align="left">
  <a href="https://www.youtube.com/watch?v=kqn9C-568doE"><img src="https://img.youtube.com/vi/kqn9C-568do/0.jpg" alt="Portable Ingest Station Software Overview"></a>
</div>

Software Setup:
<div align="left">
  <a href="https://www.youtube.com/watch?v=a_C9UawHIGE"><img src="https://img.youtube.com/vi/a_C9UawHIGE/0.jpg" alt="Portable Ingest Station Software Setup"></a>
</div>

## Step 1: Prepare Raspberry Pi OS
You will need the latest version of [Raspberry Pi OS](https://www.raspberrypi.com/software/). Methods of getting the OS onto the SD card will not be covered here as there are many resources online that covers this. The easiest way is to use the Raspberry Pi Imager.

## Step 2: Boot and Upgrade Raspberry Pi OS
Plug the SD card into Raspberry Pi and power it up. 

> **Note:** If you are doing this process in headless mode (no monitor), you might want to setup wifi connection and SSH access BEFORE plugging in the SD card.

After finished booting up. Complete the usual first boot stuff such as changing default password, expand filesystem, etc.

Update the Raspberry Pi OS by executing the following command:

    sudo apt update && sudo dist-upgrade

Press enter when prompted to proceed with upgrade.

## Step 3: Connection Configuration
When on the go, you probably would not be able to plug the raspberry pi into monitor and keyboard to configure the WiFi connection. So you would need to setup that connection in advance. This internet connection is used by NextCloud to sync the files in your local storage back to your NextCloud server.

Firstly turn on the hotspot on your smartphone. In Raspberry Pi OS, connect to your hotspot SSID. Enter the password. It should have internet access through your smartphone.

> **Note:** If you are doing this process in headless mode, installing VNC would help alot.

## Step 4: Clone Repository
In Raspberry Pi desktop, clone this repository.

    git clone https://github.com/klystrom/Portable-Ingest-Station.git

## Step 5: Setup Nextcloud
This is the part where it gets abit sketchy. Since the the support for official Nextcloud desktop app is non-existent to say the least. So we're going to install an older version of it. It should work after resolving the dependencies.

Guide to install it is [here](https://help.nextcloud.com/t/nextcloud-client-for-raspberry-pi/27989/62). Be sure to follow along the troubleshooting steps mentioned in the thread.

## Step 6: Configure
Plug in your SD card and storage, they should automount under Raspberry Pi OS.

Find out where they are mounted and edit app_nextcloud_sync_check.py.

> **Note:** You can use either of the following commands to find the mountpoints. Look for the keyword "/media/"
>
> df -h
>
> sudo cat /proc/mounts

Your SD card might have different folder structure than mine (mine is based on Fujifilm X-T2 SD Card) and you might want the files to be saved to a specific directory in the local storage. For that, edit the path in these app_nextcloud_sync_check.py.

Now is the most convenient time to test it out. As after this, you would need to reboot the Raspberry Pi in order to test after every change. So put on the GPIO board and test to make sure it works before proceeding to the next step.

## Step 7: Run On Boot
We want the two Python scripts to run on boot. For this, we are using systemd.

> **Note:** Refer [here](https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all) for more info.

Create two new .service files in the systemd directory.

    sudo nano /lib/systemd/system/local_ingest_sync.service
    sudo nano /lib/systemd/system/nextcloud_sync_check.service

Edit local_ingest_sync.service, paste in the following content. Then exit and save by Ctrl+X then enter.

    [Unit]
    Description=Sync SD to local storage
    After=multi-user.target
    
    [Service]
    ExecStart=/usr/bin/python3 <path to repo>/app_portable_ingest_station.py
    
    [Install]
    WantedBy=multi-user.target
    
Edit nextcloud_sync_check.service, paste in the following content. Then exit and save by Ctrl+X then enter.
  
    [Unit]
    Description=Check nextcloud sync status
    After=multi-user.target
    
    [Service]
    ExecStart=/usr/bin/python3 <path to repo>/app_nextcloud_sync_check.py
    
    [Install]
    WantedBy=multi-user.target
    
Enable the services.

    sudo systemctl daemon-reload
    sudo systemctl enable local_ingest_sync.service
    sudo systemctl enable nextcloud_sync_check.service
    
## DONE!
After reboot, everything should be working. Enjoy!

# Limitations
Here are the current limitations that I'm aware of. Feel free to report or help enhance this!
<ol>
  <li>No easy way to connect to another WiFi Network since there's no UI. i.e. hotel WiFi</li>
  <li>Sync status LED not accurate as it depends on the size of a file generated by Nextcloud.</li>
  <li>If the local storage is full, there are no indication.</li>
</ol>
