import sys
from morse import text_to_morse
import time


def main(message, loop=False):
	if loop:
		while True:
			text_to_morse(message)
			time.sleep(2)
	else:
		text_to_morse(message)
	
if __name__ == '__main__':
	args, name = sys.argv, sys.argv[0]
	args.pop(0)

	if args == []:
		print('Usage: {} [ MESSAGE ] -l [ TRUE/FALSE ]'.format(name))
		print('Try \'{} --help\' for more information.'.format(name))

	elif args[0] == '-l' or args[0] == '--loop':
		print('Usage: {} [ MESSAGE ] -l [ TRUE/FALSE ]'.format(name))
		print('Try \'{} --help\' for more information.'.format(name))
	
	elif '-h' in args or '--help' in args:
		print('Usage: {} [ MESSAGE ] -l [ TRUE/FALSE ]'.format(name))
		print('Example: {} go to https://spotify.greerpage.com please -l true'.format(name))
		print()
		print('-l, --loop	if set to true the message will be displayed until the process is killed (false by default)')
	
	elif '-l' in args:
		m = ' '.join(args).split('-l')
		if m[1].lower().split() == 'true':
			main(m[0], True)
		elif m[1].lower().split() == 'false':
			main(m[0], False)
		else:
			print('e')
			print('Usage: {} [ MESSAGE ] -l [ TRUE/FALSE ]'.format(name))
			print('Try \'{} --help\' for more information.'.format(name))
	
	elif '--loop' in args:
		m = ' '.join(args).split('--loop')
		if m[1].lower().split() == 'true':
			main(m[0], True)
		elif m[1].lower().split() == 'false':
			main(m[0], False)
		else:
			print('Usage: {} [ MESSAGE ] -l [ TRUE/FALSE ]'.format(name))
			print('Try \'{} --help\' for more information.'.format(name))
	else:
		for arg in args:
			if '-' in arg:
				if arg not in ['-l', '--loop', '-h', '--help']:
					print('{}: invalid flag'.format(arg))
					exit()
		main(' '.join(args), False)