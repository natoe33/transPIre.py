import os
import glob
import shutil

newpath = r'C:\Users\Nate\Downloads\new'
src = r'C:\Users\Nate\Downloads\test'
results = []

if not os.path.exists(newpath): os.makedirs(newpath)

results += glob.glob(src + '.css')

print results
