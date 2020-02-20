import sys
from morseKey import texttomorse

args = ' '.join(sys.argv)
args = args.replace('morse.py', '')

while True:
	texttomorse(args)
