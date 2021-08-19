import argparse
from os import path, remove, environ

parser = argparse.ArgumentParser()
parser.add_argument("--file", help="file name that has to be cleaned", required=True)
parser.add_argument("--user", help="name of the user", required=True)

args = parser.parse_args()

filename = args.file
user = args.user

# Path for the logfile
log_path = environ["LOG_PATH"]
file_path = path.join(log_path, user, filename)

# List of special escape sequences
keymaps = {
	r"\33[A":"\n[uparr]\n",
	r"\33[B":"\n[downarr]\n",
	r"\33[C":"[rightarr]",
	r"\33[D":"[leftarr]",
	r"\177":"[backspace]",
	r"\r":"\n[enter]\n",
	r"\4": "\n[exit]"
}

# Reading the given logfile and writing simultaneously
with open(path.join(log_path, user, f"{filename[:-4]}-f.log"),"w") as outFPtr:
	with open(file_path) as inFPtr:
	
		lines = inFPtr.readlines()
		
		log_start = False

		for line in lines:

			# if the last part of the logfile is found
			if "~/.bash_logout" in line:
				break
			
			# Checking for the start of the keylogging, the second occurence 
			if ': end-of-line\\n\\n$endif\\n' in line and not log_start:
				log_start = True
			
			# Start logging
			elif log_start:
				# Every line has '\n' appended at the end
				if(len(line) == 2):
					outFPtr.write(line[0])
				
				else:
					if line[:-1] in keymaps:
						outFPtr.write(keymaps[line[:-1]])
					else: # Write character by character, to prevent escape sequence
						for i in range(len(line) - 1):
							outFPtr.write(line[i])

remove(file_path)