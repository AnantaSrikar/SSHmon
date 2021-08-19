from flask import Flask, request
import os

app = Flask(__name__)

log_path = os.environ['LOG_PATH']

@app.route('/')
def home():
	return('Root API up and running!')

@app.route('/newShell', methods=['POST'])
def newShell():
	data = request.get_json()

	os.system(f"./log-user.sh {data['user']} {str(data['PID'])}")

	return ""