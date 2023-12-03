import os, shutil
import sys
import glob

path = os.path.join(os.getcwd(), sys.argv[1])
dest = os.path.join(os.getcwd(), sys.argv[2])

extension = str(sys.argv[3])

results = glob.glob(path + extension)
for file in results:
    shutil.move(file, dest)
