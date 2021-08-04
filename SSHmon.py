
try:
	import psutil
	print("psutils is installed: " + str(psutil.__version__))
except Exception as e:
	print("Install psutil to run this program : {}".format(e))

print('[+] Getting available ssh connections...')

ttys = {}

for i in psutil.users():
	ttys[i.terminal] = {
		'name': i.name,
		'host': i.host,
		'started': i.started
	}

print(ttys)
