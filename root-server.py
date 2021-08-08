from flask import Flask, request
from os import system

app = Flask(__name__)

@app.route('/')
def home():
	return('Root API up and running!')

@app.route('/newShell', methods=['POST'])
def newShell():
	data = request.get_json()

	system(f"./log-user.sh {data['user']} {str(data['PID'])}")

	return ""
