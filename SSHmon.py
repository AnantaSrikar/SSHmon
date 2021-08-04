"""
	Program to log any given ssh session
"""

import argparse

# Checking for psutil installation
try:
	import psutil
	print("psutils is installed: " + str(psutil.__version__))
except Exception as e:
	print(f"Install psutil to run this program : {e}")

# Getting the tty session from the argument
parser = argparse.ArgumentParser()
parser.add_argument("--tty", help="tty session that has to be logged", required=True)

args = parser.parse_args()

tty = args.tty

# Finding the given session
for i in psutil.users():
	if i.terminal == tty:
		info = {
			'name': i.name,
			'host': i.host,
			'started': i.started
		}

# Entered tty is not found
if 'info' not in globals():
	print(f"Session '{tty}'' not found")

# Proceed to start logging
else:
	print(f"Found this for {tty}")
	print(info)