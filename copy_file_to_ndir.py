
from shutil import copyfile
import csv
import re
import glob
import os
import sys


path = os.path.join(os.getcwd(), sys.argv[1])
path_to_list = os.path.join(os.getcwd(), sys.argv[2])
dst = os.path.join(os.getcwd(), sys.argv[3])


with open(path_to_list, newline='') as f:
    reader = csv.reader(f)
    filenames = list(reader)
os.chdir(path)
extension = 'jpg' 

os.chdir(path)
results = glob.glob('*.{}'.format(extension))
print(results)


for file in filenames:
    file = str(file)
    file = re.sub('\[','',file)
    file = re.sub('\'','',file) 
    file = re.sub('\]','',file)
    file = file+'.jpg'
    if file in results:
        print('file in list')
        src = os.path.join(path, file)
        dest = os.path.join(dst, file)
        print(dest)
        copyfile(src, dest)
