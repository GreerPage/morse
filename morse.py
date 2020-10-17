import sys
from morse import text_to_morse

args = ' '.join(sys.argv)
args = args.replace('morse.py', '')

while True:
	text_to_morse(args)
