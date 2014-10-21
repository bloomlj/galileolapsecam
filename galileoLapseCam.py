#!/usr/bin/env python
#
#  galileoLapseCam.py
#
#  change from James Moore 's raspiLapseCam.py for raspberry pi by boomlj at oct.22 2014. https://bitbucket.org/fotosyn/fotosynlabs/src/9819edca892700e459b828517bba82b0984c82e4/RaspiLapseCam/raspiLapseCam.py?at=master

#start when reboot:
#crontab  -e
#@reboot python  lapsecam.py >> /root/lapsecam.log &

# Import some frameworks
import os
import time
#import RPi.GPIO as GPIO
from datetime import datetime

# Grab the current datetime which will be used to generate dynamic folder names
d = datetime.now()
initYear = "%04d" % (d.year) 
initMonth = "%02d" % (d.month) 
initDate = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)

# Define the location where you wish to save files. Set to HOME as default. 
# If you run a local web server on Apache you could set this to /var/www/ to make them 
# accessible via web browser.
# Or save in a usb disk.
os.system("mount /dev/sda1 /mnt/u")

folderToSave = "/mnt/u/timelapse" + str(initYear) + str(initMonth) + str(initDate) + str(initHour) + str(initMins)
#folderToSave = "/mnt/u/timelapse"
os.mkdir(folderToSave)

# Set the initial serial for saved images to 1
fileSerial = 1

# Run a WHILE Loop of infinitely
while True:
    
    d = datetime.now()
    if d.hour > 2:
        
        # Set FileSerialNumber to 000X using four digits
        fileSerialNumber = "%04d" % (fileSerial)
        
        # Capture the CURRENT time (not start time as set above) to insert into each capture image filename
        hour = "%02d" % (d.hour)
        mins = "%02d" % (d.minute)
        
        # Define the size of the image you wish to capture. 
        imgWidth = 1280 # Max = 2592 
        imgHeight = 720 # Max = 1944
        print " ====================================== Saving file at " + hour + ":" + mins
        
        
        # Capture the image using raspistill. Set to capture with added sharpening, auto white balance and average metering mode
        # Change these settings where you see fit and to suit the conditions you are using the camera in
        os.system("fswebcam   -r" + str(imgWidth) + "x" + str(imgHeight) + "  " + str(folderToSave) + "/" + str(fileSerialNumber) + "_" + str(hour) + str(mins) +  ".jpg")

        # Increment the fileSerial
        fileSerial += 1
        
        # Wait 60 seconds (1 minute) before next capture
        time.sleep(60)
        
    else:
        
        # Just trapping out the WHILE Statement
        # print " ====================================== Doing nothing at this time"