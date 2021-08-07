import sys,os,re
from subprocess import Popen,PIPE
mytty = os.ttyname(sys.stdout.fileno()).replace('/dev/','')
connection = Popen(['strace', '-s', '16384', '-p', mytty, '-e', 'read'], shell=False, stdout=PIPE, stderr=PIPE)
while True:
	connection.poll()
	key = connection.stderr.readline()
	if 'read' in key:
		x = re.findall('read\(10, \"(.*)\", [0-9]+\) += [0-9]+',key)
		if isinstance(x,list) and len(x):
			sys.stdout.flush()
			sys.stdout.write(str(x[0].decode('string_escape')))
	else:
		print("what the fuck did u do re?")