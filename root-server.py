from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

log_path = os.environ['LOG_PATH']

def getUsersWithLogs():
	
	# List of users with processed logs
	p_users = []
	
	users_log = os.listdir(log_path)

	for user in users_log:
		user_log_path = os.path.join(log_path, user)

		user_logfiles = [f for f in os.listdir(user_log_path) if os.path.isfile(os.path.join(user_log_path, f))]

		for logfile in user_logfiles:
			if logfile[-5] == "f" and user not in p_users: # lmao F
				p_users.append(user)

	return p_users


def getUserLogs(user):
	
	logfiles = []
	
	user_log_path = os.path.join(log_path, user)

	user_logfiles = [f for f in os.listdir(user_log_path) if os.path.isfile(os.path.join(user_log_path, f))]

	for logfile in user_logfiles:
		if logfile[-5] == "f": # lmao F againXD
			logfiles.append(logfile)

	return logfiles

@app.route('/')
def home():
	return('Root API up and running!')

@app.route('/newShell', methods=['POST'])
def newShell():
	data = request.get_json()

	os.system(f"./log-user.sh {data['user']} {str(data['PID'])}")

	return ""

@app.route('/check-logs')
def checkLogs():
	users = getUsersWithLogs()

	if(len(users) == 0):
		return "No logs yet :("

	web_text = ""

	for user in users:
		web_text += f"""<a href="/check-logs/{user}">{user}</a>    """
	
	return web_text

@app.route('/check-logs/<username>')
def getShowLogs(username):
	
	if username not in getUsersWithLogs() or len(getUserLogs(username)) == 0:
		return f"No logs found for the user {username}"

	web_text = ""

	for logfile in getUserLogs(username):
		web_text += f"""<a href="/check-logs/{username}/{logfile}">{logfile}</a></br>"""
	
	return web_text

@app.route('/check-logs/<username>/<logfile>')
def showLogFile(username, logfile):
	if username not in getUsersWithLogs() or len(getUserLogs(username)) == 0:
		return f"No logs found for the user {username}"

	if not os.path.isfile(os.path.join(log_path, username, logfile)):
		return f"""No logfile named {logfile} was found! Go back <a href="/check-logs/{username}">here</a> and try again."""

	return send_from_directory(log_path, os.path.join(username, logfile))