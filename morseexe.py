from morse import *
import sys
from morseKey1 import *

args = ' '.join(sys.argv)
args = args.replace('morseexe.py', '')
#time.sleep(3)
while True:
	texttomorse(args)
