import os
import shutil

newpath = r'<path>'
src = r'<path>'
results = []
paths = ['.mp4', '.avi', '.mkv'] #common video file extentions

if not os.path.exists(newpath): os.makedirs(newpath)

while true
	#this will eventually iterate over a few different file extensions
	results += [each for each in os.listdir(src) if each.endswith('<file extention type>')]

	for i in results:
    	if os.path.getsize(src + '\\' + i) > 10: #arbitrary file size
        	shutil.move((src + '\\' + i), newpath)