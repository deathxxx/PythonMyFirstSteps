# Python 2.x program to Scan and Read a QR code
from qrtools import QR

my_QR = QR(filename="1ce73d77e9fde5b442f9da877c12e54cb25dfa7623afb6393cdb91f50c01cbfd.png")

# decodes the QR code and returns True if successful
my_QR.decode()

# prints the data
print my_QR.data
