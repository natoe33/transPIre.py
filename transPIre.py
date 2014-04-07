#!/usr/bin/python3

import os
import shutil
import time

newpath = <path>
src = <path>

if not os.path.exists(newpath): os.makedirs(newpath) # make a new folder

while True:
    for root, dirs, files in os.walk(src): # walk through the directory
        for name in files:
            # Find all of the files that end with common video extentions
            if (name.endswith('.mp4') or name.endswith('.avi') or name.endswith('.mkv'):
                # I estimated that the average movie is more than 500000000 bytes/ 476-ish MB
                if os.path.getsize(name) > 500000000:
                    # Add the file path to the beginning of the file name
                    name = os.path.join(root, name)
                    # Move the files to the new location
                    shutil.move(name, newpath)

    time.sleep(600) # Check again in 10 minutes
