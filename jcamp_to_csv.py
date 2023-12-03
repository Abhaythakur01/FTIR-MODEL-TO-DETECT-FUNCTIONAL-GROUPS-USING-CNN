


import jcamp
import os
import glob
import csv
import re
import sys



path = os.path.join(os.getcwd(), sys.argv[1])


extension = 'jdx'
os.chdir(path) 
result = glob.glob('*.{}'.format(extension))
all_files = glob.glob(path + "\*.jdx")
for file in all_files:
    data = jcamp.JCAMP_reader(file)
    nfn = re.sub('.jdx','.csv',file) #nfn = new filename
    with open(nfn, 'w', newline = '') as f:
        writer = csv.writer(f, delimiter = ',')
        writer.writerow(('x','y'))
        writer.writerows(zip(data['x'], data['y']))

    if not f.closed:
        f.close()
