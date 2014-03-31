import os
import glob
import shutil

newpath = r'<path>'
src = r'<path>'
results = []

if not os.path.exists(newpath): os.makedirs(newpath)

results += glob.glob(src + '.css')

print results
