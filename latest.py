import os
import glob
import sys

user = os.getuid()
if user != 0:
    print "Please run script as root"
    sys.exit()
    
from papirus import PapirusImage

pathsstv = '/home/pi/sstv/'

x=0
older=""
while x==0:
	newest = max(glob.iglob('*.[Jj][Pp][Gg]'), key=os.path.getctime)
	if older<>newest:
		image.write(pathsstv+newest)
	older = newest

