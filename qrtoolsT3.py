# Python 2.x program to generate QR code
from qrtools import QR

import os

my_QR = QR(data=u"Example", pixel_size=10)
my_QR.encode()

# command to move the QR code to the desktop
os.system("mv " + my_QR.filename + " .")
