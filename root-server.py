from flask import Flask, request
from os import system

app = Flask(__name__)

@app.route('/')
def home():
	return('Root API up and running!')

@app.route('/newShell', methods=['POST'])
def newShell():
	data = request.get_json()

	print(data)
	print(f"Started logging for {data['user']}")
	system(f"./log-user.sh {data['user']} {str(data['PID'])}")
	print(f"Logging ended for {data['user']} with PID {str(data['PID'])}")

	return ""

if __name__ == "__main__":
	app.run(debug=True, port=8080)
