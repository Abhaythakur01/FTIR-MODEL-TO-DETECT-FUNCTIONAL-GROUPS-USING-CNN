import jcamp
import os
import glob
import shutil
import sys


path = os.path.join(os.getcwd(), sys.argv[1])
destination = os.path.join(os.getcwd(), sys.argv[2])
final_dest = os.path.join(os.getcwd(), sys.argv[3])

extension = 'jdx'
all_files = glob.glob(path + "\*.jdx")

for file in all_files:
    data = jcamp.JCAMP_reader(file)
    wavenumbers = data.get('x_units', r'N\A').lower() != 'micrometers'
    absorbance = data.get('yunits', r'N\A').lower() == 'absorbance'
    # move file if wavenumbers is in micrometers
    
    if wavenumbers == False:
        print('bad apple')
        shutil.move(file, destination)
    
    # move file if not in absorbance
    if absorbance == False:
        shutil.move(file,final_dest)
       
