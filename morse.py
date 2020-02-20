import sys
from morseKey import texttomorse

args = ' '.join(sys.argv)
args = args.replace('morseexe.py', '')

while True:
	texttomorse(args)
