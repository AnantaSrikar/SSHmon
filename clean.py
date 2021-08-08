import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file", help="file name that has to be cleaned", required=True)
parser.add_argument("--user", help="name of the user", required=True)

args = parser.parse_args()
filename = args.file
user = args.user
basepath = "/tmp"
filepath = basepath + "/" + user + "/" + filename
start = "end-of-line"
start1 = "endif"
end = "~/.bash_logout"
text = ""
with open(filepath) as f:
	lines = f.readlines()
	found = 0
	for line in lines:
		if end in line:
			break
		if start and start1 not in line and found == 0:
			a=1
		elif start in line and start1 in line:
			found = 1
		elif start and start1 not in line and found == 1:
			line = line.rstrip()
			text += line
with open(filename +"-f.log","w") as f:
	f.write(text)
