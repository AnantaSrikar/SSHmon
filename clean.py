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
keymaps = {
	r"\33[A":"[uparr]\n",
	r"\33[B":"[downarr]\n",
	r"\33[C":"[rightarr]",
	r"\33[D":"[leftarr]",
	r"\177":"[backspace]",
}
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
			line = line.replace(r'\r','\n')
			line = line.replace(r'\t','[tab]\n')
			text += line
for key in keymaps:
	text = text.replace(key,keymaps[key])
with open(filename +"-f.log","w") as f:
	f.write(text)
