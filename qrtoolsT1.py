# Python 2.x program to generate QR code
from qrtools import QR

import os
import time

my_QR = QR(data=u"Example")
my_QR.encode()

ts = time.time()
print ts

# command to move the QR code to the desktop
# os.system("mv " + my_QR.filename + " ~/Desktop")
# os.system("mv " + my_QR.filename + " ." + my_QR.filename + str(ts))
print my_QR.filename
os.system("mv " + my_QR.filename + " .")
